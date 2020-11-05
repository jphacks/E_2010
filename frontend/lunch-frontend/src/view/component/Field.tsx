import TextField, { TextFieldProps } from '@material-ui/core/TextField'
import React from 'react'


const Field: React.FC<TextFieldProps> = ({ ...props }) => {
  return (
    <TextField variant="outlined" type="text" {...props}/>
  )
}

export default Field

export const PasswordField: React.FC<Omit<TextFieldProps, "type">> = (props) => <Field {...props}/>
