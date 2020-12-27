import React from "react"
import Header from "./Components/Header"
import Content from "./Components/Content"
import Footer from "./Components/Footer"

class App extends React.Component {
    constructor() {
        super()
        this.state = {
            isLoading: true
        }
    }
    componentDidMount() {
        setTimeout(() => {
            this.setState({
                isLoading: false
            })
        }, 1500)
    }

    render() {
        return (
            <div>
                <Header />
                {this.state.isLoading ? <h2>Content is loading...Please be patient</h2> : <Content />}
                <Footer />
            </div>
        )
    }
}

export default App;