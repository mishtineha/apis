from django.contrib import admin
from app.models import Address,Profile
from django.utils.html import format_html

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    if Profile.profile_pic:
        list_display = ('Name','profile_pic_tag','gender',)
        readonly_fields = ('profile_pic_tag',)
    else:
        list_display = ('Name','gender',)
        
    list_filter = ('gender',)
    search_fields = ('Name',)
    def profile_pic_tag(self,obj):
        if obj.profile_pic.url:
            return format_html('<img src ="{}" width = "50" height = "50" />'.format(obj.profile_pic.url))
    #profile_pic_tag.allow_tags = True
    
    profile_pic_tag.short_description = 'profile_pic'
admin.site.register(Address)
admin.site.register(Profile,ProfileAdmin)

