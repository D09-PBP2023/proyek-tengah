from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from book_swap.models import BookSwap
from book_swap.forms import BookSwapForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from main.models import Book
from django.db.models import Q
# Create your views here.
@login_required(login_url='/login')
def request_book_swap(request):
    form = BookSwapForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.instance.user = request.user
        form.save()
        return HttpResponseRedirect(reverse('show_processed_book_swap'))
    context = {
        'form': form,}
    get_initial(request)
    return render(request, "request_swap.html", context)

def get_initial(request):
    return {"user": request.user.username}

@login_required(login_url='/login')
def show_processed_book_swap(request):
    swaps= BookSwap.objects.filter(user=request.user).filter(swapped=False)
    context = {
        'username':request.user.username, 
        'swaps':swaps,
    }
    return render(request, 'processed_book_swap.html', context)

@login_required(login_url='/login')
def show_queue_book_swap(request):
    swaps= BookSwap.objects.exclude(user=request.user).filter(swapped=False)
    context = {
        'username' : request.user.username, 
        'swaps': swaps,
    }
    return render(request, 'waiting_swap.html', context)

def search_key_waiting(request):
    if request.method == 'POST':  
        search_query = request.POST['search_query']
        swaps = BookSwap.objects.filter(Q(name__contains=search_query)| Q(user__contains=search_query)).filter(user=request.user).filter(swapped=False)
        return render(request, 'waiting_swap.html', {'query':search_query, 'swaps':swaps})
    else:
        return render(request, 'waiting_swap.html',{})
    
def show_json(request):
    data = BookSwap.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def show_accepted_book_swap(request):
    swaps= BookSwap.objects.all().filter(swapped=True).filter(user=request.user)
    context = {
        'username' : request.user.username, 
        'swaps': swaps,
    }
    return render(request, 'accepted_swap.html', context)

def accept_swap(request, id):
    p = BookSwap.objects.get(pk=id)
    p.acc_user = request.user.username
    p.swapped = True
    p.save()
    return HttpResponseRedirect(reverse('show_queue_book_swap'))

def get_processed_book_json(request):
    book_swap = BookSwap.objects.filter(user=request.user).filter(swapped=False)
    return HttpResponse(serializers.serialize('json', book_swap))
    
def search_key(request):
    if request.method == 'POST':  
        search_query = request.POST['search_query']
        swaps = BookSwap.objects.filter(Q(name__contains=search_query)| Q(user__contains=search_query)).filter(user=request.user).filter(swapped=False)
        context = {
            'username' : request.user.username, 
            'swaps': swaps,
        }
        return render(request, 'waiting_swap.html', context)
    else:
        swaps= BookSwap.objects.exclude(user=request.user).filter(swapped=False)
        context = {
            'username' : request.user.username, 
            'swaps': swaps,
        }
        return render(request, 'waiting_swap.html', context)

def cancel_swap(request, id):
    book_swap = BookSwap.objects.filter(user=request.user).filter(swapped=False).filter(pk=id)
    book_swap.delete()
    return HttpResponseRedirect(reverse('show_processed_book_swap'))

