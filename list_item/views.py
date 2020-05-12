from django.shortcuts import render, redirect, reverse
from list_item.models import TaskModel
from list_item.forms import NewTaskForm, EditTaskForm
from main.models import PurposeModel
from django.http import HttpResponseRedirect, HttpResponseNotFound


# Create your views here.

def list_item_view(request, pk):
    """
    Отрисовка главной страницы = список задач
    """
    user = request.user
    tasks = TaskModel.objects.filter(
        purpose=pk
    ).order_by(
        'created'
    )
    purpose_name = PurposeModel.objects.filter(id=pk).first()
    context = {
        'tasks': tasks,
        'user': user,
        'purpose': purpose_name
    }
    return render(request, 'list.html', context)


def edit_list_view(request, pk):
    form = EditTaskForm

    try:
        edit_task = TaskModel.objects.get(id=pk)
        if request.method == 'POST':
            edit_task.name = request.POST.get('name')
            edit_task.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_task.html", {'form': form, 'pk':pk})
    except PurposeModel.DoesNotExist:
        return HttpResponseNotFound("<h2>'Запись не обнаружена</h2>")


def create_list_view(request, pk):
    """ Создать новую задачу """

    form = NewTaskForm()

    if request.method == 'POST':
        form = NewTaskForm(request.POST)
    success_url = reverse('list_item:list_item', kwargs={'pk': pk})
    if form.is_valid():
        plus_purpose = form.save(commit=False)
        plus_purpose.purpose = PurposeModel.objects.filter(id=pk).first()
        plus_purpose.save()
        return redirect(success_url)
    return render(request, "new_task.html", {'form': form, 'pk':pk})
