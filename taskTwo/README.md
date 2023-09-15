# REST API simeple application

This is a bare-bones example of a Sinatra application providing a REST
API to a DataMapper-backed model.

The entire application is contained within the `app.rb` file.

`config.ru` is a minimal Rack configuration for unicorn.

`run-tests.sh` runs a simplistic test and generates the API
documentation below.

It uses `run-curl-tests.rb` which runs each command defined in
`commands.yml`.

## Install

    pip install -r requirement.txt

## Run the app locally

    python app.py

# REST API

The REST API to the example app is described below.

## Create a new Thing

### Request
    HTTP/1.1 201 Created
    Date: Thu, 24 Feb 2023 12:36:31 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /thing/2
    Content-Length: 35

`POST /thing/`

    curl -H 'Accept: application/json' -d 'name=Foo&email=new' http://localhost:5000/api

### Response

    {"id":32557aec-e063-4342-ada0-b02b2022c245,"name":"Foo","email":"new"}

## Get a specific Thing

### Request

`GET /thing/id`

    curl -H 'Accept: application/json' http://localhost:7000/thing/32557aec-e063-4342-ada0-b02b2022c245

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2023 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 36

    {"id":32557aec-e063-4342-ada0-b02b2022c245,"name":"Foo","email":"new"}

## Get a non-existent Thing

### Request

`GET /thing/id`

    curl -i -H 'Accept: application/json' http://localhost:7000/thing/9999

### Response

    HTTP/1.1 404 Not Found
    Date: Thu, 24 Feb 2023 12:36:30 GMT
    Status: 404 Not Found
    Connection: close
    Content-Type: application/json
    Content-Length: 35

    {"message":"Invalid ID","status":"error"}

## Create another new Thing

### Request

`POST /thing/`

    curl -i -H 'Accept: application/json' -d 'name=Bar&junk=rubbish' http://localhost:7000/thing

### Response

    HTTP/1.1 201 Created
    Date: Thu, 24 Feb 2023 12:36:31 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /thing/2
    Content-Length: 35

    {"id":6a9e69b9-c016-41d4-b031-2e1d8e27400d,"name":"Bar","email":null}


## Change a Thing's state

### Request

`PUT /thing/:id/status/changed`

    curl -i -H 'Accept: application/json' -X PUT http://localhost:7000/api/6a9e69b9-c016-41d4-b031-2e1d8e27400d -d 'name=Bar&email=rubbish'

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2023 12:36:31 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 40

    {"id":6a9e69b9-c016-41d4-b031-2e1d8e27400d,"name":"Bar","email":"rubbish"}
