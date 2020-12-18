import React from "react"

function Header() {
	const date = new Date()
	const hours = date.getHours()
	const greeting = hours < 12 ? "Morning" : hours < 17 ? "Afternoon" : 'Evening'
	return (
		<div>
			<h1 className="navbar"> Hello there! Good {greeting}</h1>
		</div>
	);
}

export default Header
