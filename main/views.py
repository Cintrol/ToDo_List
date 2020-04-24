from django.shortcuts import render


# Create your views here.
#("work", True),
#("home", False),
#("learn", True)

data = {
    'lists':[
        {'name': 'work', 'is_done': False},
        {'name': 'home', 'is_done': False},
        {'name': 'learn','is_done' : True}
    ],
    'user_name': 'admin'
}

#for list, in_done in data['lists']:
#    name = list[0]
#    is_done = list[1]

def main_view(request):
    context = data
    return render(request, 'index.html', context)
