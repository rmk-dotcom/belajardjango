from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tambah/', views.tambah_produk, name='tambah_produk'),
    path('edit/<int:id>/', views.edit_produk, name='edit_produk'),
    path('hapus/<int:id>/', views.hapus_produk, name='hapus_produk'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]