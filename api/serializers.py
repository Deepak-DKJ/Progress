from rest_framework import serializers
from .models import ChapterItem

class  ChapterItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapterItem
        fields = ['id', 'pos','subject', 'chpName', 'status', 'note']