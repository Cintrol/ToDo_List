from django.shortcuts import render, redirect, reverse
from list_item.models import TaskModel
from list_item.forms import NewTaskForm
from main.models import PurposeModel


# Create your views here.

def list_item_view(request, pk=0):
    """
    Отрисовка главной страницы = список задач
    """
    user = request.user
    tasks = TaskModel.objects.filter(
        purpose_id=pk
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
    pass


def create_list_view(request, pk):
    """ Создать новую задачу """
    user = request.user
    form = NewTaskForm()

    if request.method == 'POST':
        form = NewTaskForm(request.POST)
    success_url = reverse('main:main')
    if form.is_valid():
        plus_user = form.save(commit=False)
        plus_user.user = request.user
        plus_user.save()
        return redirect(success_url)
    return render(request, "new_purpose.html", {'form': form})
