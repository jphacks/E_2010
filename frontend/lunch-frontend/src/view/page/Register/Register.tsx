import { Button, makeStyles, MenuItem, TextField } from '@material-ui/core'
import React, { useState } from 'react'
import { DateTime } from 'luxon'
import stamp from '../../../asset/stamp.png'
import { register } from '../../../fetcher/userFetchers'
import { useRecoilState } from 'recoil'
import appUserAtom from '../../../interactor/appUser'

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
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

const Register = () => {
  const c = useStyles()
  const [appUser, setAppUser] = useRecoilState(appUserAtom)
  const [name, setName] = useState("")
  const [university, setUniversity] = useState("")
  const [gender, setGender] = useState("")
  const [age, setAge] = useState(20)
  const [position, setPosition] = useState("")
  
  const [birthday, setBirthday] = useState(DateTime.local(1990, 1, 1).toFormat("yyyy-MM-dd"))
  const [research, setResearch] = useState("")
  const [selfIntroduction, setSelfIntroduction] = useState("")

  const canSubmit = name.length > 0 && university.length > 0 && research.length > 0
    && gender != null && position.length > 0

  const handleSubmit = async () => {
    if (canSubmit && appUser != null) {
      const newAppUser = { ...appUser, profile: { name, university, gender, age, position, birthday: DateTime.fromFormat(birthday, "yyyy-MM-dd"), research, selfIntroduction } }
      const registeredAppUser = await register(newAppUser)
      setAppUser(registeredAppUser)
    }
  }

  return (
    <div className={c.root}>
      <div className={c.form}>
        <img className={c.stamp} src={stamp} width="100" alt="消印" />
        <h2>ユーザー登録</h2>
        <TextField
          className={c.field}
          required
          label="氏名"
          variant="outlined"
          value={name}
          onChange={(e) => setName(e.target.value)}
          fullWidth
        />
        <TextField
          className={c.field}
          required
          label="大学名"
          variant="outlined"
          value={university}
          onChange={(e) => setUniversity(e.target.value)}
          fullWidth
        />

        <TextField
          className={c.field}
          type="number"
          required
          label="年齢"
          variant="outlined"
          value={age}
          onChange={(e) => setAge(parseInt(e.target.value))}
          fullWidth
        />

        <TextField
          className={c.field}
          required
          select
          label="性別"
          variant="outlined"
          value={gender}
          onChange={(e) => setGender(e.target.value)}
          fullWidth
        >
          <MenuItem value="male">
            男性
          </MenuItem>
          <MenuItem value="femail">
            女性
          </MenuItem>
          <MenuItem value="others">
            その他
          </MenuItem>
        </TextField>

        <TextField
          className={c.field}
          required
          label="役職"
          variant="outlined"
          value={position}
          onChange={(e) => setPosition(e.target.value)}
          fullWidth
        />

        <TextField
          className={c.field}
          required
          label="研究内容"
          variant="outlined"
          value={research}
          onChange={(e) => setResearch(e.target.value)}
          fullWidth
          multiline
          rows={4}
        />

        <TextField
          className={c.field}
          label="自己紹介"
          variant="outlined"
          value={selfIntroduction}
          onChange={(e) => setSelfIntroduction(e.target.value)}
          fullWidth
          multiline
          rows={4}
        />

        <TextField
          className={c.field}
          type="date"
          label="生年月日"
          variant="outlined"
          value={birthday}
          onChange={(e) => setBirthday(e.target.value)}
          fullWidth
          InputLabelProps={{
            shrink: true,
          }}
        />
        
      </div>
      <Button disabled={!canSubmit} color="secondary" variant="outlined" onClick={handleSubmit}>登録</Button>
    </div>
  )
}

export default Register
