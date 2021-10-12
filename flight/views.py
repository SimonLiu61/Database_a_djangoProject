from audioop import reverse

import pymysql
pymysql.install_as_MySQLdb()
from django.shortcuts import render, redirect
from flight.models import Flight
from flight.models import Ticket
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse


#信息列表处理函数 django版本写法
def index(request):
    flights = Flight.objects.all()
    print(type(flights))
    return render(request,"bookflight.html", locals())

def testadd(request):
    Flight.objects.create(flightid='CA003',planeid='001')
    return index(request)

def myticket(request):
    username = request.session['username']
    tickets = Ticket.objects.filter(userid=username)
    return render(request, "tickets.html", locals())

def bookTicket(request):
    if request.method == 'GET':
        isVip = request.session['isVip']
        flight_id = request.GET.get("flightid")
        return render(request, 'booking.html', {'flightid': flight_id,'isVip':isVip})
    else:
        username = request.session['username']
        flight_id = request.POST.get("flightid",'')
        booking_name = request.POST.get("booking_name",'')
        booking_num = request.POST.get("booking_num",'')
        Ticket.objects.create(userid=username, flightid=flight_id, money='2000')  # 数据库增加操作
        return redirect('/flight/myticket/')

def delTicket(request):
    del_id = request.GET.get("ticketid")
    Ticket.objects.filter(ticketid = del_id).delete()   #操作数据库 删除操作
    return redirect('/flight/myticket/')

