+++
title = " React - Variables, Functions, Template Literals"
weight = 7
sort_by = "weight"
[extra]
+++
## Variables and Constants

### Constant

#### Definition 

- A variable whose value cannot be changed after it has been declared

#### Declaration Method

- **const** variableName = value - Example code

~~~react const CV = 1.23; ~~~

#### Features

- Values cannot be changed after declaration - **However**, if it is an object or array, its contents can be changed

### Variable

#### Definition

- A value whose value can be changed after it has been declared

#### Declaration Method

- **let** variable_name = value - Example code

~~~react let CV = 1.23; ~~~

### Common Features

- Has a block scope

  - Constants declared inside {} cannot be called outside the block - They can be accessed within sub-blocks

  react let varA = 10; if(varA > 10){ console.log(varA); }

<br>

## Function

 ### Declaration Method

#### 1. General Method

**function** functionName(variableName) {}

Example code

~~~react function Calc(x) { return x * 2; } ~~~

2. Arrow Functions

- Note: Available starting from ES6 - When there is only one parameter, parentheses can be omitted - If the function body is an expression, return is not required - If a function has no parameters, empty parentheses like () must be specified

- Declaration method: **VariableName = Parameters => Return Statement**

Example code

react // When there is one parameter let Calc = x => x * 2;

//When there are multiple parameters let Calc = (a, b) => {     return a * b; }

### How to Call

- **FunctionName(parameters);** - Note: When there are multiple parameters, place the arguments inside parentheses and **separate them with commas**.

Example code

react Calc(5) Calc(5,10);

<br>

## Template Literals

### Definition

- According to the MDM web docs, template literals are string literals that allow embedded expressions.

- The common method for concatenating strings in JavaScript is to use the **+** operator.

  - Example code

  ~~~react let name = {firstName : 'Minsu', lastName : 'Kim'}; let greeting = "Hello, " + ${name.firstName}+ ${name.lastName}; ~~~

- When using template literals, you can use **backticks (``)**.

  - Example code

  ~~~react let name = {firstName : 'Minsu', lastName : 'Kim'}; let greeting = `Hello, ${name.firstName} ${name.lastName}`; ~~~

  

---

**References**

[Component State](https://ko.legacy.reactjs.org/docs/faq-state.html) 

[Hands-On! Modern Web Application Development with Spring Boot and React](https://www.yes24.com/Product/Goods/119973506).

<br>

<br>

<br>

[^1]: A set of characters enclosed in double quotation marks (").

