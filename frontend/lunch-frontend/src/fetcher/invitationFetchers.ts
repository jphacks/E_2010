import { DateTime } from "luxon"
import Invitation from "../models/invitation"
import InvitationStatus from "../models/invitationStatus"
import MyInvitation from "../models/myInvitation"
import wait from "../utils/wait"
import axios from 'axios'
import Profile from "../models/profile"
import AppUser from "../models/appUser"

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
  const res = await axios.get<any[]>('/api/invitations/')
  
  return res.data?.filter((data) => data.author.id !== userId).map((data) => {
    const { id, title, content, date, place, tags, created_at, status, author: { name, university, research, gender, age, position, self_introduction, birthday } } = data
    const hostProfile = { name, university, research, gender, age: parseInt(age), position, selfIntroduction: self_introduction, birthday: DateTime.fromISO(birthday)} as Profile
    return {
      id, title, content, date, place, tag: tags.split(","), createdat: DateTime.fromISO(created_at),
      status: "default",
      hostProfile
    }
  }) ?? []
}

export const fetchAppliedInvitationList: (userId: string) => () => Promise<Invitation[]> = (userId: string) => async () => {
  const res = await axios.get<any[]>(`/api/invitations/?applicant=${userId}&status=applied`)

  return res.data?.filter((data) => data.author.id !== userId).map((data) => {
    const { id, title, content, date, place, tags, created_at, status, author: { name, university, research, gender, age, position, self_introduction, birthday } } = data
    const hostProfile = { name, university, research, gender, age: parseInt(age), position, selfIntroduction: self_introduction, birthday: DateTime.fromISO(birthday) } as Profile
    return {
      id, title, content, date, place, tag: tags.split(","), createdat: DateTime.fromISO(created_at),
      status: status === "seeking" ? "default" : status === "applied" ? "applied" : "approved",
      hostProfile
    }
  }) ?? []
}

export const fetchMyInvitationList: (userId: string) => () => Promise<Invitation[]> = (userId: string) => async () => {
  const res = await axios.get<any[]>(`/api/invitations/?author=${userId}`)

  console.log(res)

  return res.data?.filter(data => data.status !== "accepted").map((data) => {
    const { id, title, content, date, place, tags, created_at, status, author: { name, university, research, gender, age, position, self_introduction, birthday } } = data
    const hostProfile = { name, university, research, gender, age: parseInt(age), position, selfIntroduction: self_introduction, birthday: DateTime.fromISO(birthday) } as Profile
    return {
      id, title, content, date, place, tag: tags.split(","), createdat: DateTime.fromISO(created_at),
      status: "mine",
      hostProfile
    }
  }) ?? []
}

export const fetchAcceptedInvitationList: (appUser: AppUser) => () => Promise<Invitation[]> = (appUser) => async () => {
  // const res1 = await axios.get<any[]>(`/api/invitations/?author=${appUser.id}&status=accepted`)
  // const res2 = await axios.get<any[]>(`/api/applications/?applicant=${appUser.id}&status=accepted`)

  const [res1, res2]: [any, any] = await Promise.allSettled([
    axios.get<any[]>(`/api/invitations/?author=${appUser.id}&status=accepted`),
    axios.get<any[]>(`/api/applications/?applicant=${appUser.id}&status=accepted`),
  ])

  console.log(res1, res2)

  const myInvs = res1.value.data?.map((data: any) => {
    const { id, title, content, date, place, tags, created_at, status } = data
    const hostProfile = appUser.profile
    return {
      id, title, content, date, place, tag: tags.split(","), createdat: DateTime.fromISO(created_at),
      status: status === "seeking" ? "default" : status === "applied" ? "applied" : "approved",
      hostProfile
    }
  }) ?? []

  const otherInvs = res2.value.data?.filter((data: any) => data.author.id !== appUser.id).map((data: any) => {
    const { id, title, content, date, place, tags, created_at, status, author: { name, university, research, gender, age, position, self_introduction, birthday } } = data
    const hostProfile = { name, university, research, gender, age: parseInt(age), position, selfIntroduction: self_introduction, birthday: DateTime.fromISO(birthday) } as Profile
    return {
      id, title, content, date, place, tag: tags.split(","), createdat: DateTime.fromISO(created_at),
      status: status === "seeking" ? "default" : status === "applied" ? "applied" : "approved",
      hostProfile
    }
  }) ?? []
  return [...myInvs, ...otherInvs]
}

export const createInvitation: (userId: string, title: string, content: string, place: string, date: DateTime, tags: string[]) => Promise<void> =
  async (userId, title, content, place, date, tags) => {
  
    await axios.post("/api/invitations/", {
      user_id: userId,
      title,
      content,
      date: date.toFormat("yyyy-MM-dd"),
      place,
      tags: tags.join(","),
    })
  return
}