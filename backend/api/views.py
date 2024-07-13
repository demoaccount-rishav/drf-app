from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from users.models import User
from users.serializers import UserSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def api_user_signup(request):
    if request.method == 'GET':

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        else:
            received_data = request.data
            # data = {'message': 'Data received but save unsuccessful',
            #         'received_data': received_data}

            finalData = dict()
            finalData["errors"] = serializer.errors

            return Response(finalData, status=201)

    else:
        return Response({'msg': 'feature under construction'}, status=201)
        '''
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        if request.method == 'PUT':
            serializer = UserSerializer(user, data=request.data)
        elif request.method == 'PATCH':
            serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)
        '''


@api_view(['POST'])
def api_user_login(request):
    try:
        user = User.objects.get(userEmail=request.data['userEmail'])
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

    serializer = UserSerializer(user, partial=True)

    return Response({'message': 'User found', "userInfo": serializer.data}, status=404)
