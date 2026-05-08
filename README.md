# 🧠 Mini Script Language Interpreter

A lightweight, custom scripting language interpreter built from scratch in Python. It implements the classic interpreter pipeline: **Lexer → Parser → AST → Interpreter**, and supports variables, arithmetic, conditionals, loops, functions, and more — all in a clean, readable mini-language with `.ms` files.

---

## 📁 Project Structure

```
Mini-Script-Language-Interpreter/
├── main.py          # Entry point — reads and runs .ms files
├── lexer.py         # Tokenizer — converts source code into tokens
├── parser.py        # Recursive-descent parser — builds the AST
├── nodes.py         # AST node definitions
├── interpreter.py   # Tree-walk interpreter — executes the AST
└── examples/        # Sample .ms scripts
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x (no external dependencies)

### Running a Script

```bash
python main.py <your_script.ms>
```

**Example:**

```bash
python main.py examples/hello.ms
```

---

## 🗣️ Language Syntax

### Variables

Variables must be declared with `let` before use. Reassignment uses plain `=`.

```
let x = 10
let name = "Abdullah"
x = x + 5
```

### Print

```
print x
print "Hello, World!"
```

### Arithmetic

Supports `+`, `-`, `*`, `/` with proper operator precedence and parentheses.

```
let result = (3 + 4) * 2
print result
```

> Division by zero raises a `ZeroDivisionError` at runtime.

### Conditionals

```
if x > 5 {
    print "big"
} else {
    print "small"
}
```

Supported comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`

### While Loop

```
let i = 0
while i < 5 {
    print i
    i = i + 1
}
```

### For Loop

```
for i = 1 to 10 {
    print i
}
```

### Functions

```
fun greet(name) {
    print name
}

greet("World")
```

Functions support parameters, multiple statements in the body, and a `return` statement.

```
fun add(a, b) {
    return a + b
}
```

### Comments

Lines starting with `#` are treated as comments and ignored.

```
# This is a comment
let x = 42   # inline comment
```

---

## 🔢 Supported Data Types

| Type    | Example          |
|---------|------------------|
| Integer | `42`             |
| Float   | `3.14`           |
| String  | `"hello world"`  |

---

## ⚙️ How It Works

The interpreter follows a classic four-stage pipeline:

### 1. Lexer (`lexer.py`)
Scans the raw source code character by character and produces a flat list of tokens. Handles integers, floats, strings, identifiers, keywords, operators, and delimiters. Skips whitespace and comments.

**Keywords:** `let`, `if`, `else`, `while`, `for`, `to`, `print`, `fun`, `return`

### 2. AST Nodes (`nodes.py`)
Defines the data classes that represent every construct in the language as a node in the Abstract Syntax Tree (AST). Includes nodes for numbers, strings, identifiers, binary operations, conditionals, variable declarations, assignments, print, if/else, while, for, function definitions, function calls, and return.

### 3. Parser (`parser.py`)
A hand-written recursive-descent parser that consumes the token stream and builds a tree of AST nodes. Handles operator precedence correctly via the `expression → term → factor` hierarchy.

### 4. Interpreter (`interpreter.py`)
A tree-walk interpreter that recursively evaluates each AST node. Maintains a flat environment dictionary (`self.env`) for variable storage. Enforces that variables must be declared with `let` before assignment.

---

## 🛡️ Error Handling

The interpreter provides clear runtime errors:

| Error              | Cause                                              |
|--------------------|----------------------------------------------------|
| `SyntaxError`      | Invalid or unexpected token in source code         |
| `NameError`        | Using undeclared variable, or re-declaring with `let` |
| `ZeroDivisionError`| Division by zero in an expression                  |
| `RuntimeError`     | Unknown or unsupported AST node encountered        |

---

## 📝 Example Script

```
# Fibonacci sequence
let a = 0
let b = 1
let i = 0

while i < 10 {
    print a
    let temp = a + b
    a = b
    b = temp
    i = i + 1
}
```

---

## 🧩 Keywords Reference

| Keyword  | Purpose                        |
|----------|--------------------------------|
| `let`    | Declare a new variable         |
| `print`  | Print a value to stdout        |
| `if`     | Conditional branch             |
| `else`   | Alternative branch             |
| `while`  | Conditional loop               |
| `for`    | Range-based loop               |
| `to`     | Defines the end of a for range |
| `fun`    | Define a function              |
| `return` | Return a value from a function |

---

## 👤 Author

**Abdullah Khan**  
GitHub: [@abdullahkhan-1](https://github.com/abdullahkhan-1)

---
