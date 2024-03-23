from django.db import models
from django.utils import timezone

class HomePage(models.Model):
    home_image = models.ImageField(upload_to='home_images', blank=False, null=False)
    short_title = models.CharField(max_length=50, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.uploaded_by

class HomeHeaderImage(models.Model):
    first_image = models.ImageField(upload_to='home_header', blank=False)
    short_content = models.CharField(max_length=100, blank=False)
    second_image = models.ImageField(upload_to='home_header', blank=False)
    short_content_2 = models.CharField(max_length=100)
    third_image = models.ImageField(upload_to='home_header', blank=False)
    short_content_3 = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.uploaded_by, str(self.created_at)

class UserRegistration(models.Model):
    TITLE_CHOICES = [
        ('mr', 'Mr'),
        ('mrs', 'Mrs'),
        ('ms', 'Ms')
    ]
    title = models.CharField(default='select', choices=TITLE_CHOICES, max_length=5)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')), default='O')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Donation(models.Model):
    online_or_cash_choices = [
        ('online', 'Online Payment'),
        ('cash', 'Cash Payment'),
    ]

    TITLE_CHOICES = [
        ('mr', 'Mr'),
        ('mrs', 'Mrs'),
        ('ms', 'Ms')
    ]

    title = models.CharField(default='select', max_length=10, choices=TITLE_CHOICES)
    full_name = models.CharField(max_length=155, blank=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    donation_amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_method = models.CharField(blank=False, max_length=10, choices=online_or_cash_choices, default='online')
    payment_link = models.BooleanField(default=False)
    donation_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.payment_method == 'online':
            self.payment_link
        else:
            self.payment_link = None
        super().save(*args, **kwargs)


    def __str__(self):
        return f'Donnor Name {self.title}. {self.full_name} Amount sent: {self.donation_amount}'
    

class Region(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class AbuseType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ReportAbuse(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    child_name = models.CharField(max_length=255, blank=False)
    age = models.IntegerField(blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    abuse_type = models.ForeignKey(AbuseType, on_delete=models.CASCADE)
    town = models.CharField(max_length=100)
    support_needed = models.TextField(blank=False)
    sub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Reporter Name {self.name}\n Date Submitted {self.sub_date}"
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField(blank=False)
    content = models.TextField(max_length=500)


class Comment(models.Model):
    contct = models.ForeignKey(Contact, on_delete=models.CASCADE)
    full_text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Feed back from: {self.contct.name}, Email: {self.contct.email}"


class Donations(models.Model):
    name = models.CharField(max_length=500)
    amount_donated = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='donations')
    purpose = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    
class TotalDonation(models.Model):
    donation = models.ForeignKey(Donations, on_delete = models.CASCADE)
    amount_need = models.PositiveIntegerField()
    amount_received = models.PositiveIntegerField()
    amount_left = models.PositiveIntegerField()
    number_of_donations = models.IntegerField(default=0)

    def __str__(self):
        return f"Amount Needed = {self.amount_left}, Received: {self.amount_received}, Remaining: {self.amount_left}"
    
    def countDonation(self):
        self.number_of_donations += 1

    def add_donation(self, amount):
        self.amount_received  += amount

    
class Cause(models.Model):
    cause_background_image = models.ImageField(upload_to='cause_images')
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    amount_needed = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    amount_raised = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    amount_left = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    total_donations = models.IntegerField(default=0)
    weeks = models.IntegerField(default=0)
    start_date = models.DateTimeField(auto_now_add=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    
    def set_amount(self, amount):
        self.amount_raised = amount
        self.amount_left = self.amount_needed - self.amount_raised

        self.total_donations += 1

    def save(self, *args, **kwargs):
        if self.start_date < timezone.now():
            self.weeks += 1
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

class Event(models.Model):
    event_background_image = models.ImageField(upload_to="event_images", blank=False, default='voc.jpg')
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=155, unique=True, blank=False)
    short_content = models.CharField(max_length=255, blank=False, default='Write some something short')
    full_content = models.TextField(default='No content to read! ')

    def __str__(self) -> str:
        return self.title


class AboutPage(models.Model):
    about_backgroud_image = models.ImageField(upload_to="about_images", blank=False)
    title = models.CharField(max_length=100, blank=False, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class AboutTeam(models.Model):
    title = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=100, unique=True, blank=False)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about_team_images', default='adebayo.png')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}. {self.name}"
    

class MissionPage(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='mission_images')


    def __str__(self) -> str:
        return self.created_at


class PicturesGallery(models.Model):
    image = models.ImageField(upload_to='pictures', blank=False)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.title}, {self.created_by}"
    

class VideosGallery(models.Model):
    video = models.FileField(upload_to='videos')
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.title}, {self.created_by}"