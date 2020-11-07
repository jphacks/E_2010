import { DateTime } from "luxon"
import InvitationStatus from "./invitationStatus"
import Profile from "./profile"

type Invitation = {
  id: string
  hostProfile: Profile
  content: string
  date: string
  place: string
  tag: string[]
  createdat: DateTime
  status: InvitationStatus | "mine"
}

export default Invitation