from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .choices import state_choices, bedroom_choices, price_choices
from .models import IndividualListInformation


def listings(request):
    """ This method is showing all the listings details """
    # listings_info = IndividualListInformation.objects.all()
    listings_info = IndividualListInformation.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings_info, 2)
    page = request.GET.get('page')
    paged_listings_info = paginator.get_page(page)

    context = {'listings': paged_listings_info
               }

    return render(request, 'listings/listings.html', context)


def individual_list(request, individual_list_id):
    # it is sending the individual listing page id with all of its description
    # or if the page is not available it will show a 404 page.
    # We are passing here the model name and the listing id which we got from the url
    individual_listing_description = get_object_or_404(IndividualListInformation, pk=individual_list_id)
    context = {
        'individual_listing_description': individual_listing_description,

    }

    return render(request, 'listings/individual_list.html', context)


def search(request):
    queryset_list = IndividualListInformation.objects.order_by('-list_date')

    # Matching the 'keyword' from the search
    if 'keywords' in request.GET:  # if the GET request contain 'keywords'
        keywords = request.GET['keywords']  # get the value of the keywords's key in the keywords variable
        if keywords:  # if the keywords is not empty
            # searching any word in the description typed in the keyword box
            # for searching in the paragraph do like below.( description__icontains=keywords )
            # its searching the paragraph that contain the keyword or not
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Matching the city form the search
    if 'city' in request.GET:
        city = request.GET['city']  # getting the value of city key from the get request
        if city:  # if city have any value
            # city__iexact is for case-insensitive filtering (__iexact)
            queryset_list = queryset_list.filter(city__iexact=city)

    # Matching the state from the search
    if 'state' in request.GET:
        state = request.GET['state']  # getting the value(actually key as we pass state=key)
        # of state from the search request
        if state:
            state_value = state_choices.get(state)
            queryset_list = queryset_list.filter(state__iexact=state_value)

    # Matching the bedrooms from search
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:        # bedrooms__lte means less than or equal
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms).order_by('-bedrooms')

    # Matching the price from search
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price).order_by('-price')

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings': queryset_list,
        'request_values': request.GET,
    }

    return render(request, 'listings/search.html', context)
