import "dotenv/config";
import express from "express";
import cors from "cors";
import morgan from "morgan";

import userRoutes from "./routes/user.routes";
import { errorHandler } from "./middlewares/errorHandler";

const app  = express();
const PORT = process.env.PORT ?? 3000;

// ── Middlewares globaux ───────────────────────────────────────────────────────
app.use(cors({ origin: process.env.CORS_ORIGIN ?? "*" }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(morgan("dev"));

// ── Routes ────────────────────────────────────────────────────────────────────
app.get("/health", (_req, res) => {
  res.json({ status: "ok", timestamp: new Date().toISOString() });
});

app.use("/api/users", userRoutes);

// ── 404 ───────────────────────────────────────────────────────────────────────
app.use((_req, res) => {
  res.status(404).json({ success: false, message: "Route introuvable." });
});

// ── Error handler (doit être en dernier) ─────────────────────────────────────
app.use(errorHandler);

// ── Start ─────────────────────────────────────────────────────────────────────
app.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`);
});

export default app;
