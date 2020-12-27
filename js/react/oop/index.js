console.log("Hello World!")

function Circle(radius) {
  this.radius = radius;
  this.draw = function() {
    console.log('Drawing a circle with radius ' + this.radius);
  }
}

const circle = new Circle(10);
circle.radius = 5;
circle.draw();







