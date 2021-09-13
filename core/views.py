from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response

class Alive(APIView):
    def get(self, request):
        response_obj = {
            'status': 'success',
            'message': 'Alive'
        }
        return Response(response_obj)

Alive_view = Alive.as_view()
