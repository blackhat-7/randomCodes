import React from "react"

function ContactCard(props) {
    return (
        <div>
            <hr></hr>
            <img src={props.contact.img}></img>
            <h3>{props.contact.name}</h3>
            <p>{props.contact.email}</p>
            <p>{props.contact.phone}</p>
            <hr></hr>
        </div>
    );
}

export default ContactCard
