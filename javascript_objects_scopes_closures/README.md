# JavaScript Objects, Scopes, and Closures

This repository contains solutions to the tasks for learning JavaScript object-oriented programming, closures, inheritance, and more.

## Learning Objectives
At the end of this project, you will be able to explain the following concepts:

### General
- Why JavaScript programming is amazing
- How to create an object in JavaScript
- What `this` means
- What `undefined` means
- Why variable type and scope are important
- What is a closure
- What is a prototype
- How to inherit an object from another

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should be semistandard compliant (rules of Standard + semicolons, reference: [AirBnB style](https://github.com/airbnb/javascript))
- All files must be executable
- The length of files will be tested using `wc`
- `var` is not allowed; use `let` or `const`

### More Info

#### Install Node.js 14
```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

#### Install semistandard
```bash
$ sudo npm install semistandard --global
```

---

## Tasks

### 0. Rectangle #0
Write an empty class `Rectangle` that defines a rectangle:
- Use the `class` notation for defining your class.

**File:** `0-rectangle.js`

### 1. Rectangle #1
Write a class `Rectangle` that defines a rectangle:
- The constructor takes two arguments `w` and `h`.
- Initialize instance attributes `width` and `height` with the values of `w` and `h`.

**File:** `1-rectangle.js`

### 2. Rectangle #2
Enhance the `Rectangle` class:
- If `w` or `h` is 0 or not a positive integer, create an empty object.

**File:** `2-rectangle.js`

### 3. Rectangle #3
Enhance the `Rectangle` class further:
- Add an instance method `print()` that prints the rectangle using the character `X`.

**File:** `3-rectangle.js`

### 4. Rectangle #4
Enhance the `Rectangle` class:
- Add an instance method `rotate()` to exchange the width and height of the rectangle.
- Add an instance method `double()` to multiply the width and height of the rectangle by 2.

**File:** `4-rectangle.js`

### 5. Square #0
Write a class `Square` that defines a square and inherits from `Rectangle`:
- The constructor takes one argument `size`.
- Call the constructor of `Rectangle` using `super()`.

**File:** `5-square.js`

### 6. Square #1
Enhance the `Square` class:
- Add an instance method `charPrint(c)` that prints the square using the character `c`. If `c` is undefined, use `X`.

**File:** `6-square.js`

### 7. Occurrences
Write a function that returns the number of occurrences of an element in a list:
- Prototype: `exports.nbOccurences = function (list, searchElement)`

**File:** `7-occurrences.js`

### 8. Esrever
Write a function that returns the reversed version of a list:
- Prototype: `exports.esrever = function (list)`
- Do not use the built-in `reverse` method.

**File:** `8-esrever.js`

### 9. Log me
Write a function that prints the number of arguments already printed and the new argument value:
- Prototype: `exports.logMe = function (item)`
- Output format: `<number arguments already printed>: <current argument value>`

**File:** `9-logme.js`

### 10. Number conversion
Write a function that converts a number from base 10 to another base:
- Prototype: `exports.converter = function (base)`
- Do not declare any new variables.

**File:** `10-converter.js`

