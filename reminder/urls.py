from django.urls import path
from . import views
from .views import ReminderList, ReminderDetail, ReminderCreate
app_name='reminder'
urlpatterns = [
    path('',views.ReminderList, name='reminder'),
    path('Create-Reminder/',ReminderCreate.as_view(), name='add'),
    path('<pk>/',ReminderDetail.as_view(), name="detail"),
    path('delete/<pk>/', views.delete, name="delete"),
]
