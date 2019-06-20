from django.shortcuts import render
# Create your views here.


def listings(request):
    return render(request, 'listings/listings.html')


def individual_list(request):
    return render(request, 'listings/individual_list.html')


def search(request):
    return render(request, 'listings/search.html')

