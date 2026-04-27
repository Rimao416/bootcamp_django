import { Router } from "express";
import {
  getUsers,
  getUserById,
  createUser,
  updateUser,
  deleteUser,
} from "../controllers/user.controller";
import {
  validate,
  createUserRules,
  updateUserRules,
  listUsersRules,
} from "../middlewares/validation";

const router = Router();

// GET    /api/users          — liste paginée + filtres
// GET    /api/users/:id      — détail
// POST   /api/users          — créer
// PATCH  /api/users/:id      — modifier (partial)
// DELETE /api/users/:id      — supprimer

router.get(   "/",    listUsersRules,  validate, getUsers);
router.get(   "/:id",                            getUserById);
router.post(  "/",    createUserRules, validate, createUser);
router.patch( "/:id", updateUserRules, validate, updateUser);
router.delete("/:id",                            deleteUser);

export default router;
