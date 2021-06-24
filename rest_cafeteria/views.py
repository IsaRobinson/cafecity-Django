from django.shortcuts import render

from rest_framework import status

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt

from cafeteria.models import Alimento

from .serializers import AlimentosSerializer


@csrf_exempt

@api_view(['GET','POST'])


def lista_alimentos(request):

    if request.method == 'GET':

        Alimentos = Alimento.objects.all()

        serializer = AlimentosSerializer(Alimentos, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':

        data = JSONParser().parse(request)

        serializer = AlimentosSerializer(data=data)

        if(serializer.is_valid()):

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def detalle_alimentos(request,id):

    try:

        alimento = Alimento.objects.get(idAlimento=id)

    except Alimento.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':

        serializer = AlimentosSerializer(alimento)

        return Response(serializer.data)

    if request.method == 'PUT':

        data = JSONParser().parse(request)

        serializer = AlimentosSerializer(alimento,data=data)

        if(serializer.is_valid()):

            serializer.save()

            return Response(serializer.data)

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        alimento.delete()

        return Response(status=status.HTTP_204_NOT_CONTENT)