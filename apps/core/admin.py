from django.contrib import admin
from image_cropping import ImageCroppingMixin
from apps.core.models import Service, PhotoService, Institution, Certificate
from apps.core.models import Client


class ClientAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'status')
    list_filter = ('status', 'created_at', 'service')
    search_fields = ('name', 'service', 'description', 'email')


class PhotoServiceAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('image_thumb', 'client')
    search_fields = ('client__name', 'client__phone', 'client__email')


class InstitutionAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('imageAdmin', 'name')
    search_fields = ['name']


admin.site.register(Service)
admin.site.register(Client, ClientAdmin)
admin.site.register(PhotoService, PhotoServiceAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Certificate)
