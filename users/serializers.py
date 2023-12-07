from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        user.set_password(user.password)
        user.is_active = True
        user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'email', 'password')
