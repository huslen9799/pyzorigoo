from django.shortcuts import render
from labproject.settings import sendResponse,connectDB,disconnectDB
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import pytz
from datetime import datetime 
@csrf_exempt
def dt_gettime(request):
    if request.method != "GET":
        resp_data =[{"function":"dt_gettime"}]
        return JsonResponse(sendResponse(request,200,resp_data,"no_action"))
    try:    
        ULAANBAATAR_TZ = pytz.timezone('Asia/Ulaanbaatar')
        current_time_ub = datetime.now(ULAANBAATAR_TZ)

        resp_data=[{
            "timezone":'Asia/Ulaanbaatar',
            "time":current_time_ub,
            }]
        return JsonResponse(sendResponse(request,200,resp_data,"no action"))
    except Exception as e:
        resp_data=[{"error":str(e)}]
        return JsonResponse(sendResponse(request,1006,resp_data,"no action"))
    
@csrf_exempt
def dt_one(request):
      if request.method != "POST":
        resp_data =[{"function":"dt_one"}]
        return JsonResponse(sendResponse(request,1001,resp_data,"no_action"))
    

  
 
        # {
        #     "action":"one",
        #     "id":5
        # }
# Create your views here.