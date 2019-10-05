from utils.Container import Container

ARGS = Container(
    headers=Container(
        accept='application/json',
        Authorization='Bearer {token}'
    ),
    params=Container(datasource='tranquility')
)
MONGO_LOGIN_PATH='./../settings/mongo_login.json'
MARIA_LOGIN_PATH='./../settings/maria_login.json'
SEED_DATA = Container()
SEED_THREADS = Container()
SEED_TOKEN = Container(
    db='NewEdenAnalytics',
    coll='eve_characters',
    value=None,
    expires=None
)
SEED_REFRESH = Container()
TOKEN_SHORT_SLEEP_SEC = 60
URL_RETRYS = 5
URLS = Container(
    location='https://esi.evetech.net/latest/characters/{char_id}/location/',
    online='https://esi.evetech.net/latest/characters/{char_id}/online/',
    ship='https://esi.evetech.net/latest/characters/{char_id}/ship/'
)