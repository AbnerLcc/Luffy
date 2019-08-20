#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Luffy.settings')
    import django
    django.setup()
    from api.models import *
    from django.contrib.contenttypes.models import ContentType
    # desc_list = CourseDetail.objects.all().values("course_id", 'name', 'pk')
    # descList = {}  # {1: {1:desc,2:desc}}
    # for dic in desc_list:
    #     #   如果已经存在
    #     cid=dic["course_id"]
    #     descid=dic["pk"]
    #     name=dic["name"]
    #     if cid in descList:
    #         descList[cid][descid] = name
    #     else:
    #         descList[cid] = {descid:name}
    #
    # print(descList)

    course=Course.objects.filter(pk=1).first()
    '普通添加法'
    # obj=PricePolicy.objects.create(
    #     price=155,
    #     period=180,
    #     content_type=ContentType.objects.get(model='course'),
    #     object_id=1
    # )

    '通过内置方法添加'
    # obj=PricePolicy.objects.create(
    #     price=155,
    #     period=180,
    #     content_object=course,
    #
    # )
    # price_policy=PricePolicy.objects.first()
    # print(type(price_policy.content_object))
    # [print( obj.price)  for obj in course.policy_list.all()]

    '''
    python	http://127.0.0.1:8000/static/img/teacher3.png	1
    linux	http://127.0.0.1:8000/static/img/teacher2.png	1
    数据分析	http://127.0.0.1:8000/static/img/teacher1.png	1
    '''
    u=course.price_policy.all()
    for i in u:
        print(i.price)
