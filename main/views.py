from django.shortcuts import render


# Create your views here.
#("work", True),
#("home", False),
#("learn", True)

data = {
    'lists':[
        {'id':1, 'name': 'work', 'is_done': False},
        {'id':2, 'name': 'home', 'is_done': False},
        {'id':3, 'name': 'learn','is_done' : True}
    ],
    'user_name': 'admin'
}

#for list, in_done in data['lists']:
#    name = list[0]
#    is_done = list[1]

def main_view(request, pk=0):
    context = data
    return render(request, 'index.html', context)

def edit_view(request, pk):
   return 'hello'
