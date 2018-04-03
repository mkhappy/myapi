# -*- coding: utf-8 -*-

from models import SensMod
from rest_framework import serializers


class SensModSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensMod
        fields = ('id', 'content','type','message','sensitive','nonsensitive','codedesc','ip', 'create_time')
