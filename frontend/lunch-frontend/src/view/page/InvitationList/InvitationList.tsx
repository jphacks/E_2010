import { makeStyles } from '@material-ui/core'
import React, { Suspense, useState } from 'react'
import { useHistory } from 'react-router-dom'
import useSWR from 'swr'
import Invitation from '../../../models/invitation'
import MyInvitation from '../../../models/myInvitation'
import useQuery from '../../hooks/useQuery'
import InvitationFilterType from '../../types/InvitationFilterType'
import InvitationCard from './component/InvitationTicketCard'
import ToggleBar from './component/ToggleBar'
import { useRecoilValue } from 'recoil'
import appUserAtom from '../../../interactor/appUser'
import { fetchAcceptedInvitationList, fetchAppliedInvitationList, fetchInvitationList, fetchMyInvitationList } from '../../../fetcher/invitationFetchers'

const useStyles = makeStyles((theme) => ({
  root: {
    paddingTop: theme.spacing(2),
  },
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

const InvitationList = () => {
  const c = useStyles()
  const history = useHistory()
  
  const filterType = (useQuery().get("filter") ?? "default") as InvitationFilterType
  
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
      <Suspense fallback={<div>Loading...</div>}>
        <div className={c.root}>
          <InvitationListInner filterType={filterType} beforeClose={beforeClose}/>
        </div>
      </Suspense>
      <ToggleBar filterType={filterType} handleChangeTab={handleChangeTab}/>
    </>
  )
}

type InnerProps = {
  filterType: InvitationFilterType
  beforeClose: boolean
}

const InvitationListInner: React.FC<InnerProps> = ({ filterType, beforeClose }) => {
  const c = useStyles()
  const appUser = useRecoilValue(appUserAtom)
  if(appUser == null) throw new Error()
  
  const { data: invitations } = useSWR<(Invitation | MyInvitation)[]>("/invitations/list", fetchInvitationList(appUser.id), { suspense: true })
  const { data: appliedInvitations } = useSWR<Invitation[]>("/invitation/applied", fetchAppliedInvitationList(appUser.id), { suspense: true })
  const { data: myInvitations } = useSWR<(Invitation | MyInvitation)[]>("/invitations/self", fetchMyInvitationList(appUser.id), { suspense: true })
  const { data: acceptedInvitations } = useSWR<(Invitation | MyInvitation)[]>("/invitations/accepted", fetchAcceptedInvitationList(appUser), { suspense: true })
  console.log(acceptedInvitations)
  const filteredInvitations =
    filterType === "mine" ? myInvitations ?? [] : filterType === "applied" ? appliedInvitations ?? [] : filterType === "approved" ? acceptedInvitations ?? [] : invitations?.filter(({ status }) => status === filterType) ?? []

  return (
    <>
      {filteredInvitations.map((invitation, i) => <InvitationCard order={i} beforeClose={beforeClose} key={invitation.id} invitaion={invitation} />)}
      {
        filteredInvitations.length === 0 && <div className={c.emptyMessageArea}><p>該当する投稿はありません</p></div>
      }
    </>
  )
}

export default InvitationList
