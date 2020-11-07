import { Button, makeStyles, TextField } from '@material-ui/core'
import React, { useState } from 'react'
import { useHistory } from 'react-router-dom'
import { DateTime } from 'luxon'
import stamp from '../../../asset/stamp.png'
import { MdClose } from 'react-icons/md'
import { createInvitation } from '../../../fetcher/invitationFetchers'
import { useRecoilValue } from 'recoil'
import appUserAtom from '../../../interactor/appUser'

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    height: "100vh",
  },

  closeButton: {
    position: "absolute",
    top: "1rem",
    right: "1rem",
    fontSize: "2.5em",
    borderRadius: "50%",
    width: "2em",
    height: "2em",
    lineHeight: "2em",
    textAlign: "center",
    verticalAlign: "middle",
    cursor: "pointer",

    "&:hover": {
      background: "#0000000f",
    }
  },

  stamp: {
    position: "absolute",
    top: "calc(1rem)",
    left: "calc(1rem + 10px)",
  },

  form: {
    padding: "2rem",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    maxWidth: "80%",
    width: "500px",
    background: "rgb(245 243 233)",
    position: "relative",
    margin: "2rem",

    "&::after": {
      position: "absolute",
      top: "-1rem",
      bottom: "-1rem",
      left: "-1rem",
      right: "-1rem",
      background: "repeating-linear-gradient(45deg, rgb(217, 25, 36), rgb(217, 25, 36) 1rem, transparent 1rem, transparent 2rem, rgb(28, 74, 156) 2rem, rgb(28, 74, 156) 3rem, transparent 3rem, transparent 4rem)",
      backgroundColor: "rgb(245 243 233)",
      content: "''",
      zIndex: "-1",
}
  },

  field: {
    margin: theme.spacing(2),
  },

  tagFieldWrapper: {
    display: "flex",
    justifyContent: "space-between",

    "&>div:first-child": {
      marginLeft: 0,
    },

    "&>div:last-child": {
      marginRight: 0,
    }
  },
}))

const InvitationCreate = () => {
  const c = useStyles()
  const appUser = useRecoilValue(appUserAtom)
  const [title, setTitle] = useState("")
  const [content, setContent] = useState("")
  const [place, setPlace] = useState("")
  const [date, setDate] = useState(DateTime.local().toFormat("yyyy-MM-dd"))
  const [tags, setTags] = useState<string[]>([])

  const history = useHistory()

  const handleSubmit = async () => {
    if(canSubmit && appUser != null){
      await createInvitation(appUser.id, title, content, place, DateTime.fromFormat(date, "yyyy-MM-dd"), tags)
      history.goBack()
    }
  }

  const canSubmit = title.length > 0 && date.length > 0 && place.length > 0

  const handleCancel = () => history.goBack()

  return (
    <>
      <div className={c.closeButton} onClick={handleCancel}><MdClose/></div>
      <div className={c.root}>
        <div className={c.form}>
          <img className={c.stamp} src={stamp} width="100" alt="消印"/>
          <h2>食事のお供を募集する</h2>
          <TextField
            className={c.field}
            required
            label="タイトル"
            variant="outlined"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            fullWidth
          />
          <TextField
            className={c.field}
            label="内容"
            variant="outlined"
            value={content}
            onChange={(e) => setContent(e.target.value)}
            fullWidth
            multiline
            rows={4}
          />
          <TextField
            className={c.field}
            required
            label="場所"
            variant="outlined"
            value={place}
            onChange={(e) => setPlace(e.target.value)}
            fullWidth
          />
          <TextField
            className={c.field}
            required
            type="date"
            label="日付"
            variant="outlined"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            fullWidth
            InputLabelProps={{
              shrink: true,
            }}
          />
          <div className={c.tagFieldWrapper}>
            <TextField
              className={c.field}
              label="タグ1"
              variant="outlined"
              value={tags[0]}
              onChange={(e) => setTags([e.target.value, tags[1], tags[2]])}
            />
            <TextField
              className={c.field}
              label="タグ2"
              variant="outlined"
              value={tags[1]}
              onChange={(e) => setTags([tags[0], e.target.value, tags[2]])}
            />
            <TextField
              className={c.field}
              label="タグ3"
              variant="outlined"
              value={tags[2]}
              onChange={(e) => setTags([tags[0], tags[1], e.target.value])}
            />
          </div>
        </div>
          <Button disabled={!canSubmit} color="secondary" variant="outlined" onClick={handleSubmit}>登録</Button>
      </div>
    </>
  )
}

export default InvitationCreate
