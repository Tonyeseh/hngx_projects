# REST API simeple application

Simple RESTAPI application

## Install

    pip install -r requirement.txt

## Run the app locally

    python app.py

# REST API

The REST API to the example app is described below.

## Create a new Person

### Request
    HTTP/1.1 201 Created
    Date: Thu, 24 Feb 2023 12:36:31 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /api/
    Content-Length: 35

`POST /api/`

    curl -H 'Accept: application/json' -d 'name=Foo&email=new' http://localhost:5000/api

### Response

    {"id":32557aec-e063-4342-ada0-b02b2022c245,"name":"Foo","email":"new"}

## Get a specific Person

### Request

`GET /api/id`

    curl -H 'Accept: application/json' http://localhost:5000/api/32557aec-e063-4342-ada0-b02b2022c245

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2023 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 36

    {"id":32557aec-e063-4342-ada0-b02b2022c245,"name":"Foo","email":"new"}

## Get a non-existent Person

### Request

`GET /api/id`

    curl -i -H 'Accept: application/json' http://localhost:5000/api/9999

### Response

    HTTP/1.1 404 Not Found
    Date: Thu, 24 Feb 2023 12:36:30 GMT
    Status: 404 Not Found
    Connection: close
    Content-Type: application/json
    Content-Length: 35

    {"message":"Invalid ID","status":"error"}

## Create another new Person

### Request

`POST /api/`

    curl -i -H 'Accept: application/json' -d 'name=Bar&junk=rubbish' http://localhost:5000/api

### Response

    HTTP/1.1 201 Created
    Date: Thu, 24 Feb 2023 12:36:31 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /api
    Content-Length: 35

    {"id":6a9e69b9-c016-41d4-b031-2e1d8e27400d,"name":"Bar","email":null}


## Change a Person's state

### Request

`PUT /api`

    curl -i -H 'Accept: application/json' -X PUT http://localhost:5000/api/6a9e69b9-c016-41d4-b031-2e1d8e27400d -d 'name=Bar&email=rubbish'

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2023 12:36:31 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 40

    {"id":6a9e69b9-c016-41d4-b031-2e1d8e27400d,"name":"Bar","email":"rubbish"}
