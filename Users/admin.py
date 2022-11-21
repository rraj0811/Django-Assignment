from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import User

from Cars.models import otherDetails
from .models import Profile
from .forms import UserRegisterForm

admin.site.register(Profile)
admin.site.register(otherDetails)

class UserRegisterForm(admin.ModelAdmin):

    form = UserRegisterForm

    fieldsets = (
        (None, {
            'fields' : ('username', 'email', 'address', 'phone', 'passowrd1', 'password2',)
        }),
    )
