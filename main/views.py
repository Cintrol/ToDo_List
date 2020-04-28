from django.shortcuts import render,redirect, reverse
from main.models import PurposeModel
from main.forms import PurposeForm, NewPurposeForm

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
    context = dict(purposes=purposes, user=request.user)
    return render(request, 'index.html', context)


def create_view(request):
    form = NewPurposeForm()
    if request.method == 'POST':
        form = NewPurposeForm(request.POST)
    success_url = reverse('main:main')
    if form.is_valid():
        form.save()
        return redirect(success_url)
    return render(request, "new_purpose.html", {'form':form})


def edit_view(request, pk):
    pass