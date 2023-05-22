# walls/views.py
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from walls.models import User,Post,Comment
from walls.serializer import UsersSerializer,PostsSerializer,CommentsSerializer
import numpy as np

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer()

class PostsView(APIView):
    def get(self,request):
        data = {
            'page_num':request.data.get('page_num'),
            'page_size':request.data.get('page_size'),
            'location_x':request.data.get('location_x'),
            'location_y':request.data.get('location_y'),
            'distance':request.data.get('distance')
        }
        querysize = data[0]*data[1]
        queryset = Post.objects.all()
        count=0
        distance = 0
        show_list = []
        for post in queryset:
            distance = np.sqrt((post.location_x - data[2])**2 + (post.location_y - data[3])**2)
            if count < querysize and distance <= data[4]:
                count+=1
                show_list.append(post)

        return Response(show_list,status=status.HTTP_200_OK)

    def post(self,request):
        data = {
            'content_type':request.data.get('content_type'),
            'media_url':request.data.get('media_url'),
            'text':request.data.get('text')
        }
        serializer = CommentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CommentsView(APIView):
    def get(self,request):
        data = {
            'page_num':request.data.get('page_num'),
            'page_size':request.data.get('page_size'),
            'post_id':request.data.get('post_id')
        }
        count=0
        querysize = data[0]*data[1]
        queryset = Comment.objects.all()
        show_list = []
        for comment in queryset:
            if count < querysize and comment.post_id == data[2]:
                show_list.append(comment)

        return Response(show_list,status=status.HTTP_200_OK)

    def post(self,request):
        data = {
            'content_type':request.data.get('content_type'),
            'media_url':request.data.get('media_url'),
            'text':request.data.get('text')
        }
        serializer = CommentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserRegisterView(APIView):
    def post(self,request):
        data = {
            'username':request.data.get('username'),
            'password':request.data.get('password')
        }
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self,request):
        data = {
            'username':request.data.get('username'),
            'password':request.data.get('password')
        }
        queryset = User.objects.all()
        for user in queryset:
            if data[0] == user.username and data[1] == user.password:
                return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)