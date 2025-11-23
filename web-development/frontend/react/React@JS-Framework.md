# React@JS-Framework

## Summary

React is a JavaScript Framework for building user interfaces. React is used to build single page applications. browser DOM(I.e thereby changing only what needs to be changed). virtual DOM object is a representation of a DOM object, like a lightweight copy.

## Table of Contents

  - [//React@JS-Framework//](#reactjs-framework)
  - [React allows us to building & create reusable UI components. Instead of](#react-allows-us-to-building-create-reusable-ui-components-instead-of)
  - [manipulating the browser's DOM directly, React creates a virtual DOM in memory,](#manipulating-the-browsers-dom-directly-react-creates-a-virtual-dom-in-memory)
  - [where it does all the necessary manipulating, before making the changes in the](#where-it-does-all-the-necessary-manipulating-before-making-the-changes-in-the)
  - [detached from the browser-speciﬁc implementation details. Since the DOM itself](#detached-from-the-browser-speciﬁc-implementation-details-since-the-dom-itself)
  - [was already an abstraction, the virtual DOM is, in fact, an abstraction of an](#was-already-an-abstraction-the-virtual-dom-is-in-fact-an-abstraction-of-an)
  - [abstraction. Think of the virtual DOM as React’s local and simpliﬁed copy of the](#abstraction-think-of-the-virtual-dom-as-reacts-local-and-simpliﬁed-copy-of-the)
  - [HTML DOM. It allows React to do its computations within this abstract world In](#html-dom-it-allows-react-to-do-its-computations-within-this-abstract-world-in)
  - [React, for every DOM object, there is a corresponding “virtual DOM object.” A](#react-for-every-dom-object-there-is-a-corresponding-virtual-dom-object-a)
  - [Manipulating the DOM is slow. Manipulating the virtual DOM is much faster,](#manipulating-the-dom-is-slow-manipulating-the-virtual-dom-is-much-faster)
  - [because nothing gets drawn onscreen. Think of manipulating the virtual DOM as](#because-nothing-gets-drawn-onscreen-think-of-manipulating-the-virtual-dom-as)
  - [editing a blueprint, as opposed to moving rooms in an actual house. When you](#editing-a-blueprint-as-opposed-to-moving-rooms-in-an-actual-house-when-you)
  - [JSX- Dynamic Markup](#jsx-dynamic-markup)
  - [Performance & Testing—————](#performance-testing)
  - [Installation Ref(https://github.com/facebook/create-react-app)](#installation-refhttpsgithubcomfacebookcreate-react-app)
  - [npm run build](#npm-run-build)
  - [npm run eject](#npm-run-eject)
  - [Removes this tool and copies build dependencies, conﬁguration](#removes-this-tool-and-copies-build-dependencies-conﬁguration)
  - [it, we use the keyword class, and the properties are assigned inside a](#it-we-use-the-keyword-class-and-the-properties-are-assigned-inside-a)
  - [keyword, and import the Parent class variables using the super()](#keyword-and-import-the-parent-class-variables-using-the-super)
  - [Arrow Functions](#arrow-functions)
  - [regular functions the this keyword represented the object that called the](#regular-functions-the-this-keyword-represented-the-object-that-called-the)
  - [Variables (let, const, var)](#variables-let-const-var)
  - [Block Scope {} involves block of code for conditional & loop statements/](#block-scope-involves-block-of-code-for-conditional-loop-statements)
  - [Var has function scope, not block scope. However to combat that, the let has](#var-has-function-scope-not-block-scope-however-to-combat-that-the-let-has)
  - [JSX stands for JavaScript Syntax Extension](#jsx-stands-for-javascript-syntax-extension)
  - [JSX Element](#jsx-element)
  - [ReactElements lives in the virtual DOM. They make the basic nodes here. Their](#reactelements-lives-in-the-virtual-dom-they-make-the-basic-nodes-here-their)
  - [Once deﬁned, ReactElements can be rendered into the “real” DOM. This is the](#once-deﬁned-reactelements-can-be-rendered-into-the-real-dom-this-is-the)
  - [you would ﬁnd it in a JavaScript ﬁle, instead of in an HTML ﬁle. JSX elements](#you-would-ﬁnd-it-in-a-javascript-ﬁle-instead-of-in-an-html-ﬁle-jsx-elements)
  - [are treated as JavaScript expressions. They can go anywhere that JavaScript](#are-treated-as-javascript-expressions-they-can-go-anywhere-that-javascript)
  - [expressions can go. That means that a JSX element can be saved in a variable,](#expressions-can-go-that-means-that-a-jsx-element-can-be-saved-in-a-variable)
  - [JSX Elements are what components are “made of”, Elements are the smallest](#jsx-elements-are-what-components-are-made-of-elements-are-the-smallest)
  - [building blocks of React apps. An element describes what you want to see on the](#building-blocks-of-react-apps-an-element-describes-what-you-want-to-see-on-the)
  - [screen. React elements are immutable. Once you create an element, you can’t](#screen-react-elements-are-immutable-once-you-create-an-element-you-cant)
  - [Rules & Use of JSX elements](#rules-use-of-jsx-elements)
  - [JSX allows us to write HTML elements in JavaScript and place them in the](#jsx-allows-us-to-write-html-elements-in-javascript-and-place-them-in-the)
  - [To add extra expressions into JSX elements use curly braces { }. You can put](#to-add-extra-expressions-into-jsx-elements-use-curly-braces-you-can-put)
  - [any valid JavaScript expression inside the curly braces in JSX. This is regular](#any-valid-javascript-expression-inside-the-curly-braces-in-jsx-this-is-regular)
  - [JSX, not as regular JavaScript! The curly braces themselves won’t be treated as](#jsx-not-as-regular-javascript-the-curly-braces-themselves-wont-be-treated-as)
  - [JSX nor as JavaScript. They are markers that signal the beginning and end of a](#jsx-nor-as-javascript-they-are-markers-that-signal-the-beginning-and-end-of-a)
  - [When you inject JavaScript into JSX, that JavaScript is part of the same](#when-you-inject-javascript-into-jsx-that-javascript-is-part-of-the-same)
  - [Nested JSX](#nested-jsx)
  - [To insert large block of HTML such as <ul>, <table> & <form> which use multi-](#to-insert-large-block-of-html-such-as-ul-table-form-which-use-multi)
  - [lines, put the HTML inside parenthesis ( )](#lines-put-the-html-inside-parenthesis)
  - [JSX expression must have exactly one outermost element / must be wrapped](#jsx-expression-must-have-exactly-one-outermost-element-must-be-wrapped)
  - [*Self-closing tags](#self-closing-tags)
  - [Close empty elements with /> *In JSX, you have to include](#close-empty-elements-with-in-jsx-you-have-to-include)
  - [*Non-self-closing tags](#non-self-closing-tags)
  - [JSX Element Attributes](#jsx-element-attributes)

---

## Content

### //React@JS-Framework//

React is a JavaScript Framework for building user interfaces. React is used to build single page applications.
### React allows us to building & create reusable UI components. Instead of

### manipulating the browser's DOM directly, React creates a virtual DOM in memory,

### where it does all the necessary manipulating, before making the changes in the

browser DOM(I.e thereby changing only what needs to be changed).
### The Virtual DOM is an abstraction of the HTML DOM. It is lightweight and

### detached from the browser-speciﬁc implementation details. Since the DOM itself

### was already an abstraction, the virtual DOM is, in fact, an abstraction of an

### abstraction. Think of the virtual DOM as React’s local and simpliﬁed copy of the

### HTML DOM. It allows React to do its computations within this abstract world In

### React, for every DOM object, there is a corresponding “virtual DOM object.” A

virtual DOM object is a representation of a DOM object, like a lightweight copy.
### A virtual DOM object has the same properties as a real DOM object, but it lacks

the real thing’s power to directly change what’s on the screen.
### Manipulating the DOM is slow. Manipulating the virtual DOM is much faster,

### because nothing gets drawn onscreen. Think of manipulating the virtual DOM as

### editing a blueprint, as opposed to moving rooms in an actual house. When you

render a JSX element, every single virtual DOM object gets updated. In summary, here’s what happens when you try to update the DOM in React: The entire virtual DOM gets updated. The virtual DOM gets compared to what it looked like before you updated it. React figures out which objects have changed. The changed objects, and the changed objects only, get updated on the real DOM through render() method. Changes on the real DOM cause the screen to change. Tip: In DOM model, HTML element tags are objects with properties ——————Why would you use React? Structure the “view” layer of your application Reusable components with their own state
### JSX- Dynamic Markup

Interactive User-Interface with Virtual DOM
### Performance & Testing—————

To use React in production, you need NPM and Node.js
### Installation Ref(https://github.com/facebook/create-react-app)

Run on terminal npx create-react-app name_0f_App npm start Starts the development server.
### npm run build

Bundles the app into static files for production. npm test Starts the test runner.
### npm run eject

### Removes this tool and copies build dependencies, conﬁguration

files and scripts into the app directory. If you do this, you can’t go back! We suggest that you begin by typing. cd my-first-react-app npm start Happy hacking! *************************************************************************** *************************************************************************** ********* React uses ES6, and you should be familiar with some of the new features like: Classes A class is a type of function, but instead of using the keyword function to initiate
### it, we use the keyword class, and the properties are assigned inside a

constructor() method. To create a class with class inheritance use the extends
### keyword, and import the Parent class variables using the super()

keyword….Parent class methods are inherited automatically.
### Arrow Functions

### The handling of this keyword is also different in arrow functions compared to

regular functions. In short, with arrow functions there are no binding of this. In
### regular functions the this keyword represented the object that called the

function, which could be the window, the document, a button or whatever. With arrow functions, the this keyword always represents the object that defined the arrow function.
### Variables (let, const, var)

### Block Scope {} involves block of code for conditional & loop statements/

expressions, Function scope(inside of a function declaration/expression), global scope.
### Var has function scope, not block scope. However to combat that, the let has

block scope. Const has block scope but should never be altered. *************************************************************************** *************************************************************************** *********
### JSX stands for JavaScript Syntax Extension

JSX is an extension of the JavaScript language based on ES6, and is translated
into regular JavaScript at runtime. JSX makes it easier to write and add HTML in React.
### JSX Element

### A basic unit of JSX is called a JSX Element or ReactElement is a

light, stateless, immutable, virtual representation of a DOM Element.
### ReactElements lives in the virtual DOM. They make the basic nodes here. Their

immutability makes them easy and fast to compare and update.
### Once deﬁned, ReactElements can be rendered into the “real” DOM. This is the

moment when React ceases to control the elements. They become slow, boring DOM nodes
### An example of a JSX element:<h1>Hello world</h1>

### This JSX element looks exactly like HTML! The only noticeable difference is that

### you would ﬁnd it in a JavaScript ﬁle, instead of in an HTML ﬁle. JSX elements

### are treated as JavaScript expressions. They can go anywhere that JavaScript

### expressions can go. That means that a JSX element can be saved in a variable,

passed to a function, stored in an object or array…you name it.
### JSX Elements are what components are “made of”, Elements are the smallest

### building blocks of React apps. An element describes what you want to see on the

### screen. React elements are immutable. Once you create an element, you can’t

change its state, props/attributes, children. An element is like a single frame in a movie: it represents the UI at a certain point in time.
### Rules & Use of JSX elements

### JSX allows us to write HTML elements in JavaScript and place them in the

DOM. JSX converts HTML <tags> into react JSX elements.
### To add extra expressions into JSX elements use curly braces { }. You can put

### any valid JavaScript expression inside the curly braces in JSX. This is regular

JavaScript, written inside of a JSX expression, written inside of a JavaScript file.
### This way Any {line of code} in between the tags of a JSX element will be read as

### JSX, not as regular JavaScript! The curly braces themselves won’t be treated as

### JSX nor as JavaScript. They are markers that signal the beginning and end of a

JavaScript injection into JSX, similar to the quotation marks that signal the boundaries of a string.
### When you inject JavaScript into JSX, that JavaScript is part of the same

environment as the rest of the JavaScript in your file. That means that JSX expression can access variables, even if those variables were declared on the outside.
### Nested JSX

You can nest JSX elements inside of other JSX elements, just
like in HTML. If a JSX expression takes up more than one line, then you must wrap the multi- line JSX expression in parentheses (). Nested JSX expressions can be saved as variables, passed to functions, etc., just like non-nested JSX expressions can!
### To insert large block of HTML such as <ul>, <table> & <form> which use multi-

### lines, put the HTML inside parenthesis ( )

### JSX expression must have exactly one outermost element / must be wrapped

in ONE top level element. Likely a <div> tag as container, If you notice that a JSX expression has multiple outer elements, the solution is usually simple: wrap the JSX expression in a <div></div>. Elements Must be Closed, JSX follows HTML rules, and therefore JSX elements must be properly closed.
### *Self-closing tags

### Close empty elements with /> *In JSX, you have to include

the slash. If you write a self-closing tag in JSX and forget the slash, you will raise an error.
### *Non-self-closing tags

### The ﬁrst opening tag and the ﬁnal closing tag of a JSX

expression must belong to the same JSX element!
### JSX Element Attributes

JSX elements can have attributes, just like HTML elements can. A JSX attribute is written using HTML-like syntax: a name, followed by an equals sign, followed by a value. The value should be wrapped in quotes, like this, A single JSX element can have many attributes, just like in HTML. Syntax
### attribute-name="attribute-value"

const panda = <img src='images/panda.jpg' alt='panda' width='500px'
### height='500px' />;

### const title = <h1 id='title'>Introduction to React.js: Part I</h1>;

### Replace class attribute name to className - This is because JSX gets

translated into JavaScript, and class is a reserved word in JavaScript. When JSX is rendered, JSX className attributes are automatically rendered as class attributes. When writing JSX, it’s common to use variables to set attributes. let sideLength = "200px"; const panda = ( <img src="images/panda.jpg" alt="panda"
height={sideLength} width={sideLength} /> Object properties are also often used to set attributes: const pics = { panda: "http://bit.ly/1Tqltv5", owl: "http://bit.ly/1XGtkM3", owlCat: "http://bit.ly/1Upbczi" const panda = ( <img src={pics.panda} alt="Lazy Panda" /> JSX Conditionals: If Statements Don't Work if inside JSX expr. const order = ( <h1> if (purchase.complete) { 'Thank you for placing an order!' </h1>
### One way to

bypass this is Putting if statement outside the JSX tags, therefore because the words if and else are not injected in between JSX tags. The if statement is on the outside, and no JavaScript injection is necessary. render() { let message; if (user.age >= drinkingAge) { message = <div>Hey, check out this alcoholic beverage!</div> } else { message = <div>Hey, check out this alcoholic beverage!</div> }. return message }
### Use of ternary

operator(condition ? X : Y) The ternary operator works the same way in React as it does in regular JavaScript. However, it shows up in React surprisingly often. render() { return <h1> { age >= drinkingAge ? 'Buy Drink' : 'Do Teen Stuff' } </h1> } or render() { return age >= drinkingAge ? <h1>Buy drink</ h1> :<h1>Do Teen Stuff</h1> }
### Short-Circuit

Operator(&&)
one final way of writing conditionals in React: the && operator. Like the ternary operator, && is not React- specific, but it shows up in React surprisingly often. && works best in conditionals that will sometimes do an action, but other times do nothing at all. const tasty = ( <ul> <li>Applesauce</li> { !baby && <li>Pizza</li> } { age > 15 && <li>Brussels Sprouts</ li> } { age > 20 && <li>Oysters</li> } { age > 25 && <li>Grappa</li> } </ul> If the expression on the leftside of ampersand && evaluates as true,
then the JSX on the right of the && will be rendered. If the first expression is false, however, then the JSX to the right of the && will be ignored and not rendered.
### .map & Keys in JSX

The array method .map() comes up often in React. It’s good to get in the habit of using it alongside JSX. If you want to create a list of JSX elements, then .map() is often your best bet.
### const strings = ['Home', 'Shop', 'About Me'];

const listItems = strings.map( (string, index) => <li key={index}> {string} </li>);
### <ul>{listItems}</ul>

### When using the map() method to return a list of items, it’s imperative to

### include keys: A key acts as a unique JSX attribute(analogous to HTML id

### attribute). If you don’t use keys when you’re supposed to, React might

accidentally scramble your list-items into the wrong order. If for some reason the
### values in the arrays don’t have a unique key you can generate using the second

### parameter of the .map(value, index) method…This should only be considered if

### your items in your list don’t have a unique id, your list is static & doesn’t

change(reordered/filtered) after rendering.
### Rendering Elements

### ReactDOM.render() is the most common way to render JSX. It takes a JSX

### expression, creates a corresponding tree of DOM nodes, and adds that tree to

the DOM. That is the way to make a JSX expression appear onscreen.
### This is the ﬁrst argument <h1>Hello world</h1> being passed to

### ReactDOM.render(). ReactDOM.render()‘s ﬁrst argument should be a JSX

### expression, and it will be rendered to the screen. The ﬁrst argument is appended

### to whatever element is selected by the second argument. That second argument

acted as a container for ReactDOM.render()‘s first argument! ReactDOM.render(<h1>Hello world</h1>, document.getElementById(‘root’));
### ReactDOM.render(<h1>Hello world</h1>, document.getElementById(‘div’));

ReactDOM.render()‘s first argument should evaluate to a JSX expression, it doesn’t have to literally be a JSX expression. The first argument could also be a variable, so long as that variable evaluates to a JSX expression.
### .getElementsByTag()/.getElementsByClass()/.querySelector()/

querySelectorAll()…..cause they select multiple elements, and return either collection or node lists.
### The majority of React programmers do use JSX, but you should understand

that it is possible to write React code without it. The following JSX expression: const h1 = <h1>Hello world</h1>; can be rewritten without JSX, like this: const h1 = React.createElement( "h1", //element tag
### null/ {} //props or attributes

"Hello, world" //children-content == innerHTML-textContent
### The null It is reserved for passing in attribute/props values, if there are no

attributes to pass in then you use ‘null’ instead.
### When a JSX element is compiled, the compiler transforms the JSX element into

### the method that you see above:React.createElement(). Every JSX element is

secretly a call to React.createElement().
### import React from 'react’;

### This imports an object named React from the

React Library which contains methods(I.e React.createElement()…etc) necessary to create HTML/JSX from components. import ReactDOM from 'react-dom';
### The methods imported from 'react-dom'

are meant for interacting with the DOM. You are already familiar with one of them: ReactDOM.render().
### The methods imported from 'react' don’t deal with the DOM at all, rather the

Virtual DOM, They don’t engage directly with anything that isn’t part of React. ReactDOM.render() is deprecated from React 17.0. Currently use
### ReactDOM.createRoot()

ReactDOM.createRoot(document.getElementById('root')).render(<h1>Hello,
### world!</h1>);

***************************************************************************
***************************************************************************
*********
### React Components

### What’s a component? React applications are made out of components. A component

### is a small, reusable chunk of code that is responsible for one job. That job is

### often to render some HTML. Components let you split the UI into independent,

reusable pieces/bots of code, and think about each piece in isolation. Components come in two types, StateFul-Class components & Stateless-Function components.
### Anatomy of a StateFul-Class components

### class YourComponentName extends React.Component{}

### All class components will have some methods and properties in common. Rather

### than rewriting those same properties over and over again every time, we extend

### the Component class from the React library. This way, we can use code that we

### import from the React library, without having to write it over and over again

### ourselves. React.Component is a JavaScript class. To create your own component

class, you must subclass React.Component. Declaring a new component class, is like a factory for building React components.
### You know that React.Component is a class, which you must subclass in order to

### create a component class of your own. You also know that React.Component is a

### property on the object which was returned by import React from 'react'

Note: Always start component names with a capital letter.
### body of your component class

### the pair of curly braces after React.Component,

and all of the code between those curly braces. Like all JavaScript classes, this one needs a body. The body will act as a set of
### instructions, explaining to your component class how it should build a React

component. It builds these components by consulting a set of instructions, which you must provide. The instructions should be written in typical JavaScript ES2015 class syntax.
### There is only one property that you must to include in your instructions: A

render() {} method is a property whose name is render, and whose value is a
### function. The term “render method” can refer to the entire property, or to just

the function part. A render method must contain a return statement. Usually, this
### return statement returns a JSX expression. A render() function can also be a ﬁne

place to put simple calculations/logic/…etc that need to happen right before a
component renders.
### A multi-line JSX expression should always be wrapped in parentheses! If we

have multiple instructions inside our return statement, it should be wrapped in parentheses().
### <YourComponentName />

### JSX elements can be either HTML-like, or component instances. JSX uses

### capitalization to distinguish between the two! That is the React-speciﬁc reason

### why component class names must begin with capital letters. In a JSX element,

that capitalized first letter says, “I will be a component instance and not an HTML tag.”
### this.props.children

this.props.children would return everything in between <MyComponentClass> and </MyComponentClass>.
### Every component’s props object has a property named children. So far, all of the

### components that you’ve seen have been self-closing tags, such as

### <MyComponentClass />. They don’t have to be! You could write

<MyComponentClass></MyComponentClass>, and it would still work.
### If a component has more than one child between its JSX tags, then

this.props.children will return those children in an array. import React from 'react';
### import ReactDOM from 'react-dom';

### class YourComponentName extends React.Component {

### // everything in between these curly-braces is instructions for how to

build components change states & work with props render() { return <h1>Hello world</h1>;
### <YourComponentName />;

ReactDOM.render(<YourComponentName />, document.getElementById('app'));
## Components Render Other Components

### A React application can contain dozens, or even hundreds, of components. Each

### component might be small and relatively unremarkable on its own. When

### combined, however, they can form enormous, fantastically complex ecosystems of

### information. In other words, React apps are made out of components, but what

makes React special isn’t components themselves. What makes React special is the ways in which components interact.
Render() methods can also return another kind of JSX:component instances. import React from 'react'; import ReactDOM from 'react-dom'; import NavBar from './NavBar.js'; class ProfilePage extends React.Component { render() { return ( <div> <NavBar /> <h1>All About Me!</h1> <p>I like movies and blah blah blah blah blah</p> <img src="https:// content.codecademy .com/courses/React/ react_photo- monkeyselfie.jpg" /> </div> ReactDOM.render(< ProfilePage />, document.getElemen tById('app')); import React from 'react'; export class NavBar extends React.Component { render() { const pages = ['home', 'blog', 'pics', 'bio', 'art', 'shop', 'about', 'contact']; const navLinks = pages.map(page => return ( <a href={'/' + page}> {page} </a> }); return <nav>{navLinks}</ nav>; import React from 'react'; import ReactDOM from 'react-dom'; class Greeting extends React.Component { render() { return <h1>Hi there, {this.props.firstNam e}!</h1>; ReactDOM.render( <Greeting firstName='Jennifer' />, document.getElemen tById('app')
### React Props of a Class Component

### A component’s props is an object. It holds information about that component

### attribute. The props object can gets passed from one component to another

### (component-2-component interaction). However if both components are on separate

files remember to use import & export. To Access/see a component’s props object, you use the expression this.props. Props are Analogous to function parameters/arguments and there are immutable.
### To render props object passed into another component Include

this.props.propertyName in the receiving component render method’s/ return statement.
### props is the name of the object that stores passed-in information. this.props

### refers to that storage object. props could refer to two pieces of passed-in

information, or it could refer to the object that stores those pieces of information.
### Pass `props` to a Component, <MyComponent foo="bar" />

If you want to pass information that isn’t a string, then wrap that information in
### curly braces. <Greeting myInfo={["top", "secret", "lol"]} />

Pass several pieces of information to <Greeting />. The values that aren’t strings are wrapped in curly braces.
### <Greeting name="Frarthur" town="Flundon" age={2} haunted={false} />

You can do more with props than just display them. You can also use props to make decisions. Default Props Properties
### // Set defaultProps equal to an object:

Component.defaultProps = {}; and then include key-values inside.
### Use an Event Handler in a Component

### In React, you deﬁne event handlers as methods on a component class. Notice that

the component class has two methods: .myFunc() and .render().
### However .myFunc() is being used as an event handler. .myFunc() will be called

any time that a user hovers over the rendered <div></div> in the DOM. class MyClass extends React.Component { myFunc() { alert('Stop it. Stop hovering.'); render() { return ( <div onHover={this.myFunc}> </div> ); } }
### You can, and often will, pass event handlers as props. You deﬁne an event

handler as a method on the component class, just like the render() method.
### When you pass an event handler as a prop in a component, Naming Convention to

take into consideration is as such(If you are listening for a “click” event, then you
### name your event handler handleClick or onClick.)

### React Events(https://reactjs.org/docs/events.html#supported-events)

### React has the same events as HTML: click, change, mouseover etc. JSX elements

### can have event listeners, just like HTML elements can. Programming in React

means constantly working with event listeners / performing actions based on user events on Component states.
### Adding Events

### Note that in HTML, event listener names are written in all lowercase, such as

onclick or onmouseover. In JSX, event listener names are written in camelCase, such as onClick or onMouseOver. React event handlers are written inside curly braces since they are functions which are javascript expressions. Example
### this for class components

### <button onClick={handleClick}>Take the Shot!</button>

<button onClick={this.handleClick}>Take the Shot!</button>
### React State of a Class Component

State are Analogous to variables declared within a function body. React components will often need dynamic information(information that can change.) in order to render. There are two ways for a component to get dynamic information: props and state.
### State allows React components to change their output over time in response to

### user actions, network responses, and anything else, without violating the strict

rule. React components has a built-in state & prop object. Their state which is an
### object that determines how the components renders and behaves. The state

### object is where you store property-values that belongs to the component. A

React component can access dynamic information in two ways: props and state.
### Unlike props, a component’s state is not passed in from the outside. A component

### decides its own state(privately & internally). This property should be declared

### inside of a constructor method, like this:

This object represents the initial “state” of any component instance class MyClass extends React.Component { constructor(props) {
super(props); this.state = { key: ‘value’ }; render() { return (
<h1>
I'm feeling {this.state.key}!
</h1>
constructor() method is called to declare state object & initialize object properties, Just like regular ES6 the super() method refers to the parent class.
### By calling the super() method in the constructor method, we call the parent's

### constructor method and gets access(inherit) to the parent’s(React.Component)

properties and methods. To read/access a component’s state, use the expression
### this.state.propertyKey

### A component changes its state by calling the function this.setState(), which

### takes two arguments: an object that will update the component’s state, and a

*callback. You basically never need the callback. this.setState() takes an object,
### and merges that object with the component’s current state. If there are

properties in the current state that aren’t part of that new object, then those properties remain how they were.
### Never update the state

### this.setState() in a render() method because it will

### cause an inﬁnite loop. Here’s why: Any time that you call this.setState(), it

AUTOMATICALLY calls .render() as soon as the state has changed.
### .bind(this)

### When you write a component class method(albeit an event

### handler) that updates the component state, you need to bind that method inside

### of your constructor function!this must be bound so that those methods correctly

update the component state during rendering. Ways to bind this.
### We can either bind (this) in the constructor method like this

### Syntax this.methodName = this.methodName.bind(this)

This way is the best, it bind once & for all…the other ways bind every time the component renders. We can bind it directly in the render method where {this.methodName} becomes {this.methodName.bind(this)}
We can bind it using arrow functions either in render return statement or the
### method expression. methodName = () => {}

### "Using arrow functions with object literals: If you are returning an object

### literal, it needs to be wrapped in parentheses(). This forces the interpreter to

evaluate what is inside the parentheses, and the object literal is returned Example: x => ({ y: x })
### Lifecycle of  Class <Components/>

### React components have several methods, called lifecycle methods, that are called

### at different parts of a component’s lifecycle. This is how you, the programmer,

### deal with the lifecycle of a component. Each component in React has a lifecycle

which you can monitor and manipulate during its three main phases. The render() method is required and will always be called, the others are optional and will be called if you define them.
### (Remember: the constructor is the ﬁrst thing called during mounting. render() is

### called later, to show the component for the ﬁrst time. If it happened in a

different order, render() wouldn’t have access to this.state, and it wouldn’t work.) Mounting means putting elements into the DOM. React has built-in methods that gets called, in this order, when mounting a
### component:

### The constructor()-use to declare state object

render()-use to render React Components in Virtual DOM
### componentDidMount()-is the ﬁnal method called during the mounting phase,

it’s called after the component is rendered. This is where we include side effects i.e this.setState() to our component.
### Components can have lots of other side-effects: loading external data with AJAX,

doing manual tweaking of the DOM, setting a global value, setInterval() and more. In general, when a component produces a side-effect, you should remember to clean it up. Updating The next phase in the lifecycle is when a component is updated.
### A component is updated whenever there is a change in the component's state or

props. React has built-in methods that gets called, when a component is updated, but only two are commonly used. render()-The first is render(), which we’ve seen in every React component. When a component’s props or state changes, render() is called.
### componentDidUpdate()-The second, Just like componentDidMount() is a good

place for mount-phase/side-effects setup, componentDidUpdate() is a good place
for update-phase work.
### Unmounting

### The next phase in the lifecycle is when a component is removed from the DOM,

React has only one built-in method that gets called when a component is
### unmounted:

### componentWillUnmount()- is called in the unmounting phase, right before the

component is completely destroyed. It’s a useful time to clean up any of your component’s mess/side-effects Example import React from 'react'; class Clock extends React.Component { constructor(props) { super(props); this.state = { date: new Date() }; render() { return <div>{this.state.date.toLocaleTimeString()}</div>; componentDidMount() { const oneSecond = 1000; this.intervalID = setInterval( () => { this.setState({ date: new Date() }); }, oneSecond); componentWillUnmount() { clearInterval(this.intervalID); (https://reactjs.org/docs/state-and-lifecycle.html)
### Classes, however, are not simple. They:are difﬁcult to reuse between

### components, are tricky and time-consuming to test

have confused many developers and caused lots of bugs Error Handling Phase Methods: Static getDerivedStateFromError(error) -
### componentDidCatch(error, info) -

### This error methods are called When there is an error either during rendering, in

a lifecycle method, or in the constructor of any child component.
### Stateless Functional Components

### A stateless functional component can be seen just as a function which returns

### JSX(HTML) based on the prop values(information) that are passed to it. It is not

### a class and does not extends the React.Component class.  We call such

components “function components” because they are literally JavaScript functions. No render & constructor methods. const Welcome = (props) => { return <h1>Hello, {props.name}</h1>; function Welcome(props) { return <h1>Hello, {props.name}</h1>;
### This function is a valid React component because it accepts a single “props”

### (which stands for properties) object argument(Expect it to be a JavaScript

### object) with data/information and returns a React element.To access these props,

give your function component a parameter named props. Within the function body,
you can access the props using this pattern: props.propertyName. You don’t need to use the this keyword.
### React Hooks

### React Hooks, plainly put, are functions that let us manage the internal state of

### Functional Stateless components without the need to convert them to Class

### StateFul components and handle post-rendering side effects directly from our

### function components. Hooks don’t work inside classes — they let us use fancy

React features without classes. Note: If you’re familiar with lifecycle methods of class components, you could say that Hooks let us “hook into” state and lifecycle features directly from our function components. React library offers a number of built-in Hooks. (https://reactjs.org/docs/hooks-
### reference.html)

### There are two main rules to keep in mind when using Hooks:

only call Hooks at the top level, never call hooks inside of loops, conditions, or nested functions.
### Hooks can only be used in React Functions. We cannot use Hooks in class

components and we cannot use Hooks in regular JavaScript functions. Basic Hooks useState(), useEffect(), useContext()
### Additional Hooks

### useReducer(), useCallback(), useMemo(), useRef()

### useImperativeHandle(), useLayoutEffect(), useDebugValue()

first & foremost import the hook from the react library with syntax import React, { useX() } from 'react';
### useState()

is a javascript functions defined in the React library.
### When called, it returns an array with two values…

### current state - reference the current value of state

### state setter - references a function that we can use to update/change the

value of this current state, it’s argument is an initial state value to initialize the value of state for the component’s first render or a callback function that changes the value of current state. Since React returns this two values as an array, We can assign this values to local
### variables using array destructuring. Calling the state setter signals to React

### that the component needs to re-render, so the whole function deﬁning the

component is called again. The magic of useState() is that it allows React to keep track of the current value of state from one render to the next! We can use state Hook to manage the value of any primitive data type and even data collections like arrays and objects! To initialize our state with any value we want, we simply pass the initial value as an argument to the useState() function call. During the first render, the initial
state argument is used. When the state setter is called, React ignores the initial state argument and uses
### the new value. When the component re-renders for any other reason, React

continues to use the same value from the previous render.
### const [current-state, stateSetter] = useState(refCurrentState);

Use the spread syntax on collections of dynamic data to copy the previous state into the next state like so: setArrayState((prev) => [ ...prev ]) setObjectState((prev) => ({ ...prev }))
### useEffect()

### Most interesting components will re-render multiple times

### throughout their lifetime and these key moments present the perfect opportunity

to execute these “side effects”. we use Effect Hooks to run some JavaScript code
### after each render, such as:

### fetching data from a backend service, subscribing to a stream of data, managing

timers and intervals, reading from and making changes to the DOM Why after each render?
### There are three key moments when the Effect Hook can be utilized:

Mounting, Updating/re-rendering & Unmounting.
### The Effect Hook is used to call another function that does something for us so

### there is nothing returned when we call the useEffect() function.The ﬁrst

### argument passed to the useEffect() function is the callback function that we

### want React to call after each time this component renders. We will refer to this

callback function as our effect. and it returns a cleanup function. Let’s learn our first programming pattern! Our programming pattern uses two React components: a stateful component, and a stateless component. “Stateful” describes any component that has a state property; “stateless” describes any component that does not.
### Ref(https://www.codecademy.com/courses/react-101/lessons/stateless-inherit-

### stateful-intro/exercises/stateless-inherit-stateful)

### Note: props and state store dynamic information. Dynamic information can change,

### by deﬁnition. That brings us to the essential new concept: you will have one

stateless component display information, and a different stateless component offer the ability to change that information. A stateful, parent component passes down a prop to a stateless, child component.
### A React component should use props to store information that can be changed,

but can only be changed by a different component(Child component).
### A stateful, parent component passes down an event handler to a stateless, child

component. The child component then uses that event handler to update its
parent’s state. A child component updates its parent’s state, and the parent passes that state to a sibling component. Advanced React!
### Higher Order component <HOC />

### Const EnhancedComponent = higherOrderComponent(originalComponent)

### Higher Order Components (HOCs) are a pattern in React that allows you to

### extract common logic or behavior from your components and reuse it across

### multiple components. HOCs are functions that take a component as an

argument and return a new component that wraps the original one, adding some additional functionality to it.
### The basic idea of a HOC is to create a reusable function that takes a

### component and returns a new component. The new component can contain

additional functionality, such as data fetching or logic for managing global state.
### HOCs are often used for cross-cutting concerns that need to be applied to

### multiple components, such as authentication or authorization. For example, you

could create an HOC that wraps a component and checks if the user is logged in before rendering it.
### HOCs can also be used for code reuse, by extracting common code from

multiple components into a higher-order component that can be shared among them.
### While HOCs can be a powerful tool for code reuse, they can also make your

### code more complex and harder to understand, especially as the number of

### HOCs in your codebase grows. To mitigate this, React also provides other

patterns for code reuse, such as render props and function as children.
### Render Props -

### Error boundaries are React components that catch JavaScript errors

### anywhere in their child component tree, log those errors, and display a

### fallback UI instead of the component tree that crashed. Error boundaries catch

errors during rendering, in lifecycle methods, and in constructors of the whole tree below them. Note Error boundaries do not catch errors for: Event handlers (learn more)
### Asynchronous code

(e.g. setTimeout or requestAnimationFrame callbacks)
### Server side rendering

### Errors thrown in the error boundary itself (rather than its children)

A class component becomes an error boundary if it defines either (or both) of
### the lifecycle methods static

### getDerivedStateFromError() or componentDidCatch(). Use static

### getDerivedStateFromError() to render a fallback UI after an error has been

thrown. Use componentDidCatch() to log error information. Ref forwarding is a technique for automatically passing a ref through a
### component to one of its children

### Ref forwarding is an opt-in feature that lets some components take

### a ref they receive, and pass it further down (in other words, “forward” it)

### to a child.In the example below, FancyButton uses React.forwardRef to obtain

### the ref passed to it, and then forward it to the DOM button that it renders:

### const FancyButton = React.forwardRef((props, ref) => (

<button ref={ref} className="FancyButton"> {props.children} </button> )); // You can now get a ref directly to the DOM button:
### const ref = React.createRef();

### <FancyButton ref={ref}>Click me!</FancyButton>;

### This way, components using FancyButton can get a ref to the

underlying button DOM node and access it if necessary—just like if they used a DOM button directly.
### Here is a step-by-step explanation of what happens in the above example:

We create a React ref by calling React.createRef and assign it to a ref variable. We pass our ref down to <FancyButton ref={ref}> by specifying it as a JSX attribute. React passes the ref to the (props, ref) => ... function inside forwardRef as a second argument. We forward this ref argument down to <button ref={ref}> by specifying it as a JSX attribute. When the ref is attached, ref.current will point to the <button> DOM node. Note
### The second ref argument only exists when you define a component

### with React.forwardRef call. Regular function or class components don’t receive

the ref argument, and ref is not available in props either. Ref forwarding is not limited to DOM components. You can forward refs to class
component instances, too.


---

*Document converted from PDF: :React@JS-Framework.pdf*
