from django.shortcuts import render
from app.models import MyModel

def my_view(request):
    models = MyModel.objects.all()
    return render(request, 'mytemplate.html', {'models': models})

