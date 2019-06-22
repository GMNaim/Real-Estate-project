from django.urls import path
from .views import individual_list, listings, search


urlpatterns = [
    path('', listings, name='listings'),
    path('<int:individual_list_id>', individual_list, name='individual list url'),
    # when we pass url like above then we need to pass this as a parameter of the connected method in view.
    # Here, we have to use individual_list_id as parameter of individual_list method in view.
    path('search', search, name='search')

]