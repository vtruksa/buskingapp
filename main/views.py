from django.shortcuts import render

def homeView(request):
    context={}
    return render(request, '_base.html', context)