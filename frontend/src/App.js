import './App.css';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Home from './Home';
import Dashboard from './Dashboard';
import Callback from './Callback';
import Songs from './Songs'

function App() {
  return (
    <Router>
    <div className="App">
      <header className="App-header">
        <Routes>
            <Route path="/" exact element={<Home />} />
            <Route path="/callback" element={<Callback />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/dashboard/:id" element={<Songs />} />
        </Routes>
      </header>
    </div>
    </Router>
  );
}

export default App;
