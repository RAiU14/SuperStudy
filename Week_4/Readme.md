# 📘 JavaScript Basics – Chapter 1 & Chapter 2

This README combines:

```text
Chapter 1 -> Variables & Strings
Chapter 2 -> Numbers, Operators & Type Conversions
```

These chapters are beginner-friendly and explain every major concept step by step.

---

# 📘 JavaScript Chapter 1 – Variables & Strings

This chapter explains the code from:

```text
Study_JS_1.js
```

It covers variables, strings, string methods, and basic output.

---

## 🧠 What is this program?

This program demonstrates:

- How to declare variables using `let` and `const`
- What strings are
- String concatenation
- Template literals
- String properties and methods
- Accessing characters using indexes
- Searching inside strings
- Variable reassignment
- Printing output using `console.log()`

---

# 📄 Chapter 1 Code – Explained Line by Line

## 📦 Section 1: Declaring Variables

```javascript
let studentName = "Priya";
```

Explanation:

- `let` creates a variable whose value can change later.
- `studentName` is the variable name.
- `=` is the assignment operator.
- `"Priya"` is a string value.

Result:

```text
A memory box named studentName now stores "Priya".
```

---

```javascript
const college = "ABC University";
```

Explanation:

- `const` creates a constant variable.
- A `const` value cannot be reassigned later.
- `college` stores the string `"ABC University"`.

Result:

```text
A locked box named college stores "ABC University".
```

Trying to change this later will cause an error.

---

## 🧵 Section 2: Working with Strings

## 2.1 String Concatenation

```javascript
let greeting = "Hello, " + studentName + "!";
```

Explanation:

- The `+` operator joins strings together.
- `"Hello, " + studentName` becomes `"Hello, Priya"`.
- Then `"!"` is added at the end.

Result:

```text
Hello, Priya!
```

---

```javascript
console.log(greeting);
```

`console.log()` prints output to the terminal.

Output:

```text
Hello, Priya!
```

---

## 2.2 Template Literals

```javascript
let message = `Welcome to ${college}, ${studentName}.`;
```

Explanation:

- Template literals use backticks: `` ` ``
- `${college}` inserts the value of the `college` variable.
- `${studentName}` inserts the value of the `studentName` variable.
- This is cleaner than using many `+` signs.

Output:

```text
Welcome to ABC University, Priya.
```

---

```javascript
console.log(message);
```

Output:

```text
Welcome to ABC University, Priya.
```

---

## 2.3 String Length

```javascript
let text = "JavaScript";
console.log("Length of 'JavaScript' is: " + text.length);
```

Explanation:

- `.length` counts the number of characters in a string.
- `"JavaScript"` has 10 characters.
- `.length` is a property, so it does not use parentheses.

Output:

```text
Length of 'JavaScript' is: 10
```

---

## 2.4 Changing Case

```javascript
let mixed = "HeLlO WoRlD";
console.log(mixed.toUpperCase());
console.log(mixed.toLowerCase());
```

Explanation:

- `.toUpperCase()` returns a new uppercase string.
- `.toLowerCase()` returns a new lowercase string.
- The original string is not changed.

Output:

```text
HELLO WORLD
hello world
```

Important note:

```text
Strings in JavaScript are immutable.
That means string methods return modified copies.
They do not change the original string directly.
```

---

## 2.5 Accessing Individual Characters

```javascript
let language = "Coding";
console.log("First character: " + language[0]);
console.log("Last character: " + language[5]);
```

JavaScript uses zero-based indexing.

For `"Coding"`:

| Character | C | o | d | i | n | g |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Index | 0 | 1 | 2 | 3 | 4 | 5 |

Explanation:

```text
language[0] -> C
language[5] -> g
```

Output:

```text
First character: C
Last character: g
```

---

## 2.6 Searching Within a String

```javascript
let sentence = "I love JavaScript";
console.log(sentence.includes("Java"));
console.log(sentence.indexOf("love"));
```

Explanation:

- `.includes("Java")` checks whether `"Java"` exists inside the string.
- It returns `true` or `false`.
- `.indexOf("love")` returns the starting index of `"love"`.

Output:

```text
true
2
```

Why `2`?

```text
I love JavaScript
0 -> I
1 -> space
2 -> l
```

If a word is not found, `.indexOf()` returns:

```text
-1
```

---

## 🔄 Section 3: Changing Variables

```javascript
let score = 10;
score = 15;
console.log("Updated score: " + score);
```

Explanation:

- `score` was declared using `let`.
- So its value can be changed later.
- When updating a variable, do not write `let` again.

Output:

```text
Updated score: 15
```

---

## 🖨️ Section 4: Simple Output

```javascript
let userName = "Sam";
let userCity = "Mumbai";
let intro = `Hi, I'm ${userName} from ${userCity}.`;
console.log(intro);
```

Output:

```text
Hi, I'm Sam from Mumbai.
```

---

```javascript
console.log("\n✅ End of Chapter 1 program.");
```

Explanation:

- `\n` creates a new line before printing the text.

Output:

```text

