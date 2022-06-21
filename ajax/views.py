from django.http import HttpResponse
from django.shortcuts import render

from ajax.models import Post

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def create(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        success = "Email : " + email + " & password : " + password
        return HttpResponse(success)

def create_post(request):
    posts = Post.objects.all()
    response_data = {}

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']    
        response_data['email'] = email
        response_data['password'] = password

        Post.objects.create(
            email = email,
            password = password
        )

        success = 'Login : ' + email + ' & Password : ' + password 

        return HttpResponse(success)

    return render(request, 'signup.html')
