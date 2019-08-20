#!/usr/bin/env python
# -*- coding:utf-8 -*-
from api import models
from rest_framework.views import Response
import uuid
from rest_framework.views import APIView
class LoginViews(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super(LoginViews, self).dispatch(request, *args, **kwargs)
    def post(self, request,*args,**kwargs):
        username=request.data.get('username',"")
        pwd=request.data.get("pwd", "")
        user= models.UserInfo.objects.filter(username=username,pwd=pwd).first()
        ret={"code":1000,"data":""}
        if user:
            print(1111)
            cookie=str(uuid.uuid4())
            models.MyCookie.objects.get_or_create(user=user,str=cookie)
            ret["data"]={"cookie":cookie}
        else:
            ret["code"]=1001
            ret["error"]='用户名或者密码错误'
        return Response(ret)