✅ End of Chapter 1 program.
```

---

# 🔑 Chapter 1 Key Takeaways

| Concept / Syntax | Description |
| :--- | :--- |
| `let` | Declares a variable that can be updated later. |
| `const` | Declares a variable that cannot be reassigned. |
| `"string"` or `'string'` | Text wrapped in quotes. |
| `` `template ${var}` `` | Template literal used to insert variables directly into strings. |
| `+` with strings | Joins strings together. |
| `.length` | Counts the number of characters in a string. |
| `.toUpperCase()` | Converts a string copy to uppercase. |
| `.toLowerCase()` | Converts a string copy to lowercase. |
| `[index]` | Accesses a character by position. Index starts at 0. |
| `.includes("text")` | Returns `true` if text exists inside the string. |
| `.indexOf("text")` | Returns the starting index of text, or `-1` if not found. |

---

# 📘 JavaScript Chapter 2 – Numbers, Operators & Type Conversions

This chapter explains the code from:

```text
Study_JS_2.js
```

It covers numbers, arithmetic, comparisons, logic, type conversions, and the `Math` object.

---

## 🧠 What is this program?

This program demonstrates:

- Numbers
- Arithmetic operators
- Operator precedence
- Comparison operators
- Logical operators
- Type conversion
- The `Math` object
- A small mini quiz example

---

# 📄 Chapter 2 Code – Explained Line by Line

## 🔢 Section 1: Numbers & Basic Arithmetic

```javascript
let age = 25;
let price = 99.99;
let bigNumber = 1e6;
```

Explanation:

- `age` stores an integer.
- `price` stores a decimal number.
- `bigNumber` uses scientific notation.
- `1e6` means `1 * 10^6`, which is `1,000,000`.

Important note:

```text
JavaScript has one main number type.
It does not separate integers and floats like some other languages.
```

---

```javascript
let sum = age + 10;
let product = price * 2;
let quotient = age / 4;
let remainder = age % 3;
let power = age ** 2;
```

Explanation:

| Code | Meaning | Result |
| :--- | :--- | :--- |
| `age + 10` | Addition | `35` |
| `price * 2` | Multiplication | `199.98` |
| `age / 4` | Division | `6.25` |
| `age % 3` | Remainder after division | `1` |
| `age ** 2` | Exponent / power | `625` |

---

```javascript
console.log("Sum:", sum);
console.log("Product:", product);
console.log("Quotient:", quotient);
console.log("Remainder:", remainder);
console.log("Power:", power);
```

Output:

```text
Sum: 35
Product: 199.98
Quotient: 6.25
Remainder: 1
Power: 625
```

---

## ➗ Section 2: Operator Precedence

```javascript
let result = 10 + 5 * 2;
console.log("10 + 5 * 2 =", result);
```

Explanation:

JavaScript follows normal math rules.

Multiplication happens before addition.

```text
10 + 5 * 2
10 + 10
20
```

Output:

```text
10 + 5 * 2 = 20
```

---

```javascript
let withParens = (10 + 5) * 2;
console.log("(10 + 5) * 2 =", withParens);
```

Explanation:

Parentheses force the addition to happen first.

```text
(10 + 5) * 2
15 * 2
30
```

Output:

```text
(10 + 5) * 2 = 30
```

---

## ⚖️ Section 3: Comparison Operators

```javascript
let x = 10;
let y = 20;

