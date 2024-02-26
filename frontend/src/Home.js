const Home = () => {

    const handleLogin = async () => {
        try {
            const response = await fetch('http://localhost:5000/login');
            const data = await response.json();
            window.location.href = data.redirect_url;
        } catch (error) {
            console.error(error);
        }
    };

    return ( 
        <div className="Home">
            <h1>Welcome to <span id="title-color">PlaylistPilot</span></h1>
            <p>Discover songs tailored to your already created playlist</p>
            <button className="project-button" onClick={handleLogin}>Sign in</button>
        </div>
     );
}
 
export default Home;