import requests
from pprint import pprint
import collections
from pathlib import Path


def get_photo(id_vk):
    url = "https://api.vk.com/method/photos.get"
    params = {
        'owner_id': id_vk,
        'album_id': 'profile',
        'access_token': '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008',
        'extended': '1',
        'v': '5.118',
        'photo_sizes': '1'
                            }
    response = requests.get(url=url, params=params).json()
    response1 = response['response']['items']
    return response1


def photo_max():
    photo_list = []
    url_list = []
    count = collections.Counter()
    for photo in get_photo(id_vk):
        name_keys = (photo['likes']['count'])
        count[name_keys] += 1
        if count[name_keys] >= 2:
            name_keys = photo['likes']['count'] + photo['date']
        url_values = photo['sizes'][-1]['url']
        photo_dict = {name_keys: url_values}
        photo_list.append(photo_dict)
        url_list.append(url_values)
    return photo_list


# def new_folder():
#     url = "https://cloud-api.yandex.net/v1/disk/resources"
#     params = {"path": album, "overwrite": "true"}
#     headers = {'Content-Type': 'application/json',
#                'Authorization': token
#                }
#     response = requests.put(url=url,  headers=headers, params=params)
#     response = response.json()
#     response = response.get('href')
#     return response

#
def upload_photo():
    url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    headers = {'Content-Type': 'application/json',
               'Authorization': token}
    params = {"path": 'VK_photo/',
              'url': photo_max(),
              "disable_redirects": "false"}
    response = requests.post(url=url,  headers=headers, params=params)
    pprint(response.json())


if __name__ == '__main__':
    # id_vk = input('введите id: ')
    id_vk = '552934290'

    get_photo(id_vk)
    photo = photo_max()
    urls = (url for name, url in photo)
    pprint(urls)

    # token = input('Введите токен')
    token = 'AQAAAAAb702VAADLW8tCNia9yU5JlUg_5YVBPtI'
    album = Path("VK_photo")