console.log("x > y?", x > y);
console.log("x < y?", x < y);
console.log("x == 10?", x == 10);
console.log("x != 10?", x != 10);
```

Explanation:

Comparisons return boolean values:

```text
true
false
```

Output:

```text
x > y? false
x < y? true
x == 10? true
x != 10? false
```

---

## Strict vs Loose Equality

```javascript
console.log("10 == '10'?", 10 == '10');
console.log("10 === '10'?", 10 === '10');
console.log("10 != '10'?", 10 != '10');
console.log("10 !== '10'?", 10 !== '10');
```

Explanation:

- `==` checks value after converting types.
- `===` checks both value and type.
- `!=` checks loose inequality.
- `!==` checks strict inequality.

Output:

```text
10 == '10'? true
10 === '10'? false
10 != '10'? false
10 !== '10'? true
```

Important rule:

```text
Prefer === and !== in JavaScript.
They avoid many confusing type conversion bugs.
```

---

```javascript
console.log("null == undefined?", null == undefined);
console.log("null === undefined?", null === undefined);
```

Output:

```text
null == undefined? true
null === undefined? false
```

---

## 🔗 Section 4: Logical Operators

```javascript
let isAdult = true;
let hasID = false;

console.log("isAdult AND hasID?", isAdult && hasID);
console.log("isAdult OR hasID?", isAdult || hasID);
console.log("NOT isAdult?", !isAdult);
```

Explanation:

| Operator | Name | Meaning |
| :--- | :--- | :--- |
| `&&` | AND | Both conditions must be true. |
| `||` | OR | At least one condition must be true. |
| `!` | NOT | Flips the boolean value. |

Output:

```text
isAdult AND hasID? false
isAdult OR hasID? true
NOT isAdult? false
```

---

## 🔄 Section 5: Type Conversion

## String to Number

```javascript
let numStr = "42";
let num = Number(numStr);

console.log("numStr as number:", num);
console.log(typeof num);
```

Explanation:

- `Number()` converts a value into a number.
- `"42"` becomes `42`.

Output:

```text
numStr as number: 42
number
```

---

## Invalid Number Conversion

```javascript
let invalid = Number("Hello");
console.log("Invalid conversion:", invalid);
```

Explanation:

`"Hello"` cannot be converted into a number.

So JavaScript returns:

```text
NaN
```

`NaN` means:

```text
Not-a-Number
```

Output:

```text
Invalid conversion: NaN
```

---

## parseFloat() and parseInt()

```javascript
let priceString = "19.99";
let priceNumber = parseFloat(priceString);
let intVersion = parseInt(priceString);
```

Explanation:

- `parseFloat("19.99")` gives `19.99`.
- `parseInt("19.99")` gives `19`.

```text
parseInt() removes the decimal part.
```

---

## Number to String

```javascript
let value = 123;
let asString = String(value);

console.log("Number as string:", asString);
console.log(typeof asString);
```

Explanation:

- `String(value)` converts a number to a string.
- `123` becomes `"123"`.

Output:

```text
Number as string: 123
string
```

You can also use:

```javascript
value.toString();
```

---

## 🧮 Section 6: The Math Object

```javascript
console.log("PI:", Math.PI);
console.log("Round 4.7:", Math.round(4.7));
console.log("Floor 4.7:", Math.floor(4.7));
console.log("Ceil 4.1:", Math.ceil(4.1));
console.log("Absolute -5:", Math.abs(-5));
console.log("Random 0-1:", Math.random());
console.log("Random 1-10:", Math.floor(Math.random() * 10) + 1);
```

Explanation:

| Code | Meaning |
| :--- | :--- |
| `Math.PI` | Gives the value of PI. |
| `Math.round(4.7)` | Rounds to nearest integer. |
| `Math.floor(4.7)` | Rounds down. |
| `Math.ceil(4.1)` | Rounds up. |
| `Math.abs(-5)` | Converts negative value to positive. |
| `Math.random()` | Gives a random decimal from 0 up to less than 1. |
| `Math.floor(Math.random() * 10) + 1` | Random number from 1 to 10. |

Example output:

```text
PI: 3.141592653589793
Round 4.7: 5
Floor 4.7: 4
Ceil 4.1: 5
Absolute -5: 5
Random 0-1: 0.782341
Random 1-10: 7
```

---

## 🧪 Section 7: Combining Everything – Mini Quiz

```javascript
let userName = "Rahul";
let userScore = 85;
let bonus = 10;
let total = userScore + bonus;

