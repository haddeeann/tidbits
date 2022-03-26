// literally just a map.
// sometimes I feel new to earth. Like I haven't used Maps before?
// whatever. I guess I was just using object and arrays, like a newb.
// -0 and +0 are equal

const mapOne = new Map();

mapOne.set('a', 15);
mapOne.set('b', 25);

console.log(mapOne);

mapOne.delete('b');
mapOne.set('ghosts', 45);
console.log(mapOne);

console.log(mapOne.size)

/* 1. Advantages of key: no accidental inherited keys. Things made with an object will have prototype chain inheritied keys.
2. Map's keys can be any values, including functions, objects or primitives.
3. The keys in a Map are ordered nicely. It's ordered in the order of inertion entry. You can't rely on property order on objects. Although there is a property order (as of now) it's compliex.
4. There is map size so you can easily see the size of a map. You have to manually figure out the size of an object.
5. Performs better when adding and removing key-value pairs. It's _optimized_ for that.
6. Only drawback.. no built in serialization or parsing.
https://stackoverflow.com/questions/29085197/how-do-you-json-stringify-an-es6-map
*/