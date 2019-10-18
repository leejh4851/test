from django.shortcuts import render
from ordersystem.forms import *
from ordersystem.models import Destination

# Create your views here.
def postal(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form() 
    return render(request,'ordersystem/posttest.html',{'form':form})

def postresult(request):
    destinationList = Destination.objects.all()
    return render(request,'ordersystem/postresult.html',{'destinationList':destinationList})

def orderwrite(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm() 
    return render(request,'ordersystem/orderwrite.html',{'form':form})   


def orderlist(request): 
    orderList = Orders.objects.all()
    return render(request,'ordersystem/orderlist.html',{'orderList':orderList})

def orderdetail(request,id): 
    order = Orders.objects.get(id=id)
    return render(request,'ordersystem/orderdetail.html',{'order':order})

def goodslist(request): 
    goodsList = Goods.objects.all()
    return render(request,'ordersystem/goodslist.html',{'goodsList':goodsList})


