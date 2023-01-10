from django.shortcuts import render

def parent(request):
    return render(request,'parent.html')


def child(request):
    return render(request,'child.html')

    
