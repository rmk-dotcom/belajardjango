from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Produk

@login_required(login_url='/login/')
def index(request):
    produk = Produk.objects.all()
    context = {
        'nama': 'Meisheila',
        'kota': 'Purwokerto',
        'produk': produk,
    }
    return render(request, 'index.html', context)

@login_required(login_url='/login/')
def tambah_produk(request):
    if request.method == 'POST':
        nama = request.POST['nama']
        stok = request.POST['stok']
        harga = request.POST['harga']
        Produk.objects.create(nama=nama, stok=stok, harga=harga)
        return redirect('index')
    return render(request, 'tambah_produk.html')

@login_required(login_url='/login/')
def edit_produk(request, id):
    produk = Produk.objects.get(id=id)
    if request.method == 'POST':
        produk.nama = request.POST['nama']
        produk.stok = request.POST['stok']
        produk.harga = request.POST['harga']
        produk.save()
        return redirect('index')
    return render(request, 'edit_produk.html', {'produk': produk})

@login_required(login_url='/login/')
def hapus_produk(request, id):
    produk = Produk.objects.get(id=id)
    produk.delete()
    return redirect('index')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Username atau password salah!'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')