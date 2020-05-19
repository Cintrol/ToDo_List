from django.shortcuts import render, redirect, reverse
from list_item.models import TaskModel
from list_item.forms import TaskForm
from main.models import PurposeModel
from django.http import HttpResponseRedirect, HttpResponseNotFound, \
    HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
import json

PAGE_COUNT = 6


@login_required(login_url='/registration/login/')
def list_item_view(request, pk):
    """
    Отрисовка главной страницы = список задач
    """
    user = request.user
    tasks = TaskModel.objects.filter(
        purpose=pk,
    ).order_by(
        '-created'
    )
    purpose_name = PurposeModel.objects.filter(id=pk).first()
    paginator = Paginator(tasks, PAGE_COUNT)
    page = request.GET.get('page')
    try:
        tasks_page = paginator.page(page)
    except PageNotAnInteger:
        tasks_page = paginator.page(1)
    except EmptyPage:
        tasks_page = paginator.page(paginator.num_pages)
    if purpose_name in PurposeModel.objects.filter(user=user):
        context = {
            'tasks': tasks_page.object_list,
            'user': user,
            'purpose': purpose_name,
            'pages': list(paginator.page_range)
        }
        return render(request, 'list.html', context)
    return HttpResponseNotFound("<h2>Запись не обнаружена</h2>")


@login_required(login_url='/registration/login/')
def edit_list_view(request, pk):
    edit_task = TaskModel.objects.get(id=pk)
    purpose_id = edit_task.purpose_id
    try:

        if request.method == 'POST':
            edit_task.name = request.POST['name']
            edit_task.expare_date = request.POST['expare_date']
            edit_task.save()
            success_url = reverse('list_item:list_item',
                                  kwargs={'pk': purpose_id})
            return redirect(success_url)
        else:
            form = TaskForm
            return render(request, "edit_task.html",
                          {'form': form, 'pk': pk, 'purpose_id': purpose_id})
    except PurposeModel.DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не обнаружена</h2>")


@login_required(login_url='/registration/login/')
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
        if form.is_valid():
            form.save()
            return redirect(success_url)
    return render(request, "new_task.html", {'form': form, 'pk': pk})


@login_required(login_url='/registration/login/')
def delete_list_view(request, pk):
    if request.method == 'POST':
        delete_task = TaskModel.objects.get(id=pk)

        delete_task.delete()
        return HttpResponse(status=201)
    return HttpResponse(status=404)


@login_required(login_url='/registration/login/')
def done_view(request):
    data = json.loads(request.body.decode())
    pk = int(data.get('id'))
    task = TaskModel.objects.get(id=pk)
    value = not task.is_done
    task.is_done = value
    task.save()
    return HttpResponse(status=201)


def all_done_view(request):
    data = json.loads(request.body.decode())
    pk = int(data.get('id'))
    purpose_ = PurposeModel.objects.get(id=pk).is_done
    tasks = TaskModel.objects.filter(purpose_id=pk)
    for task in tasks:
        if purpose_:
            task.is_done = False
        else:
            task.is_done = True
        task.save()
    if purpose_:
        # если purpose.is_done была истина, то теперь False и блоки нужно убрать
        return HttpResponse(status=201)
    else:
        # или добавить
        return HttpResponse(status=202)
