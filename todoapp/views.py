from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from .models import Task
from . forms import TaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class TaskListview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task1'
class TaskDetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'
class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvupdate',kwargs={'pk':self.object.id})
class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url=reverse_lazy('cbvdelete')

def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority,date=date)
        task.save()

    return render(request,'index.html',{'task1':task1})
    # return render(request,'index.html')
def details(request):
    task=Task.objects.all()
    return  render(request,"details.html",{'task':task})
def delete(request,id):
    if request.method == 'POST':
        movie=Task.objects.get(id=id)
        movie.delete()
        return redirect("/")
    return render(request,"delete.html")

def update(request,id):
    task=Task.objects.get(id=id)
    form=TaskForm(request.POST or None ,request.FILES,instance=task)
    if form.is_valid():
        form.save()
        return redirect("/")
    # return render(request,'edit.html')
    return render(request,'edit.html',{'form':form,'task':task})
