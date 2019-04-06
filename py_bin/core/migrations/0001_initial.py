# Generated by Django 2.2 on 2019-04-05 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=10, unique=True)),
                ('content', models.TextField()),
                ('content_format', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('view_count', models.IntegerField(blank=True, max_length=300, null=True)),
                ('status', models.IntegerField(max_length=5)),
                ('protected', models.BooleanField()),
                ('password', models.CharField(max_length=50)),
                ('expiry', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]