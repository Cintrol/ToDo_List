from django.shortcuts import render


# Create your views here.

ddata = {
    'lists':[
        {'name': 'Купить шарики', 'is_done': False, 'date': '01.02.1998'},
        {'name': 'Заказать торт', 'is_done': False, 'date': ''},
        {'name': 'Купить подарок','is_done': True, 'date': '03.09.1905'}
    ],
    'user_name': 'admin'
}


def list_item_view(request):
    context = ddata
    return render(request, 'list.html', context)
