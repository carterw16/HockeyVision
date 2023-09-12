import './App.css';
import { Gallery } from './Components/Gallery/Gallery';
import { Game } from './Components/Game/Game';
import { MainLayout } from './Layout/MainLayout';
import { Navigate, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <MainLayout>
        <Routes>
          <Route exact path="/" element={ <Navigate to="/gallery" /> }/>
          <Route path="/game/:id" element={ <Game/> }/>
          <Route exact path="/gallery" element={ <Gallery/> }/>
        </Routes>
      </MainLayout>
    </div>
  );
}

export default App;
