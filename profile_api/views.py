from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, response, format=None):
        """Returns a list of APIViews features"""

        an_apiviews = [
            'Uses HTTP method as function (get, post, put, delete)',
            'Is similar to a traditional django views',
            'Gives you the most control to your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiviews': an_apiviews})