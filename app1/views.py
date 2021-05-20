from django.shortcuts import render

# Create your views here.
def fnTest(request):
    return render(request,'test.html')

