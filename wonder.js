let data = [
    {
        "pagePostType": "product",
        "pagePostType2": "single-product",
        "deviceType": "desktop",
        "deviceManufacturer": "",
        "deviceModel": "",
        "ecommerce": {
            "detail": {
                "products": [
                    {
                        "name": "Red Velvet Decorative Storage Box",
                        "id": 32,
                        "price": "189.00",
                        "category": "Storage",
                        "sku": "SR-458254"
                    }
                ]
            }
        }
    },
    {
        "gtm.start": 1642790441381,
        "event": "gtm.js",
        "gtm.uniqueEventId": 3
    },
    {
        "event": "gtm.dom",
        "gtm.uniqueEventId": 7
    },
    {
        "event": "gtm.load",
        "gtm.uniqueEventId": 8
    },
    {
        "event": "gtm.timer",
        "gtm.timerId": 8,
        "gtm.timerEventNumber": 1,
        "gtm.timerInterval": 6000,
        "gtm.timerLimit": 1,
        "gtm.timerStartTime": 1642790441491,
        "gtm.timerCurrentTime": 1642790448111,
        "gtm.timerElapsedTime": 6620,
        "gtm.triggers": "879458_13",
        "gtm.uniqueEventId": 9
    }
];

function loopArr(arr) {
    let sku = '';
    for(let i of arr) {
        if(typeof(i) === 'object' && Array.isArray(i)) {
            loopArr(i);
        } else if(typeof(i) === 'object' ) {
            let temp = loopObj(arr);
            if(temp.length > 0) {
                sku = temp;
            }
        }
    }
    return sku;
}
    
function loopObj(obj) {
    let sku = '';
    for (const [key, value] of Object.entries(obj)) {
        if(typeof(value) === 'object' && Array.isArray(value)) {
            loopArr(value);
        } else if(typeof(value) === 'object') {
            let temp = loopObj(value);
            if(temp.length > 0) {
                sku = temp;
            }
        } else if(key === 'sku') {
            sku = value;
        }
    }
    return sku;
}

function findSku(dataLayer) {
    let sku = 'good point';
    let temp = '';
    if(typeof(dataLayer) === 'object' && Array.isArray(dataLayer)) {
        temp = loopArr(dataLayer);
        if(temp.length > 0) {
            sku = temp;
        }
    } else if(typeof(dataLayer) === 'object' ) {
        temp = loopObj(dataLayer);
        if(temp.length > 0) {
            sku = temp;
        }
    }
    return sku;
}

console.log(findSku(data));
