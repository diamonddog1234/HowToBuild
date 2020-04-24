import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthWindow from "./components/AuthWindow"
import ViewTable from './components/ViewTable/ViewTable';
import { Grid, Container, Typography, createMuiTheme, MuiThemeProvider } from '@material-ui/core';
import { blue, red } from '@material-ui/core/colors';

const theme = createMuiTheme({
  typography: {
    fontFamily: [
      '-apple-system',
      'BlinkMacSystemFont',
      '"Segoe UI"',
      '"Helvetica Neue"',
      '"Roboto',
      'Arial',
      'sans-serif',
      '"Apple Color Emoji"',
      '"Segoe UI Emoji"',
      '"Segoe UI Symbol"',
    ].join(','),
  },
  
  palette: {
    primary: red,
    secondary: {
      main: red[500],
    },
  },
});

function App() {
  return (
    <MuiThemeProvider theme={theme}>
      <Container style={{maxWidth:'90%'}}>
        <Typography>Даунская таблица</Typography>
        <ViewTable/>
      </Container>
    </MuiThemeProvider>
  );
}

export default App;
