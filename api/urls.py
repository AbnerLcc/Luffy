#!/usr/bin/env python
# -*- coding:utf-8 -*-



from django.urls import path,re_path
from .views import course,account,degree

app_name='api'
urlpatterns = [
    path('course/',course.CourseViews.as_view({"get":"list"}),name='course'),
    re_path('course/(?P<pk>\d+)/$',course.CourseViews.as_view({'get': 'retrieve'}),name='course_detail'),
    path('login/',account.LoginViews.as_view(),name='login'),
    path('degree/',degree.DegreeView.as_view(),name='degree'),
]
