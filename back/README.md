# Users CRUD — Backend

Express · TypeScript · Prisma · PostgreSQL · Docker

---

## Stack

| Couche       | Outil                |
|--------------|----------------------|
| Runtime      | Node.js 20           |
| Framework    | Express 4            |
| Langage      | TypeScript 5         |
| ORM          | Prisma 5             |
| Base données | PostgreSQL 16        |
| Validation   | express-validator    |
| Container    | Docker + Compose     |

---

## Structure

```
src/
├── index.ts                  # Entry point, app Express
├── controllers/
│   └── user.controller.ts    # Logique CRUD
├── routes/
│   └── user.routes.ts        # Définition des routes
├── middlewares/
│   ├── errorHandler.ts       # Gestion centralisée des erreurs
│   └── validation.ts         # Règles express-validator
└── lib/
    ├── prisma.ts             # Singleton PrismaClient
    └── types.ts              # DTOs et interfaces

prisma/
├── schema.prisma             # Modèle User + enums
└── seed.ts                   # Données initiales
```

---

## Démarrage rapide (développement)

```bash
# 1. Cloner et installer
npm install

# 2. Variables d'environnement
cp .env.example .env

# 3. Lancer PostgreSQL via Docker
docker compose up postgres -d

# 4. Migration + génération Prisma
npm run db:migrate
npm run db:generate

# 5. Seed (optionnel)
npm run db:seed

# 6. Démarrer le serveur
npm run dev
```

Serveur disponible sur `http://localhost:3000`

---

## Démarrage complet via Docker

```bash
docker compose up --build
```

Cela lance PostgreSQL + l'API. Les migrations sont appliquées automatiquement au démarrage.

---

## API Reference

### Base URL
```
http://localhost:3000/api
```

### Endpoints

| Méthode | Route            | Description                      |
|---------|------------------|----------------------------------|
| GET     | `/users`         | Liste paginée avec filtres       |
| GET     | `/users/:id`     | Détail d'un utilisateur          |
| POST    | `/users`         | Créer un utilisateur             |
| PATCH   | `/users/:id`     | Modifier partiellement           |
| DELETE  | `/users/:id`     | Supprimer                        |
| GET     | `/health`        | Health check                     |

---

### GET /api/users

**Query params**

| Param    | Type   | Défaut | Description                        |
|----------|--------|--------|------------------------------------|
| `search` | string | —      | Recherche dans prénom, nom, email  |
| `role`   | enum   | —      | `USER` / `MODERATOR` / `ADMIN`     |
| `status` | enum   | —      | `ACTIVE` / `INACTIVE`             |
| `page`   | number | 1      | Page courante                      |
| `limit`  | number | 10     | Résultats par page (max 100)       |

**Réponse**
```json
{
  "success": true,
  "data": [...],
  "meta": {
    "total": 6,
    "page": 1,
    "limit": 10,
    "totalPages": 1
  }
}
```

---

### POST /api/users

**Body**
```json
{
  "firstName": "Jean",
  "lastName": "Dupont",
  "email": "jean.dupont@example.com",
  "location": "Paris, FR",
  "role": "USER",
  "status": "ACTIVE",
  "note": "Recruté via LinkedIn"
}
```

---

### PATCH /api/users/:id

Tous les champs sont optionnels (partial update).

```json
{
  "status": "INACTIVE",
  "role": "MODERATOR"
}
```

---

## Format de réponse

```json
{
  "success": true,
  "data": { ... },
  "message": "Utilisateur créé avec succès."
}
```

En cas d'erreur :
```json
{
  "success": false,
  "message": "Un utilisateur avec cet email existe déjà."
}
```

---

## Modèle User

```prisma
model User {
  id        String   @id @default(cuid())
  firstName String
  lastName  String
  email     String   @unique
  location  String?
  role      Role     @default(USER)
  status    Status   @default(ACTIVE)
  note      String?
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}

enum Role   { USER  MODERATOR  ADMIN }
enum Status { ACTIVE  INACTIVE }
```
