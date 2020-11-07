import React, { useState } from "react";
import "./App.css"

function Tweet({ name, message }) {
    const [tweetCount, setTweetCount] = useState(0);
    const [tweetColor, setTweetColor] = useState('');

    const increament = () => {
        setTweetCount(tweetCount + 1);
        if (tweetCount >= 9) {
            setTweetColor('green');
        }
    }

    return (
        <div className="Tweet">
            <h3>{name}</h3>
            <p>{message}</p>
            <h3 className={tweetColor}>Tweets: {tweetCount}</h3>
            <button onClick={increament}>Retweet</button>
        </div >
    );
}

export default Tweet;