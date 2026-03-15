from rest_framework import serializers 
from .models import account
from django.contrib.auth.hashers import make_password
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class RoomUser(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ('username' , 'profileImage')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ('username' , 'email', 'first_name' , 'last_name' , 'profileImage' , 'profile_banner')
        read_only_fields = (['email' , 'username'])

class CustomUserDetailsSerializer(UserDetailsSerializer):
    
    full_name = serializers.SerializerMethodField()

    class Meta(UserDetailsSerializer.Meta):
        model = account
        fields = ('full_name', 'username' , 'email', 'first_name' , 'last_name' , 'profileImage' , 'profile_banner' )
        read_only_fields = ('email', 'full_name')

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip() or obj.username

    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('userprofile', {})
    #     instance = super().update(instance, validated_data)

    #     if profile_data:
    #         profile = instance.userprofile
    #         for attr, value in profile_data.items():
    #             setattr(profile, attr, value)
    #         profile.save()

    #     return instance

####################################################################3

# class Sign_UpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = account
#         fields = ('username' , 'email' , 'password' , 'first_name' , 'last_name' , 'profileImage')

#     def create(self, validated_data):
#         return account.objects.create(**validated_data)
    
#     def validate_password(self, value: str) -> str:
#         return make_password(value)
    

# class JoinRoom(serializers.ModelSerializer):
#     class Meta:
#         model = account
#         fields = ('join_room')