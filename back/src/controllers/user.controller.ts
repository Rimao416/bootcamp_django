import { Request, Response, NextFunction } from "express";
import { Role, Status } from "@prisma/client";
import { prisma } from "../lib/prisma";
import { AppError } from "../middlewares/errorHandler";
import { CreateUserDto, UpdateUserDto, UserFilters } from "../lib/types";

// ── GET /users ────────────────────────────────────────────────────────────────
export const getUsers = async (
  req: Request,
  res: Response,
  next: NextFunction
): Promise<void> => {
  try {
    const {
      search,
      role,
      status,
      page = "1",
      limit = "10",
    } = req.query as Record<string, string>;

    const pageNum  = parseInt(page, 10);
    const limitNum = parseInt(limit, 10);
    const skip     = (pageNum - 1) * limitNum;

    const where: any = {};

    if (search) {
      where.OR = [
        { firstName: { contains: search, mode: "insensitive" } },
        { lastName:  { contains: search, mode: "insensitive" } },
        { email:     { contains: search, mode: "insensitive" } },
      ];
    }

    if (role)   where.role   = role   as Role;
    if (status) where.status = status as Status;

    const [users, total] = await Promise.all([
      prisma.user.findMany({
        where,
        skip,
        take: limitNum,
        orderBy: { createdAt: "desc" },
      }),
      prisma.user.count({ where }),
    ]);

    res.json({
      success: true,
      data: users,
      meta: {
        total,
        page: pageNum,
        limit: limitNum,
        totalPages: Math.ceil(total / limitNum),
      },
    });
  } catch (error) {
    next(error);
  }
};

// ── GET /users/:id ────────────────────────────────────────────────────────────
export const getUserById = async (
  req: Request,
  res: Response,
  next: NextFunction
): Promise<void> => {
  try {
    const { id } = req.params;

    const user = await prisma.user.findUnique({ where: { id } });

    if (!user) {
      throw new AppError("Utilisateur introuvable.", 404);
    }

    res.json({ success: true, data: user });
  } catch (error) {
    next(error);
  }
};

// ── POST /users ───────────────────────────────────────────────────────────────
export const createUser = async (
  req: Request,
  res: Response,
  next: NextFunction
): Promise<void> => {
  try {
    const body: CreateUserDto = req.body;

    const user = await prisma.user.create({
      data: {
        firstName: body.firstName,
        lastName:  body.lastName,
        email:     body.email,
        location:  body.location,
        role:      body.role   ?? "USER",
        status:    body.status ?? "ACTIVE",
        note:      body.note,
      },
    });

    res.status(201).json({
      success: true,
      data: user,
      message: "Utilisateur créé avec succès.",
    });
  } catch (error) {
    next(error);
  }
};

// ── PATCH /users/:id ──────────────────────────────────────────────────────────
export const updateUser = async (
  req: Request,
  res: Response,
  next: NextFunction
): Promise<void> => {
  try {
    const { id } = req.params;
    const body: UpdateUserDto = req.body;

    const existing = await prisma.user.findUnique({ where: { id } });
    if (!existing) throw new AppError("Utilisateur introuvable.", 404);

    const user = await prisma.user.update({
      where: { id },
      data: {
        ...(body.firstName !== undefined && { firstName: body.firstName }),
        ...(body.lastName  !== undefined && { lastName:  body.lastName  }),
        ...(body.email     !== undefined && { email:     body.email     }),
        ...(body.location  !== undefined && { location:  body.location  }),
        ...(body.role      !== undefined && { role:      body.role      }),
        ...(body.status    !== undefined && { status:    body.status    }),
        ...(body.note      !== undefined && { note:      body.note      }),
      },
    });

    res.json({
      success: true,
      data: user,
      message: "Utilisateur mis à jour.",
    });
  } catch (error) {
    next(error);
  }
};

// ── DELETE /users/:id ─────────────────────────────────────────────────────────
export const deleteUser = async (
  req: Request,
  res: Response,
  next: NextFunction
): Promise<void> => {
  try {
    const { id } = req.params;

    const existing = await prisma.user.findUnique({ where: { id } });
    if (!existing) throw new AppError("Utilisateur introuvable.", 404);

    await prisma.user.delete({ where: { id } });

    res.json({
      success: true,
      message: "Utilisateur supprimé.",
    });
  } catch (error) {
    next(error);
  }
};
