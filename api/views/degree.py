#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import reverse,redirect
from rest_framework.views import Response,APIView
from api.auth_threee.auth import LoginAuth
class DegreeView(APIView):

    authentication_classes = [LoginAuth,]
    def get(self,request, *args, **kwargs):
        ret={'code':1000,'data':'学位课'}
        return Response(ret)
