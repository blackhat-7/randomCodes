function arrays() {
  const months = ['Jan', 'Feb', 'Mar', 'Apr', 'Jun'];
  console.log(months);
  months.splice(2, 0, 'a');
  console.log(months);
  months.splice(4, 1, 'b');
  console.log(months);
  months.splice(3, 3, 'c');
  console.log(months);

  for (const ele of month) {
    console.log(ele);
  }
  months.push(5);
  console.log(months.findIndex(month => 'Apr'));
}

function sets() {
  const mySet = new Set([1, 4, 5]);
  mySet.add(2);
  for (const ele of mySet) {
    console.log(ele);
  }
  console.log(mySet.has(5));
  console.log(mySet.delete(2));
}

function objects() {
  const person = {
    firstName: 'Max',
    age: '21',
    hobbies: ['Sports', 'Cooking'],
    greet() {
      console.log('Hi, I am ' + this.firstName);
  } };
  console.log(person.hobbies);
  person.lastname = "Schwarz";
  console.log(person.lastname);
  delete person.age;
  person.greet();

}

function maps() {
  const resultData = new Map();
  resultData.set('average', 1.53);
  resultData.set('lasResult', null);
  
  const germany = {name: 'Germany', population: 82};
  resultData.set(germany, 0.89);

  for (ele of resultData) {
    console.log(ele);
  }

  resultData.delete(germany);
}



main();