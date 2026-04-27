import { PrismaClient, Role, Status } from "@prisma/client";

const prisma = new PrismaClient();

async function main() {
  console.log("🌱 Seeding database...");

  await prisma.user.deleteMany();

  const users = await prisma.user.createMany({
    data: [
      {
        firstName: "Amara",
        lastName: "Diallo",
        email: "amara.diallo@mail.com",
        location: "Abidjan, CI",
        role: Role.ADMIN,
        status: Status.ACTIVE,
      },
      {
        firstName: "Sophie",
        lastName: "Martin",
        email: "s.martin@mail.com",
        location: "Paris, FR",
        role: Role.USER,
        status: Status.ACTIVE,
      },
      {
        firstName: "Elias",
        lastName: "Kofi",
        email: "e.kofi@mail.com",
        location: "Accra, GH",
        role: Role.MODERATOR,
        status: Status.ACTIVE,
      },
      {
        firstName: "Lena",
        lastName: "Müller",
        email: "lena.m@mail.com",
        location: "Berlin, DE",
        role: Role.USER,
        status: Status.INACTIVE,
      },
      {
        firstName: "Carlos",
        lastName: "Reyes",
        email: "c.reyes@mail.com",
        location: "Bogotá, CO",
        role: Role.ADMIN,
        status: Status.ACTIVE,
      },
      {
        firstName: "Nadia",
        lastName: "Okonkwo",
        email: "n.okonkwo@mail.com",
        location: "Lagos, NG",
        role: Role.USER,
        status: Status.INACTIVE,
      },
    ],
  });

  console.log(`✅ ${users.count} users created`);
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(() => prisma.$disconnect());
