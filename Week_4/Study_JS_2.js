// =============================================
// Study_JS_2.js – Numbers, Operators & Types
// Day 2 of JavaScript Learning
// =============================================

// ---------- Section 1: Numbers ----------
let age = 25;
let price = 99.99;
let bigNumber = 1e6;   // 1,000,000

let sum = age + 10;
let product = price * 2;
let quotient = age / 4;
let remainder = age % 3;
let power = age ** 2;

console.log("===== Numbers & Arithmetic =====");
console.log("Age:", age);
console.log("Price:", price);
console.log("Big Number:", bigNumber);
console.log("Sum:", sum);
console.log("Product:", product);
console.log("Quotient:", quotient);
console.log("Remainder (age % 3):", remainder);
console.log("Power (age ** 2):", power);

// ---------- Section 2: Operator Precedence ----------
console.log("\n===== Operator Precedence =====");
console.log("10 + 5 * 2 =", 10 + 5 * 2);        // 20
console.log("(10 + 5) * 2 =", (10 + 5) * 2);    // 30

// ---------- Section 3: Comparisons ----------
console.log("\n===== Comparisons =====");
let x = 10;
let y = 20;
console.log("x > y?", x > y);               // false
console.log("x < y?", x < y);               // true
console.log("x == 10?", x == 10);           // true
console.log("x != 10?", x != 10);           // false

console.log("\n--- Loose vs Strict ---");
console.log("10 == '10'?", 10 == '10');     // true
console.log("10 === '10'?", 10 === '10');   // false
console.log("10 != '10'?", 10 != '10');     // false
console.log("10 !== '10'?", 10 !== '10');   // true
console.log("null == undefined?", null == undefined);   // true
console.log("null === undefined?", null === undefined); // false

// ---------- Section 4: Logical Operators ----------
console.log("\n===== Logical Operators =====");
let isAdult = true;
let hasID = false;
console.log("isAdult AND hasID?", isAdult && hasID);   // false
console.log("isAdult OR hasID?", isAdult || hasID);    // true
console.log("NOT isAdult?", !isAdult);                 // false

// ---------- Section 5: Type Conversion ----------
console.log("\n===== Type Conversion =====");
let numStr = "42";
let num = Number(numStr);
console.log("Convert '42' to number:", num);
console.log("Type of num:", typeof num);

let invalid = Number("Hello");
console.log("Convert 'Hello' to number:", invalid);   // NaN

let priceString = "19.99";
let priceNumber = parseFloat(priceString);
let intVersion = parseInt(priceString);
console.log("parseFloat('19.99'):", priceNumber);
console.log("parseInt('19.99'):", intVersion);

let value = 123;
let asString = String(value);
console.log("Convert 123 to string:", asString);
console.log("Type of asString:", typeof asString);

// ---------- Section 6: Math Object ----------
console.log("\n===== Math Object =====");
console.log("PI:", Math.PI);
console.log("Round 4.7:", Math.round(4.7));
console.log("Floor 4.7:", Math.floor(4.7));
console.log("Ceil 4.1:", Math.ceil(4.1));
console.log("Absolute -5:", Math.abs(-5));
console.log("Random 0-1:", Math.random());
console.log("Random 1-10:", Math.floor(Math.random() * 10) + 1);

// ---------- Section 7: Mini Quiz ----------
console.log("\n===== Mini Quiz =====");
let userName = "Rahul";
let userScore = 85;
let bonus = 10;
let total = userScore + bonus;
let passed = total >= 60;
let message = `${userName} scored ${total} points. Passed? ${passed}`;
console.log(message);

console.log("\n✅ End of Chapter 2 program.");
