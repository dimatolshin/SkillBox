from django.contrib import admin
from .models import *
import os
from dotenv import load_dotenv

load_dotenv()


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ['name', 'image']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if not change:
            image_url = obj.image.url
            obj.image_url = image_url

        if change:

            if obj.image:
                obj.image_url = obj.image.url

        obj.save()


@admin.register(CardForPage8)
class CardForPage8Admin(admin.ModelAdmin):
    pass


@admin.register(CardForPage13)
class CardForPage13Admin(admin.ModelAdmin):
    pass


@admin.register(CardForPage14)
class CardForPage14Admin(admin.ModelAdmin):
    pass


@admin.register(CardForPage15)
class CardForPage15Admin(admin.ModelAdmin):
    pass


@admin.register(CardForPage16)
class CardForPage16Admin(admin.ModelAdmin):
    pass


@admin.register(Page5)
class Page5Admin(admin.ModelAdmin):
    readonly_fields = ['title']


@admin.register(Page6)
class Page6Admin(admin.ModelAdmin):
    readonly_fields = ['title']


@admin.register(Page8)
class Page8Admin(admin.ModelAdmin):
    readonly_fields = ['title']


@admin.register(Page11)
class Page11Admin(admin.ModelAdmin):
    readonly_fields = ['title']


@admin.register(Page13)
class Page13Admin(admin.ModelAdmin):
    readonly_fields = ['title']


@admin.register(Page14)
class Page14Admin(admin.ModelAdmin):
    readonly_fields = ['title']


@admin.register(Page15)
class Page15Admin(admin.ModelAdmin):
    readonly_fields = ['title']


@admin.register(Page16)
class Page16Admin(admin.ModelAdmin):
    readonly_fields = ['title']


@admin.register(Page22)
class Page22Admin(admin.ModelAdmin):
    readonly_fields = ['title']


@admin.register(Сourse)
class СourseAdmin(admin.ModelAdmin):
    fields = ['name', 'direction', 'page5', 'page6', 'page8', 'page11', 'page13', 'page14', 'page15', 'page16',
              'page22', 'url_link']
    readonly_fields = ['url_link']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if not change and obj.name and obj.direction:
            obj.url_link = f'https://{os.getenv("NAME_SERVER")}/api/main_page/?course_name={obj.name}&direction={obj.direction}'

        if change and obj.name and obj.direction:
            obj.url_link = f'https://{os.getenv("NAME_SERVER")}/?course_name={obj.name}&direction={obj.direction}'

        obj.save()



