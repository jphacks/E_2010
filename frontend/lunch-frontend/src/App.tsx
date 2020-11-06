import React from 'react'
import Entry from './view/Entry'
import "./App.css"
import { RecoilRoot } from 'recoil';

const App: React.FC = () => (
  <RecoilRoot>
    <Entry/>
  </RecoilRoot>
)
export default App;