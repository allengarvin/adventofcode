use aoc
db.numbers.remove({})
db.pairs.remove({})

var numbers = cat("01-input.txt").trim().split("\n").map(x=>+x);
const mul = (acc, val) => acc * val;

numbers.forEach(function (x) { db.numbers.insert({_id:x}); });
numbers.forEach(function (x) { 
    numbers.forEach( function (y) {
        if( x != y && x + y < 2020 )
            db.pairs.insert({ sum : x + y, pair : [x, y] });
    })
})

var prob1 = numbers.filter(function (x) { return db.numbers.find({ _id : 2020-x}).length() > 0; }).reduce(mul)
var prob2 = numbers.filter(function (x) { return db.pairs.find({sum : 2020 - x}).length(); }).reduce(mul)

print(prob1)
print(prob2)
