# Асинхронный парсер PEP

## Описание
В проекте реализован асинхронный парсер документов PEP на базе фреймворка Scrapy. Вывод собранной информации осуществляется в два файла:
- файл со списком PEP
- статусы всех стандартов PEP

## Запуск проекта
- Клонируйте репозиторий
```
git@github.com:Vadikray/scrapy_parser_pep.git
```
- Установите и активируйте виртуальное окружение
```
python3 -m venv venv
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
python3 -m pip install --upgrade pip
```
- Запускаем парсер pep
```
scrapy crawl pep
```

## Технологии
- Python v3.7.9
- Scrapy v2.5.1

## Автор
Конюшков В.А.
https://t.me/Vadikray