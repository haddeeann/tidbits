// "class" declaration
function Car(make, model) {
  this.make = make;
  this.model = model;
}

// the start method
Car.prototype.start = function() {
  console.log('vroom');
}

// overriding the toString method
Car.prototype.toString = function() {
  console.log('Car - ' + this.make + ' - ' + this.model);
}

// inheritance example
function SportsCar(make, model, turbocharged) {
  Car.call(this, make, model);
  this.turbocharged = turbocharged;
}

// actual inheritance logic
SportsCar.prototype = Object.create(Car.prototype);
SportsCar.prototype.constructor = SportsCar;

// overriding the start method
SportsCar.prototype.start = function() {
  console.log('VROOOOM');
}

// Now testing the classes
var car = new Car('Nissan', 'Sunny');
car.start(); // vroom
console.log(car.make); // Nissan

var sportsCar = new SportsCar('Subaru', 'BRZ', true);
sportsCar.start(); // VROOOOM
console.log(car.turbocharged); // true