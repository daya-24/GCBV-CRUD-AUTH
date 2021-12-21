from django.urls import path
from . import views

urlpatterns = [

    path('create/', views.LaptopCreateView.as_view(), name='add_lap'),
    path('list/', views.LaptopListView.as_view(), name='show_lap'),
    path('update/<int:pk>/', views.LaptopUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.LaptopDeleteView.as_view(), name='delete')

]