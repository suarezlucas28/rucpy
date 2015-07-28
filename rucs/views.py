from django.shortcuts import render
from rest_framework import viewsets
from rucs.serializers import RucSerializer
from rucs.models import Ruc

# Create your views here.
class RucViewSet(viewsets.ModelViewSet):
    queryset = Ruc.objects.all()
    serializer_class = RucSerializer