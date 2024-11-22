from rest_framework import serializers
from .models import Item, Room, User, Messages, Topic


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def to_representation(self, instance):
        response = super().to_representation(instance)
        # Add additional custom processing for the response if needed
        return response

    def validate(self, data):
        # Example: Custom validation logic
        if data.get("field_name") == "invalid_value":
            raise serializers.ValidationError(
                {"field_name": "This value is not allowed."}
            )
        return data

    # hash password
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = "__all__"


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"
