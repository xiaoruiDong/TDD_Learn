from django.shortcuts import render
from django.http import HttpResponse
from lists.models import Item
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
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        # by using create, we dont have to use save()
        Item.objects.create(text=new_item_text)
    else:
        new_item_text = ''

    return render(request, 'home.html', {'new_item_text': new_item_text})
