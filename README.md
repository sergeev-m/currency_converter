# Конвектор валют.

Тестовое задание.


### Технологии
- Python 3.11
- FastApi 0.100.0
- Docker

### Как запустить проект:
- Клонировать репозиторий и перейти в него в командной строке:

```bash
https://github.com/sergeev-m/currency_convector.git
cd currency_convector
```

- Запустить
```bash
docker-compose up -d
````

Пример запроса:

```
GET /api/rates?from=USD&to=RUB&value=1
```

Ответ:

```json
{
"result": 62.16
}
```

### Контакты

Михаил  
[email](server-15@yandex.ru)  
[telegram](https://t.me/sergeev_mikhail)
