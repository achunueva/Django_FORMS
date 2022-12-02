from django.urls import path
from . import views

urlpatterns = [
    path('text/', views.Text_view.as_view(), name='text'),
    path('text/add/', views.Text_create.as_view(), name='add'),
    path('text/<int:id>/update/', views.Text_update.as_view(), name='update'),
    path('text/<int:id>/delete/', views.Text_delete.as_view(), name='delete')
]