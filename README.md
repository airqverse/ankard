### About Ankard
A flashcard project to optimize my learning efficiency.

### Architecture Design
```
ankard/
├── services/
│   ├── api_gateway/                              # Delivery layer (Django, FastAPI, etc.)
│   │   ├── controller/                           # Views, DRF ViewSets, serializers
│   │   ├── settings/                             # Django project(config) folder
│   │   ├── urls.py
│   │   ├── manage.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   └── core/                                     # Application & domain logic
│       ├── domains/                              # Entities, aggregates, value objects
│       │   └── users/
│       │       ├── models/
│       │       │   └── user.py                   # Domain Entity
│       │       ├── value_objects/
│       │       └── events/
│       ├── services/                             # Service layer = Application orchestration
│       │   └── users/
│       │       ├── register_user_service.py
│       │       └── change_email_service.py
│       ├── interfaces/                           # Infrastructure ports (DB, APIs, etc.)
│       │   └── user_repository.py
│       ├── shared/                               # Reusable validators, enums, exceptions
│       └── setup.py                              # Makes app_core installable in api_gateway
│
├── web/                                          # SPA frontend
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md                                     # Wow, I'm in myself XD
```

### Database Responsibility
| Layer | Reads/Writes DB? | Knows about ORM? | Role |
| ----- | ---------------- | ---------------- | ---- |
| Domain (models/) | ❌ | ❌ | Core business rules |
| Value Objects | ❌ | ❌ | Pure data & rules |
| Service Layer | ✅ | ❌ | Coordinates use cases |
| Repository | ✅ | ✅ | Implements queries, persistence |
| Infrastructure | ✅ | ✅ | Actual connection to DB via Django ORM |
