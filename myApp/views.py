from django.shortcuts import render

# Create your views here.
def templetes_view(request):
    return render(request,'myApp/1.html')