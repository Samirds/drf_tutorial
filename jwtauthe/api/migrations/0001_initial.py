# Generated by Django 4.2 on 2023-04-18 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name')),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Others', 'other')], default='Male', max_length=10)),
                ('age', models.IntegerField(verbose_name='Age')),
                ('email', models.EmailField(max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=128, verbose_name='Password')),
                ('adddress', models.CharField(blank=True, max_length=500, null=True, verbose_name='Address')),
                ('pincode', models.IntegerField(blank=True, null=True, verbose_name='Pin Code')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
