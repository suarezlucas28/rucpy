from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rucs.serializers import RucSerializer
from rest_framework.renderers import JSONRenderer
from rucs.models import Ruc

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
        
@csrf_exempt
def ruc_detail(request, ci):
    try:
        ruc_object = Ruc.objects.get(ci=ci)
    except Ruc.DoesNotExist:
        ruc_object = Ruc()
        serializer = RucSerializer(ruc_object)
        return JSONResponse(serializer.data)

    if request.method == 'GET':
        serializer = RucSerializer(ruc_object)
        return JSONResponse(serializer.data)
