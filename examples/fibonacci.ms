# Fibonacci sequence — first 10 terms

print "Fibonacci sequence:"

let a = 0
let b = 1
let count = 0

while count < 10 {
    print a
    let temp = a + b
    a = b
    b = temp
    count = count + 1
}