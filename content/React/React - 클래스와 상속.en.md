+++
title = "React - Classes and Inheritance"
weight = 7
sort_by = "weight"
[extra]
+++
## Class

### Definition

- A template for creating objects, similar to classes in other object-oriented languages

### Features

- May contain fields, constructors, and class methods

### How to Use

- Declared using the **class** keyword - If a constructor is needed, it can be implemented using the **constructor** keyword - Example code

class Person {

}

// If a constructor is needed class Person {     constructor() { } } ~~~

<br>

### Inheritance

#### Definition

- The act of one object inheriting and using the properties or methods of another object

#### How to Use

- Use of the **extends** keyword

  - Used in the form 'class ChildClassName extends ParentClassName' - **Caution** - In the inherited class, the constructor must call the superclass constructor using the **super** keyword - Failure to call it with the super keyword will result in an error

- Example code

  ~~~react class Person{ constructor(firstName, lastName, age){ this.firstName = firstName; this.lastName = lastName; this.age = age; } }
  
  
  class Child extends Person{ constructor(firstName, lastName, age, hobby, favorite){ super(firstName, lastName, age); } } ~~~

  



---

**References**

[Practical! Modern Web Application Development with Spring Boot and React](https://www.yes24.com/Product/Goods/119973506).