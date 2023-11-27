# Создание образа
docker build -t my_django:v1 .

# Запуск контейнера
docker run -it -p 8000:8000 my_django:v1

