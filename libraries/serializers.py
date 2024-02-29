from rest_framework import serializers

from .models import LibraryMember


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryMember
        fields = '__all__'
