import React from "react"
import Product from "./Product";
import products from "./productData"

class Content1 extends React.Component {
    render() {
        const productComponents = products.map(product => {
            return (<Product key={product.id} name={product.name} price={product.price} desc={product.desc} />);
        });

        return (
            <div>
                {productComponents}
            </div>
        );
    }
}

export default Content1
