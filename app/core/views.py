from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a hello world"""

        mytest = ["Hello from outerspace", "This is a new world"]

        return Response({'message': mytest})

    def post(self, request):
        """generate message with name parameter"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})
