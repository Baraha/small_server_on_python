from flask import request
from flask_restful import Resource
import hashlib
import requests


def ItemDataSchema(data):
	return {
		"id": data.get('id'),
		"email_hash": data.get('hash'),
		"url": data.get('profileUrl'),
		"alias": data.get('preferredUsername'),
		"thumb": data.get('thumbnailUrl'),
		"photos": data.get('photos'),
		"person": data.get('name').get("formatted"),
		"location": data.get('currentLocation'),
		"emails ": data.get('emails'),
		"accounts": data.get('accounts'),
		"urls ": data.get('urls')
	}



class DataResource(Resource):
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
		hash_object = data.get('hash')
		id_object = data.get('id')

		return ItemDataSchema(data)