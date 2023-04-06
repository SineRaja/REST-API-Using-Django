from django.shortcuts import render
from rest_framework.response  import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Student, Feedback
from .serailizer import StudentSerailizer, FeedbackSerailizer

# Create your views here.

class StudentDetail(APIView):
    def get(self, request):
        obj = Student.objects.all()
        serailizer = StudentSerailizer(obj, many=True)
        return Response(serailizer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StudentSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    

class StudentInfo(APIView):
    def get(self,request,id):
        try:
            obj = Student.objects.get(id=id)  
            
        except Student.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerailizer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            obj = Student.objects.get(id=id)
        
        except Student.DoesNotExist:
            msg = {"msg":"not found error"}
            
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerailizer(obj, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
        
    def patch(self, request, id):
        try:
            obj = Student.objects.get(id=id)
        
        except Student.DoesNotExist:
            msg = {"msg":"not found error"}
            
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerailizer(obj, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,id):
        try:
            obj = Student.objects.get(id=id)
            
        except Student.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        obj.delete()
        return Response({"msg":"Deleted"}, status=status.HTTP_204_NO_CONTENT)
    
    
    
class FeedbackDetail(APIView):
    def get(self, request):
        obj = Feedback.objects.all()
        serailizer = FeedbackSerailizer(obj, many=True)
        return Response(serailizer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = FeedbackSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    


class FeedbackInfo(APIView):
    def get(self,request,id):
        try:
            obj = Feedback.objects.get(id=id)  
            
        except Feedback.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FeedbackSerailizer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            obj = Feedback.objects.get(id=id)
        
        except Feedback.DoesNotExist:
            msg = {"msg":"not found error"}
            
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FeedbackSerailizer(obj, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
        
    def patch(self, request, id):
        try:
            obj = Feedback.objects.get(id=id)
        
        except Feedback.DoesNotExist:
            msg = {"msg":"not found error"}
            
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FeedbackSerailizer(obj, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,id):
        try:
            obj = Feedback.objects.get(id=id)
            
        except Feedback.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        obj.delete()
        return Response({"msg":"Deleted"}, status=status.HTTP_204_NO_CONTENT)
    