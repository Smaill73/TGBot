### Описание проекта
Телеграмм бот предназначен для быстрого поиска фильмов по рейтингам и странам

### Как пользоваться


#### custom command:

**/low** - выводит топ 10 фильмов с минимальной оценкой

Запрос без параметров:

CURL GET https://api.kinopoisk.dev/v1.4/movie?page=1&limit=11&rating.kp=0

Пример ответ запроса:

```console
{
  "docs": [
    {
      "id": 666,
      "externalId": {
        "kpHD": "48e8d0acb0f62d8585101798eaeceec5",
        "imdb": "tt0232500",
        "tmdb": 9799
      },
      "name": "Человек паук",
      "alternativeName": "Spider man",
      "enName": "Spider man",
      "names": [
        {
          "name": "string",
          "language": "string",
          "type": "string"
        }
      ],
      "type": "movie",
      "typeNumber": 1,
      "year": 2023,
      "description": "string",
      "shortDescription": "string",
      "slogan": "string",
      "status": "completed",
      "facts": [
        {
          "value": "string",
          "type": "string",
          "spoiler": true
        }
      ],
      "rating": {
        "kp": 6.2,
        "imdb": 8.4,
        "tmdb": 3.2,
        "filmCritics": 10,
        "russianFilmCritics": 5.1,
        "await": 6.1
      },
      "votes": {
        "kp": "60000",
        "imdb": 50000,
        "tmdb": 10000,
        "filmCritics": 10000,
        "russianFilmCritics": 4000,
        "await": 34000
      },
      "movieLength": 120,
      "ratingMpaa": "pg13",
      "ageRating": 16,
      "logo": {
        "url": "string"
      },
      "poster": {
        "url": "string",
        "previewUrl": "string"
      },
      "backdrop": {
        "url": "string",
        "previewUrl": "string"
      },
      "videos": {
        "trailers": [
          {
            "url": "https://www.youtube.com/embed/ZsJz2TJAPjw",
            "name": "Official Trailer",
            "site": "youtube",
            "size": 0,
            "type": "TRAILER"
          }
        ]
      },
      "genres": [
        {
          "name": "string"
        }
      ],
      "countries": [
        {
          "name": "string"
        }
      ],
      "persons": [
        {
          "id": 6317,
          "photo": "https://st.kp.yandex.net/images/actor_iphone/iphone360_6317.jpg",
          "name": "Пол Уокер",
          "enName": "Paul Walker",
          "description": "string",
          "profession": "string",
          "enProfession": "string"
        }
      ],
      "reviewInfo": {
        "count": 0,
        "positiveCount": 0,
        "percentage": "string"
      },
      "seasonsInfo": [
        {
          "number": 0,
          "episodesCount": 0
        }
      ],
      "budget": {
        "value": 207283,
        "currency": "€"
      },
      "fees": {
        "world": {
          "value": 207283,
          "currency": "€"
        },
        "russia": {
          "value": 207283,
          "currency": "€"
        },
        "usa": {
          "value": 207283,
          "currency": "€"
        }
      },
      "premiere": {
        "country": "США",
        "world": "2023-02-25T02:44:39.359Z",
        "russia": "2023-02-25T02:44:39.359Z",
        "digital": "string",
        "cinema": "2023-02-25T02:44:39.359Z",
        "bluray": "string",
        "dvd": "string"
      },
      "similarMovies": [
        {
          "id": 0,
          "name": "string",
          "enName": "string",
          "alternativeName": "string",
          "type": "string",
          "poster": {
            "url": "string",
            "previewUrl": "string"
          },
          "rating": {
            "kp": 6.2,
            "imdb": 8.4,
            "tmdb": 3.2,
            "filmCritics": 10,
            "russianFilmCritics": 5.1,
            "await": 6.1
          },
          "year": 2021
        }
      ],
      "sequelsAndPrequels": [
        {
          "id": 0,
          "name": "string",
          "enName": "string",
          "alternativeName": "string",
          "type": "string",
          "poster": {
            "url": "string",
            "previewUrl": "string"
          },
          "rating": {
            "kp": 6.2,
            "imdb": 8.4,
            "tmdb": 3.2,
            "filmCritics": 10,
            "russianFilmCritics": 5.1,
            "await": 6.1
          },
          "year": 2021
        }
      ],
      "watchability": {
        "items": [
          {
            "name": "string",
            "logo": {
              "url": "string"
            },
            "url": "string"
          }
        ]
      },
      "releaseYears": [
        {
          "start": 2022,
          "end": 2023
        }
      ],
      "top10": 1,
      "top250": 200,
      "ticketsOnSale": true,
      "totalSeriesLength": 155,
      "seriesLength": 20,
      "isSeries": true,
      "audience": [
        {
          "count": 1000,
          "country": "Россия"
        }
      ],
      "lists": [
        "250 лучших сериалов"
      ],
      "networks": {
        "items": [
          {
            "name": "Netflix",
            "logo": {
              "url": "string"
            }
          }
        ]
      },
      "updatedAt": "2024-04-04T13:58:16.608Z",
      "createdAt": "2024-04-04T13:58:16.608Z"
    }
  ],
  "total": 0,
  "limit": 0,
  "page": 0,
  "pages": 0
}
```

