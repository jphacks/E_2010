import React from 'react'
import { BrowserRouter as Router, Route, Redirect, Switch } from 'react-router-dom'
import InvitationList from './page/InvitationList/InvitationList'
import Login from './page/Login/Login'

const Entry = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/login" component={Login} />
        <Route exact path="/register" component={Login} />
        <Route exact path="/invitations" component={InvitationList} />
        <Route exact path="/invitations/create" component={Login} />
        <Route exact path="/invitations/:invitationId" component={Login} />
        <Route exact path="/invitations/:invitationId/edit" component={Login} />
        <Route exact path="/user/:userId" component={Login} />
        <Redirect to="/invitations"/>
      </Switch>
    </Router>
  )
}

export default Entry
