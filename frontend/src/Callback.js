import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';

const Callback = () => {
    const navigate = useNavigate();

    useEffect(() => {
        const urlParams = new URLSearchParams(window.location.search);
        const code = urlParams.get('code');
        
        if(code) {
            fetch('http://localhost:3000/callback', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ code: code })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                navigate('/dashboard');
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
        }
    }, [navigate]);

    return null;
};
 
export default Callback;
