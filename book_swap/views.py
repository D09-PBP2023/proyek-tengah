from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse  
from django.urls import reverse
from book_swap.models import BookSwap
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from main.models import Book
from django.db.models import Q
import json
from django.core.serializers import serialize

def get_model_data(request):
    data = serialize('json', Book.objects.all())
    return JsonResponse(data, safe=False)

def get_specified_book_json(request, id):
    data = serialize('json', Book.objects.filter(pk=id))
    return JsonResponse(data, safe=False)

def delete_all_swap(request):
    BookSwap.objects.all().delete()
    return HttpResponse('deleted')

# create Book Swap
@login_required(login_url='/login')
def create_swap(request):
    if request.method == 'POST':
        import json
        post_data = json.loads(request.body.decode("utf-8"))
        ownedbook = post_data.get('ownedbook')
        wantedbook = post_data.get('wantedbook')
        frommessage = post_data.get('message')
        #print(from_user, ownedbook, wantedbook, frommessage)
        new_product = BookSwap.objects.create(
            from_user = request.user.username,
            have_book = ownedbook,
            from_message = frommessage,
            want_book = wantedbook,
        )
        new_product.save()
        return HttpResponseRedirect(reverse('book_swap:show_processed_book_swap'))
    
    return HttpResponseNotFound()


def show_create_swap(request):
    list_all_book = Book.objects.all()  
    return render(request, 'create_swap_page.html', {'username':request.user.username, 
                                                'list_all_book':list_all_book,})

@login_required(login_url='/login')
def show_processed_book_swap(request):
    swaps= BookSwap.objects.filter(from_user=request.user).filter(swapped=False)
    context = {
        'username':request.user.username, 
        'swaps':swaps,
    }
    return render(request, 'processed_book_swap.html', context)

@login_required(login_url='/login')
def show_queue_book_swap(request):
    swaps= BookSwap.objects.exclude(from_user=request.user).filter(swapped=False)
    context = {
        'username' : request.user.username, 
        'swaps': swaps,
    }
    return render(request, 'waiting_swap.html', context)

def search_key_waiting(request):
    if request.method == 'POST':  
        search_query = request.POST['search_query']
        swaps = BookSwap.objects.filter(Q(name__contains=search_query)| Q(from_user__contains=search_query)).filter(from_user=request.user).filter(swapped=False)
        return render(request, 'waiting_swap.html', {'query':search_query, 'swaps':swaps})
    else:
        return render(request, 'waiting_swap.html',{})
    
def show_json(request):
    data = BookSwap.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def show_accepted_book_swap(request):
    swaps= BookSwap.objects.all().filter(swapped=True).filter(from_user=request.user)
    context = {
        'username' : request.user.username, 
        'swaps': swaps,
    }
    return render(request, 'accepted_swap.html', context)

def accept_swap(request):
    if request.method == 'POST':
        swaps = BookSwap.objects.all().filter(processed=False)
        acceptedSwap = swaps.get(pk=request.POST.get('id'))
        acceptedSwap.processed = True
        acceptedSwap.to_user = request.user.username
        acceptedSwap.to_message = request.POST.get('message')
        acceptedSwap.save()
        return HttpResponseRedirect(reverse('book_swap:show_processed_book_swap'))

    
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
@csrf_exempt
def cancel_swap(request):
    if request.method == 'POST':
        swaps = BookSwap.objects.filter(from_user = request.user).filter(swapped=False)
        deletedSwaps = swaps.get(pk=request.POST.get('id'))
        print(request.POST.get('id'))
        deletedSwaps.delete()
        return HttpResponseRedirect(reverse('book_swap:show_processed_book_swap'))

# Processed Book Swap JSON
def get_processed_book_json(request):
    book_swap = BookSwap.objects.filter(swapped=False).filter(from_user=request.user.username)
    return HttpResponse(serializers.serialize("json", book_swap),
        content_type="application/json")
# Waiting Accept Book Swap JSON
def get_waiting_accept_book_json(request):
    book_swap = BookSwap.objects.exclude(from_user=request.user).filter(processed=False).filter(swapped=False)
    return HttpResponse(serializers.serialize("json", book_swap),
        content_type="application/json")
# Accepted Book Swap JSON
def get_accepted_book_json(request):
    book_swap = BookSwap.objects.filter(from_user=request.user).filter(processed=True)
    return HttpResponse(serializers.serialize("json", book_swap),
        content_type="application/json")
# Finished Book Swap JSON
def get_finished_book_json(request):
    book_swap = BookSwap.objects.filter(from_user=request.user).filter(swapped=True)
    return HttpResponse(serializers.serialize("json", book_swap),
        content_type="application/json")

# Create Book Swap
@login_required
@csrf_exempt
def create_swap_mobile(request):
    if request.method == 'POST':
        ownedbook = request.POST.get('bookid')
        wantedbook = request.POST.get('bookid2')
        frommessage = request.POST.get('message')
        new_product = BookSwap.objects.create(
            from_user = request.user.username,
            have_book = ownedbook,
            from_message = frommessage,
            want_book = wantedbook,
        )
        new_product.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
# Accept Book Swap
@login_required
@csrf_exempt
def cancel_swap_mobile(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        book_swap = BookSwap.objects.filter(swapped=False).filter(from_user=request.user.username)
        book_swap.get(pk=id).delete()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
# Accept Book Swap
@login_required
@csrf_exempt
def accept_swap_mobile(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        book_swap = BookSwap.objects.exclude(from_user=request.user).filter(processed=False).filter(swapped=False)
        acceptedSwap = book_swap.get(pk=id)
        acceptedSwap.processed = True
        acceptedSwap.to_user = request.user.username
        acceptedSwap.to_message = request.POST.get('message')
        acceptedSwap.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

# Finish Book Swap
@login_required
@csrf_exempt
def finish_swap_mobile(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        book_swap = BookSwap.objects.filter(from_user=request.user).filter(processed=True)
        acceptedSwap = book_swap.get(pk=id)
        acceptedSwap.swapped = True
        acceptedSwap.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
