from django.core import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PembayaranSerializer, DetailPembayaranSerializer
from .models import Pembayaran

# Create your views here.
class PembayaranView(APIView):

    def post(self, request):
        serializer = PembayaranSerializer(data=request.data)
        if serializer.is_valid():

            pembayaran = Pembayaran.objects.filter(username=serializer.validated_data['username']).first()
            if pembayaran is not None:
                return Response({"message": "You already make payment"}, status=status.HTTP_400_BAD_REQUEST)
            
            pembayaran = serializer.save()
            detail_serializer = DetailPembayaranSerializer(instance=pembayaran)
            return Response(detail_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)