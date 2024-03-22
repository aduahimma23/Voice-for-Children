from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('mission/', mission_view, name='mission'),
    path('gallery/', gallery_view, name='gallery'),
    path('donate', donateform_view, name='donate'),
    path('contact/', contact_view, name='contact'),
    path('donation/', donations, name='donations'),
    path('causes/', causes_view, name='causes'),
    path('register/', register_view, name='register'),
    path('event/', event_list_view, name='event'),
    path('event/<int:event_id>/', event_detail_view, name='event_detail'),
]