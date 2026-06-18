// ==============================================
// 📘 JavaScript Chapter 3 – Arrays & Objects
// ==============================================

console.log("📦 Chapter 3: Arrays & Objects\n");

// ==============================================
// SECTION 1: Arrays
// ==============================================

console.log("=== SECTION 1: Arrays ===\n");

// 1.1 Creating an array
let fruits = ["Apple", "Banana", "Mango"];
console.log("fruits:", fruits);

// 1.2 Accessing elements by index (zero-based)
console.log("First fruit:", fruits[0]);   // Apple
console.log("Second fruit:", fruits[1]);  // Banana
console.log("Last fruit:", fruits[2]);    // Mango

// 1.3 Array length
console.log("Number of fruits:", fruits.length); // 3

// 1.4 Modifying an element
fruits[1] = "Blueberry";
console.log("After changing index 1:", fruits); // ["Apple", "Blueberry", "Mango"]

// 1.5 Adding elements – push() (adds to end)
fruits.push("Orange");
console.log("After push('Orange'):", fruits); // ["Apple", "Blueberry", "Mango", "Orange"]

// 1.6 Removing the last element – pop()
let lastFruit = fruits.pop();
console.log("Removed:", lastFruit);        // Orange
console.log("After pop():", fruits);       // ["Apple", "Blueberry", "Mango"]

// 1.7 Finding elements – indexOf() and includes()
let index = fruits.indexOf("Blueberry");
console.log('Index of "Blueberry":', index); // 1

let hasMango = fruits.includes("Mango");
console.log('Includes "Mango"?', hasMango);   // true

let hasGrape = fruits.includes("Grape");
console.log('Includes "Grape"?', hasGrape);   // false

// 1.8 Arrays can hold mixed types
let mixed = ["Hello", 42, true, null];
console.log("Mixed array:", mixed);

// ==============================================
// SECTION 2: Objects
// ==============================================

console.log("\n=== SECTION 2: Objects ===\n");

// 2.1 Creating an object (using object literal)
let person = {
  firstName: "Riya",
  lastName: "Sharma",
  age: 28,
  isStudent: false
};

console.log("person object:", person);

// 2.2 Accessing properties – dot notation
console.log("First name (dot):", person.firstName);
console.log("Age (dot):", person.age);

// 2.3 Accessing properties – bracket notation (useful for dynamic keys)
console.log("Last name (bracket):", person["lastName"]);

// 2.4 Adding a new property
person.city = "Delhi";
console.log("After adding city:", person);

// 2.5 Updating an existing property
person.age = 29;
console.log("After updating age:", person);

// 2.6 Deleting a property
delete person.isStudent;
console.log("After deleting isStudent:", person);

// 2.7 Objects can hold any type, including arrays and other objects
let student = {
  name: "Amit",
  subjects: ["Math", "Science", "English"],
  address: {
    street: "123 Main St",
    city: "Mumbai"
  }
};

console.log("Student object:", student);
console.log("Subjects:", student.subjects);
console.log("Second subject:", student.subjects[1]); // Science
console.log("City from nested object:", student.address.city);

// ==============================================
// SECTION 3: Combining Arrays & Objects
// ==============================================

console.log("\n=== SECTION 3: Combining Arrays & Objects ===\n");

// 3.1 Array of objects
let users = [
  { id: 1, name: "Alice" },
  { id: 2, name: "Bob" },
  { id: 3, name: "Charlie" }
];

console.log("Users array:", users);
console.log("Second user's name:", users[1].name); // Bob

// 3.2 Object with arrays as values (already seen above)
let classroom = {
  className: "JavaScript 101",
  students: ["Priya", "Rahul", "Sneha"]
};

console.log("Classroom:", classroom);
console.log("Class name:", classroom.className);
console.log("Students list:", classroom.students);

// ==============================================
// SECTION 4: Quick Practice – Mini Exercise
// ==============================================

console.log("\n=== SECTION 4: Mini Exercise ===\n");

// Create a product object and an array of products
let product1 = { name: "Laptop", price: 75000, inStock: true };
let product2 = { name: "Mouse", price: 1500, inStock: false };
let product3 = { name: "Keyboard", price: 3000, inStock: true };

let products = [product1, product2, product3];

console.log("All products:", products);

// Calculate total value of in‑stock products
let totalValue = 0;
for (let i = 0; i < products.length; i++) {
  if (products[i].inStock) {
    totalValue += products[i].price;
  }
}
console.log("Total value of in‑stock products:", totalValue);

// ==============================================
console.log("\n✅ End of Chapter 3 program.");