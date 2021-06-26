from django.contrib import admin
from .models import Brand, Display_type, Post, Display_dioganal, Memory_type, Ram_type, Battery_type, Phones
from user.models import User


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

    list_display = [
        'id',
        'username',
        'first_name',
        'last_name',
        'date_joined',
        'is_staff'
    ]


admin.site.register(User, UserAdmin)


class PhonesAdmin(admin.ModelAdmin):
    class Meta:
        model = Phones

    list_display = [
        'id',
        'name',
        'brand_id'
    ]

admin.site.register(Phones, PhonesAdmin)


class BrandAdmin(admin.ModelAdmin):
    class Meta:
        model = Brand

    list_display = [
        'id',
        'name'
    ]


admin.site.register(Brand, BrandAdmin)


class Display_typeAdmin(admin.ModelAdmin):
    class Meta:
        model = Display_type

    list_display = [
        'id',
        'name'
    ]


admin.site.register(Display_type, Display_typeAdmin)


class Memory_typeAdmin(admin.ModelAdmin):
    class Meta:
        model = Memory_type

    list_display = [
        'id',
        'name'
    ]


admin.site.register(Memory_type, Memory_typeAdmin)


class Display_dioganalAdmin(admin.ModelAdmin):
    class Meta:
        model = Display_dioganal

    list_display = [
        'id',
        'name'
    ]


admin.site.register(Display_dioganal, Display_dioganalAdmin)


class RamAdmin(admin.ModelAdmin):
    class Meta:
        model = Ram_type

    list_display = [
        'id',
        'name'
    ]

admin.site.register(Ram_type, RamAdmin)


class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post

    list_display = [
        'id',
        'subject',
        'content',
        'image'
    ]


admin.site.register(Post, PostAdmin)


class Battery_typeAdmin(admin.ModelAdmin):
    class Meta:
        model = Battery_type

    list_display = [
        'id',
        'name'
    ]


admin.site.register(Battery_type, Battery_typeAdmin)
