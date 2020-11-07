import { makeStyles } from '@material-ui/core'
import React from 'react'
import Profile from '../../models/profile'
import icon from "../../asset/icon1.png"

const useStyle = makeStyles((theme) => ({
  cardInner: {
    padding: theme.spacing(2),
    color: "white",
    background: "rgb(108, 161, 211)",
    
  },
  upper: {
    display: "flex",
    marginTop: theme.spacing(2),
    marginBottom: theme.spacing(2),
  },

  img: {
    width: "20%",
    maxWidth: "80px",
    marginRight: theme.spacing(2),
    background: "#e1f1ff",
    borderRadius: "50%",
  }
}))

type Props = {
  profile: Profile
  onClick?: () => void
  className: string
}

const ProfileCard: React.FC<Props> = ({ profile, onClick, className="" }) => {
  const c = useStyle()
  return (
    <article className={c.cardInner + " " + className} onClick={onClick}>
      <div>プロフィール</div>
      <div className={c.upper}>
        <img className={c.img} src="https://github.com/yousukeayada/general/blob/master/jphacks/img/icon1.png" alt="投稿者のアイコン画像" />
        <div>
          <div>{profile.name}</div>
          <div>{profile.university}</div>
          <div>{profile.position}</div>
        </div>
      </div>
      <dl>
        <dt>自己紹介</dt>
        <dd>{profile.selfIntroduction}</dd>
        <dt>研究内容</dt>
        <dd>{profile.research}</dd>
      </dl>
    </article>
  )
}

export default ProfileCard
