from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

from app1.forms import UserForm
from app1.models import UserModel

def viewAll(request):
    k = UserModel.objects.all();
    return render(request, 'list.html', {'list': k})

def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.save()
            k = UserModel.objects.all();
            return render(request, 'list.html', {'list': k})
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form})

def edit(request):
    id=request.GET['id']
    post = UserModel.objects.get(id=id)
    form = UserForm(instance=post)
    return render(request, "edit.html", {"form": form})
def editform(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form = UserModel.objects.filter(id=form.cleaned_data['id']).update(username=form.cleaned_data['username'],fruit=form.cleaned_data['fruit'])
            k = UserModel.objects.all();
            return render(request, 'list.html', {'list': k})
            
            #https://django.readthedocs.io/en/stable/topics/forms/modelforms.html
