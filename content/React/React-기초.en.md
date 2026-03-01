+++
title = "React Basics"

weight = 7
sort_by = "weight"

[extra]
+++
## React

### Definition

- React is a JavaScript-based web development library for building user interfaces, serving as a tool that helps create apps by combining components.

### Features

1. Use of independent and reusable components

- Modularize the UI using independent and reusable components

2. Using VDOMs to Improve Efficiency

- To enhance efficiency, the concept of **VDOM**[^1] is used.

3. Using Parent Elements When Components Return Multiple Elements

- When a component returns multiple elements, they must be placed within a parent element. - **div** or similar elements can be used as the parent element. - Example code

~~~react function App(){ return( <div> <h1> Hello, World </h1> <p>First React-based Webpage</p> </div> ); } ~~~

**A more simplified version**

~~~react //프래그먼트 사용 function App{ return( <React.Fragment> <h1> Hello, World </h1> <p>First React-based Webpage</p> </React.Fragment> ); }


// More simplified fragment version function App {   return(     <>       <h1>Hello, World</h1>       <p>First React-based Webpage</p>     </>   ); }

- The above code is available starting from React version 16.2.

4. Component Composition Method

- When building components in React, there are two approaches: using classes and using functions.

  1. **Function Method**

     - When constructing functions, the return statement is essential as it determines how the component is rendered.

     - Example code

  ~~~react function App(){ return <h1> Hello, World </h1> } ~~~

  2. **Class-based Approach** - Requires a **render()** method when structured as a class - The render() method displays and updates the component's rendered output - Example code

  ~~~react class App extends React.Component{ render() } ~~~

  

<br/><br/><br/><br/><br/>

### Books Referenced

[Hands-On! Modern Web Application Development with Spring Boot and React](https://www.yes24.com/Product/Goods/119973506).

---







[^1]: Visual Document Object Model (Document Object Model)

