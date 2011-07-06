from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponseForbidden,HttpResponse,HttpResponseServerError
from words.todos.models import ToDo
from django.views.generic.simple import direct_to_template
from django.contrib import auth

def fetch_todolist(user):
    return (user.todos.order_by('-id').filter(done=False),user.todos.order_by('-id').filter(done=True)[:5])

def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/todos/login/')
    return direct_to_template(request,'todos/index.html')

def login(request):
    auth.logout(request)
    if request.POST:
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/todos/')
        else:
            info='Invalid username or password!'
    return render_to_response('todos/login.html',locals())

def handle_todo(request,todo_id,done=None,highlight=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/todos/login/')
    todo=get_object_or_404(ToDo,id=todo_id)
    if not request.user.id==todo.user.id:
        return HttpResponseForbidden()
    try:
        if done!=None:
            todo.done=done
        if highlight!=None:
            todo.highlight=highlight
        todo.save()
        return HttpResponse(str(todo.id))
    except:
        return HttpResponseServerError()

def new(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/todos/login/')
    if request.POST:
        todo=ToDo.objects.create(user=request.user,name=request.POST['task'])
        return HttpResponse("({'task':'%s','id':%d})" % (todo.name,todo.id))

def undone(request,todo_id):
    return handle_todo(request,todo_id,False)

def done(request,todo_id):
    return handle_todo(request,todo_id,True)

def highlight(request,todo_id):
    return handle_todo(request,todo_id,None,True)

def unhighlight(request,todo_id):
    return handle_todo(request,todo_id,None,False)

def todolist(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/todos/login/')

    (todos,dones)=fetch_todolist(request.user)
    todosjson=''
    donejson=''
    for todo in todos:
        todosjson=todosjson+"'%s':{'id':%d, 'highlight':%d}," % (str(todo),todo.id,int(todo.highlight))
    for done in dones:
        donejson=donejson+"'%s':{'id':%d, 'highlight':%d}," % (str(done),done.id,int(done.highlight))
    json='({\'ToDos\':{%s},\'Dones\':{%s}})' % (todosjson,donejson)
    return HttpResponse(json)
