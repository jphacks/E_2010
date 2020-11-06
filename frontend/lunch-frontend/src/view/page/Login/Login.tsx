import React, { useState } from 'react'
import { makeStyles } from '@material-ui/core/styles'
import Field, { PasswordField } from '../../component/Field'
import Button from '@material-ui/core/Button'
import { useSetRecoilState } from 'recoil'
import appUserAtom from '../../../interactor/appUser'
import { login } from '../../../fetcher/userFetchers'

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    height: "100vh",
  },
  fieldBox: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    width: "300px",
    maxWidth: "80%",
    paddingBottom: "5vh",
  },
  field: {
    margin: theme.spacing(2),
  },
  button: {
    marginTop: theme.spacing(2),
    height: "3rem",
  }
}))

const Login = () => {
  const c = useStyles()

  const setAppUser = useSetRecoilState(appUserAtom)
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const handleLogin = async () => {
    const appUser = await login(email, password)
    setAppUser(appUser)
  }

  return (
    <div className={c.root}>
      <div className={c.fieldBox}>
        <div>Welcome to Lunch Link Learning</div>
        <Field className={c.field} label="メールアドレス" value={email} onChange={e => setEmail(e.target.value)} fullWidth={true}/>
        <PasswordField className={c.field} label="パスワード" value={password} onChange={e => setPassword(e.target.value)} fullWidth={true}/>
        <Button className={c.button} variant="outlined" color="primary" fullWidth={true} onClick={handleLogin}>ログイン</Button>
      </div>
    </div>
  )
}

export default Login
