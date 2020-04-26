from django.shortcuts import render
from main.models import ListModel

def main_view(request, pk=0):
    lists = ListModel.objects.all()
    lists_one = ListModel.objects.get(name='Learn')
    lists_filter = ListModel.objects.filter(name='Learn')
    context = dict(lists=lists, user=request.user)
    return render(request, 'index.html', context)


def edit_view(request, pk):
   return 'hello'
