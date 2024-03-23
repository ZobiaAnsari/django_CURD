from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from django.http import HttpResponse
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)

            return HttpResponse(json_data, content_type = 'application/json')
        stu =Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')


    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = py_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)
    
    if request.method =='PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(data = py_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'data deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data)