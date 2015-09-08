# coding=utf-8
from datetime import datetime
from django.db import models
from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageRatioField


class Service(models.Model):
    name = models.CharField("Nome", max_length=100)

    class Meta:
        verbose_name = u'Serviço'
        verbose_name_plural = u'Serviços'

    def __unicode__(self):
        return self.name


class Client(models.Model):
    name = models.CharField("Nome", max_length=100, null=True, blank=True)
    phone = models.CharField("Telefone", max_length=20, unique=True, help_text="Somente números. Ex.: 99999999999")
    email = models.EmailField(null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField("Descrição", max_length=140, null=True, blank=True, help_text="Até 140 caracteres.")
    service = models.ManyToManyField('Service', null=True, blank=True)
    image = models.ImageField("Imagem", upload_to='uploads/client/', blank=True)
    image_small = ImageRatioField('image', '185x185', verbose_name='Imagem pequena', help_text="Foto do perfil do usuário.")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(verbose_name='Data de Criação', default=datetime.now)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = u'Cliente'
        verbose_name_plural = u'Clientes'
        get_latest_by = 'created_at'

    def __unicode__(self):
        return u'%s' % str(self.phone)

    def get_image_small(self):
        return get_thumbnailer(self.image).get_thumbnail({'size': (185, 185), 'box': self.image_small, 'crop': True, 'detail': True, }).url


class PhotoService(models.Model):
    photo = models.ImageField(verbose_name="Foto serviço", upload_to='uploads/client/service', blank=True)
    photo_thumb = ImageRatioField('photo', '200x200')
    client = models.ForeignKey(Client, verbose_name="Cliente")

    class Meta:
        verbose_name = 'Foto de Serviço'
        verbose_name_plural = 'Fotos de Serviços'
        ordering = ['client']

    def __unicode__(self):
        return u'%s' % str(self.photo).split('/')[-1]

    def image_thumb(self):
        return get_thumbnailer(self.photo).get_thumbnail({'size': (200, 200), 'box': self.photo_thumb, 'crop': True, 'detail': True, }).url

    image_thumb.is_safe = True
    image_thumb.allow_tags = True
    image_thumb.short_description = u'Imagem'


class Institution(models.Model):
    name = models.CharField("Nome", max_length=100, null=True, blank=True)
    image = models.ImageField("Logo", upload_to='uploads/client/', blank=True)
    image_small = ImageRatioField('image', '90x90', verbose_name='Logo pequena', help_text="Foto do perfil do usuário.")

    class Meta:
        verbose_name = u'Instituição'
        verbose_name_plural = u'Instituições'

    def get_image_small(self):
        return get_thumbnailer(self.image).get_thumbnail({'size': (185, 185), 'box': self.image_small, 'crop': True, 'detail': True, }).url

    get_image_small.is_safe = True
    get_image_small.allow_tags = True
    get_image_small.short_description = u'Imagem'

class Certificate(models.Model):
    institution = models.ForeignKey(Institution, verbose_name="Instituição parceira")
    client = models.ForeignKey(Client, verbose_name="Cliente")
    service = models.ForeignKey(Service, verbose_name="Serviço")

    class Meta:
        verbose_name = u'Certificado'
        verbose_name_plural = u'Certificados'