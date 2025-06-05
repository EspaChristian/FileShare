from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadFile
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'FileShare_App/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def home(request):
    files = UploadFile.objects.all().order_by('-id') 
    return render(request, 'FileShare_App/home.html', {'files': files})


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'FileShare_App/upload.html', {'form': form})
 

def upload_success(request):
    return render(request, 'FileShare_App/success.html')


def delete_file(request, file_id):
    file = get_object_or_404(UploadFile, id=file_id)
    file.delete()
    return redirect('home')