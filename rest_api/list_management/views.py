from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class ItemList(APIView):
    """
    List our list items.
    """

    def get(self, request):

        return Response({'test': 'response'})
