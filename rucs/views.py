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
    
    print ci
    
    ruc_object = Ruc.objects.filter(ci=ci)
    
    if len(ruc_object)>0:
        ruc_object = ruc_object[0]
    else:
        ruc_object = Ruc()
    
    if request.method == 'GET':
        serializer = RucSerializer(ruc_object)
        return JSONResponse(serializer.data)
