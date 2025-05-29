from drf_yasg.utils import swagger_auto_schema
from adrf.decorators import api_view
from django.http import HttpRequest, JsonResponse
import requests

from .example import get_response_examples
from .models import *
from .serializer import СourseSerializer, DataMainPage, AMOCRM


@swagger_auto_schema(
    methods=(['GET']),
    query_serializer=DataMainPage(),
    responses={
        '404': get_response_examples({'error': True, 'Error': 'Данные переданы некорректные.'}),
        '200': get_response_examples(schema=СourseSerializer()),
    },
)
@api_view(["GET"])
async def main_page(request: HttpRequest):
    course_name = request.GET.get('course_name')
    course = await Сourse.objects.filter(name=course_name) \
        .select_related(
        'page5',
        'page6',
        'page8',
        'page11',
        'page13',
        'page14',
        'page15',
        'page16',
        'page22'
    ) \
        .prefetch_related(
        'page8__cards__image',
        'page11__collect_image',
        'page13__cards__image',
        'page14__cards__image',
        'page15__cards__image',
        'page16__cards__image'
    ) \
        .afirst()

    if not course:
        return JsonResponse({'error': 'Курс не найден'}, status=404)
    data = СourseSerializer(course).data
    return JsonResponse(data, status=200)


@swagger_auto_schema(
    methods=(['POST']),
    request_body=AMOCRM(),
    responses={
        '404': get_response_examples({'error': True, 'Error': 'Данные переданы некорректные.'}),
        '200': get_response_examples({'Info': 'Ваша заявка принята успешно'}),
    },

)
@api_view(["POST"])
async def amo_crm(request: HttpRequest):
    username = request.data.get('name')
    phone = request.data.get('phone')
    email = request.data.get('email')
    course_name = request.data.get('course_name')
    utm_source = request.data.get('utm_source')
    utm_medium = request.data.get('utm_medium')
    utm_content = request.data.get('utm_content')
    utm_campaign = request.data.get('utm_campaign')
    utm_term = request.data.get('utm_term')
    full_link = request.data.get('full_link')

    course = await Сourse.objects.filter(name=course_name).afirst()

    if not course:
        return JsonResponse({'Error': 'Курс не найден'}, status=404)

    if not username or not phone or not email or not course_name:
        return JsonResponse({'Error': 'Данные переданы некорректно'}, status=404)

    param = {
        "status_id": 37944607,
        "lead_name": f"Приобрести курс {course_name}",
        "email": f"{email}",
        "phone": f"{phone}",
        "name": f"{username}",
        "utm_source": utm_source,
        "utm_medium": utm_medium,
        "utm_content": utm_content,
        "utm_campaign": utm_campaign,
        "utm_term": utm_term,
        "platform": "Quiz",
        "direction": f"{course.direction}",
        "course_name": f"{course_name}",
        "url": full_link,
    }
    url = 'https://crm-mediator-api.lerna.me/v1/gluing/queue'

    # Отправка POST-запроса
    try:
        response = requests.post(
            url,
            json=param,
            timeout=10,
            headers={
                "Content-Type": "application/json",
            },
        )

        if response.status_code == 200:
            return JsonResponse({'Info': 'Ваша заявка принята успешно'}, status=200)

    except requests.exceptions.RequestException as e:
        return JsonResponse({'Error': e}, status=404)
