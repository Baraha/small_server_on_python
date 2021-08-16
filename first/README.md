## Documentation

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






#### Настройка окружения
Перейдите в каталог, в котром собираетесь хранить исходные файлы проектов.  
Скачайте исходники:
```bash
git clone https://github.com/Baraha/crypto_server.git
```

Для того, чтобы запустить парсинг, нужно послать Post запрос, Сделать это
можно из приложений по типу Restman или Postman

Тут я оставлю пример post запроса через консоль
##### Запуск сервера
```bash
python3 main.py
```

##### Post запрос
```bash
curl -X POST http://127.0.0.1:5000/api/user_info/ -H "Content-type: application/json" -d '{"email":"kostbebix@gmail.com"}'
```