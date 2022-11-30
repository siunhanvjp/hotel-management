from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Branch, Customer, Booking, RoomType, SupplyType, RoomTypeSupplyType, BedInfo, User
from django.db import connection
import datetime
# Create your views here.

bedlist = ['1.5', '2.0']


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            return render(request, 'db-login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')
            
    return render(request, 'db-login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    customers = Customer.objects.all()
    
    
    context={'customers': customers}
    return render(request,'db-customer.html', context)

@login_required(login_url='login')
def view_booking(request,pk):
    bookings = Booking.objects.filter(customerid = pk).order_by('-bookingdate')
    customer = Customer.objects.get(customerid = pk)
    context={'bookings': bookings, 'customer':customer}
    return render(request, 'db-booking.html', context)

@login_required(login_url='login')
def addroomtype(request):
    
    supplies = SupplyType.objects.all()
    context={'supplies': supplies}
    if (request.method == 'POST'):
        room_name = request.POST.get('roomname')
        
        
        if RoomType.objects.filter(roomname=room_name).exists():
            messages.error(request, 'Duplicate room type name.')
            return render(request,'db-addroomtype.html', context)
        
        area = request.POST.get('area')
        numguest = request.POST.get('numguest')
        des = request.POST.get('description')
        
        RoomType.objects.create(roomname = room_name, area = area, numguest = numguest, description = des)
        
        created_room = RoomType.objects.get(roomname = room_name, area = area, numguest = numguest, description = des)
        
        for bed in bedlist:
            quantity = request.POST.get(bed)
            if( quantity != "0"):
                BedInfo.objects.create(roomid = created_room, size = float(bed), quantity = quantity)
        
        for supply in supplies:
            quantity = request.POST.get(supply.sppid)
            if(quantity!="0"):
                RoomTypeSupplyType.objects.create(sppid = supply, roomid = created_room, quantity = quantity)
        
        
        messages.success(request, 'Added successfully !!!')
    
    return render(request,'db-addroomtype.html', context)

cursor = connection.cursor()
@login_required(login_url='login')
def statistic(request):
    branches = Branch.objects.all()
    branch_id = 'CN1'
    year = 2022
    data_list = "["
    if request.method == 'POST':
        branch_id = request.POST.get('branch_id')
        year = request.POST.get('year')


    cursor.execute('call ThongKeLuotKhach (%(branch_id)s,%(year)s)',{'branch_id':branch_id, 'year': year})
    results = cursor.fetchall()
    for result in results:
        data_list += str(result[1]) + ','
        
    data_list = data_list[:-1]; 
    data_list += ']'; 
    context = {'branches': branches, 'results': results, 'year': year, 'branch_id': branch_id, 'data_list': data_list}
    return render(request, 'db-statistic.html', context)
    
    
    