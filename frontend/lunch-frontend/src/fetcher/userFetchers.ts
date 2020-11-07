import AppUser from "../models/appUser"
import wait from "../utils/wait"
import axios from "axios"
import nullIfEmpty from "../utils/nullIfEmpty"
import { DateTime } from "luxon"

export const login: (email: string, password: string) => Promise<AppUser> = async (email, _) => {
  const res = await axios.get<unknown[]>(`/api/users/?email=${email}`)
  if(res.data.length === 0){
    throw new Error("ユーザーが登録されていません")
  }
  const { id, email: newEmail, self_introduction, ...profile } = res.data[0] as any

  return { id, email: newEmail, profile: { ...profile, selfIntroduction: self_introduction } } as AppUser
}

export const register: (email: string, name: string, university: string, gender: string, age: number, position: string, birthday: DateTime, research: string, selfIntroduction: string) => Promise<AppUser> =
  async(email, name, university, gender, age, position, birthday, research, selfIntroduction) => {
  const res = await axios.post<any>("/api/users/", Object.fromEntries(Object.entries({
    email: nullIfEmpty(email),
    name: nullIfEmpty(name),
    university: nullIfEmpty(university),
    research: nullIfEmpty(research),
    gender: nullIfEmpty(gender) ,
    age,
    position: nullIfEmpty(position) ,
    self_introduction: nullIfEmpty(selfIntroduction),
    birthday: birthday?.toFormat("yyyy-MM-dd")
  }).filter(([_, value]) => value != null)))

  const { id, email: newEmail, self_introduction, ...profile } = res.data

  return { id, email: newEmail, profile: { ...profile, selfIntroduction: self_introduction }} as AppUser
}

export const logout: () => Promise<void> = async () => {
  await wait(500)
}