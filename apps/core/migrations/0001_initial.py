# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Certificado',
                'verbose_name_plural': 'Certificados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name=b'Nome', blank=True)),
                ('phone', models.CharField(help_text=b'Somente n\xc3\xbameros. Ex.: 99999999999', unique=True, max_length=20, verbose_name=b'Telefone')),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('latitude', models.CharField(max_length=20, null=True, blank=True)),
                ('longitude', models.CharField(max_length=20, null=True, blank=True)),
                ('description', models.CharField(help_text=b'At\xc3\xa9 140 caracteres.', max_length=140, null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True)),
                ('image', models.ImageField(upload_to=b'uploads/client/', verbose_name=b'Imagem', blank=True)),
                (b'image_small', image_cropping.fields.ImageRatioField(b'image', '185x185', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=b'Foto do perfil do usu\xc3\xa1rio.', verbose_name=b'Imagem pequena')),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Data de Cria\xc3\xa7\xc3\xa3o')),
            ],
            options={
                'ordering': ('-created_at',),
                'get_latest_by': 'created_at',
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name=b'Nome', blank=True)),
                ('image', models.ImageField(upload_to=b'uploads/client/', verbose_name=b'Logo', blank=True)),
                (b'image_small', image_cropping.fields.ImageRatioField(b'image', '90x90', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=b'Foto do perfil do usu\xc3\xa1rio.', verbose_name=b'Logo pequena')),
            ],
            options={
                'verbose_name': 'Institui\xe7\xe3o',
                'verbose_name_plural': 'Institui\xe7\xf5es',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhotoService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'uploads/client/service', verbose_name=b'Foto servi\xc3\xa7o', blank=True)),
                (b'photo_thumb', image_cropping.fields.ImageRatioField(b'photo', '200x200', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='photo thumb')),
                ('client', models.ForeignKey(verbose_name=b'Cliente', to='core.Client')),
            ],
            options={
                'ordering': ['client'],
                'verbose_name': 'Foto de Servi\xe7o',
                'verbose_name_plural': 'Fotos de Servi\xe7os',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
            ],
            options={
                'verbose_name': 'Servi\xe7o',
                'verbose_name_plural': 'Servi\xe7os',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='client',
            name='service',
            field=models.ManyToManyField(to='core.Service', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='certificate',
            name='client',
            field=models.ForeignKey(verbose_name=b'Cliente', to='core.Client'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='certificate',
            name='institution',
            field=models.ForeignKey(verbose_name=b'Institui\xc3\xa7\xc3\xa3o parceira', to='core.Institution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='certificate',
            name='service',
            field=models.ForeignKey(verbose_name=b'Servi\xc3\xa7o', to='core.Service'),
            preserve_default=True,
        ),
    ]
