import { makeStyles } from '@material-ui/core'
import React from 'react'
import InvitationFilterType from '../../../types/InvitationFilterType'
import { BiPlus } from 'react-icons/bi'
import { useHistory } from 'react-router-dom'

const useStyle = makeStyles((theme) => ({
  root: {
    position: "fixed",
    left: "50%",
    transform: "translateX(-50%)",
    bottom: "3rem",
    display: "flex",
    flexWrap: "wrap",
    justifyContent: "center",
    width: "100%",
  },
  group: {
    margin: "2rem",
    borderRadius: "3rem",
    boxShadow: "0 0 10px 2px gray",
    background: "#fd905dee",
    display: "flex",
    justifyContent: "space-around",
    alignItems: "center",
    transition: "all .3s",

    "&:hover": {
      transform: "scale(1.1)",
    }
  },
  menuItem: {
    padding: theme.spacing(2),
    margin: theme.spacing(1),
    whiteSpace: "nowrap",
    cursor: "pointer",
    borderRadius: "3rem",
    verticalAlign: "middle",
    display: "flex",

    "&.selected": {
      background: "#ffffffee",
    },

    "&:hover:not(.selected)": {
      background: "#ffffff55",
    }
  },
  icon: {
    fontSize: "1.5em",
  }
}))

type Props = {
  filterType: InvitationFilterType
  handleChangeTab: (status: InvitationFilterType) => void
}

const ToggleBar: React.FC<Props> = ({ filterType, handleChangeTab }) => {
  const c = useStyle()
  const history = useHistory()

  
  return (
    <div className={c.root}>
      <div className={c.group}>
        <div className={c.menuItem + (filterType === "default" ? " selected" : "")} onClick={() => handleChangeTab("default")}>　一覧　</div>
        <div className={c.menuItem + (filterType === "applied" ? " selected" : "")} onClick={() => handleChangeTab("applied")}>応募済み</div>
        <div className={c.menuItem + (filterType === "mine" ? " selected" : "")} onClick={() => handleChangeTab("mine")}>自分の投稿</div>
        <div className={c.menuItem + (filterType === "approved" ? " selected" : "")} onClick={() => handleChangeTab("approved")}>成立済み</div>
      </div>
      <div className={c.group}>
        <div className={c.menuItem} onClick={() => history.push("/invitations/create")}>
          <BiPlus className={c.icon}/>
        </div>
      </div>
    </div>
  )
}

export default ToggleBar
