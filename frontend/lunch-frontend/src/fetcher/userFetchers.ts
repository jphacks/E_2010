import AppUser from "../models/appUser";
import wait from "../utils/wait";

export const login: (email: string, password: string) => Promise<AppUser> = async (email, password) => {
  await wait(500)
  return { id: "001",  email, profile: null }
}

export const register: (appUser: AppUser) => Promise<AppUser> = async (appUser: AppUser) => {
  await wait(500)
  return appUser
}

export const logout: () => Promise<void> = async () => {
  await wait(500)
}