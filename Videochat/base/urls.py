from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('',views.lobby),
    path('room/',views.room),
    path('get_token/',views.getToken),
    path('create_member/',views.createMember),
    path('get_member/',views.getMember),
    path('delete_member/',views.deleteMember),
]