**/high** - выводит топ 10 фильмов с максиамльной оценкой

Запрос без параметров:

CURL GET https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&rating.kp=9-10

Ответ запроса:
```console
{
  "docs": [
    {
      "id": 666,
      "externalId": {
        "kpHD": "48e8d0acb0f62d8585101798eaeceec5",
        "imdb": "tt0232500",
        "tmdb": 9799
      },
      "name": "Человек паук",
      "alternativeName": "Spider man",
      "enName": "Spider man",
      "names": [
        {
          "name": "string",
          "language": "string",
          "type": "string"
        }
      ],
      "type": "movie",
      "typeNumber": 1,
      "year": 2023,
      "description": "string",
      "shortDescription": "string",
      "slogan": "string",
      "status": "completed",
      "facts": [
        {
          "value": "string",
          "type": "string",
          "spoiler": true
        }
      ],
      "rating": {
        "kp": 6.2,
        "imdb": 8.4,
        "tmdb": 3.2,
        "filmCritics": 10,
        "russianFilmCritics": 5.1,
        "await": 6.1
      },
      "votes": {
        "kp": "60000",
        "imdb": 50000,
        "tmdb": 10000,
        "filmCritics": 10000,
        "russianFilmCritics": 4000,
        "await": 34000
      },
      "movieLength": 120,
      "ratingMpaa": "pg13",
      "ageRating": 16,
      "logo": {
        "url": "string"
      },
      "poster": {
        "url": "string",
        "previewUrl": "string"
      },
      "backdrop": {
        "url": "string",
        "previewUrl": "string"
      },
      "videos": {
        "trailers": [
          {
            "url": "https://www.youtube.com/embed/ZsJz2TJAPjw",
            "name": "Official Trailer",
            "site": "youtube",
            "size": 0,
            "type": "TRAILER"
          }
        ]
      },
      "genres": [
        {
          "name": "string"
        }
      ],
      "countries": [
        {
          "name": "string"
        }
      ],
      "persons": [
        {
          "id": 6317,
          "photo": "https://st.kp.yandex.net/images/actor_iphone/iphone360_6317.jpg",
          "name": "Пол Уокер",
          "enName": "Paul Walker",
          "description": "string",
          "profession": "string",
          "enProfession": "string"
        }
      ],
      "reviewInfo": {
        "count": 0,
        "positiveCount": 0,
        "percentage": "string"
      },
      "seasonsInfo": [
        {
          "number": 0,
          "episodesCount": 0
        }
      ],
      "budget": {
        "value": 207283,
        "currency": "€"
      },
      "fees": {
        "world": {
          "value": 207283,
          "currency": "€"
        },
        "russia": {
          "value": 207283,
          "currency": "€"
        },
        "usa": {
          "value": 207283,
          "currency": "€"
        }
      },
      "premiere": {
        "country": "США",
        "world": "2023-02-25T02:44:39.359Z",
        "russia": "2023-02-25T02:44:39.359Z",
        "digital": "string",
        "cinema": "2023-02-25T02:44:39.359Z",
        "bluray": "string",
        "dvd": "string"
      },
      "similarMovies": [
        {
          "id": 0,
          "name": "string",
          "enName": "string",
          "alternativeName": "string",
          "type": "string",
          "poster": {
            "url": "string",
            "previewUrl": "string"
          },
          "rating": {
            "kp": 6.2,
            "imdb": 8.4,
            "tmdb": 3.2,
            "filmCritics": 10,
            "russianFilmCritics": 5.1,
            "await": 6.1
          },
          "year": 2021
        }
      ],
      "sequelsAndPrequels": [
        {
          "id": 0,
          "name": "string",
          "enName": "string",
          "alternativeName": "string",
          "type": "string",
          "poster": {
            "url": "string",
            "previewUrl": "string"
          },
          "rating": {
            "kp": 6.2,
            "imdb": 8.4,
            "tmdb": 3.2,
            "filmCritics": 10,
            "russianFilmCritics": 5.1,
            "await": 6.1
          },
          "year": 2021
        }
      ],
      "watchability": {
        "items": [
          {
            "name": "string",
            "logo": {
              "url": "string"
            },
            "url": "string"
          }
        ]
      },
      "releaseYears": [
        {
          "start": 2022,
          "end": 2023
        }
      ],
      "top10": 1,
      "top250": 200,
      "ticketsOnSale": true,
      "totalSeriesLength": 155,
      "seriesLength": 20,
      "isSeries": true,
      "audience": [
        {
          "count": 1000,
          "country": "Россия"
        }
      ],
      "lists": [
        "250 лучших сериалов"
      ],
      "networks": {
        "items": [
          {
            "name": "Netflix",
            "logo": {
              "url": "string"
            }
          }
        ]
      },
      "updatedAt": "2024-04-04T13:58:16.608Z",
      "createdAt": "2024-04-04T13:58:16.608Z"
    }
  ],
  "total": 0,
  "limit": 0,
  "page": 0,
  "pages": 0
}
```

