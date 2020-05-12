from django.shortcuts import render, redirect, reverse
from list_item.models import TaskModel
from list_item.forms import TaskForm
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

    edit_task = TaskModel.objects.get(id=pk)
    purpose_id = edit_task.purpose_id
    try:

        if request.method == 'POST':
            edit_task.name = request.POST['name']
            edit_task.expare_date = request.POST['expare_date']
            edit_task.save()
            success_url = reverse('list_item:list_item',kwargs={'pk': purpose_id})
            return redirect(success_url)
        else:
            form = TaskForm
            return render(request, "edit_task.html", {'form': form, 'pk':pk})
    except PurposeModel.DoesNotExist:
        return HttpResponseNotFound("<h2>'Запись не обнаружена</h2>")


def create_list_view(request, pk):
    """ Создать новую задачу """
    form = TaskForm()
    success_url = reverse('list_item:list_item', kwargs={'pk': pk})
    if request.method == 'POST':
        form = TaskForm({
            'name': request.POST['name'],
            'expare_date': request.POST['expare_date'],
            'purpose': pk
        })
        form.save()
        return redirect(success_url)
    return render(request, "new_task.html", {'form': form, 'pk':pk})

def delete_list_view(request, pk):
    try:
        delete_task = TaskModel.objects.get(id=pk)
        purpose_id = delete_task.purpose_id
        delete_task.delete()
        success_url = reverse('list_item:list_item', kwargs={'pk': purpose_id})
        return redirect(success_url)
    except PurposeModel.DoesNotExist:
        return HttpResponseNotFound("<h2>'Запись не обнаружена</h2>")

