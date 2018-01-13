from django.contrib import admin
from .models import UserProfileInfo


class UserProfileInfoAdmin(admin.ModelAdmin):
    fields = ('user', 'point', )
    readonly_fields = ('user', )


admin.site.register(UserProfileInfo, UserProfileInfoAdmin)