import { Role, Status } from "@prisma/client";

export interface CreateUserDto {
  firstName: string;
  lastName: string;
  email: string;
  location?: string;
  role?: Role;
  status?: Status;
  note?: string;
}

export interface UpdateUserDto {
  firstName?: string;
  lastName?: string;
  email?: string;
  location?: string;
  role?: Role;
  status?: Status;
  note?: string;
}

export interface UserFilters {
  search?: string;
  role?: Role;
  status?: Status;
  page?: number;
  limit?: number;
}

export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  message?: string;
  meta?: PaginationMeta;
}

export interface PaginationMeta {
  total: number;
  page: number;
  limit: number;
  totalPages: number;
}
