### About Ankard
A flashcard project to optimize my learning efficiency.

### Architecture Design
```
ankard/
├── backend/
│   ├── apps/
│   ├── config/
│   ├── manage.py
│   ├── requirements.txt
│   ├── static/
|   ├── .env
│   └── Dockerfile
├── frontend/
│   ├── public/
│   ├── src/
│   ├── tsconfig.json
│   ├── package.json
│   ├── vite.config.js
│   ├── Dockerfile
│   └── dist/
├── nginx/                 # TODO: Update for production. Use values from .env.
│   ├── default.conf
│   └── Dockerfile
├── docker-compose.yml     # TODO: Update for production. Use values from .env.
├── .gitignore
└── README.md
```
