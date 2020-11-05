import { DateTime } from "luxon"

type Profile ={
  name: string,
  university: string,
  research: string,
  gender: string,
  age: number,
  position: string,
  selfIntroduction: string,
  birthday: DateTime,
}

export default Profile