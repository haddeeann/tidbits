const fs = require('fs');

let textObj = {
    "name": "patricia g.",
    "occupation": "delivery driver",
    "rate of pay": "$22/hr"
}

fs.writeFileSync('text.json', JSON.stringify(textObj));

const textBuffer = fs.readFileSync('text.json');
const textStr = textBuffer.toString();
let textFileObj = JSON.parse(textStr);

console.log(textFileObj.name);

textFileObj.name = 'Jazzy Jeff, DJ';

fs.writeFileSync('text.json', JSON.stringify(textFileObj));

console.log('hi');