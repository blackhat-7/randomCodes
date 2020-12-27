import React, { Component } from "react"

export default class MemeGenerator extends Component {
    constructor() {
        super()
        this.state = {
            topText: "",
            bottomText: "",
            imgUrl: "http://i.imgflip.com/1bij.jpg",
            allMemeImgs: []
        }
        this.handleChange = this.handleChange.bind(this)
        this.generateImage = this.generateImage.bind(this)
    }

    handleChange(e) {
        const { name, value } = e.target
        this.setState({
            [name]: value
        })
    }

    componentDidMount() {
        fetch("https://api.imgflip.com/get_memes")
            .then(response => response.json())
            .then(response => {
                const { memes } = response.data
                this.setState({ allMemeImgs: memes })
            })
    }

    generateImage(e) {
        e.preventDefault()
        const index = Math.floor(Math.random() * (this.state.allMemeImgs.length))
        const img = this.state.allMemeImgs[index].url
        console.log(this.state.allMemeImgs[index])
        this.setState({ imgUrl: img })
    }

    render() {
        return (
            <div>
                <form onSubmit={this.generateImage}>
                    <input type="text" name="topText" placeholder="Top Text" value={this.state.topText} onChange={this.handleChange} />
                    <br />
                    <input type="text" name="bottomText" placeholder="Bottom Text" value={this.state.bottomText} onChange={this.handleChange} />
                    <br />
                    <button name="submit">Gen</button>
                </form>

                <hr />
                <h1>{this.state.topText}</h1>
                <img src={this.state.imgUrl} alt="Problem loading image" />
                <h1>{this.state.bottomText}</h1>
                <hr />
            </div>
        )
    }
}