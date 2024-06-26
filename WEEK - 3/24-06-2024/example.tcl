# Basics of TCL

# Hello World
Here's a basic "Hello, World!" example in TCL:

```tcl
puts "Hello, World!"
```

# Variables
You can create and use variables easily:

```tcl
set myVar "Hello, TCL"
puts $myVar
```

# Arithmetic Operations
You can perform arithmetic operations using `expr`:

```tcl
set a 5
set b 10
set sum [expr $a + $b]
puts "Sum: $sum"
```

# Control Structures

# If-Else
```tcl
set age 20
if { $age < 18 } {
    puts "You are a minor."
} elseif { $age < 65 } {
    puts "You are an adult."
} else {
    puts "You are a senior."
}
```

# Loops
###### For Loop
```tcl
for {set i 0} {$i < 5} {incr i} {
    puts "Iteration $i"
}
```

# While Loop
```tcl
set count 0
while { $count < 5 } {
    puts "Count: $count"
    incr count
}
```

# Foreach Loop
```tcl
set fruits {apple banana cherry}
foreach fruit $fruits {
    puts "Fruit: $fruit"
}
```

# Procedures (Functions)
You can define and call procedures:

```tcl
proc greet {name} {
    puts "Hello, $name!"
}

greet "Sai Venkat"
```

# Example Script: Simple Calculator
Here's a simple calculator script that takes two numbers and an operation as input and prints the result:

```tcl
proc calculator {a b operation} {
    switch $operation {
        "+" {
            set result [expr $a + $b]
        }
        "-" {
            set result [expr $a - $b]
        }
        "*" {
            set result [expr $a * $b]
        }
        "/" {
            if {$b == 0} {
                return "Division by zero error"
            }
            set result [expr $a / $b]
        }
        default {
            return "Invalid operation"
        }
    }
    return $result
}

puts "Enter first number:"
gets stdin num1

puts "Enter second number:"
gets stdin num2

puts "Enter operation (+, -, *, /):"
gets stdin op

set result [calculator $num1 $num2 $op]
puts "Result: $result"
```

# File I/O
Reading from and writing to files is straightforward:

# Writing to a File
```tcl
set fileId [open "output.txt" "w"]
puts $fileId "This is a line of text."
close $fileId
```

# Reading from a File
```tcl
set fileId [open "output.txt" "r"]
while {[gets $fileId line] >= 0} {
    puts $line
}
close $fileId
```

