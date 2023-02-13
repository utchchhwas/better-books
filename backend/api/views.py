from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRoutes(request):
    """Get all available API routes."""
    return Response([
        '/api/routes/',
        'api/book/<isbn>',
        'api/search/<search-term>',
    ])
