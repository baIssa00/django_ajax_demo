from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def compute(request):
    a = request.POST.get("a")
    b = request.POST.get("b")
    result = int(a) + int(b)
    return JsonResponse({"operation_result": result})

def ajax_posting(request):
    if request.is_ajax():
        login = request.POST.get('login')
        password = request.POST.get('password')
        if login and password:
            response = {
                'msg' : 'Utilisateur ajouté!'
            }
            return JsonResponse(response)
