import Profile from "./profile"

type AppUser = {
  id: string
  email: string
  profile: Profile | null
}

export default AppUser