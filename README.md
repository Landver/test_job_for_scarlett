# Library API

## Install and build app
```
git clone ...
cd library-test-project
sh build.sh
```

## Book Parser
Instead of just manually add the dummy book I had created the scraper that scan https://thegreatestbooks.org/the-greatest-fiction-since
And parse it's books. To parse the book run command:
`docker exec -ti ligrary-web /bin/bash -c "src/manage.py parsebooks"`

## API docs 
#### Book List API `/api/books/`
#### Example of search request to find books by their genre name: http://135.181.78.121:8344/api/books/?genres__name=Action%20and%20Adventure
`HTTP 200 OK`
`Allow: GET, POST, HEAD, OPTIONS`
`Content-Type: application/json`
```
{
    "count": integer("count book instance"),
    "next": string("url next page"),
    "previous": string("url previous page"),
    "results": [
        {
            "id": integer("book id"),
            "writer": {
                "id": integer("writer id"),
                "first_name": string("First Name"),
                "last_name": string("Last Name")
            },
            "genres": [
                {
                    "id": integer("genre id"),
                    "name": string("genre name")
                }
            ],
            "name": string("book name"),
            "synopsis": string("book synopsis"),
            "release_date": string("release date"),
            "price": decimal("price")
        }
    ]
}
```

#### Book Detail API `api/books/<id:int>/`
`HTTP 200 OK`
`Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS`
`Content-Type: application/json`
```
{
    "id": integer("book id"),
    "writer": {
        "id": integer("writer id"),
        "first_name": string("First Name"),
        "last_name": string("Last Name")
    },
    "genres": [
        {
            "id": integer("genre id"),
            "name": string("genre name")
        }
    ],
    "name": string("book name"),
    "synopsis": string("book synopsis"),
    "release_date": string("book date"),
    "price": decimal("book price")
}
```