// // https://www.freecodecamp.org/news/how-did-i-miss-javascript-symbols-c1f1c0e1874a/

// Symbols are new primitive type introduced in ES6. Symbols are completely unique identifiers. Just like their primitive counterparts (Number, String, Boolean), they can be created using the factory function Symbol() which returns a Symbol.
// used in some cases to prevent name clashing of private keys
let _counter = Symbol('counter');
const _action  = Symbol('action');
console.log(_counter);
class Countdown {
    constructor(counter, action) {
        this[_counter] = counter;
        this[_action] = action;
    }
    dec() {
        let counter = this[_counter];
        if (counter < 1) return;
        counter--;
        this[_counter] = counter;
        if (counter === 0) {
            this[_action]();
        }
    }
}

// const obj = {
//     [Symbol('my_key')]  : 1, 
//      enum               : 2, 
//      nonEnum            : 3
//   };
  
//   Object.defineProperty(obj, 'nonEnum', { enumerable: false }); // Making 'nonEnum' as not enumerable.
  
//   // Ignores symbol-valued property keys:
//   > Object.getOwnPropertyNames(obj)
//   ['enum', 'nonEnum']
  
//   // Ignores string-valued property keys:
//   > Object.getOwnPropertySymbols(obj)
//   [Symbol(my_key)]
  
//   // Considers all kinds of keys:
//   > Reflect.ownKeys(obj)
//   [Symbol(my_key),'enum', 'nonEnum']
  
//   // Only considers enumerable property keys that are strings:
//   > Object.keys(obj)
//   ['enum']

let code = 'coffee' + 'developer';