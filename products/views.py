# Create your views here.
import json
from django.views import View 
from django.http import JsonResponse
from .models import Menu


class ProductListView(View):
    def get(self, request):
        menus = Menu.objects.all()
        
        result = []
        for menu in menus:
            result.append(menu.name)

        return JsonResponse({'result': result}, status=200) 

    def post(self, request):
        try:
            data = json.loads(request.body) # JSON -> Python

            name = data['name']
            Menu.objects.create(name=name)

            return  JsonResponse({'message':'SUCCESS!'}, status=201) 

        except KeyError:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)