import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthWindow from "./components/AuthWindow"
import ViewTable from './components/ViewTable/ViewTable';
import { Grid, Container, Typography, createMuiTheme, MuiThemeProvider } from '@material-ui/core';
import { blue, red } from '@material-ui/core/colors';
import { Kompot } from './components/ViewTable/Kompot'

import { Map, TileLayer, LayersControl } from 'react-leaflet'
import { houseSettings } from './components/ViewTable/tableSettings';


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
const position = [51.505, -0.09]
const stamenTonerTiles = 'http://stamen-tiles-{s}.a.ssl.fastly.net/toner-background/{z}/{x}/{y}.png';
const stamenTonerAttr = 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>';
const mapCenter = [39.9528, -75.1638];
const zoomLevel = 12;
function App() {
  return (
    <MuiThemeProvider theme={theme}>
      <Container style={{maxWidth:'90%'}}>
      <Kompot settings={houseSettings}/>
      <Map center={position} zoom={13}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution="&copy; <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
        />
       
      </Map>
      </Container>
    </MuiThemeProvider>
  );
}

export default App;
