from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def index_page(request):
    contex= {}
    return render(request,'user_example/index.html',contex)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] # note the password file has name: password1

            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('index_page')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request,'registration/register.html',context)
