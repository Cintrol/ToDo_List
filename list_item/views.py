from django.shortcuts import render
from list_item.models import TaskModel

# Create your views here.

def list_item_view(request, pk=0):
    """
    Отрисовка главной страницы = список задач
    """
    user = request.user
#    purpose =
    tasks = TaskModel.objects.filter(
        user=user
    ).order_by(
        'created'
    )
    context = dict(tasks=tasks, user=request.user)
    return render(request, 'index.html', context)

