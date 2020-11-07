import { Button, Dialog, DialogActions, DialogContent, DialogTitle, makeStyles } from '@material-ui/core'
import React, { Fragment, Suspense, useState } from 'react'
import Invitation from '../../../../models/invitation'
import MyInvitation from '../../../../models/myInvitation'
import forkImage from "../../../../asset/corn.png"
import InvitationCard from '../../../component/InvitationCard'
import ProfileCard from '../../../component/ProfileCard'
import appUserAtom from '../../../../interactor/appUser'
import { useRecoilValue } from 'recoil'
import axios from "axios"
import useSWR from 'swr'
import { DateTime } from 'luxon'

const useStyles = makeStyles((theme) => ({
  root: {
    border: `1px solid #dddddd`,
    background: "white",
    display: "flex",
    flexDirection: "column",
    padding: theme.spacing(2),
    margin: theme.spacing(2),
    marginLeft: theme.spacing(4),
    marginRight: theme.spacing(4),
    position: "relative",
    cursor: "pointer",
    transition: "all .3s",

    "&:after":{
      content: "''",
      display: "block",
      position: "absolute",
      border: "50px solid transparent",
      borderBottom: "50px solid  #f7f7f7",
      bottom: "-60px",
      right: "-65px",
      boxShadow: "0px 7px 6px -9px black",
      transform: "rotate(135deg)",
      transition: "all .3s",
    },

    "&:before": {
      content: "''",
      display: "block",
      position: "absolute",
      border: "50px solid transparent",
      borderTop: "50px solid  #f7f7f7",
      top: "-60px",
      left: "-65px",
      boxShadow: "0px -7px 6px -9px black",
      transform: "rotate(135deg)",
      transition: "all .3s ease-out",
    },

    "&:hover:not(.selected)": {
      transform: "scale(1.02)",
      boxShadow: "0 0 10px 2px #cfcfcf",

      "&:after": {
        opacity: 0,
        bottom: "-120px",
        right: "-125px",
      },
      "&:before": {
        opacity: 0,
        top: "-120px",
        left: "-125px",
      },
      "& img": {
        top: "-30px",
        right: "0",
        opacity: 1,
        transition: "all .3s .2s",
      },
    },

    "&.selected": {
      background: "inherit",
      border: "none",
      "&:after": {
        opacity: 0,
        bottom: "-120px",
        right: "-125px",
      },
      "&:before": {
        opacity: 0,
        top: "-120px",
        left: "-125px",
      },
    },
    "&:active:not(.selected)": {
      transform: "scale(.98)",
    },
  },

  "@keyframes slidein": {
    from: {
      transform: "translateY(50vh)",
      opacity: 0,
    },

    to: {
      transform: "translateY(0)",
      opacity: 1,
    }
  },

  "@keyframes slideinReverse": {
    from: {
      transform: "translateY(0)",
      opacity: 1,
    },
    
    to: {
      opacity: 0,
      transform: "translateY(50vh)",
    }
  },
  
  iconImg: {
    position: "absolute",
    top: "-50px",
    right: "-40px",
    opacity: 0,
    filter: "drop-shadow(0 3px 5px green)",
    transition: "all .3s",
    zIndex: 10,
    pointerEvent: "none",
  },

  cardInnerAnimcation: {
    animation: "$slidein .5s",
    "&.beforeClose": {
      animation: "$slideinReverse .5s",
    },
  },

  buttonArea: {
    display: "flex",
    flexDirection: "column",
    margin: theme.spacing(2),
    alignItems: "center",
  },

  profileCard: {
    marginTop: "1rem",
    position: "relative",
    
    "&::before": {
      content: "''",
      position: "absolute",
      top: "-30px",
      left: "50%",
      marginLeft: "-15px",
      border: "15px solid transparent",
      borderBottom: "15px solid rgb(108, 161, 211)",
    }
  },

  profileListItem: {
    marginBottom: 0,
  },
  
  dialogContent: {
    display: "flex",
    flexDirection: "column",
    minWidth: "600px",
  },

  invitationCard: {
    flex: 1,
  },

  applicantsArea: {
    overflowY: "scroll",
  },

  approveButtonWrapper: {
    background: "rgb(108, 161, 211)",
    textAlign: "right",
    padding: theme.spacing(1),
  },

  approveButton: {
    background: "white",
  }
}))

type Props = {
  invitaion: Invitation | MyInvitation
  order: number
  beforeClose: boolean
}

