import { atom } from "recoil"
import AppUser from "../models/appUser"

const appUserAtom = atom<AppUser | null>({
  key: "app-user",
  default: null,
})

export default appUserAtom