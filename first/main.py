import pip
pip.main(['install', '-r', 'requirements.txt'])

from app import create_app

app = create_app()

if __name__ == "__main__":
	# Запуск сервера
	app.run(host="0.0.0.0")
