import { makeStyles } from '@material-ui/core'
import { DateTime } from 'luxon'
import React, { useState } from 'react'
import { useHistory } from 'react-router-dom'
import Invitation from '../../../models/invitation'
import InvitationStatus from '../../../models/invitationStatus'
import MyInvitation from '../../../models/myInvitation'
import useQuery from '../../hooks/useQuery'
import InvitationFilterType from '../../model/InvitationFilterType'
import InvitationCard from './component/InvitationTicketCard'
import ToggleBar from './component/ToggleBar'

const useStyles = makeStyles((theme) => ({
  emptyMessageArea: {
    height: "100vh",
    display: "flex",
    flexDirection: "column",
    alignItems: "stretch",
    justifyContent: "center",
    
    "& p": {
      textAlign: "center",
      paddingBottom: "3rem",
    }
  }
}))

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

const SAMPLE_INVITATIONS = [
    ...(["default", "approved", "denied", "applied"] as InvitationStatus[])
    .map((status) => Array(5).fill(null).map((_, i) => invitationBuilder(`${status}${i}`, status)))
    .flat(2),
    MY_INVITATION
  ]

const InvitationList = () => {
  const c = useStyles()
  const history = useHistory()
  
  const filterType = (useQuery().get("filter") ?? "default") as InvitationFilterType
  const invitations = SAMPLE_INVITATIONS.filter(({status}) => status === filterType)

  const [beforeClose, setBeforeClose] = useState(false)
  const handleChangeTab = (filterType: InvitationFilterType) => {
    setBeforeClose(true)
    setTimeout(() => {
      history.push(`/invitations?filter=${filterType}`)
      setBeforeClose(false)
    }, 500)
  }

  return (
    <>
      <div>
        {invitations.map((invitation, i) => <InvitationCard order={i} beforeClose={beforeClose} key={invitation.id} invitaion={invitation} />)}
        {
          invitations.length === 0 && <div className={c.emptyMessageArea}><p>該当する投稿はありません</p></div>
        }
      </div>
      <ToggleBar filterType={filterType} handleChangeTab={handleChangeTab}/>
    </>
  )
}

export default InvitationList
