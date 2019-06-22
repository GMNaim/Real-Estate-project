from django.shortcuts import render
from listings.models import IndividualListInformation
from realtors.models import RealtorInformation
from listings.choices import bedroom_choices, state_choices, price_choices


def index(request):
    home_page_listings = IndividualListInformation.objects.order_by('-list_date').filter(is_published=True)[:3]  # for first 3 data
    context = {
        'home_page_listings': home_page_listings,
        'state_choices': state_choices,
        'bedromm_choices': bedroom_choices,
        'price_choices': price_choices,

    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Getting all realtors
    realtors = RealtorInformation.objects.order_by('-hire_date')

    # getting MVP(seller of the month)

    mvp_realtors = RealtorInformation.objects.all().filter(is_mvp=True)

    context = {
        "realtors": realtors,
        "mvp_realtors": mvp_realtors
    }
    return render(request, 'pages/about.html', context)
