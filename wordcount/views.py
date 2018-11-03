from django.http import HttpResponse
from django.shortcuts import render
'''
def homepage(request):
    return render(request,'home.html')
'''
'''
def homepage(request):
    return render(request,'wordcount/home.html')
'''

def contact(request):
    return HttpResponse("<h1>This is our contact page</h1><br>My name is Ajay Kumar Yadav")
