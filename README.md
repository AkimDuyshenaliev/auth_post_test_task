# Installation and launch:

Requirements:

- git
- Docker
- Docker compose
- SQLite
- Makefile (optional, but preferred)

With Makefile:

- Run the project: `make up`
- Stop the project: `make down`
- Show logs: `make logs`
- Restart the project: `make restart`
- Rebuild the project: `make rebuild`

Without Makefile:

- Run the project: `docker compose up -d`
- Stop the project: `docker compose down`
- Show logs: `docker compose logs app -f`
- Restart the project:
  `make down`
  `make up`
- Rebuild the project:
  `docker compose down -v`
  `docker compose up -d --build`
  `docker image prune -a -f`

Server will open at: 
`http://0.0.0.0:8000` or `http://localhost:8000`

Swagger is available at: `/docs`

Routers:
----------
Authentication:
* Register a user: `/auth/signup`
* Login an existing user: `/auth/signin`

Posts:
* Get a post by id: `/post/get`
* Create a post: `/post/create`
* Edit a post: `/post/edit`
* Delete a post: `/post/delete`

Reactions: (likes and dislikes)
* Leave a reaction to a post: `/reaction`