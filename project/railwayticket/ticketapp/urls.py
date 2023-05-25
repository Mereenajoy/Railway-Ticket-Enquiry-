from django.urls import path

from . import views

urlpatterns =[
    path("",views.index,name="index"),
    path("searchtrain",views.searchtrain,name="searchtrain"),
    path("showtrain",views.showtrain,name="showtrain"),
    path("showtrain1",views.showtrain1,name="showtrain1"),
    path("userhome",views.userhome,name='userhome'),
    path('login',views.login,name='login' ),
    path('register',views.register,name='regster'),
    path('contact_form',views.contact_form,name='contact_form'),
    # path("show",views.show,name="show"),
    path('demo',views.demo),
    path('view_booking',views.view_booking,name="view_booking"),
    path('book',views.book,name='book'),
    path('profile',views.profile,name='profile'),
    path('trains/',views.search_trains,name="search_trains"),
    path('trains/<int:train_id>/schedules/', views.train_schedules, name='train_schedules'),
    path('updateprofile',views.updateprofile,name='updateprofile'),
    path('pay_success',views.pay_success,name="pay_success"),
    path("pay_cancel",views.pay_cancel,name="pay_cancel"),
    path('confirm_booking',views.confirm_booking,name='confirm_booking'),
    path('checkout_session',views.checkout_session,name='checkout_session'),
    path('cancel_ticket',views.cancel_ticket,name='cancel_ticket'),
]