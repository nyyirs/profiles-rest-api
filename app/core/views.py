from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a hello world"""

        mytest = ["Hello from outerspace", "This is a new world"]

        return Response({'message': mytest})
