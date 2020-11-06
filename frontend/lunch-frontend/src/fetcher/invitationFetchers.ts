import { DateTime } from "luxon"
import Invitation from "../models/invitation"
import InvitationStatus from "../models/invitationStatus"
import MyInvitation from "../models/myInvitation"
import wait from "../utils/wait"

const invitationBuilder: (id: string, status: InvitationStatus) => Invitation = (id, status) => ({
  id,
  hostProfile: {
    name: "山田太郎",
    university: "東京大学",
    research: "VRについて研究しています",
    gender: "男",
    age: 22,
    position: "院生",
    selfIntroduction: "好きな食べ物はハンバーグです。",
    birthday: DateTime.local(1998, 2, 27),
  },
  content: status + "一緒に晩ご飯を食べてくれる人を募集しています。ひとりぼっちになりたくないので助けてください。",
  date: "11/7 午後6時ごろ",
  place: "〇〇食堂",
  tag: ["tagA", "tagB"],
  createdat: DateTime.local(),
  status
})

const MY_INVITATION: MyInvitation = {
  id: "mine0",
  applicants: Array(3).fill({
    name: "山田太郎",
    university: "東京大学",
    research: "VRについて研究しています",
    gender: "男",
    age: 22,
    position: "院生",
    selfIntroduction: "好きな食べ物はハンバーグです。",
    birthday: DateTime.local(1998, 2, 27),
  }),
  content: "一緒に晩ご飯を食べてくれる人を募集しています。ひとりぼっちになりたくないので助けてください。",
  date: "11/7 午後6時ごろ",
  place: "〇〇食堂",
  tag: ["tagA", "tagB"],
  createdat: DateTime.local(),
  status: "mine",
}

const SAMPLE_INVITATIONS = (["default", "approved", "denied", "applied"] as InvitationStatus[])
    .map((status) => Array(5).fill(null).map((_, i) => invitationBuilder(`${status}${i}`, status)))
    .flat(2)

export const fetchInvitationList: (userId: string) => () => Promise<Invitation[]> = (userId: string) => async () => {
  await wait(500)
  return SAMPLE_INVITATIONS
}

export const fetchMyInvitationList: (userId: string) => () => Promise<MyInvitation[]> = (userId: string) => async () => {
  await wait(500)
  return [MY_INVITATION]
}

export const createInvitation: () => Promise<void> = async () => {
  await wait(500)
  return
}