import React, { ComponentProps } from 'react'
import { Redirect, Route } from 'react-router-dom'
import { useRecoilValue } from 'recoil'
import appUserAtom from '../../interactor/appUser'

const PrivateRoute: React.FC<ComponentProps<typeof Route>> = ({...props}) => {
  const appUser = useRecoilValue(appUserAtom)
  if(appUser != null){
    return <Route {...props}/>
  }else{
    return <Redirect to="login"/>
  }
}

export default PrivateRoute
