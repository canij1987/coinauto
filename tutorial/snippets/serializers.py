from rest_framework import serializers
from .models import UserProfileInfo


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserProfileInfo
        fields = ('id', 'owner', 'point')


class ProfileSerializer2(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserProfileInfo
        fields = ('id', 'owner', 'point', 'connect_key', 'secret_key')
        read_only_fields = ('connect_key', 'secret_key')


