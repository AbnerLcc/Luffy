#!/usr/bin/env python
# -*- coding:utf-8 -*-
from rest_framework import serializers
from .. models import Course,CourseDetail,CourseCategory


class CourseSerializers(serializers.ModelSerializer):
    price_policy=serializers.SerializerMethodField()
    level = serializers.CharField(source='get_level_display')
    course_type = serializers.CharField(source='get_course_type_display')
    def get_price_policy(self,obj):
        price_query=obj.price_policy.all()
        price={}
        for obj1 in price_query:
            valid_period=obj1.get_valid_period_display()
            price[valid_period]=obj1.price
        return price
    class Meta:
        model=Course
        fields=['pk','price_policy','name','course_img','level','brief',"order","attachment_path","course_type"]


class CourseCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=CourseCategory
        fields='__all__'




# 课程详细查询,分别跨表查询章节,因为是课程详情是onetoone关系,因此直接查询课程表即可,
# 即需要详情时,直接查询详情表即可
class CourseDetailSerializers(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name')
    img=serializers.CharField(source='course.course_img')
    recommend_courses=serializers.SerializerMethodField()
    teachers=serializers.SerializerMethodField()
    # 单选页面提取数据
    level=serializers.CharField(source='course.get_level_display')
    class Meta:
        model=CourseDetail
        fields=['course_name','why_study','career_improvement','img','level','recommend_courses',"teachers",'career_improvement']
        # depth=1
    def get_recommend_courses(self,obj):
        queryset=obj.recommend_courses.all()
        return [{"id":course_obj.pk,"title":course_obj.name} for course_obj in queryset]
    def get_teachers(self,obj):
        queryset=obj.teachers.all()
        return [{"id":teachers_obj.pk,"name":teachers_obj.name} for teachers_obj in queryset]