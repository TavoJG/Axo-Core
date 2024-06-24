from rest_framework import serializers

from authentication.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ["id", "email", "is_staff", "groups"]
