from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if the password match or not
        if password == password2:
            # Check username is already exist or not
            if User.objects.filter(username=username).exists():  # if the username is already exist in the db
                messages.info(request, 'Username "' + username + '" is already taken!')
                return redirect('register')
            else:
                # Check email is already exists or not
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email ' + email + ' is being used')
                    return redirect('register')
                else:
                    # Looks good (email and username is unique)

                    user = User.objects.create(username=username,
                                               email=email, first_name=first_name, last_name=last_name)
                    user.set_password(password)  # we have to set the password externally
                    # as we are providing raw password...

                    # If want to automatically Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now looged in ')
                    # user.save()
                    # return redirect('index')

                    user.save()
                    print('user created.')
                    messages.success(request, 'You are now registered and can log in now!')
                    return redirect('login')

        else:
            messages.warning(request, 'Password did not match')
            return redirect('register')
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # checking username and password is matching or not. if not it will return None.
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)  # login the user
            print('user logged in.')
            messages.success(request, 'You are now logged in!')
            return redirect('dashboard')
        else:
            messages.warning(request, ' Invalid Credential!')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('user logged out.cccc')
        messages.success(request, 'You are logged out')
        return redirect('index')


def dashboard(request):
    # sending the contacts info filter by logged in user.
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        "user_contact": user_contacts,
    }
    return render(request, 'accounts/dashboard.html', context)
