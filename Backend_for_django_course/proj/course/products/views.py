from uuid import uuid4

from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Token, Good
from .serializers import GoodSerializer


def get_token(request):
    token = uuid4()
    token = Token.objects.create(rand_token=token)
    result = {'token': token.rand_token}
    return JsonResponse(data=result)


@api_view(["GET"])
def list_goods(request):
    if is_valid_token(request=request):
        goods = Good.objects.all()
        serializer = GoodSerializer(goods, many=True)
        return Response(data=serializer.data)


class NewGoodAPI(APIView):
    def get(self, request):
        if token := is_valid_token(request=request):
            result = {'token': token.rand_token}
            return Response(data=result, status=status.HTTP_200_OK)

    def post(self, request):
        if is_valid_token(request=request):
            good_serializer = GoodSerializer(data=request.data)
            if good_serializer.is_valid():
                good = good_serializer.validated_data
                Good.objects.create(**good)
                return Response(data={"success": True},
                                status=status.HTTP_201_CREATED)
            else:
                return Response(good_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def is_valid_token(request):
    if "token" in request.GET:
        try:
            return Token.objects.get(rand_token=request.GET["token"])
        except Token.DoesNotExist:
            return HttpResponse(content="Token is invalid",
                                status=status.HTTP_401_UNAUTHORIZED)
    return HttpResponse(content="Token must be present",
                        status=status.HTTP_401_UNAUTHORIZED)
