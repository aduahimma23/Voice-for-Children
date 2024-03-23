from django.contrib import admin
from .models import *


admin.site.register(HomeHeaderImage)
admin.site.register(AboutPage)
admin.site.register(AboutTeam)
admin.site.register(HomePage)
admin.site.register(Region)
admin.site.register(AbuseType)
admin.site.register(MissionPage)
admin.site.register(PicturesGallery)
admin.site.register(VideosGallery)

class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender')
    list_filter = ('gender', 'title')
    search_fields = ('first_name', 'last_name', 'email', 'gender')

admin.site.register(UserRegistration, UserRegistrationAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_text', 'sent_at')
    list_filter = ('full_text', 'sent_at')

admin.site.register(Comment, CommentAdmin)


class DonationAdmin(admin.ModelAdmin):
    list_display = ('title', 'full_name', 'donation_amount')
    list_filter = ('title', 'full_name', 'donation_amount')
    search_fields = ('title', 'full_name', 'donation_amount')

admin.site.register(Donation, DonationAdmin)

class CausesAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_date', 'total_donations')
    list_filter = ('posted_date', 'total_donations')
    search_fields = ('title', 'posted_date', 'total_donations')

admin.site.register(Cause, CausesAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_content')
    search_fields = ('title', '')

admin.site.register(Event, EventAdmin)

class ReportAbuseAdmin(admin.ModelAdmin):
    list_display = ('child_name', 'sub_date')
    readonly_fields = ('sub_date',)

admin.site.register(ReportAbuse, ReportAbuseAdmin)
