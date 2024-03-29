from django.shortcuts import render

# 배달원 등록
import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.core.serializers import serialize
from member.models import Rider, Customer
from orderrequest.models import OrderApply

from django.views.decorators.csrf import csrf_exempt

from member.models import Rider, Customer

# TEST
from django.core.serializers import serialize
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializers import DeliverySerializer

##################주석 풀면 orders -> Customer##################

# Create your views here.
def order_confirm_view(request, pk):    # 들어온 주문을 확인
    obj = OrderApply.objects.get(pk=pk)     # 지정된 배달원

    if request.method == 'GET':
        serializer = DeliverySerializer(obj)
        data = json.loads(serialize('json', serializer))
        # return HttpResponse(status=200)
        # return JsonResponse(serializer.data, safe=False)
        return render(request, 'delivery/order_confirm.html', {})


# def order_confirm_view(request):
#     if request.method == 'GET':
#         order_list = orders.objects.all()
#         list = {'order_list': order_list}
#         return render(request, 'delivery/order_confirm.html', list)
#         # data = json.loads(serialize('json', order_list))
        
#         return render(request, 'delivery/order_confirm.html', {})


def order_confirm_view(request):
    if request.method == 'GET':
        order_list = OrderApply.objects.all()
        list = {'order_list': order_list}
        return list


# http://127.0.0.1:8000/delivery/register/ -> POST로
# {"rider_id": "", "rider_pw": "", "rider_name": "", "rider_intro": "", "min_delivery_amount": } 형식으로 send
# @csrf_exempt
def register_rider_view(request):   # 라이더 등록
    # rider_cus = get_object_or_404(Customer, pk=cus_id)
    # rider_cus = Customer.objects.all().filter(id=cus_id)

    if request.method == 'GET':
        rider_list = Rider.objects.all()
        data = json.loads(serialize('json', rider_list))
        # return JsonResponse({'rider_list': data})
        return render(request, 'delivery/register_rider.html')
    
    if request.method == 'POST':
        if request.META['CONTENT_TYPE'] == 'application/json':
            request = json.loads(request.body)
            rider = Rider(
                # rider_id = request['rider_id'],
                # rider_pw = request['rider_pw'],
                rider_name = request['rider_name'],
                min_delivery_amount=request['min_delivery_amount'],
                rider_intro = request['rider_intro'],
                # recommended_person=request['recommended_person'],
                rider_area = request.POST('rider_area'),
                # bankbook = request['bankbook'],
                # license = request['license'],


                # multiselectfield(여러개 값을 받야아 하는) 체크박스 값이 잘 post되는지 테스트 필요
                # rider_vehicle = request.POST.getlist('input태그 id값')
                # rider_vehicle = request.POST.getlist('vehicle')
                # rider_vehicle = request.POST.getlist('input태그 name값[]')
                rider_vehicle=request.POST.getlist('vehicle[]'),


                # rider_vehicle = request['rider_vehicle'],
            )
        else:
            rider = Rider()
            rider.rider_nickname = request.user
            rider.rider_name = request.POST['rider_name']
            rider.intro = request.POST['rider_intro']
            rider.min_delivery_amount = request.POST['min_delivery_amount']
            rider.rider_area = request.POST['rider_area']
            rider.rider_vehicle = request.POST.getlist('vehicle[]')

            # rider = Rider(
            #     # rider_nickname = request.POST['rider_nickname'],
            #     # rider_id=request.POST['rider_id'],
            #     # rider_pw=request.POST['rider_pw'],
            #     rider_name=request.POST['rider_name'],
            #     min_delivery_amount=request.POST['min_delivery_amount'],
            #     rider_intro = request.POST['rider_intro'],
            #     # recommended_person=request.POST['recommended_person'],
            #     rider_area=request.POST['rider_area'],
            #     # bankbook=request.POST['bankbook'],
            #     # license=request.POST['license'],

            #     # rider_vehicle = request.POST.getlist('vehicle')
            #     # rider_vehicle=request.POST['rider_vehicle'],
            #     rider_vehicle=request.POST.getlist('vehicle[]'),
            # )
        rider.save()
        # return HttpResponse(status=200)
        return render(request, 'main.html')
    
    return render(request, 'register_rider.html')


def order_list_view(request):   # 선착순 주문 목록
    # if request.method == 'GET': # 주문 목록
    #     order_list = Customer.objects.all()
    #     data = json.loads(serialize('json', order_list))
    #     return JsonResponse({'order_list': data})
    #     return render(request, 'delivery/order_list.html', {})

    # TEST 후 이 주석 풀어주면 됨
    # if request.method == 'GET':
    #     # all_orders = orders.objects
    #     order_list = OrderApply.objects.all()
    #     # order_list = all_orders.all()
    #     list = {'order_list': order_list}
    #     return render(request, 'delivery/order_list.html', list)

    # TEST(이것도 됨)
    if request.method == 'GET':
        # order_list = OrderApply.objects.values()
        order_list = OrderApply.objects.all()   # cus_orderer 정보 받아오려면 이렇게 써야 함
        order_list = {'order_list': order_list}
        # cus_list = Customer.objects.values()
        # cus_list = {'cus_list': cus_list}
        # order = order_list.get()
        # orders.objects.value()[0]
        return render(request, 'delivery/order_list.html', order_list)


# def order_list_view(request, pk):
#     obj = orders.objects.get(pk=pk)

#     if request.method == 'GET':
#         serializer = DeliverySerializer(obj)
    
#         return JsonResponse(serializer.data, safe=False)

    # if request.method == 'GET':
    #     order_list = orders.objects.all()
    #     list = {'order_list': order_list}
    #     return render(request, 'delivery/order_list.html', list)

