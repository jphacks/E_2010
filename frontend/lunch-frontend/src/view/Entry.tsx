import React from 'react'
import { BrowserRouter as Router, Redirect, Switch } from 'react-router-dom'
import InvitationCreate from './page/InvitationCreate/InvitationCreate'
import InvitationList from './page/InvitationList/InvitationList'
import Login from './page/Login/Login'
import Register from './page/Register/Register'
import PrivateRoute from './router/PrivateRoute'
import UnAuthRoute from './router/UnAuthRoute'
import UnRegisterRoute from './router/UnRegisterRoute'

const Entry = () => {
  return (
    <Router>
      <Switch>
        <UnAuthRoute exact path="/login" component={Login} />
        <UnRegisterRoute exact path="/register" component={Register} />
        <PrivateRoute exact path="/invitations" component={InvitationList} />
        <PrivateRoute exact path="/invitations/create" component={InvitationCreate} />
        <PrivateRoute exact path="/invitations/:invitationId" component={Login} />
        <PrivateRoute exact path="/invitations/:invitationId/edit" component={Login} />
        <PrivateRoute exact path="/user/:userId" component={Login} />
        <Redirect to="/invitations"/>
      </Switch>
    </Router>
  )
}

export default Entry
