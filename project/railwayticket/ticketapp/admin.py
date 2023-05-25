from django.contrib import admin
from .models import *

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['rgid', 'username', 'email', 'phno', 'aadhar','password']
    search_fields = ['username', 'email', 'phno']
    list_filter = ['usertype']
    list_per_page = 10
admin.site.register(Register, RegisterAdmin)

class AddTrainAdmin(admin.ModelAdmin):
    list_display = ('trainname', 'train_no', 'departuretime', 'arrivaltime', 'max_seat', 'price', 'seat_type')
    search_fields = ('trainname', 'train_no')
    list_filter = ('departuretime', 'arrivaltime')
    ordering = ('train_no',)

admin.site.register(Add_Train, AddTrainAdmin)

class PassengerAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'train', 'seat', 'age', 'gender', 'status', 'date1', 'fare')
    list_filter = ('train', 'status', 'date1')
    search_fields = ('name', 'user__email')
    list_per_page = 20
admin.site.register(Passenger, PassengerAdmin)

class SeatAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate')
    search_fields = ('name',)
    list_per_page = 20
admin.site.register(Seat, SeatAdmin)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(Place, PlaceAdmin)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    readonly_fields = ('name', 'email', 'message')
admin.site.register(ContactMessage, ContactMessageAdmin)

class TrainScheduleAdmin(admin.ModelAdmin):
    list_display = ['from_city', 'to_city', 'date', 'train', 'remaining_seats']
    list_filter = ['from_city', 'to_city', 'date', 'train']
    search_fields = ['from_city__city_name', 'to_city__city_name', 'train__trainname']
    list_per_page = 20
admin.site.register(Train_shedulde, TrainScheduleAdmin)

class BookDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'train', 'seat', 'age', 'gender', 'status', 'date1', 'fare')
    list_filter = ('status', 'date1')
    search_fields = ('name', 'user__username', 'train__name')  # Example search fields, adjust as needed

admin.site.register(Book_details, BookDetailsAdmin)

