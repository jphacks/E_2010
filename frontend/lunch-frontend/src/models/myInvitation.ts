import { DateTime } from "luxon"
import Profile from "./profile"

type MyInvitation = {
  id: string
  content: string
  date: string
  place: string
  tag: string[]
  createdat: DateTime
  applicants: Profile[]
  status: "mine"
}

export default MyInvitation