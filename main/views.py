from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {} # empty
    return render(request, "main.html", context)