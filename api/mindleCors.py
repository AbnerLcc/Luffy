#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.utils.deprecation import MiddlewareMixin
from django.middleware.security import SecurityMiddleware
class MiddleGet(MiddlewareMixin):
    def process_response(self,request,response):
        response['Access-Control-Allow-Origin']='*'


        # 预检通过了 post请求没有放行
        if request.method=='OPTIONS':

            response['Access-Control-Allow-Headers'] = "Content-Type"
            response['Access-Control-Allow-Method'] = 'DELETE,ADD,PUT'
        return response