let passed = total >= 60;
let message = `${userName} scored ${total} points. Passed? ${passed}`;
console.log(message);
```

Explanation:

This combines:

- Variables
- Arithmetic
- Comparison
- Boolean result
- Template literal
- Output

Output:

```text
Rahul scored 95 points. Passed? true
```

---

# 🔑 Chapter 2 Key Takeaways

| Concept / Syntax | Description |
| :--- | :--- |
| `Number` | One type for integers, decimals, and scientific notation. |
| `+` | Addition. |
| `-` | Subtraction. |
| `*` | Multiplication. |
| `/` | Division. |
| `%` | Modulo, gives remainder. |
| `**` | Exponentiation. |
| `()` | Controls operation order. |
| `==` | Loose equality, allows type conversion. |
| `===` | Strict equality, checks value and type. Preferred. |
| `!=` | Loose inequality. |
| `!==` | Strict inequality. Preferred. |
| `&&` | Logical AND. |
| `||` | Logical OR. |
| `!` | Logical NOT. |
| `Number()` | Converts to number. May return `NaN`. |
| `parseInt()` | Converts to integer. |
| `parseFloat()` | Converts to decimal number. |
| `String()` | Converts to string. |
| `.toString()` | Converts value to string. |
| `Math` | Built-in object for useful math operations. |

---

# 🚀 How to Run the Scripts

## 1. Install Node.js

Download and install Node.js.

After installing, check:

```bash
node -v
```

If Node.js is installed correctly, it will show a version number.

---

## 2. Save the files

Use these filenames:

```text
Study_JS_1.js
Study_JS_2.js
```

---

## 3. Open terminal in the folder

Navigate to the folder where your JavaScript files are saved.

---

## 4. Run Chapter 1

```bash
node Study_JS_1.js
```

---

## 5. Run Chapter 2

```bash
node Study_JS_2.js
```

---

## No Node.js?

You can paste the code into an online JavaScript compiler like OneCompiler and run it there.

---

# 🧪 Practice Tasks

## Chapter 1 Practice

Try these changes:

1. Change `studentName = "Priya"` to your own name.
2. Change `"Coding"` to `"JavaScript"` and check what `language[5]` prints.
3. Use `.indexOf("script")` on `"I love JavaScript"`.
4. Try `.includes("Python")`.
5. Try changing the `college` variable after declaring it with `const` and read the error message.

---

## Chapter 2 Practice

Try these changes:

1. Change `age` to `30` and check how all calculations update.
2. Compare `"10"` and `10` using both `==` and `===`.
3. Add this condition:

```javascript
console.log(age >= 18 && age <= 60);
```

4. Generate a random number between 1 and 100:

```javascript
console.log(Math.floor(Math.random() * 100) + 1);
```

5. Try converting these values using `Number()`:

```javascript
Number("50");
Number("50px");
Number("Hello");
Number("");
```

---

# 🧠 Final Summary

Chapter 1 teaches:

```text
Variables
Strings
Template literals
String methods
String indexing
Basic console output
```

Chapter 2 teaches:

```text
Numbers
Arithmetic
Operator precedence
Comparisons
Logical operators
Type conversion
Math object
```

Together, these two chapters give a strong beginner foundation for JavaScript.
