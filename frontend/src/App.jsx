import React from 'react';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Homepage } from "./pages/Homepage";
import GenerationPage from './pages/GenerationPage';

function App() {
  
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path="/generation" element={<GenerationPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;