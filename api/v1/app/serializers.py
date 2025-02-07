from rest_framework import serializers
from apps.models import Feedbacks

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = '__all__'

