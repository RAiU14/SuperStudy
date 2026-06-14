// ============================================
// JavaScript Chapter 1: Variables & Strings
// A simple program for beginners
// ============================================

// ----- 1. DECLARING VARIABLES -----
let studentName = "Priya";
const college = "ABC University";

// ----- 2. WORKING WITH STRINGS -----
let greeting = "Hello, " + studentName + "!";
console.log(greeting);

let message = `Welcome to ${college}, ${studentName}.`;
console.log(message);

let text = "JavaScript";
console.log("Length of 'JavaScript' is: " + text.length);

let mixed = "HeLlO WoRlD";
console.log(mixed.toUpperCase());
console.log(mixed.toLowerCase());

let language = "Coding";
console.log("First character: " + language[0]);
console.log("Last character: " + language[5]);

let sentence = "I love JavaScript";
console.log(sentence.includes("Java"));
console.log(sentence.indexOf("love"));

// ----- 3. CHANGING VARIABLES -----
let score = 10;
score = 15;
console.log("Updated score: " + score);

// ----- 4. SIMPLE OUTPUT -----
let userName = "Sam";
let userCity = "Mumbai";
let intro = `Hi, I'm ${userName} from ${userCity}.`;
console.log(intro);

console.log("\n✅ End of Chapter 1 program.");