# Osaühingud
An application that suspiciously resembles the functionality of Äriregister.

## Used technologies
* Vue 3 with Sass, TypeScript and few small libraries for Front-End
* FastAPI with SQLAlchemy for Back-End
* PostgreSQL for database

## How to run?
### Docker
Docker should be pre-installed. Docker will create three separate containers for Front-End, Back-End and PostgreSQL database.
```shell
docker-compose up -d
```
### Manually
Python (>3.9), Node.js (>latest LTS) should be pre-installed. A lower version does not guarantee anything.

#### Back-End

##### Install dependencies
```shell
pip install -r requirements.txt
```

##### Start server
```shell
python main.py
```

#### Front-End
Located in `./frontend` directory.

##### Install dependencies
```shell
npm install
```
##### Serve project
```shell
npm run serve
```

## Initial data
To create initial data, you should send POST request to `/admin/initialize-data`.
```shell
curl -X POST http://localhost:8000/admin/initialize-data
```
Response should contain code 200 OK and body `Initial data created`.

## Explanations
### Validations
Mostly, validations are duplicated on FE and BE, but some case, where validation is not duplicated may occur.
### Used technologies
Used technologies are free-to-use and can be launched on any platform. 
Vue.js used as my primary and preferred Front-End framework. 
FastAPI looks for me more modern, in the comparison with Flask and Django, for example.
SQLAlchemy used to avoid creating numerous mappings for different models, 
but some occurrences may still happen here in exceptional cases.

