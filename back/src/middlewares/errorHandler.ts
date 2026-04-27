import { Request, Response, NextFunction } from "express";

export class AppError extends Error {
  statusCode: number;

  constructor(message: string, statusCode: number) {
    super(message);
    this.statusCode = statusCode;
    Error.captureStackTrace(this, this.constructor);
  }
}

export const errorHandler = (
  err: Error,
  _req: Request,
  res: Response,
  _next: NextFunction
): void => {
  if (err instanceof AppError) {
    res.status(err.statusCode).json({
      success: false,
      message: err.message,
    });
    return;
  }

  // Prisma unique constraint violation
  if ((err as any).code === "P2002") {
    res.status(409).json({
      success: false,
      message: "Un utilisateur avec cet email existe déjà.",
    });
    return;
  }

  // Prisma record not found
  if ((err as any).code === "P2025") {
    res.status(404).json({
      success: false,
      message: "Utilisateur introuvable.",
    });
    return;
  }

  console.error("[ERROR]", err);
  res.status(500).json({
    success: false,
    message: "Erreur interne du serveur.",
  });
};
