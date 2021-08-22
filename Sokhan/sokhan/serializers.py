from rest_framework import serializers

from sokhan.models import Post


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['text']

    def create(self, validated_data):
        return Post.objects.create(
            **validated_data,
            owner=self.context['request'].user,
        )


class ProfilePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['text']


class UserPostSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Post
        fields = ['owner', 'text']
