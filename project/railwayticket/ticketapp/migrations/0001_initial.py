# Generated by Django 4.2.1 on 2023-05-07 04:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainname', models.CharField(max_length=30, null=True)),
                ('train_no', models.IntegerField(null=True)),
                ('departuretime', models.CharField(max_length=30, null=True)),
                ('arrivaltime', models.CharField(max_length=30, null=True)),
                ('distance', models.IntegerField(null=True)),
                ('max_seat', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('rgid', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Of User')),
                ('username', models.CharField(max_length=30, verbose_name='User Name')),
                ('email', models.EmailField(max_length=30, verbose_name='email')),
                ('phno', models.IntegerField(verbose_name='Phone no')),
                ('password', models.CharField(max_length=10, verbose_name='password')),
                ('usertype', models.CharField(default='U', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Train_shedulde',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('from_city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from1', to='ticketapp.place')),
                ('to_city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_city1', to='ticketapp.place')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketapp.add_train')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=30, null=True)),
                ('status', models.CharField(max_length=30, null=True)),
                ('date1', models.DateField(default=datetime.date(2023, 5, 7))),
                ('fare', models.IntegerField(null=True)),
                ('seat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ticketapp.seat')),
                ('train', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ticketapp.add_train')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ticketapp.register')),
            ],
        ),
        migrations.AddField(
            model_name='add_train',
            name='seat_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketapp.seat'),
        ),
    ]
