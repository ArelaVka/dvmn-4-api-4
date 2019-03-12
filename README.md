# dvmn-4-api-4
dvmn - API веб-сервисов - Урок 4. Ты просто космос
# Задание
* Автоматизировать сбор фотографий космоса
* Сделайть скрипт для их публикации в инстаграм
## Для использования необходимо
* установить python3
* установить необходимые зависимости (используя pip или pip3):
```bash
pip3 install -r requirements.txt
```
* создать файл с аутентификационными данными для подключения к instagram (.env):
```
INSTA_LOGIN=<instagram_login>
INSTA_PASS=<instagram_password>
```
### Для загрузки изображений с Хаббла можно использовать отдельно скрипт fetch_hubble.py
```bash
python3 fetch_hubble.py
```
### Для загрузки изображений SpaceX можно использовать отдельно скрипт fetch_spacex.py
```bash
python3 fetch_spacex.py
```
### Использование основного скрипта (main.py) загрузит изображения в директорию images и выгрузит в instagram
```bash
python3 main.py
```
