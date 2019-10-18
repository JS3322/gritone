from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# from . < 같은 폴더 내의 models 임포트

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Cstom User Admin """
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
