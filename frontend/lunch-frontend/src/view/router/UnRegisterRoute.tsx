import React, { ComponentProps } from 'react'
import { Redirect, Route } from 'react-router-dom'
import { useRecoilValue } from 'recoil'
import appUserAtom from '../../interactor/appUser'

const UnRegisterRoute: React.FC<ComponentProps<typeof Route>> = ({ ...props }) => {
  const appUser = useRecoilValue(appUserAtom)
  console.log(appUser)
  if (appUser == null) {
    return <Redirect to="login" />
  } else if(appUser.profile == null){
    return <Route {...props} />
  } else {
    return <Redirect to="invitations" />
  }
}

export default UnRegisterRoute