const InvitationTicketCard: React.FC<Props> = ({ order, beforeClose, invitaion: invitation}) => {
  const c = useStyles()
  const appUser = useRecoilValue(appUserAtom)
  const [open, setOpen] = useState(false)

  const handleAction = async () => {
    if(appUser == null) return
    if(invitation.status === "default"){
      await axios.post(`/api/invitations/${invitation.id}/apply/`, {
        user_id: appUser.id
      })
    }else if(invitation.status === "applied"){
      const res = await axios.get(`/api/applications/?invitation=${invitation.id}&applicant=${appUser.id}`)
      const applicationId = res.data[0].id
      await axios.put(`/api/applications/${applicationId}/cancel/`)
    }
    setOpen(false)
  }

  return (
    <>
      <article className={c.root + " " + invitation.status} >
        <img className={c.iconImg} src={forkImage} width="100" alt="とうもろこしのイラスト" />
        <InvitationCard invitation={invitation} className={c.cardInnerAnimcation + (beforeClose ? " beforeClose" : "")} onClick={() => setOpen(!open)}/>
      </article>
      <Dialog
        open={open}
        onClose={() => setOpen(false)}
      >
        <DialogTitle id="alert-dialog-title">{
          invitation.status === "default" ? "応募しますか？" :
          invitation.status === "applied" ? "応募中です" :
          invitation.status === "mine" ? "応募者一覧" : "マッチングが成立しています"
        }</DialogTitle>
        <DialogContent className={c.dialogContent}>
          <InvitationCard invitation={invitation} className={c.invitationCard}/>
          {
            invitation.status === "mine" ? (
              <div className={c.applicantsArea}>{
                <Suspense fallback={"LOADING..."}>
                  <ApplicantList invitation={invitation as Invitation}/>
                </Suspense>
                // invitation.applicants.map((profile, i) => (
                //   <Fragment key={i}>
                //     <ProfileCard profile={profile} className={c.profileCard + " " + c.profileListItem} />
                //     <div className={c.approveButtonWrapper}>
                //       <Button color="default" variant="contained" className={c.approveButton}>承認する</Button>
                //     </div>
                //   </Fragment>
                // ))
              }</div>
            ) : (
              <ProfileCard profile={invitation.hostProfile} className={c.profileCard}/>
            )
          }
        </DialogContent>
          <DialogActions>
            <Button onClick={() => setOpen(false)} color="primary">
              戻る
            </Button>
            {
              (invitation.status === "default" || invitation.status === "applied") &&
              <Button onClick={handleAction} color="primary">{
                invitation.status === "default" ? "応募する" :
                invitation.status === "applied" ? "応募キャンセル" : ""
              }</Button>
            }
        </DialogActions>
      </Dialog>
    </>
  )
}

type AppProps = {
  invitation: Invitation
}

const ApplicantList: React.FC<AppProps> = ({invitation}) => {
  const c = useStyles()
  const { data } = useSWR("/invitation" + invitation.id, async () => {
    const res = await axios.get<any[]>(`/api/applications/?invitation=${invitation.id}`)
    console.log(res)
    const applicants = res.data.map(data => data.applicant)
    console.log(applicants)
    const applicantsProfile = await Promise.allSettled(
      applicants.map((userId) => axios.get(`/api/users/?id=${userId}`))
    )
    console.log(applicantsProfile)
    return applicantsProfile
  }, { suspense: true })

  const handleApprove = (id: number) => async () => {
    const res = await axios.get<any[]>(`/api/applications/?invitation=${invitation.id}`)
    console.log(id)
    const appId = res.data.find(data => data.applicant === id).id
    const applicantId = res.data.find(data => data.applicant === id).applicant
    await axios.put(`/api/applications/${appId}/accept/`, {
      applicant_id: applicantId
    })
  }

  if(data == null) return <div>LOADING...</div>
  console.log(data)
  console.log((data as any[]).map((data: any) => data.value.data))


  return (
    <>{
      (data as any[]).map((data: any) => data.value.data).flat().map(({ id, name, university, research, gender, age, position, self_introduction, birthday}: any, i: any) => {
      const profile = {
        name,
        university,
        research,
        gender,
        age: Number.isInteger(age) ? parseInt(age) : 20,
        position,
        selfIntroduction: self_introduction,
        birthday: DateTime.local(),
      }
      return (
        <Fragment key={i}>
          <ProfileCard profile={profile} className={c.profileCard + " " + c.profileListItem} />
          <div className={c.approveButtonWrapper}>
            <Button color="default" variant="contained" className={c.approveButton} onClick={handleApprove(id)}>承認する</Button>
          </div>
        </Fragment>
      )
    })
  }</>
  )
}

export default InvitationTicketCard
