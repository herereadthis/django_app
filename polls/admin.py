from django.contrib import admin
from polls.models import Choice, Poll

# Register your models here.
# customize the admin form by creating a model admin object, then pass it
# as the second argument to admin.site.register()
# inline: you can do TabularInline (saves space) or StackedInline


class ChoiceInline(admin.TabularInline):
    # Choice Model
    model = Choice
    # add extra fields
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {
                'fields': ['question']
            }),
        ('Date information',
            {
                'fields': ['pub_date'],
                # makes the makes the fieldset auto-hide
                'classes': ['collapse']
            }),
    ]
    # tells Django: choice objects are edited on the Poll admin page. By
    # default, provide enough field for 3 choices.
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')

admin.site.register(Poll, PollAdmin)
