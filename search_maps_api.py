import requests
from config import SEARCH_MAPS_API_KEY


def find_nearest_organisation(ll, span, organization_type):
    response = requests.get('http://search-maps.yandex.ru/1.x/', params={
        'apikey': SEARCH_MAPS_API_KEY,
        'spn': ','.join(map(str, span)),
        'll': ",".join(map(str, ll)),
        'text': organization_type,
        'lang': 'ru_RU',
        'type': 'biz',
    })

    if not response:
        raise RuntimeError(
            f'''Ошибка выполнения запроса:
                {response.request.url}
                Http статус: {response.status_code} ({response.reason})''')

    # Преобразуем ответ в json-объект
    data = response.json()
    # Получаем первый топоним из ответа геокодера.
    # Согласно описанию ответа он находится по следующему пути:
    features = data['response']['GeoObjectCollection']['featureMember']
    return features[0]['GeoObject'] if features else None

