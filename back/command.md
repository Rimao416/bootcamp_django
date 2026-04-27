1. Initialisation du projet
bash
# Créer le dossier et entrer dedans
mkdir back
cd back
# Initialiser npm
npm init -y
2. Installation des dépendances de production
bash
# Serveur et outils de base
npm install express cors dotenv morgan express-validator
# Client de base de données
npm install @prisma/client
3. Installation des dépendances de développement
bash
# TypeScript et types
npm install -D typescript ts-node ts-node-dev @types/express @types/cors @types/node @types/morgan
# Prisma (l'outil CLI)
npm install -D prisma
4. Configuration de TypeScript
bash
# Créer le fichier tsconfig.json
npx tsc --init
5. Initialisation de Prisma (Base de données)
bash
# Initialiser prisma (crée le dossier prisma/ et le fichier .env)
npx prisma init
6. Commandes pour gérer la base de données (après avoir défini le schéma)
Une fois que tu as écrit ton modèle dans prisma/schema.prisma :

bash
# Générer le client Prisma (à faire à chaque changement de modèle)
npx prisma generate
# Créer la base de données et appliquer les changements (migration)
npx prisma migrate dev --name init
# Optionnel : Envoyer des données de test
npm run db:seed
7. Scripts utiles (à ajouter dans le package.json)
Pour que le projet tourne, les scripts suivants ont été configurés dans le fichier package.json :

json
"scripts": {
  "dev": "ts-node-dev --respawn --transpile-only src/index.ts",
  "build": "tsc",
  "start": "node dist/index.js",
  "db:migrate": "prisma migrate dev",
  "db:generate": "prisma generate"
}
En résumé, une fois tout configuré, la commande que tu utiliseras le plus au quotidien est :

bash
npm run dev
8:46 PM
