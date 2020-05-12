from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from main.models import PurposeModel
from main.forms import PurposeForm, NewPurposeForm
from list_item.views import list_item_view
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


PAGE_COUNT = 6

@login_required(login_url='registration/login/')
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
    page = paginator.num_pages
    try:
        purposes_page = paginator.page(page)
    except PageNotAnInteger:
        purposes_page = paginator.page(1)
    except EmptyPage:
        purposes_page = paginator.page(paginator.num_pages)
    context = dict(purposes=purposes, user=request.user, page=page)
    return render(request, 'index.html', context)


def create_view(request):
    user = request.user
    form = NewPurposeForm()
    if request.method == 'POST':
        form = NewPurposeForm(request.POST)
    success_url = reverse('main:main')
    if form.is_valid():
        plus_user = form.save(commit=False)
        plus_user.user = request.user
        plus_user.save()
        return redirect(success_url)
    return render(request, "new_purpose.html", {'form':form})


def edit_view(request, pk):
    form = PurposeForm

    try:
        edit_purpose = PurposeModel.objects.get(id=pk)
        if request.method == 'POST':
            edit_purpose.name = request.POST.get('name')
            edit_purpose.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_purpose.html", {'form': form})
    except PurposeModel.DoesNotExist:
        return HttpResponseNotFound("<h2>'Запись не обнаружена</h2>")


def delete_view(request, pk):
    try:
        delete_purpose = PurposeModel.objects.get(id=pk)
        delete_purpose.delete()
        return HttpResponseRedirect("/")
    except PurposeModel.DoesNotExist:
        return HttpResponseNotFound("<h2>'Запись не обнаружена</h2>")


def to_list_view(request, pk):
    return render(request, 'list.html', pk)
