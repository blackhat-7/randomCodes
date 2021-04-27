




function arrays() {
    // arr = [1, 3, 5, 7, 9]
    // arr.forEach(function(item, index, array) {
    //     console.log(item, index, array)
    // })
    // arr.pop()
    // arr.push(11)
    // arr.shift()
    // arr.unshift(-1)
    // console.log(arr)
    // console.log(arr.indexOf(5))
    // arr.splice(2, 1)
    // console.log(arr)
    // const arrCopy = arr.slice()
    // console.log(arrCopy)
    // arr[6] = 'something'
    // console.log(Object.keys(arr))
    // console.log(arr.length)
    // console.log(Array.isArray(arr))

    newArr = []
    console.log(newArr.length)
    newArr[99] = 0
    console.log(newArr.length)
    console.log(Array.from(Array(2), ()=> new Array(4)))
    console.log(newArr.fill(2))
    const newArr2 = Array(5)
    newArr2[0] = 0.0
    if (newArr2[0])
        console.log(newArr2[0])
    
}

function strings() {
    myStr = "   I like coding in javascript.  "
    console.log(myStr.length)
}

arrays()
// strings()