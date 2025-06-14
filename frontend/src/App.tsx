import { useState, useEffect } from 'react';
import LoginPage from './components/LoginPage';

function App() {
  const [helloMessage, setHelloMessage] = useState<string>('');

  useEffect(() => {
    const fetchHelloWorld = async () => {
      try {
        const response = await fetch('/api/hello');
        const data = await response.json(); // Assuming your Django Ninja API returns JSON
        setHelloMessage(data);
      } catch (error) {
        console.error('Error fetching hello message:', error);
        setHelloMessage('Failed to load message.');
      }
    };

    fetchHelloWorld();
  }, []);

  return (
    <LoginPage message={helloMessage} />
  );
}

export default App;
