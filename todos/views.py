from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponseForbidden,HttpResponse,HttpResponseServerError
from words.todos.models import ToDo
from django.views.generic.simple import direct_to_template

def fetch_todolist(user):
    return (user.todos.filter(done=False),user.todos.filter(done=True)[:5])

def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/todos/login/')
    return direct_to_template(request,'todos/index.html')

def detail(request,todo_id):
    if not request.user.is_authenticated():
        return HttpRespenseRedirect('/todos/login/')
    todo=get_object_or_404(Todo,id=todo_id)
    if not todo.user.id==request.user.id:
        return HttpResponseForbidden() 
    return render_to_response('todos/detail.html',{'ToDo':todo})

def handle_todo(request,todo_id,done=None,highlight=None):
    if not request.user.is_authenticated():
        return HttpRespenseRedirect('/todos/login/')
    todo=get_object_or_404(ToDo,id=todo_id)
    if not request.user.id==todo.user.id:
        return HttpResponseForbidden()
    try:
        if done!=None:
            todo.done=done
        if highlight!=None:
            todo.highlight=highlight
        todo.save()
        return HttpResponse('0:SUCCESS')
    except:
        return HttpResponseServerError()

def new(request):
    if not request.user.is_authenticated():
        return HttpRespenseRedirect('/todos/login/')
    pass


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
        return HttpRespenseRedirect('/todos/login/')
    (todos,dones)=fetch_todolist(request.user)
    todosjson=''
    donejson=''
    for todo in todos:
        todosjson=todosjson+"'%s':{'id':%d, 'highlight':%d}," % (str(todo),todo.id,int(todo.highlight))
    for done in dones:
        donejson=donejson+"'%s':{'id':%d, 'highlight':%d}," % (str(done),done.id,int(done.highlight))
    json='({\'ToDos\':{%s},\'Dones\':{%s}})' % (todosjson,donejson)
    return HttpResponse(json,mimetype='text/json')
