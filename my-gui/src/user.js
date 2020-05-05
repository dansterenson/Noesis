import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'

function User({ match }) {
    useEffect(() => {
        fetchItems();
        //console.log(match);
    }, []);

    const [items, setItem] = useState([{}]);
    const fetchItems = async () => {
        const fetchItem = await fetch(
            `http://127.0.0.1:5000/users/${match.params.id}`);
        const items = await fetchItem.json();

        //console.log(items);
        setItem(items);
    };


    return (
        <div>
            <h1>User Details</h1>
            {items.map(item => (
                <h3 key={item.user_id}>User_name: {item.user_name} <br></br>
                    User_id: {item.user_id} <br></br>
                    Birthday: {item.birthday} <br></br>
                    Gender: {item.gender} <br></br>
                    <Link to={`/users/${match.params.id}/snapshots`}> Get Snapshots</Link>
                </h3>
            ))}
        </div>
    );
}

export default User;