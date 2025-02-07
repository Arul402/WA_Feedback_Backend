from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.models import Feedbacks
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from .serializers import FeedbackSerializer
from rest_framework.permissions import AllowAny

def example_view(request):
    return JsonResponse({"message": "This is an example view from app"})



# 1. Create Feedback (POST)
@api_view(['POST'])
@permission_classes([AllowAny])
def create_feedback(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        feedback = serializer.save()
        return Response({"message": "Feedback submitted successfully", "id": feedback.id}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_feedbacks(request):
    feedbacks = Feedbacks.objects.all().order_by('-created_at')
    serializer = FeedbackSerializer(feedbacks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_feedback(request, pk):
    feedback = get_object_or_404(Feedbacks, id=pk)
    serializer = FeedbackSerializer(feedback)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([AllowAny])
def update_feedback(request, pk):
    feedback = get_object_or_404(Feedbacks, id=pk)
    serializer = FeedbackSerializer(feedback, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Feedback updated successfully"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_feedback(request, pk):
    feedback = get_object_or_404(Feedbacks, id=pk)
    feedback.delete()
    return Response({"message": "Feedback deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
