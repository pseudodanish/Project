from rest_framework import serializers
from .models import Story, Page, ThreeDObject, Texture

class TextureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Texture
        fields = '__all__'

class ThreeDObjectSerializer(serializers.ModelSerializer):
    textures = TextureSerializer(many=True, read_only=True)

    class Meta:
        model = ThreeDObject
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    objects = ThreeDObjectSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = '__all__'

class StorySerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = '__all__'
