from django.urls import path
from .views import individual_list, listings, search


urlpatterns = [
    path('', listings, name='listings'),
    path('<int:individual_list_id>', individual_list, name='individual_list'),
    path('search', search, name='search')

]