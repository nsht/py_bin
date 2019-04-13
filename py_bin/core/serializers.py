from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Bin
from .utils import generate_slug


class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = "__all__"

    def create(self, validated_data):
        slug = generate_slug()
        chk_slug = Bin.objects.filter(slug=slug).first()
        # keep generating new slugs until no collitions are detected
        # very low probability of happening twice.
        while chk_slug is not None:
            slug = generate_slug()
            chk_slug = Bin.objects.filter(slug=slug).first()
        bin = Bin(
            slug=slug,
            content=validated_data.get("content"),
            content_format=validated_data.get("content_format"),
        )
        if validated_data.get("password") != "" or validated_data is not None:
            bin.protected = True
            bin.is_public = False
            # uses PBKDF2 by default, use check_password to verify passwords
            bin.password = make_password(validated_data.get("password"))
        bin.save()
        return bin
