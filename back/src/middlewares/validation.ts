import { body, param, query, validationResult } from "express-validator";
import { Request, Response, NextFunction } from "express";

// ── Vérifie le résultat des validations ──────────────────────────────────────
export const validate = (req: Request, res: Response, next: NextFunction): void => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    res.status(422).json({
      success: false,
      message: "Données invalides.",
      errors: errors.array().map((e) => ({ field: e.type, message: e.msg })),
    });
    return;
  }
  next();
};

// ── Règles : créer un utilisateur ────────────────────────────────────────────
export const createUserRules = [
  body("firstName")
    .trim()
    .notEmpty().withMessage("Le prénom est requis.")
    .isLength({ min: 2, max: 50 }).withMessage("Le prénom doit contenir entre 2 et 50 caractères."),

  body("lastName")
    .trim()
    .notEmpty().withMessage("Le nom est requis.")
    .isLength({ min: 2, max: 50 }).withMessage("Le nom doit contenir entre 2 et 50 caractères."),

  body("email")
    .trim()
    .notEmpty().withMessage("L'email est requis.")
    .isEmail().withMessage("L'email est invalide.")
    .normalizeEmail(),

  body("location")
    .optional()
    .trim()
    .isLength({ max: 100 }).withMessage("La localisation ne peut pas dépasser 100 caractères."),

  body("role")
    .optional()
    .isIn(["USER", "MODERATOR", "ADMIN"]).withMessage("Rôle invalide. Valeurs acceptées : USER, MODERATOR, ADMIN."),

  body("status")
    .optional()
    .isIn(["ACTIVE", "INACTIVE"]).withMessage("Statut invalide. Valeurs acceptées : ACTIVE, INACTIVE."),

  body("note")
    .optional()
    .trim()
    .isLength({ max: 500 }).withMessage("La note ne peut pas dépasser 500 caractères."),
];

// ── Règles : modifier un utilisateur ─────────────────────────────────────────
export const updateUserRules = [
  param("id")
    .notEmpty().withMessage("L'identifiant est requis."),

  body("firstName")
    .optional()
    .trim()
    .isLength({ min: 2, max: 50 }).withMessage("Le prénom doit contenir entre 2 et 50 caractères."),

  body("lastName")
    .optional()
    .trim()
    .isLength({ min: 2, max: 50 }).withMessage("Le nom doit contenir entre 2 et 50 caractères."),

  body("email")
    .optional()
    .trim()
    .isEmail().withMessage("L'email est invalide.")
    .normalizeEmail(),

  body("location")
    .optional()
    .trim()
    .isLength({ max: 100 }).withMessage("La localisation ne peut pas dépasser 100 caractères."),

  body("role")
    .optional()
    .isIn(["USER", "MODERATOR", "ADMIN"]).withMessage("Rôle invalide."),

  body("status")
    .optional()
    .isIn(["ACTIVE", "INACTIVE"]).withMessage("Statut invalide."),

  body("note")
    .optional()
    .trim()
    .isLength({ max: 500 }).withMessage("La note ne peut pas dépasser 500 caractères."),
];

// ── Règles : query params de liste ───────────────────────────────────────────
export const listUsersRules = [
  query("page")
    .optional()
    .isInt({ min: 1 }).withMessage("La page doit être un entier positif."),

  query("limit")
    .optional()
    .isInt({ min: 1, max: 100 }).withMessage("La limite doit être comprise entre 1 et 100."),

  query("role")
    .optional()
    .isIn(["USER", "MODERATOR", "ADMIN"]).withMessage("Rôle invalide."),

  query("status")
    .optional()
    .isIn(["ACTIVE", "INACTIVE"]).withMessage("Statut invalide."),
];
