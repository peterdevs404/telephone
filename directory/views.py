from django.shortcuts import render, redirect
from .models import Directory
from .forms import DirectoryForm
from django.urls import reverse
from django.contrib import messages

def index(request):
    context = {
        "contacts" : Directory.objects.all()
    }
    return render(request, 'directory/index.html', context)

def insert(request):
        form = DirectoryForm(request.POST or None, )
        context = {
            'form': form
        }
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect(reverse('index'))
        return render(request, 'directory/add.html', context)
    
def remove(request, id):
        telephone = Directory.objects.get(id=id)
        telephone.delete()
        messages.success(request, 'record deleted')
        return redirect(reverse('index'))

def amend(request, id):
        telephone = Directory.objects.get(id=id)
        form = DirectoryForm(request.POST or None,
                                            request.FILES or None, instance=telephone)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        return render(request, 'directory/delete.html', context)
