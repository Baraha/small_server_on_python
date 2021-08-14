from flask import request
from flask_restful import Resource
import hashlib
import requests


def checkItem(data):
	# Проверяем наличие имени
	if data.get('name'):
		# Забираем форматированный формат имени
		return data.get('name').get("formatted")
	return None


def ItemDataSchema(data):
	# Создаем Json формат, лучше использовать marshmallow, если бы это было приложение
	return {
		"id": data.get('id'),
		"email_hash": data.get('hash'),
		"url": data.get('profileUrl'),
		"alias": data.get('preferredUsername'),
		"thumb": data.get('thumbnailUrl'),
		"photos": data.get('photos'),
		"person": checkItem(data),
		"location": data.get('currentLocation'),
		"emails ": data.get('emails'),
		"accounts": data.get('accounts'),
		"urls ": data.get('urls')
	}



class DataResource(Resource):
	"""
	Сервис дает возможность работать с gravatar забирая и форматируя данные о каждом пользователе
	чтобы возспользоваться, body нашего request должно быть таким
	{
	"email":"kostbebix@yahoo.com"
	}
	email - Почта нашего пользователя, по которой и будет происходит поиск

	Ответ от сервера:

	{
	"id": "17467145",
    "email_hash": "d6ac4c55425d6f9d28db9068dbb49e09",
    "url": "http://gravatar.com/kostbebix",
    "alias": "kostbebix",
    "thumb": "https://secure.gravatar.com/avatar/d6ac4c55425d6f9d28db9068dbb49e09",
    "photos": [
        {
            "value": "https://secure.gravatar.com/avatar/d6ac4c55425d6f9d28db9068dbb49e09",
            "type": "thumbnail"
        }
    ],
    "person": "kost BebiX",
    "location": "Kiev, Ukraine",
    "emails ": [
        {
            "primary": "true",
            "value": "k.bx@ya.ru"
        }
    ],
    "accounts": [
        {
            "domain": "twitter.com",
            "display": "@kost_bebix",
            "url": "http://twitter.com/kost_bebix",
            "username": "kost_bebix",
            "verified": "true",
            "shortname": "twitter"
        }
    ],
    "urls ": []
	}
	"""
	def post(self):
		data = request.json['email']
		name = data[: data.find("@")]
		url = f'https://ru.gravatar.com/{name}.json'
		r = requests.get(url)
		if r.status_code == 404:
			return {"error": "User not found"}

		if r.status_code == 500:
			return {"error": "Unexpected error"}

		hash_object_data = r.json().get('entry')
		data = hash_object_data[0]
		
		return ItemDataSchema(data)