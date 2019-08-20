from api.serializers1.course import *

from rest_framework.views import Response

from rest_framework.viewsets import GenericViewSet,ViewSetMixin

from ..models import *
class CourseViews(GenericViewSet, ViewSetMixin):

    def list(self,request,*args,**kwargs):
        ret={"code":1000,'data':None}

        # 防止序列化类时报错
        try:
            course_queryset=Course.objects.all()
            catagory_queryset=CourseCategory.objects.all()
            course=CourseSerializers(instance=course_queryset,many=True)
            course_category=CourseCategorySerializers(catagory_queryset,many=True)
            data={"course":course.data,'category': course_category.data }
            ret['data']=data
        except Exception as e:
            ret["code"]=1001
            print(e)

        return Response(ret)

    def retrieve(self,request,pk,*args,**kwargs):
        ret = {"code": 1000, 'data': None}
        try:
            desc_obj = CourseDetail.objects.filter(course_id=pk).first()
            desc = CourseDetailSerializers(instance=desc_obj, many=False)

            course_obj=Course.objects.filter(pk=pk).first()
            course = CourseSerializers(instance=course_obj, many=False)

            data = {"course": course.data, 'desc': desc.data}
            ret['data'] = data
        except Exception as e:
            print(e)
            ret["code"] = 1001
        print(ret)
        return Response(ret)



