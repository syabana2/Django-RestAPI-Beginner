from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, response, format=None):
        """Returns a list of APIViews features"""

        an_apiviews = [
            'Uses HTTP method as function (get, post, put, delete)',
            'Is similar to a traditional django views',
            'Gives you the most control to your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiviews': an_apiviews})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello %s' % name

            return Response({'message': message})
        else :
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle a delete of an object"""
        return Response({'method': 'DELETE'})