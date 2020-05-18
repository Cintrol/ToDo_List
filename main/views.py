from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from main.models import PurposeModel
from main.forms import PurposeForm, NewPurposeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib.auth import logout
from todo_list.settings import PAGE_COUNT

@login_required(login_url='/registration/login/')
def main_view(request, pk=0):
    """
    Отрисовка главной страницы = список целей
    """
    user = request.user
    purposes = PurposeModel.objects.filter(
        user=user,
    ).order_by(
        'created'
    )
    paginator = Paginator(purposes, PAGE_COUNT)
    page = request.GET.get('page')

    try:
        purposes_page = paginator.page(page)
    except PageNotAnInteger:
        purposes_page = paginator.page(1)
    except EmptyPage:
        purposes_page = paginator.page(paginator.num_pages)

    context = dict(purposes=purposes_page.object_list, user=user.username, pages=list(paginator.page_range))
    return render(request, 'index.html', context)

@login_required(login_url='/registration/login/')
def create_view(request):
    form = NewPurposeForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        form = NewPurposeForm({
            'name':name,
            'user':request.user
        })
    success_url = reverse('main:main')
    if form.is_valid():
        form.save()
        return redirect(success_url)
    return render(request, "new_purpose.html", {'form':form})

@login_required(login_url='/registration/login/')
def edit_view(request, pk):
    form = PurposeForm

    try:
        edit_purpose = PurposeModel.objects.get(id=pk)
        if request.method == 'POST':
            edit_purpose.name = request.POST.get('name')
            edit_purpose.save()
            return redirect(reverse('main:main'))
        else:
            return render(request, "edit_purpose.html", {'form': form})
    except PurposeModel.DoesNotExist:
        return HttpResponseNotFound("<h2>'Запись не обнаружена</h2>")


def delete_view(request, pk):
    try:
        delete_purpose = PurposeModel.objects.get(id=pk)
        delete_purpose.delete()
        return redirect(reverse('main:main'))
    except PurposeModel.DoesNotExist:
        return HttpResponseNotFound("<h2>'Запись не обнаружена</h2>")



