from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from .forms import *
from .models import *

def home_view(request):
    main_home_contents = HomePage.objects.all()
    home_header = HomeHeaderImage.objects.first()
    pictures = PicturesGallery.objects.all()[:5]
    videos = VideosGallery.objects.all()[:5]
    events = Event.objects.all()[:3]
    causes = Cause.objects.all()[:3]

    return render(request, 'main/index.html', {'main_home_contents': main_home_contents, 'pictures': pictures, 'videos': videos, 'events': events, 'causes': causes, 'home_header': home_header})

def donateform_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.sub_date = timezone.now()
            donation.save()
            messages.success('Donation Successfully Sent')
            return redirect('thank_you')
        else:
            messages.success("Dontion couldn't compplete! ")
    else:
        form = DonationForm()
    return render(request, 'forms/donate_form.html', {'form': form})

def contact_view(request):
    contact_info = ChangeContactInfo()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success('Successfully Submitted')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form, "contact_info": contact_info})

def donations(request):
    return render(request, 'main/donate.html')

def causes_view(request):
    causes = Cause.objects.all()
    return render(request, 'main/causes.html', {'causes': causes})

def register_view(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreateForm()
        
    context = {'form': form}

    return render(request, 'forms/register.html', context)

def about_view(request):
    aboutpage = AboutPage.objects.all()
    aboutteam = AboutTeam.objects.all()
    
    return render(request, 'main/about.html', {'aboutpage': aboutpage, 'aboutteam': aboutteam})

def mission_view(request):
    mission = MissionPage.objects.first()

    return render(request, 'main/mission.html', {'mission': mission})

def gallery_view(request):
    pictures = PicturesGallery.objects.all()
    videos = VideosGallery.objects.all()

    return render(request, 'main/gallery.html', {'pictures': pictures, 'videos': videos})

def event_list_view(request):
    events = Event.objects.order_by('-date')

    return render(request, 'main/event.html', {'events': events})

def event_detail_view(request, event_id):
    events_detail = get_object_or_404(Event, pk=event_id)

    return render(request, 'main/event_detail.html', {'events_detail': events_detail})