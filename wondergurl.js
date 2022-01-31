let dataLayer = [
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

function loopArr(data) {
    if(typeof(data) === 'object' && !Array.isArray(data) && data['sku']) {
        return data['sku'];
    }

    if(typeof(data) === 'object' && !Array.isArray(data)) {
        // type is an object
        for(const [key, value] of Object.entries(data)) {
            if(typeof(value) === 'object') {
                return loopArr(value);
            }
            // else {
            //     if(key === 'sku') {
            //         console.log(`${key}: ${value}`);
            //     }
            // }
        }
    } else if(typeof(data) === 'object' && Array.isArray(data)) {
        // type is an array, loop through like an array
        for(let i = 0; i < data.length; i++) {
            if(typeof(data[i]) === 'object') {
                return loopArr(data[i]);
            }
        }
    }
}

function findSku(data) {
    return loopArr(data);
}

findSku(window.dataLayer);