**/custom** - выводит топ 10 фильмов с максиамльной оценкой, выпущенные выбранные пользователем страной

Запрос с параметрами:

CURL POST: 

https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&countries.name=%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F

https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&countries.name=%D0%A1%D0%A8%D0%90

https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&countries.name=%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%BE%D0%B1%D1%80%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D1%8F

https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&countries.name=%D0%A4%D1%80%D0%B0%D0%BD%D1%86%D0%B8%D1%8F


Ответ запроса:
```console
{
  "docs": [
    {
      "id": 666,
      "externalId": {
        "kpHD": "48e8d0acb0f62d8585101798eaeceec5",
        "imdb": "tt0232500",
        "tmdb": 9799
      },
      "name": "Человек паук",
      "alternativeName": "Spider man",
      "enName": "Spider man",
      "names": [
        {
          "name": "string",
          "language": "string",
          "type": "string"
        }
      ],
      "type": "movie",
      "typeNumber": 1,
      "year": 2023,
      "description": "string",
      "shortDescription": "string",
      "slogan": "string",
      "status": "completed",
      "facts": [
        {
          "value": "string",
          "type": "string",
          "spoiler": true
        }
      ],
      "rating": {
        "kp": 6.2,
        "imdb": 8.4,
        "tmdb": 3.2,
        "filmCritics": 10,
        "russianFilmCritics": 5.1,
        "await": 6.1
      },
      "votes": {
        "kp": "60000",
        "imdb": 50000,
        "tmdb": 10000,
        "filmCritics": 10000,
        "russianFilmCritics": 4000,
        "await": 34000
      },
      "movieLength": 120,
      "ratingMpaa": "pg13",
      "ageRating": 16,
      "logo": {
        "url": "string"
      },
      "poster": {
        "url": "string",
        "previewUrl": "string"
      },
      "backdrop": {
        "url": "string",
        "previewUrl": "string"
      },
      "videos": {
        "trailers": [
          {
            "url": "https://www.youtube.com/embed/ZsJz2TJAPjw",
            "name": "Official Trailer",
            "site": "youtube",
            "size": 0,
            "type": "TRAILER"
          }
        ]
      },
      "genres": [
        {
          "name": "string"
        }
      ],
      "countries": [
        {
          "name": "string"
        }
      ],
      "persons": [
        {
          "id": 6317,
          "photo": "https://st.kp.yandex.net/images/actor_iphone/iphone360_6317.jpg",
          "name": "Пол Уокер",
          "enName": "Paul Walker",
          "description": "string",
          "profession": "string",
          "enProfession": "string"
        }
      ],
      "reviewInfo": {
        "count": 0,
        "positiveCount": 0,
        "percentage": "string"
      },
      "seasonsInfo": [
        {
          "number": 0,
          "episodesCount": 0
        }
      ],
      "budget": {
        "value": 207283,
        "currency": "€"
      },
      "fees": {
        "world": {
          "value": 207283,
          "currency": "€"
        },
        "russia": {
          "value": 207283,
          "currency": "€"
        },
        "usa": {
          "value": 207283,
          "currency": "€"
        }
      },
      "premiere": {
        "country": "США",
        "world": "2023-02-25T02:44:39.359Z",
        "russia": "2023-02-25T02:44:39.359Z",
        "digital": "string",
        "cinema": "2023-02-25T02:44:39.359Z",
        "bluray": "string",
        "dvd": "string"
      },
      "similarMovies": [
        {
          "id": 0,
          "name": "string",
          "enName": "string",
          "alternativeName": "string",
          "type": "string",
          "poster": {
            "url": "string",
            "previewUrl": "string"
          },
          "rating": {
            "kp": 6.2,
            "imdb": 8.4,
            "tmdb": 3.2,
            "filmCritics": 10,
            "russianFilmCritics": 5.1,
            "await": 6.1
          },
          "year": 2021
        }
      ],
      "sequelsAndPrequels": [
        {
          "id": 0,
          "name": "string",
          "enName": "string",
          "alternativeName": "string",
          "type": "string",
          "poster": {
            "url": "string",
            "previewUrl": "string"
          },
          "rating": {
            "kp": 6.2,
            "imdb": 8.4,
            "tmdb": 3.2,
            "filmCritics": 10,
            "russianFilmCritics": 5.1,
            "await": 6.1
          },
          "year": 2021
        }
      ],
      "watchability": {
        "items": [
          {
            "name": "string",
            "logo": {
              "url": "string"
            },
            "url": "string"
          }
        ]
      },
      "releaseYears": [
        {
          "start": 2022,
          "end": 2023
        }
      ],
      "top10": 1,
      "top250": 200,
      "ticketsOnSale": true,
      "totalSeriesLength": 155,
      "seriesLength": 20,
      "isSeries": true,
      "audience": [
        {
          "count": 1000,
          "country": "Россия"
        }
      ],
      "lists": [
        "250 лучших сериалов"
      ],
      "networks": {
        "items": [
          {
            "name": "Netflix",
            "logo": {
              "url": "string"
            }
          }
        ]
      },
      "updatedAt": "2024-04-04T13:58:16.608Z",
      "createdAt": "2024-04-04T13:58:16.608Z"
    }
  ],
  "total": 0,
  "limit": 0,
  "page": 0,
  "pages": 0
}
```

**/history** - выводит последние 10 использованных команд пользователем

#### default command:

**/start** - запускает бота, выводит приветсвие с именем пользователя

**/help** - выводит все командв бота

### Как запустить
1. Устонавливаем и запускаем виртуальное окружение:

Команда для Windows:

```
python -m venv venv
```

Команда для Linux и macOS:

```
python3 -m venv venv 
```

Команда для Windows:

```
source venv/Scripts/activate
```

Для Linux и macOS:

```
source venv/bin/activate
```

2. Установка зависимости

```
pip install -r requirements.txt
```

3. Запуск main.py файла

```
python main.py
```