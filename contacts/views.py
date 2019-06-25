from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        user_id = request.POST['user_id']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        # Check if user has made an inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            haa_connected = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if haa_connected:
                messages.warning(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact_info = Contact(listing=listing, listing_id=listing_id, name=name, phone=phone, email=email,
                               message=message, user_id=user_id)

        contact_info.save()

        # Sending Email (for gmail)
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Please sign into your account for more info.',
            'gmnaim3336@gmail.com',
            [realtor_email],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a realtor '
                                  'will get back to you soon.')
        return redirect('/listings/'+listing_id)
