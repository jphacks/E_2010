import { makeStyles } from '@material-ui/core'
import React from 'react'
import Invitation from '../../models/invitation'
import MyInvitation from '../../models/myInvitation'

const useStyle = makeStyles((theme) => ({
  cardInner: {
    padding: theme.spacing(2),
    // background: "linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)",
    color: "white",

    "&.default": {
      background: "rgb(79, 184, 174);",
    },
    "&.applied": {
      background: "rgb(174, 184, 79);",
    },
    "&.approved": {
      background: "rgb(79, 125, 184);",
    },
    "&.mine": {
      background: "rgb(199, 101, 158);",
    },
  },
  tagArea: {
    display: "flex",
  },
  tag: {
    margin: theme.spacing(1),
    padding: theme.spacing(1),
    background: "#fd905d",
    color: "white",

  },
  content: {
    margin: `${theme.spacing(2)} 0`,
  },
  footer: {
    display: "flex",
    justifyContent: "space-between",
    flexWrap: "wrap",
    width: "100%"
  },
}))

type Props = {
  invitation: Invitation | MyInvitation
  className?: string
  onClick?: () => void
}

const InvitationCard: React.FC<Props> = ({ invitation, className, onClick }) => {
  const c = useStyle()
  
  return (
    <div className={c.cardInner + " " + invitation.status + " " + className} onClick={onClick}>
      <div className={c.tagArea}>
        {invitation.tag.map(tag => (
          <div className={c.tag} key={tag}>{tag}</div>
        ))}
      </div>
      <p className={c.content}>{invitation.content}</p>
      <div className={c.footer}>
        <div>
          {invitation.place}
        </div>
        <div>
          {invitation.date}
        </div>
      </div>
    </div>
  )
}

export default InvitationCard
