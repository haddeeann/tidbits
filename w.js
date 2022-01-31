
let products = [ 
    { 
        "product_name": "bouncing_bear", 
        "product_category": "bears", 
        "product_ID": "bb_112", 
        "product_price": "3334.23", 
        "product_quantity": "3", 
        "product_notes": "This product is obscenely expensive." 
    }, 
    { 
        "product_name": "fluffy_Boots", 
        "product_category": "shoes", 
        "product_ID": "fb_223", 
        "product_price": "124.99", 
        "product_quantity": "1", 
        "product_notes": "These boots are never in stock." 
    }, 
    { 
        "product_name": "Happy_baby", 
        "product_category": "infants", 
        "product_ID": "hb_11", 
        "product_price": "500.63", 
        "product_quantity": "3", 
        "product_notes": "Trades for unhappy babies prohibited." 
    } 
];

// Write a function that will calculate the 
// total order value of the example in JS.2.
function totalOrderValue(products) {
    return products.map(p => {
        return p.product_price * p.product_quantity;
    }).reduce((a, b) => a + b);
}

totalOrderValue(products);
// Write a function that will loop through these products 
// and return a new array of objects containing the properties
//  “productId”, “qty”, and “price”. 
function sortProducts(products) {
    return products.map(product => {
        return {
            "productId": product.product_ID,
            "qty": product.product_quantity,
            "price": product.product_price
        }
    });
}

// console.log(sortProducts(products));