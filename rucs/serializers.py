'''
Created on 28/07/2015

@author: luke
'''
from rest_framework import serializers
from rucs.models import Ruc


class RucSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ruc
        fields = ('ci', 'name', 'dv')