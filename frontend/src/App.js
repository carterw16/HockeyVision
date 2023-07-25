import './App.css';
import { Gallery } from './Components/Gallery/Gallery';
import { MainLayout } from './Layout/MainLayout';
import { Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <MainLayout>
        <Routes>
          <Route path="/game/:id" element="Game"/>
          <Route exact path="/" element={ <Gallery/> }/>
        </Routes>
      </MainLayout>
    </div>
  );
}

export default App;
