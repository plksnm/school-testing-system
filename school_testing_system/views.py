from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from .models import Tasks
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import render

def first_page(request):
    return render(request, 'school_testing_system/first_page.html', {})


def tasks_list(request):
    tlist = Tasks.objects.all()
    template = loader.get_template('school_testing_system/tasks_list.html')
    context = {
        'tlist': tlist,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'school_testing_system/tasks_list.html', {})


def task(request, task_id):
    task = Tasks.objects.get(pk = task_id)
    template = loader.get_template('school_testing_system/task.html')
    context = {
        'task':task,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'school_testing_system/tasks_list.html', {})


def login(request):
    return render(request, 'school_testing_system/login.html', {})

def register(request):

    return render(request, 'school_testing_system/register.html', {})

def createUser_render(request, error, username = "", email = "", password = ""):
    return render(request, 'school_testing_system/register.html', {'error': error, 'username':username, 'email':email, 'password': password})

@csrf_exempt
def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:

        #return render(request, 'school_testing_system/tasks_list.html', {})
        return tasks_list(request)
        # Redirect to a success page.
    else:
        # Return an 'invalid login' error message.
        return render(request, 'school_testing_system/login.html', {'error' : True})

@csrf_exempt
def createUser(request):
    error = {
            'login': "",
            'email': "",
            'password': "",
        }
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    email = request.POST.get('email', None)
    if username == None and password == None:
        return createUser_render(request = request, error = error)
    if len(password) < 8:
        error['password'] = "Минимальная длина пароля 8 символов!"
        return createUser_render(request, error, username, email)
    user, created = User.objects.get_or_create(username = username, email = email)
    if created:
        user.set_password(password)
        user.save()
        return render(request, 'school_testing_system/login.html', {'error': error})
    else:
        error['login'] = "Такой пользователь уже существует"
        return createUser_render(request, error, "", email, password)

@csrf_exempt
def testing(request, task_id):
    task = Tasks.objects.get(pk = task_id)
    template = loader.get_template('school_testing_system/task.html')
    context = {
        'task':task,
        's':"ok"
    }
    return HttpResponse(template.render(context, request))
