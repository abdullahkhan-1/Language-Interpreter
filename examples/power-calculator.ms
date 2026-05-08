# Compute base ^ exponent using repeated multiplication

let base = 3
let exponent = 5
let result = 1
let i = 0

while i < exponent {
    result = result * base
    i = i + 1
}

print "3 ^ 5 ="
print result

# Also compute 2 ^ 10
let base2 = 2
let exp2 = 10
let res2 = 1
let j = 0

while j < exp2 {
    res2 = res2 * base2
    j = j + 1
}

print "2 ^ 10 ="
print res2