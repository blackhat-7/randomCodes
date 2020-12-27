// const fibonacci = x => {
//     if (x == 0 || x == 1) {
//         return x;
//     }
//     return fibonacci(x-1) + fibonacci(x-2)
// };

// let nums = [1, 10, 20, 30, 40, 50, 60]

// nums = nums.filter(num => {
//     return num <= 30;
// })

// let num_fibs = nums.map(num => {
//     return [num, fibonacci(num)];
// });

// const rubiksCubeFacts = {
//     possiblePermutations: '43,252,003,274,489,856,000',
//     invented: 1974,
//     largestCube: '17x17',
//     _myFastestTime: 20,

//     set myFastestTime(newTime) { this._myFastestTime = newTime; },
//     get myFastestTime() { return this._myFastestTime; }
// };

// const {possiblePermutations, invented, largestCube} = rubiksCubeFacts;
// console.log(`${possiblePermutations}         ${invented}              ${largestCube}`);

// rubiksCubeFacts._myFastestTime = 18;
// console.log(rubiksCubeFacts.myFastestTime);




class Media {
  constructor(type) {
    this.type = type
  }

  use() {
    if (this.type == 'song') { this.play(); }
  }
}


class Song extends Media {
  constructor(title, author) {
    super('song');
    this.title = title;
    this.author = author;
  }

  play() {
    console.log("Now playing " + this.title + " by " + this.author);
  }
}

const mySong = new Song('insert song name', 'Shaunak');
mySong.use();
