from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List
# Create your views here.


def home_page(request):
    # use httpresponse
    # return HttpResponse('<html><title>To-Do lists</title>')

    # Otherwise we can use render, The first object is the request object,
    # the second is the templates name
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return render(request, 'home.html')

    #return render(request, 'home.html', {'new_item_text': request.POST.['item_text'], })

    # # version 2
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()
    #
    # return render(request, 'home.html', {
    #     'new_item_text': item.text,
    # })

    # version 3
    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     # by using create, we dont have to use save()
    #     return redirect('/lists/the-only-list-in-the-world/')

    return render(request, 'home.html',)


def view_list(request, list_id):

    # version 1
    # items = Item.objects.all()

    # # version 2
    # list_ = List.objects.get(id=list_id)
    # items = Item.objects.filter(list=list_)
    # return render(request, 'list.html', {'items': items})

    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_list(request):

    # This view is just like a redirect station i think
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % list_.id, )

def add_item(request, list_id):

    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % list_.id, )
