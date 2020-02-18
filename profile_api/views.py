from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication

from profile_api import serializers
from profile_api import models
from profile_api import permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test Viewsets"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        an_viewsets = [
            'Uses Action (list, create, retreive, update, partial_update)',
            'Automatically map to URLs using Routers',
            'Provide more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'an_viewsets': an_viewsets})

    def create(self, request):
        """Create a hello message with a name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello %s' % name

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handler to getting an object with ids"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handler to update an object with ids"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handler to updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handler to delete an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)