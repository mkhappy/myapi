# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from models import SensMod
from my_serializers import SensModSerializer
# from rest_framework import viewsets
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse

from QcloudApi.qcloudapi import QcloudApi
import json


import sys
reload(sys)
sys.setdefaultencoding('utf-8')


module = 'wenzhi'    # "wenzhi.api.qcloud.com"
action = 'TextSensitivity'
region = 'sh'
config = {
        'Region': region,
        'secretId': settings.SECRET_ID,
        'secretKey': settings.SECRET_KEY,}


def my404(request):
    resp = {u'code': 404, u'message': 'null'}
    return HttpResponse(json.dumps(resp), content_type="application/json")

# class SensViewSet(viewsets.ModelViewSet):
class SensView(APIView):
   # def get(self, request, pk):
   #     try:
   #         sens = SensMod.objects.get(pk=pk)
   #     except SensMod.DoesNotExist:
   #         return Response(status=status.HTTP_404_NOT_FOUND)
   #     serializer = SensModSerializer(sens)
   #     return Response(serializer.data)

    def post(self, request):
        if u'content' and u'type' in request.data: 
            r_content = request.data[u'content']
            r_type    = request.data[u'type']
            if r_content != "" and r_type != "" :
                params = {u'content': r_content, u'type': r_type}
                try:
                    service = QcloudApi(module, config)
                    # print service.generateUrl(action, params)
                    result_data = json.loads(service.call(action, params))
                    # print '--------------result_data:', result_data
                except Exception, e:
                    print '----------exception:', e
                    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    return my404(request)
                result_data[u'content'] = r_content
                result_data[u'type']    = r_type
                # fixed message with None text 
                if result_data[u'message'] == "":
                    result_data[u'message'] = None
                # get ip 
                ip = request.META.get('REMOTE_ADDR', None)
                result_data[u'ip'] = ip
                # handle codedesc
                codedesc = result_data.get(u'codeDesc', None)
                del(result_data[u'codeDesc'])
                result_data[u'codedesc'] = codedesc
                # output
                serializer = SensModSerializer(data=result_data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return my404(request)

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(SensView, self).dispatch(*args, **kwargs)

