from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.stm

from .models import *
import json
from django.views import *

# Create your views here.
import uuid

MISSING_PARAM = 'Some mandatory param is missing'
MISSING_PARAM_CODE = 410

response_dict = {"response_string": "", "response_code": 200}


def create_user(request):
    user_id = uuid.uuid4()
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    user_obj = User(user_id=user_id, first_name=first_name,
                    last_name=last_name)
    user_obj.save()
    response_dict['response_string'] = str(user_id)
    return HttpResponse(json.dumps(response_dict))


def create_bill(request):
    ''' Additionally check that all the users are registered uuids'''
    bill_id = str(uuid.uuid4())
    bill_details = {}
    req_params = request.POST
    total_bill = 0
    for k, v in req_params.items():
        bill_details[k] = v
        total_bill = total_bill + int(v)
    bill_models = Bill(
        bill_id=bill_id, bill_details=bill_details, total_bill=total_bill)
    bill_models.save()
    response_dict['response_string'] = bill_id + ' has ' + str(bill_details) + '=' + str(total_bill)
    # Call Generate Report 
    try:
    	generate_report()
    except Exception as e:
    	print(str(e))
    return HttpResponse(json.dumps(response_dict))


def simplify(request):
    bill_id = request.POST.get('bill_id')
    if not bill_id:
        response_dict['response_string'] = MISSING_PARAM
        respose_dict['response_code'] = MISSING_PARAM_CODE
    bill_obj = Bill.objects.get(bill_id=bill_id)
    bill_details = eval(bill_obj.bill_details)
    total_bill = bill_obj.total_bill
    new_bill = do_simplification(bill_details)
    bill_details = new_bill
    simple_bill = Simplify(
        bill_id=bill_id, bill_details=bill_details, total_bill=total_bill)
    simple_bill.save()
    response_dict['response_string'] = bill_details + new_bill
    return HttpResponse(json.dumps(response_dict))


def do_simplification(bill_details):
    total_people = len(bill_details.keys())
    print('total people', total_people)
    for k, v in bill_details.items():
        print(k,type(v))
    return 10

def generate_report():
	pass