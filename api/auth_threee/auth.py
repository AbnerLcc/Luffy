#!/usr/bin/env python
# -*- coding:utf-8 -*-

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api.models import MyCookie




class LoginAuth(BaseAuthentication):
    def authenticate(self, request):
        # 在确保cookie唯一性可以使用uuid4有一定几率会重复
        cookie = request.GET.get('cookie', '')
        obj = MyCookie.objects.filter(str=cookie).first()

        # 返回两个数据,分别赋值给request.user   request.auth
        # 返回none则是匿名用户
        if obj:
            return (obj.user.username,obj)

        else:
            raise AuthenticationFailed({'code':1001,'error':"认证失败"})