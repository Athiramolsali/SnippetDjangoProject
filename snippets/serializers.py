from rest_framework import serializers
from .models import Tag,Snippet


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']
        

class CreateSnippetSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(write_only=True)  # Accept tag title as input
    tag_data = TagSerializer(read_only=True, source='tag')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'tag','tag_data']



class OverviewSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'tag']



class UpdateSnippetSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(write_only=True,required=False)  # Accept tag title as input
    tag_data = TagSerializer(read_only=True, source='tag')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'updated_at', 'tag','tag_data']
        extra_kwargs = {
            'note': {'required': False},  # Make note optional
            'title':{'required':False},
        }
