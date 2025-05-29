from rest_framework import serializers
from .models import *


class DataMainPage(serializers.Serializer):
    course_name = serializers.CharField()


class AMOCRM(serializers.Serializer):
    username = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()
    course_name = serializers.CharField()
    utm_source = serializers.CharField()
    utm_medium = serializers.CharField()
    utm_content = serializers.CharField()
    utm_campaign = serializers.CharField()
    utm_term = serializers.CharField()
    full_link = serializers.CharField()


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image_url']


class Page5Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page5
        fields = '__all__'


class Page6Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page6
        fields = '__all__'


class CardForPage8Serializer(serializers.ModelSerializer):
    image = ImageSerializer(allow_null=True)

    class Meta:
        model = CardForPage8
        fields = '__all__'


class Page8Serializer(serializers.ModelSerializer):
    cards = CardForPage8Serializer(many=True)

    class Meta:
        model = Page8
        fields = '__all__'


class Page11Serializer(serializers.ModelSerializer):
    collect_image = ImageSerializer(many=True)

    class Meta:
        model = Page11
        fields = '__all__'


class CardForPage13Serializer(serializers.ModelSerializer):
    image = ImageSerializer(allow_null=True)

    class Meta:
        model = CardForPage13
        fields = '__all__'


class Page13Serializer(serializers.ModelSerializer):
    cards = CardForPage13Serializer(many=True)

    class Meta:
        model = Page13
        fields = '__all__'


class CardForPage14Serializer(serializers.ModelSerializer):
    image = ImageSerializer(allow_null=True)

    class Meta:
        model = CardForPage14
        fields = '__all__'


class Page14Serializer(serializers.ModelSerializer):
    cards = CardForPage14Serializer(many=True)

    class Meta:
        model = Page14
        fields = '__all__'


class CardForPage15Serializer(serializers.ModelSerializer):
    image = ImageSerializer(allow_null=True)

    class Meta:
        model = CardForPage15
        fields = '__all__'


class Page15Serializer(serializers.ModelSerializer):
    cards = CardForPage15Serializer(many=True)

    class Meta:
        model = Page15
        fields = '__all__'


class CardForPage16Serializer(serializers.ModelSerializer):
    image = ImageSerializer(allow_null=True)

    class Meta:
        model = CardForPage16
        fields = '__all__'


class Page16Serializer(serializers.ModelSerializer):
    cards = CardForPage16Serializer(many=True)

    class Meta:
        model = Page16
        fields = '__all__'


class Page22Serializer(serializers.ModelSerializer):
    class Meta:
        model = Page22
        fields = '__all__'


class СourseSerializer(serializers.ModelSerializer):
    page5 = Page5Serializer(allow_null=True)
    page6 = Page6Serializer(allow_null=True)
    page8 = Page8Serializer(allow_null=True)
    page11 = Page11Serializer(allow_null=True)
    page13 = Page13Serializer(allow_null=True)
    page14 = Page14Serializer(allow_null=True)
    page15 = Page15Serializer(allow_null=True)
    page16 = Page16Serializer(allow_null=True)
    page22 = Page22Serializer(allow_null=True)

    class Meta:
        model = Сourse
        fields = '__all__'
