import React, { ComponentProps } from 'react'
import { Redirect, Route } from 'react-router-dom'
import { useRecoilValue } from 'recoil'
import appUserAtom from '../../interactor/appUser'

const UnAuthRoute: React.FC<ComponentProps<typeof Route>> = ({ ...props }) => {
  const appUser = useRecoilValue(appUserAtom)
  console.log(appUser)
  if (appUser == null) {
    return <Route {...props} />
  } else if(appUser.profile == null){
    return <Redirect to="register" />
  } else {
    return <Redirect to="invitations" />
  }
}

export default UnAuthRoute
