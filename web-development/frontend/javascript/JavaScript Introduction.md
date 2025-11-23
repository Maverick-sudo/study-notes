# JavaScript Introduction

## Summary

❶Internal JavaScript in HTML is the default scripting language in HTML. can be placed in the <body>, or in the <head> section of an HTML page, or in both. JavaScript can "display" data in different ways: Using .innerHTML Syntax the HTML element(class/Id element selector value). The innerHTML after the document is loaded.

## Table of Contents

  - [//JavaScript Introduction//](#javascript-introduction)
  - [In HTML, JavaScript code is inserted between <script> & </script> tags. Scripts](#in-html-javascript-code-is-inserted-between-script-script-tags-scripts)
  - [document.getElementById(“id”).innerHTML⇔The id attribute defines](#documentgetelementbyididinnerhtmlthe-id-attribute-defines)
  - [property defines the HTML content](#property-defines-the-html-content)
  - [*Using document.write()⇔Using document.write() after an HTML](#using-documentwriteusing-documentwrite-after-an-html)
  - [document is loaded, will delete all existing HTML:The document.write()](#document-is-loaded-will-delete-all-existing-htmlthe-documentwrite)
  - [method should only be used for testing. *Never use document.write()](#method-should-only-be-used-for-testing-never-use-documentwrite)
  - [Using window.alert()⇔ In JavaScript, the window object is the global](#using-windowalert-in-javascript-the-window-object-is-the-global)
  - [scope object, that means that variables, properties, and methods by](#scope-object-that-means-that-variables-properties-and-methods-by)
  - [Using console.log()⇔For debugging purposes, you can call the](#using-consolelogfor-debugging-purposes-you-can-call-the)
  - [When Javascript is used in HTML pages, Javascript can reach on EVENTS(things](#when-javascript-is-used-in-html-pages-javascript-can-reach-on-eventsthings)
  - [change)….Javascripts lets you execute code when events are detected through an](#changejavascripts-lets-you-execute-code-when-events-are-detected-through-an)
  - [propagation)](#propagation)
  - [External scripts can be referenced with a full URL(absolute) or with a path](#external-scripts-can-be-referenced-with-a-full-urlabsolute-or-with-a-path)
  - [<script src="https://www.xyz.com/js/myScript.js"></script>](#script-srchttpswwwxyzcomjsmyscriptjsscript)
  - [It separates HTML and code](#it-separates-html-and-code)
  - [It makes HTML and JavaScript easier to read & maintain](#it-makes-html-and-javascript-easier-to-read-maintain)
  - [Cached JavaScript ﬁles can speed up page loads](#cached-javascript-ﬁles-can-speed-up-page-loads)
  - [Comment Syntax // singleLine  & /*multiLine*/](#comment-syntax-singleline-multiline)
  - [semicolon at the end of each executable](#semicolon-at-the-end-of-each-executable)
  - [Javascript ignores white space, but as a good](#javascript-ignores-white-space-but-as-a-good)
  - [JavaScript statements can be grouped together in](#javascript-statements-can-be-grouped-together-in)
  - [code blocks, inside curly brackets {...}. The](#code-blocks-inside-curly-brackets-the)
  - [purpose of code blocks is to define statements](#purpose-of-code-blocks-is-to-define-statements)
  - [to identify the JavaScript action to be](#to-identify-the-javascript-action-to-be)
  - [Hyphens are not allowed in JavaScript. They are](#hyphens-are-not-allowed-in-javascript-they-are)
  - [Avoid code lines longer than 80characters, if a](#avoid-code-lines-longer-than-80characters-if-a)
  - [Ref: Javascript Best Practices(https://www.w3schools.com/js/](#ref-javascript-best-practiceshttpswwww3schoolscomjs)
  - [js_best_practices.asp) & Style Guide(https://www.w3schools.com/js/](#js_best_practicesasp-style-guidehttpswwww3schoolscomjs)
  - [js_conventions.asp) & Common Mistakes(https://www.w3schools.com/js/](#js_conventionsasp-common-mistakeshttpswwww3schoolscomjs)
  - [js_mistakes.asp) & cheatsheets (https://overapi.com/javascript)](#js_mistakesasp-cheatsheets-httpsoverapicomjavascript)
  - [Javascipt Syntax // Program Construct rules //](#javascipt-syntax-program-construct-rules)
  - [Comparisons Operator == equal to, >greater than, <less than](#comparisons-operator-equal-to-greater-than-less-than)
  - [<= less than or equal to](#less-than-or-equal-to)
  - [Logical Operators](#logical-operators)
  - [❶When using the && operator, both conditions must evaluate to true for the](#❶when-using-the-operator-both-conditions-must-evaluate-to-true-for-the)
  - [❸The ! not operator reverses, or negates, the value of a boolean:the ! operator](#❸the-not-operator-reverses-or-negates-the-value-of-a-booleanthe-operator)
  - [if (condition) {](#if-condition)
  - [are separated by a colon :](#are-separated-by-a-colon)
  - [condition ? {block of code to be executed if the condition is true;} : {block of](#condition-block-of-code-to-be-executed-if-the-condition-is-true-block-of)
  - [code to be executed if the condition is false;}](#code-to-be-executed-if-the-condition-is-false)
  - [Conditional statements](#conditional-statements)
  - [Very often when you write code, you want to perform different actions for](#very-often-when-you-write-code-you-want-to-perform-different-actions-for)
  - [different decisions. This statements are used to perform different actions based](#different-decisions-this-statements-are-used-to-perform-different-actions-based)
  - [______________________](#______________________)
  - [//  block of code to be executed if the condition is false;}](#block-of-code-to-be-executed-if-the-condition-is-false)
  - [⓷Else if Statement Use the else if statement to specify a new condition if the](#⓷else-if-statement-use-the-else-if-statement-to-specify-a-new-condition-if-the)
  - [ﬁrst condition is false. The else if statement allows for more than two possible](#ﬁrst-condition-is-false-the-else-if-statement-allows-for-more-than-two-possible)
  - [if (condition1) {](#if-condition1)
  - [} else if (condition2) {](#else-if-condition2)

---

## Content

### //JavaScript Introduction//

❶Internal JavaScript in HTML is the default scripting language in HTML.
### In HTML, JavaScript code is inserted between <script> & </script> tags. Scripts

can be placed in the <body>, or in the <head> section of an HTML page, or in both. JavaScript can "display" data in different ways: Using .innerHTML Syntax
### document.getElementById(“id”).innerHTML⇔The id attribute defines

the HTML element(class/Id element selector value) . The innerHTML
### property defines the HTML content

### *Using document.write()⇔Using document.write() after an HTML

### document is loaded, will delete all existing HTML:The document.write()

### method should only be used for testing. *Never use document.write()

after the document is loaded. It will overwrite the document.
### Using window.alert()⇔ In JavaScript, the window object is the global

### scope object, that means that variables, properties, and methods by

default belong to the window object. This also means that specifying
### the window keyword is optional

### Using console.log()⇔For debugging purposes, you can call the

console.log() method in the browser to display data.
### When Javascript is used in HTML pages, Javascript can reach on EVENTS(things

### that happen to HTML elements i.e loading webpage, clicked button, input ﬁeld

### change)….Javascripts lets you execute code when events are detected through an

event handler attributes I.e onclick attribute is added to the <button> element. document.querySelector(“ “).addEventListener(“click”, function() {}, event
### propagation)

❷External JavaScript files have the file extension .js To use an external script, put the name of the script file in the src (source) attribute of a <script> tag:
### External scripts can be referenced with a full URL(absolute) or with a path

relative(same/specified folder) to the current web page. Path relative(same folder) to the current web page. Syntax <script src="myScript.js"></script> Path relative(specified folder) to the current web page. <script src="/js/myScript.js"></script> External scripts can be referenced with a full URL(absolute)
### <script src="https://www.xyz.com/js/myScript.js"></script>

Placing scripts in external files has some advantages:
### It separates HTML and code

### It makes HTML and JavaScript easier to read & maintain

### Cached JavaScript ﬁles can speed up page loads

### Comment Syntax // singleLine  & /*multiLine*/

Semicolons Separate Javascript Statements, add a
### semicolon at the end of each executable

statement. Multiple statements can be on one line when separated by semicolons.
### Javascript ignores white space, but as a good

practice put spaces around operators(= + - * / % ++ --).
### JavaScript statements can be grouped together in

### code blocks, inside curly brackets {...}. The

### purpose of code blocks is to define statements

to be executed together especially Javascript function statements. JavaScript statements often start with a keyword
### to identify the JavaScript action to be

performed. I.e do…while, if…else, var, function, debugger, for, return, break. JavaScript is very Case Sensitive.
### Hyphens are not allowed in JavaScript. They are

reserved for subtractions.Underscore is allowed.
### Avoid code lines longer than 80characters, if a

statement does not fit on one line, best place to break it is after an operator.
### Ref: Javascript Best Practices(https://www.w3schools.com/js/

### js_best_practices.asp) & Style Guide(https://www.w3schools.com/js/

### js_conventions.asp) & Common Mistakes(https://www.w3schools.com/js/

### js_mistakes.asp) & cheatsheets (https://overapi.com/javascript)

Declaring (Creating) JavaScript Variables
P.S JavaScript Identifiers are unique names, used to name & identify variables, functions, & labels. The first character must be a letter(A-Z or a-z), or an underscore (_), or a dollar sign ($).Subsequent characters may be letters, digits, underscores, or dollar signs. Numbers are not allowed as the first character.This way JavaScript can easily distinguish identifiers from numbers. Identifiers are case sensitive. The Concept of Data Types Expressions in parentheses(x
- y) are fully computed
before the value is used in the rest of the expression. JavaScript evaluates expressions from left to right. Different sequences can produce different results When adding a number and a string, JavaScript will treat the number as a string. You can use single quotes’ inside a string, as long as they don't match the double quotes” surrounding the string. Also Backslash \ Escape Character helps turns special character into exceptionable strings. \\ prints backslash\\ \’ prints single quote \’ \” prints double quote \” It's a good programming practice to declare all variables at the beginning of a script, You can declare many variables in one statement. Start the statement with var and separate the variables by comma. A variable without a value will have the value of undefined, however the value can be something that has to be calculated or provided later, const variables must be assigned a value when they are declared. Empty value (“ “) has nothing to do with undefined
Re-Declaring JavaScript Variables Variables defined with var can be redeclared, reassigned, & NOT have block scope{ }. Variables defined with let cannot be Redeclared/ must be Declared before use/ & have Block Scope{ }. Variables defined with const cannot be redeclared, reassigned and have block scope{ }. Use of Lower Camel Case to join multiple words into a variable name starting with a lowercase letter: myFirstName, myFirstCar, americanEagle; Use const when you declare a new Array[], new object {}, new function()….const defines a constant reference to a value, because of this you can’t reassign const value, array, object, but you can change it. JavaScript Arrays[ ] are written with square brackets. Array items are separated by commas. Array indexes are zero-based, which means the first item is [0], second is [1], and so on. JavaScript objects are written with curly braces { }. Object properties are written as name:value pairs, separated by commas.
### Javascipt Syntax // Program Construct rules //

An expression is a combination of values, variables, and operators, which computes to a value. The computation is called an evaluation. Javascript Syntax defines two types of values. Fixed Values are called literals. I.e Numbers & “Strings”. Variable values are called variables and are used to store data values I.e var, let, const Variables are containers for storing data (values). JavaScript uses an assignment operator ( = ) to assign fixed values to variables nameS. JavaScript uses arithmetic operators ( + — * / =) to compute values. JavaScript uses comparison operators (=== !== && || ) to compare values. JavaScript Booleans represents one of two values: true or false. Boolean() function can be used to find out if an (expression/variable= parameter/ argument) is true or false.
### Comparisons Operator == equal to, >greater than, <less than

Everything with a value is true, without a value(null, undefined, empty string, minus 0, zero 0, false) is false.
Boolean can be Objects Since they are created from Literals, They are defined as objects using the keyword new new Boolean(). Creating new boolean objects slows down & complicates code execution. Comparison Operators == equal to(in value) === equal value & equal type. Identity operator != not equal(value) !=== not equal value & type > greater than >= greater than or equal to < less than
### <= less than or equal to

/*Used in conditional statements to compare values nd take action depending on
### the result*/

Comparing data of different types may give unexpected results. When comparing a “string” with a number, JavaScript will convert the string to a number when doing the comparison. An empty string(“ “) converts to 0. A non-numeric string converts to NaN (not a number) which will always return false.
### Logical Operators

Logical operators are used to determine the logic between variables or values. Logical operators are often used in conditional statements to add another layer of logic to our code. ✓&& and ✓ || or ✓ ! not the and operator (&&)
### the or operator (||)

### the not operator, otherwise known as the bang operator (!)

### ❶When using the && operator, both conditions must evaluate to true for the

entire condition to evaluate to true and execute. Otherwise, if either condition is false, the && condition will evaluate to false and the else block will not execute. ❷When using the || operator, only one of the conditions must evaluate to true for the overall statement to evaluate to true.
### ❸The ! not operator reverses, or negates, the value of a boolean:the ! operator

will either take a true value and pass back false, or it will take a false value and pass back true. Conditional(Ternary) Operator ? We can use a ternary operator to simplify an if...else statement.
### if (condition) {

// block of code to be executed if the condition is true;
} else { // block of code to be executed if the condition is false;} ShorthandSyntax Using Ternary Operator Two expressions follow the ? and
### are separated by a colon :

### condition ? {block of code to be executed if the condition is true;} : {block of

### code to be executed if the condition is false;}

Also use it as a conditional operator that assigns a value to a variable based on some condition. Syntax variableName = (condition-true/false) ? value1:value2
### Conditional statements

### Very often when you write code, you want to perform different actions for

### different decisions. This statements are used to perform different actions based

on different conditions. A code block is a block of code to be executed between { and }. ___________________________________________________________
### ______________________

⓵If statement Use the if statement to specify a block of JavaScript code to be executed if a condition is true.
### if (condition) {

// block of code to be executed if the condition is true; ___________________________________________________________
### ______________________

⓶Else Statement Use the else statement to specify a block of code to be executed if the condition is false.
### if (condition) {

// block of code to be executed if the condition is true; } else {
### //  block of code to be executed if the condition is false;}

___________________________________________________________
### ______________________

### ⓷Else if Statement Use the else if statement to specify a new condition if the

### ﬁrst condition is false. The else if statement allows for more than two possible

outcomes. You can add as many else if statements as you’d like, to make more complex conditionals!
### if (condition1) {

// block of code to be executed if condition1 is true
### } else if (condition2) {

// block of code to be executed if the condition1 is false and condition2 is
true; } else { // block of code to be executed if the condition1 is false and condition2 is false;} ___________________________________________________________
### ______________________

### ⓸Switch statement A switch statement provides an alternative syntax to else if

that is easier to read and write.The switch statement is used to perform different
### actions based on different conditions. Use the switch statement to select one of

many code blocks to be executed. Instead of writing multiple else if. switch(expression) { case (expression): // code block; break; case (expression): // code block; break; default: // code block
### The switch expression(The switch keyword initiates the statement and is followed

### by ( ... ), which contains the value that each case will compare) & is evaluated

### once ☞The value of the expression is then compared with the values of each

### cases. ☞If there is a match, the associated block of code is executed. ☞If there

is no match, the default code block is executed(The default keyword specifies the code to run if there is no case match). When JavaScript reaches a break keyword, it breaks out of the switch block. This will stop the execution inside the switch block. It is not necessary to break the last case in a switch block. The block breaks (ends) there anyway.
### Switch cases use strict comparison (===). The values must be of the same type

to match. A strict comparison can only be true if the operands are of the same type.
### LOOP Statements

Loops are programming tools that repeat a block of code until a condition is met,
### Loops can execute a block of code a number of times. Loops are handy, if you

want to run the same code over and over again, each time with a different value.
### JavaScript supports different kinds of loops:

___________________________________________________________ ______________________
⓵for - loops through a block of code a number of times Syntax for (statement 1; statement 2; statement 3) {
### // code block to be executed;}

for(let I=0; I<10; I++) { console.log(I) }
### Statement1: executed once, before code block execution(initializes the variable

used in the loop⇥let 1=0), you can initiate many values in statement1(separated by comma). When let is used to declare the i variable in a loop, the i variable will only be visible within the loop.
### Statement2: deﬁnes & evaluates the condition of the initial variable for code

block execution. If statement 2 returns true, the loop will start over again, if it returns false, the loop will end.
### Statement3: executed everytime after each statement2 has been executed. It

can do anything like -ve increment(i--), +ve increment(i++), or anything else. ___________________________________________________________
### ______________________

⓶for/in - loops through the properties: values of an object{} Syntax
### for (let variable in object) {// code to be executed}

const car = {type: "Fiat", model: "500x”, color: "white"}; let automobiles = “ “ //undefined declared variable for (let x in car)
// property\key in object {automobile += car[x];} // code block to be executed //returns Fiat 500x white.
### if we used {automobile += car;} //returns type model color

### The for in loop iterates over a person object☞Each iteration returns a key/

property (x)☞The key/property is used to access the value of the key/property ☞ The value of the key is variable[x].
### /*The JavaScript for in statement can also loop over the properties of an Array,

Do not use for in over an Array if the index order is important. The index order is
### implementation-dependent, and array values may not be accessed in the order

you expect. It is better to use a for of loop, or Array.forEach() when the order
### is important.*/

___________________________________________________________
### _________________________

⓷for/of - loops through the Properties: values of an iterable object{}. It lets you loop over iterable data structures such as Arrays, Strings, Maps, NodeLists, & more: Syntax for (let variable of object) {// code to be executed} const car = [“BMW”, “Fiat”, “benz”]; let allCars = “ “;
### //undeﬁned variable

for (let x of cars) //variable of iterable
{allCars += x;} // code block to be executed
### //returns BMW Fiat Benz

### variable- For every iteration the value of the next property is assigned to the

variable. Variable can be declared with const, let, or var. iterable - An object that has iterable properties. ___________________________________________________________
### ______________________

### ⓸while - loops through a block of code while a speciﬁed condition is true, you

will discover that a while loop is much the same as a for loop, with statement 1 and statement 3 omitted.. Syntax
### while (condition) {// code block to be executed;}

___________________________________________________________
### ______________________

### ⓹do/while - also loops through a block of code while a speciﬁed condition is

true. The do while loop is a variant of the while loop. This loop will execute the code block once, before checking if the condition is true, then it will repeat the
### loop as long as the condition is true. The loop will always be executed at least

once, even if the condition is false, because the code block is executed before the condition is tested. Syntax do {// code block to be executed;} while (condition);
### Break Statement/ keyword

### It’s used to jump out of a loop if a condition

occurs(true). The break statement with a label reference can be used to jump out of any code block. Without a label ref can only be used to jump out of a loop or a switch condition.
### Continue Statement/ Keyword

### It’s used to break one iteration(in the loop),

if a specified condition occurs, and continues with the next iteration in the loop. The continue statement (with or without a label reference) can only be used to skip one loop iteration. Javascript Data Types string Object number Date boolean Array object String function Number There are 6 types of objects: Boolean
null & undefined can not contain values. And 2 data types that cannot contain values:
### The typeof Operator

You can use the typeof operator to find the data type of a JavaScript variable.
### The .constructor Property

The constructor property returns the constructor function for all JavaScript variables. Check if the object is an array function Syntax function isArray(myArray) { return myArray.constructor === Array;} Check if the object is a Date function Syntax function isDate(myDate) {
### return myDate.constructor === Date;}

Any variable can be emptied, by setting the value to undefined. The type will also be undefined. “ “ Empty values are not undefined, they have legal value & type. null is nothing, something that doesn’t exist. However it’s data type is an object. You can empty an object by setting it to null. Difference between Undefined & Null. typeof undefined undefined null === undefined false typeof null object null == undefined true
### JavaScript Type Conversion

JavaScript variables can be converted to a new variable and another data type:
### By the use of a JavaScript function

.Number() convert strings/dates/boolean to numbers⌫ false 0 true 1 .parseFloat() Parses a string and returns a floating point number
### .parseInt() Parses a string and returns an integer

.String() & toString() converts numbers/dates/boolean to
### strings⌫returns “true” “false”

.toExponential() converts numbers to string written using Exponential notation Automatically by JavaScript itself
### When JavaScript tries to operate on a

"wrong" data type, it will try to convert the value to a "right" type. However The
result is not always what you expect. JavaScript automatically calls the variable's toString() function when you try to "output" an object or a variable.
### ⒈ A JavaScript function()

A function is a reusable block of code that groups together a sequence of statements to perform a specific task.
### Or block of JavaScript code designed to perform a particular task, & can be

### executed when "called" for.  A JavaScript program is a list of programming

statements. In HTML, JavaScript programs are executed by the web browser. Javascript Statements are composed of Values, operators, Expressions, Keywords, & Comments.
### Syntax function declaration

### function myFunction (parameter1, parameter2,) { line of code; }

### Keyword  Identiﬁer  (arg1, arg2 ) {execute line of code; }

### One way to create a function is by using a function declaration. Just like how a

variable declaration binds a value to a variable name, a function declaration binds a function to a name, or an identifier. To call myFunction, type the function_identifier followed by parenthesis () and it executes line of code.
### Functions often compute a return value. The return value is "returned" back to

### the "caller" {return code;}. To pass back information from the function call, we

### use a return statement. To create a return statement, we use the return keyword

preceded by the code that we wish to execute. If the line of code is omitted,
### undeﬁned is returned instead. When a return statement is used in a function

body, the execution of the function is stopped and the code that follows it will not be executed.
### Helper Functions

### We can also use the return value of a function inside

### another function. These functions being called within another function are often

### referred to as helper functions. Since each function is carrying out a speciﬁc

task, it makes our code easier to read and debug if necessary.
### Parameters and Arguments

### Parameters allow functions to accept input(s) and perform a task using the

input(s). We use parameters as placeholders for information that will be passed to the function when it is called.
### The accepted real inputs/values passed into the function when it’s called are

### Arguments. Arguments can be passed to the function as values or variables. The

variables are initialized with values before being used in the function call.
### Parameter Rules

JavaScript function definitions do not specify data types for parameters. JavaScript functions do not perform type checking on the passed arguments. JavaScript functions do not check the number of arguments received.
### Default parameters allow parameters to have a predetermined value in case

there is no argument passed into the function or if the argument is undefined when called. Functions can be used the same way as you use variables, in all types of formulas, assignments, and calculations.
### Instead of using a variable(let, var, const) to store the return value of a

### function, you can use the function directly, as a variable value. Using function

### expression, we can assign a function to a variable name, with the function

### keyword. In a function expression, the function name is usually omitted. A

### function expression with no identiﬁer name is called an Anonymous function. A

function expression is often stored in a variable in order to refer to it. Below is a Image of Function Exp.
### Anonymous Function

### Functions stored in variables do not need function

names. They are always invoked (called) using the variable name.
Variables declared with var, let and const are quite similar when declared inside a function.
### They are called Local variables & have Function Scope, They can only be accessed

### from within the function { }& become LOCAL to the function, Since local

### variables are only recognized inside their functions{ }, variables with the same

### name can be used in different functions{ }. Each Function creates a new scope,

Local variables are created when a function starts, and deleted when the function is completed.
### Scope determines the accessibility of variables, objects, and functions from

different parts of the code. If you assign a value to a variable that has not been declared, it will automatically become a GLOBAL variable.
### Arrow functions remove the need to type out the keyword function every time

### you need to create a function expression. Instead, you ﬁrst include the

parameters inside the ( ) and then add an arrow => that points to the function
### body surrounded in { } like this

### The handling of this is also different in arrow functions compared to regular

functions. In short, with arrow functions there are no binding of this. In regular functions the this keyword represented the object that called the function, which
### could be the window, the document, a button or whatever. With arrow functions,

the this keyword always represents the object that defined the arrow function. Syntax const identifier = function(a, b) {return line of code;} const
### identiﬁer = function() {line of code;}

const identifier = (a, b) => {line of code;} const identifier = () => {line of code;}
### Functions that take only a single parameter do not need that parameter to be

enclosed in parentheses(). However, if a function takes zero or multiple parameters, parentheses are required.
### A function body composed of a single-line block code does not need curly

### braces. Without the curly braces, whatever that line evaluates will be

### automatically returned. The contents of the block should immediately follow the

arrow => and the return keyword can be removed. This is referred to as implicit return. JavaScript functions are executed in the sequence they are called. Not in the sequence they are defined.
### An asynchronous operation / (deferred computations) is one that allows the

computer to “move on” to other tasks while waiting for the operation to complete.
### Asynchronous programming means that time-consuming operations don’t have to

bring everything else in our programs to a halt. Functions running in parallel with other functions are called asynchronous.
### JavaScript is non-blocking: instead of stopping the execution of code while it

### waits, JavaScript uses an event-loop which allows it to efﬁciently execute other

### tasks while it awaits the completion of these asynchronous actions-(actions we

### can wait on while moving on to other tasks). Originally, JavaScript used

### promises & callback functions to handle Asynchronous actions, and upgraded to

### Async-Await. The problem with callbacks is that they encourage complexly

nested code which quickly becomes difficult to read, debug, and scale. Below
### are three ways to handle an Asynchronous Actions

(https://www.codecademy.com/courses/learn-node-js/articles/javascript-for- node-js)
### Synchronous code executes in the sequence it is written; statements wait

until the ones before them have finished running before they get to run.
### Synchronous code is considered blocking because long running tasks block the

execution of any other code until the synchronous operation has completed.
### Blocking can be useful in some situations (like reading important conﬁguration

### data on startup before letting anything else run), but will make your

application unresponsive if used for long running tasks like making HTTP calls or reading files from disk.
### Asynchronous code works by starting a long running task, and letting it

### complete in the background while other code is still able to execute. Once

### the long running task has completed, the handler function (called a callback)

### is immediately executed with the result from the task. Asynchronous code is

### considered non-blocking because it does not prevent the rest of your code

from executing while the asynchronous task occurs in the background.
### ❶ Javascript use of Callbacks

A callback is a simple function that's passed as a value to another function, and
### will only be executed when the event happens. We can do this because JavaScript

### has ﬁrst-class functions, which can be assigned to variables and passed around

### to other functions (called higher-order functions)

### A higher-order function is a function that either accepts functions as

parameters, returns a function, or both! We call the functions that get passed in
### as parameters and invoked

### callback functions because they get called during

the execution of the higher-order function. When we pass a callback function in as an argument to another function, we
### don’t invoke it i.e ✗ identiﬁer()

### cause that evaluates to the return value of

calling the function itself. With callbacks, we pass in the function itself by typing
### the function name(identiﬁer) without the parentheses. Anonymous

functions(functions stored in variables) can be arguments too!
### setTimeout(), setInterval() is a Node API (a comparable API is provided by web

browsers) that uses callback functions to schedule tasks to be performed after
### a delay or after speciﬁed intervals

setTimeout() & setInterval both use same parameters: a callback function and a delay in milliseconds. Syntax
### setTimeout(callbackFunc, milliseconds); Example below

### console.log("This is the ﬁrst line of code.");//  ﬁrst line of code

const usingSTO = () => {console.log('line of code');} //second line of code
setTimeout(usingSTO, 2999); // we set a Timeout for the asynchronous
### function in line 2

console.log("This is the last line of code"); //third line of code.
### This delay is performed asynchronously—the rest of our program won’t stop

### executing during the delay. Asynchronous JavaScript uses something called the

event-loop. After time in milliseconds, the callbackFunc() is added to the line of
### code waiting to be run, Before it can run, any synchronous code from the program

will run. Next, any code in front of it in the line will run. IN THE EXAMPLE
## Above Synchronous Code Line 1 & 3 Will Run And Produce Results

## First, Before Async Funct In Line 2.

We can rewrite line 2 & setTimeout in a similar form.
### setTimeout( () => {console.log('line of  code’) }, delay in milliseconds);

### The setInterval() function will continue to execute until the clearInterval()

function is called…Using the clearTimeout() function will prevent the function specified from being executed.
### ❷ JavaScript use of Promises

### A promise is commonly deﬁned as a proxy for a value that will eventually

### become available. Promises are objects that act as & represent the eventual

outcome(result) of an Asynchronous operation—“I promise to do this while you
### keep doing what you’re doing & expect my result soon”.  A Promise object can be

in one of three states. Let’s learn how to create promises. Pending: The initial/default state of a promise— the operation has not completed yet. We refer to a promise as settled if it is no longer pending— it is either fulfilled or rejected.
### Fulﬁlled/Resolved: The operation has completed successfully and the promise

now has a resolved value(result/outcome)..
### Rejected: The operation has failed and the promise has a reason for the

failure. This reason is usually an Error of some kind. The construction of the promise syntax
### We create a promise variable

### (myFirstPromise is a higher-order function) using the new(a keyword) with a

### callback function(myExecFuncName) as parameter/argument which starts an

asynchronous operation & dictates how the promise(myFirstPromise) should be
settled. This callback function should be a function with two parameters (resolve, reject) based on their condition.
### const myFirstPromise = new Promise(myExecFunc);

function Name new Keyword- Promise Keyword —
### (the executor

### function which runs automatically when the constructor is called.)

### const myExecFunc = (resolve, reject) => { line of code based on conditions wt

respect to resolve & reject functions used as parameters};
### Shorthand Syntax

### const myFirstPromise = new Promise( (resolve, reject) =>

{Executor function to express resolve & reject conditions} );
### The resolve() function

if invoked will change promise status from pending to fulfilled
### The reject() function

if invoked changes promise status from pending to rejected.
### Promise objects come with an aptly named .then() method—> A Handler function

that handles the outcomes of the promise object returned. It allows us to say, “I have a promise, when it resolves, then here’s what I want to happen…or when it’s
### rejected, do this…”

### The .then(onFulﬁlled, onRejected)  Syntax is a higher-order function….it’s

Arguments represent promise state HANDLERS.
### The ﬁrst handler, is a success handler or called onFulﬁlled function, and it

should contain the logic for the promise resolving.
### The second handler, is a failure handler or called onRejected Function, and

it should contain the logic for the promise rejecting.
### To handle a promise that resolved, we invoke .then(onFulﬁlled) on the

### promise, passing in a success handler(onFulﬁlled) callback function/

### parameter. To create even more readable code, we can use a different

### promise function: .catch(). The .catch(onRejected) function takes only one

### argument, onRejected. In the case of a rejected promise, this failure handler

### will be invoked with the reason for rejection. Using .catch() accomplishes the

same thing as using a .then() with only a failure handler.
### Note: If the appropriate handler is not provided, instead of throwing an

error, .then() will just return a promise with the same settled value as the promise it was called on.
### Using Promise.all()

To maximize efficiency we should use concurrency, multiple asynchronous
### operations happening together. With promises, we can do this with the function

### Promise.all().// Promise.all() accepts an array of promises as its argument and

returns a single promise. That single promise will settle in one of two ways. Syntax
### const promiseArray = [ﬁrstPromise, secondPromise, thirdPromise];

Promise.all(promiseArray).then(onFulfill).catch(onReject);
### Promise.all([ﬁrstPromise, secondPromise,

thirdPromise]).then(onFulfill).catch(onReject);
### const all = Promise.all([

### new Promise((resolve, reject) => setTimeout(() => resolve(1), 1000)),

### new Promise((resolve, reject) => setTimeout(() => resolve(2), 2000)),

### new Promise((resolve, reject) => setTimeout(() => resolve(3), 3000))

### ]).catch(err => console.log("Promise was rejected!", err));

### all.then(results => console.log(results)); // [1, 2, 3]

### If every promise in the argument array resolves, the single promise returned

from Promise.all() will resolve with an array containing the resolve value from each promise in the argument array.
### We invoke .then() with a success

handler(onFulfilled) which will print the array of resolved values if each promise resolves successfully.
### If any promise from the argument array rejects, the single promise returned

from Promise.all() will immediately log a reject with the reason that promise rejected.
### We invoke .catch() with a failure handler(onRejected)

### which will print the ﬁrst rejection message if any promise rejects. This

behavior is sometimes referred to as failing fast.
### Chaining Multiple Promises which depend on each other

### One common pattern we’ll see with asynchronous programming is multiple

### operations which depend on each other to execute or that must be executed in a

certain order, This process of chaining promises together is called composition. Promises are designed with composition in mind! fetch(“api”-URL) .then(data => console.log(data))
### .catch(err => console.log(err));

### In this example we fetch some JSON data via an HTTP request. The fetch function

returns a Promise object, and will either resolve or reject the Promise internally.
We attach a then handler to the Promise returned by fetch to handle the response once the Promise resolves.
### ❸  Use of Async

### The async...await syntax allows us to write asynchronous code that reads

similarly to traditional synchronous, imperative programs, Instead of using callbacks & native promises. const myFuncName = async ( ) => {// Function body here}; myFuncName(); //calling the function
### async function myFuncName( ) {// Function body here};

### myFuncName(); //calling the function. This is better

### We wrap our asynchronous logic inside a function prepended with the async

### keyword. Then, we invoke that function. async functions always return a promise

object. This means we can use traditional promise syntax, like .then() & .catch with our async functions.
### An async function will return in one of three ways:

If there’s nothing returned from the function, it will return a promise with a resolved value of undefined. If a promise is returned from the function, it will simply return that promise. If there’s a non-promise value returned from the function, it will return a promise resolved to that value. Await
### The await keyword can only be used inside an async function. await is an

operator: it returns the resolved value of a promise. Since promises resolve in an
### undetermined amount of time, await halts, or pauses, the execution of our async

function until a given promise is resolved. In other words, it handles the promise object returned internally. Syntax const asyncFuncExample = async ( ) => { or. async function asyncFuncExample ( ) {
let resolvedValue1 = await myPromise1();
### console.log(resolvedValue);

let resolvedValue2 = await myPromise2(resolvedValue1); console.log(resolvedValue2);
### asyncFuncExample(); // invokes/calls the async’d function

We mark our function(asyncFuncExample) as async
### Inside our function

### block{ }, we create a variable resolvedValue1 assigned await myPromise1() with

no argument. This means resolvedValue1 is assigned the resolved value of the
### awaited promise

Next, we log resolvedValue1 to the console.
### Then, we create

a variable resolvedValue2 assigned to await myPromise2(resolvedValue1) with resolvedValue1 passed as an argument. Therefore, secondValue is assigned this promise’s resolved value. Finally, we log resolvedValue2 to the console. We’re able to handle the logic for a promise in a way that reads like synchronous code. // Creating a new promise that runs the function in the setTimeout after 5 seconds.
### const newPromise = new Promise((resolve, reject) => {

setTimeout(() => resolve("All done!"), 5000); });
// Creating an asynchronous function using an arrow expression and saving it to a the variable asyncFunction.
### const asyncFunction = async () => {

// Awaiting the promise to resolve and saving the result to the variable finalResult. const finalResult = await newPromise;
### // Logging the result of the promise to the console

console.log(finalResult); // Output: All done!
asyncFunction();
### Handling Independent Promises

### Remember that await halts the execution of our async function. This allows us to

### conveniently write synchronous-style code to handle dependent promises. But

### what if our async function contains multiple promises which are not dependent on

the results of one another to execute? I.e they can run concurrently/ simultaenously async function concurrent() {
### const ﬁrstPromise = ﬁrstAsyncThing();

### const secondPromise = secondAsyncThing();

console.log(await firstPromise, await secondPromise);
### } // In our concurrent() function, both promises are constructed without using

await. We then await each of their resolutions to print them to the console.
### Notice the secondAsyncThing() didn’t have an argument of the resolve value from

the firstPromise, since they are independent promises. (Ref https://www.codecademy.com/courses/introduction-to-javascript/lessons/ async-await/exercises/concurrency)
### Await Promise.all()

### Another way to take advantage of concurrency when we have multiple promises

### which can be executed simultaneously is to await a Promise.all(). We can pass an

### array of promises as the argument to Promise.all(), and it will return a single

promise. This promise will resolve when all of the promises in the argument array have resolved. This promise’s resolve value will be an array containing the resolved values of each promise from the argument array. Promise.all() also has the benefit of failing fast, meaning it won’t wait for the rest of the asynchronous actions to complete once any one has rejected. Syntax
### async function asyncPromAll() {

const resultArray = await Promise.all( [ asyncTask1(), asyncTask2(), asyncTask3(), asyncTask4() ] ); resultArray.forEach( i => { console.log(resultArray[i]); }// we use forEach/for (condition) to loop through our array.
### Beneﬁts of Async

### The true beauty of async...await is when we have a series of asynchronous

### actions which depend on one another result. With native promise syntax, we use a

chain of .then() functions making sure to return correctly each one. This can lead
### of a mistake

The async...await syntax also makes it easy to store and refer to resolved values
### from promises further back in our chain which is a much more difﬁcult task with

### native promise syntax. The async...await version more closely resembles

synchronous code, which helps developers maintain and debug their code. With async...await, we use try...catch statements for error handling. By using this
### syntax, not only are we able to handle errors in the same way we do with

synchronous code, but we can also catch both synchronous and asynchronous errors. This makes for easier debugging! Read More(https://developer.mozilla.org/en-US/docs/Web/JavaScript/ Reference/Statements/async_function)
### ⒉A JavaScript Objects

In JavaScript, almost "everything" is an object. At their core, JavaScript objects are containers{ } storing related data and functionality, but that deceptively simple task is extremely powerful in practice. Booleans can be objects (if defined with the new keyword) Functions are always objects Numbers can be objects (if defined with the new keyword) Arrays are always objects Strings can be objects (if defined with the new keyword) Objects are always objects Dates are always objects. Maths are always objects. Regular expressions are
### always objects

### JavaScript objects are containers for named values, called properties & also

methods. In Javascript, variables can contain single or multiple values, object are
### variables too i.e objects are a collection of organized data into of named

values(property/key-value pairs). A key is like a variable name/ property name
that points to a location in memory that holds a value. Common to declare objects with const keyword. Objects are mutable: They are addressed by reference(key), not by value.
### There are different ways to create new objects:

*Define an object constructor, and then create objects of the constructed type.
*Create an object using Object.create().
✓Create a single object, with the keyword new. ✓Create a single object, using an object literal
### easiest and most popular way to

### create a javascript object, you deﬁnes & create an object in one statement, an

object literal is a list of name: value pairs inside curly braces {}. const person = { name: “value”, age: “valu”, sex: “val” const person = {}; person.name= “value”; person.age= “value”; person.sex= “value”; const person = new Object(); person.name= “value”; person.age= “value”;
### person.sex= “value”;

Key: “value assigned” ✍ Properties are key-value pairs, person = objectName Access Object properties. objectName.key Dot Notation
### objectName[“key”] Bracket Notation

### We must use bracket notation[] when accessing key’s values that have

numbers(0-9), spaces “ “, or “quotation marks” in them. Without bracket notation in these situations, our code might throw an error. objectName[expression] expression must evaluate to a property name. I.e let x= “name”; x= person[x] An object that has iterable properties.
### What ?. Actually Means

?. lets you safely access a property only if the value before it is not null or undefined. If it is null/undefined, the whole expression returns undefined instead of throwing an error.
### Why Developers Use It

### It prevents app crashes when dealing with: API responses

(res?.data?.profile?.email), Deeply nested objects, User-generated data, Optional
### props in React

Example: const userName = response?.user?.info?.name || "Guest";
If any part is missing, you don’t get errors — you just get undefined. Without optional chaining:
### res.data   //

throws "Cannot read property 'data' of undefined" if res is undefined With optional chaining:
### res?.data  //

returns undefined instead of crashing if res is undefined Add New Properties
### objectName.key = “newvalue”;

### One of two things can happen with property assignment:

### If the property already exists on the object, whatever value it held before will

be replaced with the newly assigned value.
### If there was no property with that name, a new property will be added to

the object. The above syntax can add and replace Key’s value in an object. Delete Properties
### delete objectName.key

### The delete keyword deletes both the value of the property and the property

### itself. After deletion, the property cannot be used unless added back again. The

### delete operator is designed to be used on object properties. It has no effect on

### variables or functions. The delete operator should not be used on predeﬁned

JavaScript object properties. It can crash your application.
### /*Methods are actions that can be performed on objects*/

### A function deﬁned as the property of an object, is called a method to the

object. To explain further, When the data stored on an object is a identifier() we
### call that a method. A property(key-value pairs) is what an object has, while a

### method is what an object does. The key serves as our method’s name, while the

### value is an anonymous identiﬁer() expression(without the function keyword), A

key’s value can be of any data type in the language including other objects & functions Example let goat = {
### dietType: 'herbivore',

makeSound: function() {console.log('baaa');} Or Shorthand Syntax Let goat = { dietType: 'herbivore', makeSound() {console.log('baaa');} Javascript ES6 update, we can omit the colon: and the function keyword, replacing it with ()
### const alienShip = {invade: function() {line of code}};

const alienShip = {invade() {line of code}}; Accessing Object Methods objectName.methodName()
### Add New Method

### objectName.methodName = function() {code};

Arrow shorthand syntax is not appropriate for objects.
### Javascript Destructuring Assignment Shorthand Syntax

### The Javascript Destructuring Assignment is a convenient way of extracting

### multiple values from data stored in objects & Arrays, allows object/arrays to be

### extracted into speciﬁc variables. It uses a pair of curly braces/square brackets

### with variables names on the lefthand side of an assignment to extract values

from objects. The number of variables can be less than the total properties of the object. const finance = { Income: $10, Revenue: $30, Costs: $5 const {income, revenue, costs} = finance;
### Console.log(income); //prints $10

const numbers = [1, 2, 3]; //A ES5 regular Array const [num1, num2, num3] = numbers;
### const [num1, num2, num3] = [1, 2, 3]; //

An ES6 destructured array called a named-value Array
### Rest Operator(…arg)

### Speciﬁed when a function is declaration/expression,

Takes a number of parameters and combines them into an array[ ] function myFunc(…arg) { };
### Spread Operator(…arg)

### Speciﬁed when a function is called, Takes an array of

parameters and splits it into their individual parameter
### myFunc(…arg)

### Rest & Spread operator can be used on Arrays & Objects….such that, rest

operator is used to represent that there are other sets of variable value(arrays)/ key-value pairs(objects) in an array/object declaration. Spread operator is used to represent this values during their execution. Nested Objects
### In application code, objects are often nested— an object might have another

### object as a property which in turn could have a property that’s an array of even

more objects! Remember arrays as also objects. Syntax Example Let myObj = { name: "John", age: 30, cars: {car1:"Ford", car2:"BMW", car3:"Fiat"} To access car3 value without reference= myObjxcarsxcar3 or myObj[“cars”] [“car3”]
### let p1 = “cars”; let p2 = “car3’

### To access car3 value using reference= myObj×p1.p2 or myObj[p1][p2]

### Values in objects can be arrays[], and values in arrays can be objects{}

All properties have a Key, In addition they also hold a value. The value is one of the property's attributes. Other attributes are: enumerable, configurable, and writable/readable.
### In JavaScript, all attributes can be read, but only the value attribute can be

changed (and only if the property is writable).
### Looping Through Objects

### We learned how to iterate through arrays using their numerical indexing, but the

### key-value pairs in objects aren’t ordered! JavaScript has given us alternative

solution for iterating through objects with the for...in syntax .for...in will execute a given block of code for each property in an object.
### 𝟏 Displaying the Object Properties by name

### document.getElementById("demo")×innerHTML =

### person.name + "," + person.age + "," + person.city;

𝟐 Displaying the Object Properties in a Loop let txt = ""; for (let x in person) { txt += person[x] + " "; document.getElementById("demo")xinnerHTML = txt; 𝟑 Displaying the Object as Array
### There are also useful Object class methods such as Object.assign(),

Object.entries(), Object.keys(), & Object.values() just to name a few. Any JavaScript object can be converted to an array using the above function, With objectName as the argument.. Object.keys() will return an array containing property keys, Object.values() will
### return an array containing key’s value, Object.entries() will return an array

containing an objects key-value pairs. Syntax const myArray = Object.entries/
### keys/values(objectName);

### Object.assign(target, source) takes two parameters, one being the target(new

### {key-value pairs} to be added) followed by comma, and source(objectName) and

### copies all enumerable own properties from one or more source objects to a

target object. It returns the modified target object.
### document.getElementById("demo")×innerHTML = myArray; or console.log(myArray);

### For a comprehensive list, browse (https://developer.mozilla.org/en-US/docs/Web/

JavaScript/Reference/Global_Objects/Object#Methods)
### Advanced Objects Notation

Objects are collections of related data(key-value pairs) and functionality. We store that functionality as methods on our objects. Let robot = { model: '1E78V2', energyLevel: 100,
### provideInfo() {

return `I am ${this.model} and my current energy level is ${this.energyLevel}.` }};
### The this keyword references the calling object variableName i.e robot which

### provides access to the calling object’s properties. The value of this.Key, when

used in an object, is the object variable itself. **In a constructor function this does not have a value. It is a substitute for the new object(). The value of this will become the new object when a new object is created.** What happens when we use Arrow functions
### Arrow functions do not have

their own this. They are not well suited for defining object methods. provideInfo: () => {return `I am ${this.model} and my current energy level is
### ${this.energyLevel}.`}

### It inherently bind, or tie, an already deﬁned this.key value to the function

vairableName itself that is NOT the calling object. In the code snippet above, the
value of this.key is the global object, or an object that exists in the global scope,
### which doesn’t have a property and therefore returns undeﬁned, The key takeaway

from the example above is to avoid using arrow functions when using this in a method!
### Privacy in objects, we deﬁne it as the idea that only certain properties should

### be mutable or able to change in value. One common convention is to place an

### underscore _ before the name of a property(_key) to mean that the property

should not be altered/which indicate these properties should not be accessed directly.
### Javascript Object Constructor function

A function designed to create new objects, is called an object constructor. // This is a function constructor: function myFunction(arg1, arg2, arg3) { this.argX = arg1; this.argY = arg2; this.argZ = arg3; **The value of this, when used in a function, references the new object
### constructed that "owns" the function.**

### A constructor invocation creates a new object. The new object inherits the

properties and methods from its constructor. The this keyword in the constructor does not have a value. The value of this will be the new object created when the function is invoked.
### A factory function is a function that returns an object and can be reused to

### make multiple object instances. Factory functions often accept parameters

allowing us to customize the returned object. Let myPerson(first, last, age, eye) { firstName = first; lastName = last; age = age; job() {console.log(Trader);}
### ３A JavaScript Classes & Methods

### JavaScript Classes are templates for JavaScript Objects a tool that developers

### use to quickly produce similar objects. Class methods are created with the same

syntax as object methods. Use the keyword class to create a className Always add a constructor(properties) method Then add any
number of methods. "use strict"The syntax in classes must be written in "strict mode".
### You will get an error if you do not follow the "strict mode" rules because in

strict mode you’ll get an error if you use a variable without declaring it Syntax class ClassName { constructor(input1, input2, …..) {
### this×input1 = input1;   // In the context of a Class, this keyword references

the calling Class Object i.e ClassName which provides access to the calling Class properties. thisxinput2 = input2; //We use this to set the value OF the constructor properties to constructor arguments.
### }//curly braces close the constructor method(I.e acts as a Object

Constructor function to initialize the objects key=>value pairs) method_1() { line of code } method_2() { ... } method_3() { ... }
### }//curles braces close the class object

### const objectName = new ClassName(input1, input2); //instance of an object

### console.log(objectName.method_1()); //executing Class method

### To chain methods, we use return this in method block of code

### Although you may see similarities between class and object syntax, there is

one important method that sets them apart
### The constructor method is a

### syntactic sugar & special method. It is used to initialize object properties, If

you do not define a constructor method, JavaScript will add an empty constructor method.
### An instance is an object that contains the property names and methods of a

### class, but with their own unique property values., using the new keyword to

### create an object instance. The new keyword calls the constructor(), runs the

code inside of it, and then returns the new instance.
### Syntax of creating an object instance

### Let objectName = new ClassName(input1, input2, …….);

### We created a new Object with const objectName and assigned directly object’s

properties using the new keyword & constructor template(input1, input2).
objectNamexinput1 = valueofinput1; objectNamexinput2 = valueofinput2; …………………………………….
### The syntax for calling methods on an instance is the same as calling them on

### an object — append the instance with a period, then the property or method

name. For methods, you must also include opening and closing parentheses(). A JavaScript class is not an object. It’s an object template or blueprint to create objects Default Methods for Class Getters are methods that get & return the value of internal properties. We use the get keyword followed by a function. get xyz() {line of code;} Setters can safely reassign property values. Along with getter methods, we can also create setter methods which reassign values of existing properties within an object. ✗Getters can perform an action on the data when getting a property. ✗Like getter methods, there are similar advantages to using setter methods that include checking input. ✗Getters can return different values using conditionals. ✗performing actions on properties, and displaying a clear intention for how the object is supposed to be used. ✗In a getter, we can access the properties of the calling object using this.key ✗Nonetheless, even with a setter method, it is still possible to directly reassign properties.
✗The functionality of our code is easier for other developers to understand. We use get & set pairs Instead of adding or replacing method with this syntax objectName.key = “newValue”;.
### Inheritance(further explained in sublime text)

### When multiple classes share properties or methods, they become candidates for

### inheritance — a tool developers use to decrease the amount of code they need to

write. Inheritance is useful for code reusability: reuse properties and methods of an existing class when you create a new class. With inheritance, you can create a parent class (also known as a superclass) with
### properties and methods that multiple child classes (also known as subclasses)

share. The child classes inherit the properties and methods(including getter) from their parent class. To use class inheritance, use the extends keyword. A class created with a class inheritance inherits all the methods from another class/parentclass/superclass. super() method refers to the parent class. By calling the super() method in the constructor method, we call the parent's constructor method and gets access to the parent's properties and methods.
### you must always call the super method before you can use the this keyword — if

you do not, JavaScript will throw a reference error. To avoid reference errors, it is best practice to call super(input_args*) on the first line of subclass constructors.
### In addition to the inherited features, child classes can contain their own

properties, getters, setters, and methods. Static class methods are defined on the Parent Class itself. You cannot call a static method on an regular object, only on a class object.
### Sometimes you will want a class to have methods that aren’t available in

individual instances/children classes, but that you can call directly from the class. Classes also allows you to use getters and setters. It can be smart to use getters and setters for your properties, especially if you want to do something special with the value before returning them, or before you
### set them. Class method and getter syntax is the same as it is for objects except

you can not include commas between methods.
### One beneﬁt of Inheritance is that when you need to change a method or

property that multiple classes share, you can change the parent class, instead of each subclass. *************************************************************************** *************************************************************************** *****************************************************
### String are objects with Methods->actions that can be performed or

### executed on it

### (ref https://www.w3schools.com/jsref/jsref_obj_string.asp)

Let/var/const text1 = “for extracting a part of a string”; text1.slice(start, end) extracts a part of a string and returns the extracted part in a new string. JavaScript counts positions from zero. First position is 0. Start & end can accept negative indexes. Converting to Upper & Lower case text1.toUpperCase () & text1.toLowerCase text1 is converted to upper or lower case with the above syntax. text1 = "Hello" + " " + "World!"; using concat() text2 = "Hello".concat(" ", "World!"); instead for + operator.
text1.substring(sta rt, end) same with slice, doesn’t accept negatives. text1.indexOf() method returns the index of (the position of) the first occurrence of a specified text in a string. text1.lastindexOf() method returns the index of the last occurrence of a specified text in a string. Both indexOf(), & lastIndexOf() return -1 if the text is not found and also accepts a second parameter as the starting position for the search. The charAt() method returns the character at a specified index (position-0,1,2,3….) in a string. text1.charAt() / The charCodeAt() method returns the unicode of the character at a specified index in a string.
text1.substr(start , length) same with slice, second parameter specifies the length to be extracted. text1.search() method accepts same arguments however it can’t take a second start position argument text1.includes() method returns true if a string contains a specified value. text1.startsWith(s earchvalue, position to start search) text1.endsWith(sea rchvalue, length to search) *All string methods return a new string. They don't modify the original string. Formally said: Strings are immutable: Strings cannot be changed,
### only replaced*

𝟐 Numbers are objects with Methods->actions that can be performed or
### executed on it

### JavaScript has only one type of number. Numbers can be written with or without

decimals. Extra large or small numbers can be written in exponent notation. JavaScript will try to convert strings to numbers in all numeric operations except
### JavaScript uses the + operator for both addition and concatenation. Numbers are

### added. Strings are concatenated. The JavaScript interpreter works from left to

right except arithmetic brackets() taking precision. NaN is a JavaScript reserved
### word indicating that a number is not a legal number, You can use the global

JavaScript function isNaN() to find out if a value is a number. Infinity (or -Infinity) is the value JavaScript will return if you calculate a number outside the largest possible number. All number methods can be used on any type of numbers (literals, variables, or expressions) Method Description Property Description
isFinite() Checks whether a value is a finite number constructor Returns the function that created JavaScript's Number prototype isInteger() Checks whether a value is an integer MAX_VALUE Returns the largest number possible in JavaScript isNaN() Checks whether a value is Number.NaN MIN_VALUE Returns the smallest number possible in JavaScript isSafeInteger Checks whether a value is a safe integer NEGATIVE_I NFINITY Represents negative infinity (returned on overflow)
toExponential (x) Converts a number into an exponential notation, a parameter(x) defines the no. of characters behind the decimal point, after the number has been rounded up. NaN Represents a "Not-a- Number" value toFixed(x) Returns a string with x numbers of digits after the decimal point. POSITIVE_I NFINITY Represents infinity (returned on overflow) toLocaleStrin g() Converts a number into a string, based on the locale settings prototype Allows you to add properties and methods to an object toPrecision(x) Returns a string with a number written to specified x length
toString() Converts a number to a string valueOf() Returns the primitive value of a number
### 𝟑 Math Object☞Syntax Math.property

### Allows you to perform Mathematical tasks on numbers. Unlike other objects, the

### math object has no constructor and it’s static, can be used without creating a

### math object ﬁrst. JavaScript provides 8 mathematical constants that can be

accessed as Math properties: Javascript Math Methods Syntax☞Math.method. (number) (https://www.w3schools.com/jsref/jsref_obj_math.asp) Math.round(x) // returns the nearest integer Math.abs(x) // returns the absolute +positive value of x Math.E // returns Euler's number Math.ceil(x) // returns value of x rounded up its nearest int. Math.sin(x) // returns the sine value of x Math.PI // returns PI Math.floor(x) // returns value of x rounded down its nearest int. Math.cos(x) // returns the cosine value of x Math.SQRT2 // returns the square root of 2 Math.trunc(x) // returns the integer part of x, Math.min(x,y,z,…) Math.max(x,y,z,…) //find the lowest or highest value in a list of arguments. Math.SQRT1_2 // returns the square root of 1/2
Math.sign(x) // returns if x is +ve, -ve, or null. Math.log(x) // returns the natural logarithm of x. Math.LN2 // returns the natural logarithm of 2 Math.pow(x, y) // returns the value of x to the power of y. Math.log2(x) // returns the base 2 logarithm of x. Math.LN10 // returns the natural logarithm of 10 Math.sqrt(x) // returns the square root of x. Math.log10(x) // returns the base 10 logarithm of x. Math.LOG2E // returns base 2 logarithm of E JavaScript provides 8 mathematical constants that can be accessed as Math properties: Math.LOG10E // returns base 10
### logarithm of E

Math.random() * x // returns a random number btw 0(inclusive), & x(exclusive)
### value less than(<) x //

Math.random() * x + 1 // returns a random number btw 0(inclusive) & x(inclusive) value less than or equal(<=) to x // To create a proper random function, Syntax
### Math.random() * (max - min) + min;

//This JavaScript function always returns a random number between min (included) and max (excluded)// Syntax Math.floor(Math.random() * (max - min + 1) ) + min; //This JavaScript function always returns a random number between min (included) and
### max (included)//

### 𝟒 Arrays are objects with Methods->actions that can be performed or

executed on it(ref https://www.w3schools.com/jsref/jsref_obj_array.asp)
The real strength of JavaScript arrays are the built-in array properties and methods. For and .forEach() can be used to loop through an array. /*Tip You can create an array, and then provide the elements*/ The full array can be accessed by referring to arrayName. JavaScript arrays are special variables used to store multiple values in a single variableName at a time, and this values can be accessed by referring to an index number Array indexes start with 0. [0] is the first element. [1] is the second element... Arrays[ ] are special kind of objects and can have variables of different types in the same array, you can have objects{}, functions(), & arrays[] in same array. .push() add a new element to an array .pop() removes the last elements from an array. The return of the .push() is a new array length, return of the .pop() is the element removed. .toString() converts an array to a string of(comma separated) array values. .join() joins all array elements into a string, but in addition you can specify the separator as the parameter. .shift() method removes the first array element and "shifts" all other elements to a lower index, it’s return is the element removed, .unshift() method adds a new element at the beginning of an array & shifts all other elements to a higher index, it’s return is the new array length. Arrays[ ] are Objects{ }, arrays use numbers to access it’s elements ✗(numbered indexes), objects use propertyName to access its members ✗(named indexes). Arrays with named indexes are called associative arrays (or hashes). ⌫JavaScript does not support arrays with named indexes.
.splice(x, y) method can be used to add new items to an array, with 2 (parameters), 1st-defines position where new elements should be added, 2nd-defines how many elements should be removed. Returns an array with deleted items. You should use objects{ } when you want the property names to be strings (text) You should use arrays[ ] when you want the element names to be numbers. instanceOf & Array.isArray() validates is a variable is an array, typeof returns object. .length returns the length of an array, always one more than the highest array index. .concat() method, creates a new array by merging(concatenating) existing arrays which defines the parameters to use. It.s always return a new array, does not change the existing arrays. .slice() method slices out a piece/part of an array, into a new array, but does not change the existing array. Its parameters/arguments, if one slices out the rest of the array, if two, The method then selects elements from the start argument, and up to (but not including) the end argument. Changing an Array const arrayName = [“item1”, “item2”, …]; {arrayName[0] = “xyz”; returns [“xyz”, “item2”,…]; } Syntax const arrayName = [“item1”, “item2”, …]; Avoid using newArray( ) to create an Array[ ]. New keyword complicates and slows your code. JavaScript Sorting Arrays & Iterator Callback Function
Numeric sort() method sorts an int array numerically. To sort ascending order varName.sort(function(a, b) {return a - b}); To .sort() in descending order varName.sort(function(a, b) {return b - a}); To .sort() in random order varName.sort(function(a, b) {return 0.5 - Math.random()}); The .reverse() method reverses the elements in an array. /*After sorting an array, you can use the index to obtain highest&lowest values*/ Math.max.apply(null, points); finds highest number in array.100 Math.min.apply(null, points); finds lowest number in array.1
How Numeric Sort works const points = [40, 100, 1, 5, 25, 10]; The .sort() function(i.e function is the argument here, compares two values in an array, sorts the values according to the returned -If the result is negative a is sorted before b. (40, 100)(a - b) -60, a sorted before b -If the result is positive b is sorted before a. (25, 10)(a-b) +15, b sorted before a. -If the result is 0 no changes are done with the sort order of the two values. Array.forEach() The .forEach() method calls a function (a callback function) once for each array element. The functions takes 3 arguments(value, index, array). Iteration Array.filter() The .filter() method creates a new array with array elements that passes a test. takes 3 arguments(value, index, array). Iteration Array.map() The .map() method creates a new array by performing a function on each array element. The method does not execute the function for array elements without values & does not change the original array. takes 3 arguments(value, index, array). Iteration
Array.every() The .every() method checks if every/all array values passes a test. takes 3 arguments(value, index, array). Returns boolean true/false. Iteration Array.some() The .some() method checks if some array values passes a test. takes 3 arguments(value, index, array). Returns boolean true/ false. Iteration Array.find() The .find() method returns the value of the first array element that passes a test function. takes 3 arguments(value, index, array). Meanwhile findIndex() method returns the index of the first array element that passes a test function. Iteration The reduce() method works from left-to-right in the array. See also reduceRight() works right-to-left, does not produce the original array. The functions takes 4 arguments(total, value, index, array). Iteration Array.includes(search- element) .includes() This method allows us to check if an element is present in an array. Array.lastIndexOf(element, start) The .lastIndexOf() is the same as Array.indexOf(), but returns the position of the last occurrence of the specified element. Array.reduce() The .reduce () method runs a function on each array element to produce (reduce it to) a single value. Sum of + Array.indexOf(element, start) The .indexOf() method searches an array for an element value and returns its position. You may specify a search start ⇔ +ve ltr, -ve rtl.
### Javascript Array Const. const cars = ["Saab", "Volvo", "BMW"]

### Just like every variable Once declared with const, arrayName cannot be

### reassigned. However you can perform array methods & properties on it, like

changing and adding an element. Using const to declare an array must be
### initialized/given a content when it’s declared, array declared with var can be

initialized at any time. Array declared with const has block scope, declared with
### var doesn’t have block scope. Redeclaring an array declared with var is allowed,

redeclaring/reassigning an array to const in same scope or same block is not allowed.
### 𝟓 Creating Date Objects

Date objects are created with the new Date() constructor.
### There are 4 ways to create a new date object:

Javascript counts months from 0 to 11, December is 11. Date objects are created with the new Date() constructor. Syntax const d = ⇲
### new Date(); create current date & time

### new Date(year, month, day, hours, minutes, seconds,

milliseconds); create current date-time with 7numbers to specify
### new Date(milliseconds); creates current date as zero time

plus milliseconds: zero time is 01 Jan 1970, 1day = 86,400,000ms. new Date(date string); creates a new date object from a “date string”. /* Date.parse()
### method converts dates to milliseconds*/

Get Date Methods->Getting info from date object & Set Date Methods- >Setting date values for date object. Method Description Method Description getFullYear() Get the year as a four digit number (yyyy) setDate() Set the day as a number (1-31) getMonth() Get the month as a number (0-11) setFullYear() Set the year (optionally month and day)
getDate() Get the day as a number (1-31) setHours() Set the hour (0-23) getHours() Get the hour (0-23) setMillisecond s() Set the milliseconds (0-999) getMinutes() Get the minute (0-59) setMinutes() Set the minutes (0-59) getSeconds() Get the second (0-59) setMonth() Set the month (0-11) getMillisecond s() Get the millisecond (0-999) setSeconds() Set the seconds (0-59) getTime() Get the time (milliseconds since January 1, 1970) setTime() Set the time (milliseconds since January 1, 1970) getDay() Get the weekday as a number (0-6) Date.now() Get the time. ECMAScript Javascript Date Methods- >actions that can be performed or executed on it Once date objects are created, you may operate a number of methods. i.e display/setting date objects using local time, UTC,GMT. Javascript Date Inputs/ Output as “Strings” relative to browser time zone.
The toDateString() method converts a date to a more readable format(“string”). ISO Date "2015-03-25" (YYYY-MM-DD) *preferred format. The toUTCString() method converts a date to a UTC string (a date display standard). Short Date "03/25/2015"
## ("Mm/Dd/Yyyy”)

The toISOString() method converts a Date object to a string, using the ISO standard format. Long Date "Mar 25 2015" or "25 Mar 2015"
## ("Mmm Dd Yyyy”)

ISO dates can be written with added hours, minutes, and seconds (YYYY-MM- DDTHH:MM:SSZ). T is separator
### 𝟲 JavaScript Bitwise Operators

### JavaScript stores numbers as 64 bits ﬂoating point numbers, but all bitwise

operations are performed on 32 bits binary numbers. Before a bitwise operation is performed, JavaScript converts numbers to 32 bits signed integers. After the bitwise operation is performed, the result is converted back to 64 bits JavaScript numbers. Operator Name Description AND Sets each bit to 1 if both bits are 1 Sets each bit to 1 if one of two bits is XOR Sets each bit to 1 if only one of two bits is 1 NOT Inverts all the bits
Zero fill left shift Shifts left by pushing zeros in from the right and let the leftmost bits fall off Signed right shift Shifts right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off >>> Zero fill right shift Shifts right by pushing zeros in from the left, and let the rightmost bits fall off 𝟕 JavaScript Regular Expressions Syntax
### /pattern/ﬂags;

A regular expression is a sequence of characters that forms a search-filter pattern.
### (https://www.w3schools.com/jsref/jsref_obj_regexp.asp) & (https://

regex101.com/) For creating and testing REGEX.
### The test() method is a RegExp expression method. It searches a string for a

pattern, and returns true or false, depending on the result.
### The exec() method is a RegExp expression method. It searches a string for a

specified pattern, and returns the found text as an object. If no match is found, it returns an empty (null) object. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/ Regular_Expressions/Cheatsheet
### const regExp = /Reg_Ex_Pattern/ﬂags;

### const re = new RegExp('pattern', 'ﬂags');

***************************************************************************
***************************************************************************
*****************************************************
### Code Debugging

### Often, when programming code contains errors, nothing will happen. There are no

error messages, and you will get no indications where to search for errors. Searching for (and fixing) errors in programming code is called code debugging. Built-in debuggers can be turned on and off, forcing errors to be reported to the user.
### With a debugger, you can also set breakpoints (places where code execution can

be stopped), and examine variables while the code is executing.
### In the debugger window, you can set breakpoints in the JavaScript code. At each

breakpoint, JavaScript will stop executing, and let you examine JavaScript values. After examining values, you can resume the execution of code (typically with a play button).
### The debugger keyword stops the execution of JavaScript, and calls (if available)

### the debugging function. This has the same function as setting a breakpoint in

the debugger. If no debugging is available, the debugger statement has no effect.
### JavaScript Errors try and catch; throw and ﬁnally

The try statement allows you to define a block of code to be tested for errors while it is being executed.
### The catch statement allows you to deﬁne a block of code to be executed/

returned, if an error occurs in the try block. The JavaScript statements try and catch come in pairs.
### When an error occurs, JavaScript will normally stop and generate an error

### message. The technical term for this is: JavaScript will throw an exception

### (throw an error). The throw statement allows you to create a custom error

message. If you use throw together with try and catch, you can control program flow and generate custom error messages.
### Modern browsers will often use a combination of JavaScript and built-in HTML

### validation, using predeﬁned validation rules deﬁned in HTML attributes*/

The finally statement lets you execute code, after try & catch, regardless of the result Syntax
### try {Block of code to try for error}

### throw “return speciﬁed/customized error string, message”

catch(error) {Block of code to handle errors object caught from try block & print
### to the console}

finally {Block of code to be executed regardless of the try / catch result}//
finally = default. Catches & handles the errors from TRY // console.error(err.stack); // console.error(err.name); // console.error(err.message); // console.table(error); // console.error(error); // console.table(error); // console.warn(error);
### // console.log(error);

### JavaScript has a built in error object that provides error information when an

error occurs.The error object provides two useful properties: error name and message(“string”). error Name Description EvalError An error has occurred in the eval() function RangeError Using A number "outside of range" of values has occurred ReferenceError An illegal reference has occurred i.e use of an undeclared variable SyntaxError A syntax error has occurred TypeError A type error has occurred I.e use of a value outside the range of expected data types. URIError An error in encodeURI() has occurred, i.e use of illegal characters.
### Syntax errors: These are spelling errors in your code that actually cause the

program not to run at all, or stop working part way through — you will usually be
### provided with some error messages too. These are usually okay to ﬁx, as long as

you are familiar with the right tools and know what the error messages mean! Logic errors: These are errors where the syntax is actually correct but the code
### is not what you intended it to be, meaning that program runs successfully but

gives incorrect results. These are often harder to fix than syntax errors, as there usually isn't an error message to direct you to the source of the error.
### Asynchronous JavaScript and XML (AJAX) Event-loop

### JavaScript uses an event loop to handle asynchronous function calls. When a

### program is run, function calls are made and added to a stack. The functions that

### make requests that need to wait for servers to respond then get sent to a

separate queue. Once the stack has cleared, then the functions in the queue are executed.
### An event occurs in a web page (the page is loaded, a button is clicked)

### An XMLHttpRequest object is created by JavaScript

### The XMLHttpRequest object sends a request to a web server

### The server processes the request

### The server sends a response(In form or XML/JSON back to the web page

### The response is read & parsed by JavaScript

### Proper action (like page update) is performed by JavaScript

All modern browsers support the XMLHttpRequest object.
### The XMLHttpRequest object can be used to exchange data with a web server

### behind the scenes. This means that it is possible to update parts of a web page,

without reloading the whole page. An alternate to XMLHttpRequest() The Fetch() API interface allows web browser to make HTTP requests to web servers.
### AJAX just uses a combination of:

### A browser built-in XMLHttpRequest object (to request data from a web server)

“ + “ JavaScript and HTML DOM (to display or use the response data).
### AJAX applications might use XML to transport data, but it is equally common to

transport data as plain text or JSON text. We use “GET” to retrieve data from a source. JSON is JavaScript Object Notation, which is how the response is going to be formatted. Creating the boilerplate. —We need to create the XMLHttpRequest object using the new keyword and assign it to a variable. All modern browsers have a built-in browser XMLHttpRequest/xhr object.
### const xhr = new XMLHttpRequest();

—Define a callback Function, which should contain block of code to execute when
response of our request is ready or when event handler code is fulfilled. xhr.onload = () => { }. xhr.onload = function() { } xhr.onreadystatechange = () => { }. xhr.onreadystatechange = function() { } Use JSON.parse(responseText); if the response is coming as a JSON type document response. Ref: readyStates & processes (https://www.w3schools.com/tags/ ref_httpmessages.asp) —Sending & specifying the Request
### To send a request to a server, use the

open() and send() methods of the XMLHttpRequest object I.e xhr.open() &
### xhr.send()

### .open() creates a new request and the arguments passed in determine the type

and URL of the request. .open(method, url, async, user, psw) .send() has no arguments/parameters. method: the request type GET or POST
### Always use POST requests when:

A cached file is not an option (update a file or database on the server). Sending a large amount of data to the server (POST has no size limitations). Sending user input (which can contain unknown characters), POST is more robust and secure than GET.
### HTTP GET requests are made with the intention of retrieving information or

### data from a source (server) over the web. HTTP POST requests are made with

the intention of sending new information to the source (server) that will receive it. GET requests have no body, so the information that the source(server) requires,
### in order to return the proper response, must be included in the request URL path

or query string, For a POST request, the new information is stored in the body of the request.
### url: the server(ﬁle) location

### The url parameter of the open() method, is an address to a ﬁle on a server:

### The ﬁle can be any kind of ﬁle(i.e plain.txt & .xml, or server scripting ﬁles

like .asp & .php) which can perform actions on the server before sending the response back.
### Query strings are used to send additional information to the server during an

HTTP GET request. The query string is separated from the original URL using the question mark character ?.
### In a query string, there can be one or more key-

value pairs joined by the equal character =. For separating multiple key-value pairs, an ampersand character & is used.
### async: true (asynchronous) or false (synchronous)

### Server requests should be sent asynchronously(true) which is the default async

### parameter. By sending asynchronously, the JavaScript does not have to wait for

### the server response, but can instead. It can execute other scripts while waiting

for server response & deal with the response after the response is ready user: optional user name
### psw: optional password

A JavaScript Fetch API is used to access and manipulate requests and responses
### within the HTTP pipeline(server

browser), fetching resources asynchronously across a network.
### A basic fetch() request will accept a URL parameter, send a request

and .then contain a success and failure promise handler function. In the example, the block of code begins by calling the fetch(‘url’) function. Then a then() method is chained to the end of the fetch(). It ends with the response callback to handle success and the rejection callback to handle failure. BoilerPlate Synytax for Fetch() fetch('url') .then(
### function (res) { console.log(response); },

### function (rej) { console.log(rejection message) };

### ).then(jsonResponse => {return jsonResponse})

### In the case of ‘POST’(difference being a second argument determines that this

### request is a POST request and what information will be sent to the API)

fetch('https://api-to-call.com/endpoint', { method: 'POST', body: JSON.stringify({id: '200'}) }).then(
### response  => { console.log(response); },

### rejection => { console.log(rejection.message);

).then(jsonResponse => {return jsonResponse})
### JavaScript Hoisting & Strict Mode

Hoisting is JavaScript's default behavior of moving declarations to the top of the current scope / to the top of the current script / the current function. JavaScript only hoists declarations(assigning variableName), not
initializations(assigning value to variable).
### We should also be aware of the hoisting feature in JavaScript which allows

### access to function declarations before they’re deﬁned. Arrow functions are not

hoisted. They must be defined before they are used. In JavaScript, a variable can be declared after it has been used, In other words; a variable can be used before it has been declared. Variables defined with let and const are hoisted to the top of the block, but not initialized. The block of code is aware of the variable, but it cannot be used until it has been declared. Using a let & const variable before it is declared will result in a ReferenceError
### & SnntaxError

The variable is in a "temporal dead zone" from the start of the block until it is
### declared*/

### "use strict"; Deﬁnes & indicates that the JavaScript code should be executed in

"strict mode". You can use strict mode in all your programs. It helps you to write cleaner code, like preventing you from using undeclared variables. Strict mode is declared by adding "use strict"; to the beginning of a script or a function. Declared at the beginning of a script, it has global scope (all code in the script will execute in strict mode), Declared inside a function, it has local scope
### (only the code inside the function is in strict mode)

Strict mode makes it easier to write "secure" JavaScript. Strict mode changes previously accepted "bad syntax" into real errors. Not allowed in strict Mode Using an object, without declaring it, is not allowed: Deleting a variable (or object) is not allowed. Deleting an undeletable property is not allowed: The with statement is not allowed: Deleting a function is not allowed. Duplicating a parameter name is not allowed: The word eval cannot be used as a variable: The word arguments cannot be used as a variable: Octal numeric literals are not allowed: Octal escape characters are not allowed:
Writing to a read-only property is not allowed: Writing to a get-only property
### is not allowed:

### JSON stands for JavaScript Object Notation

### JSON is a language independent lightweight data-interchange format(in text

format) for storing and transporting data between computers.
### The ﬁle type for JSON ﬁles is ".json"

### The MIME type for JSON text is "application/json"

It’s syntax is a subset & derived from JavaScript object notation, but the
### JSON format is text only

Therefore Data is in name/value pairs(aka key/value pairs), separated by commas where Curly{} braces hold objects, Square[] brackets hold arrays.
### Every name-value pair is separated from another pair by a comma, ,. Similarly,

every item in an array is delimited by a comma as well. Trailing commas are forbidden.
### In JSON, values must be one of the following data types:

a string-Strings in JSON must be written in double quotes.
### However, In JSON, keys must be “strings”, written with double quotes:

a number-Numbers in JSON must be an integer or a floating point.
### an object (JSON object)-Objects as values in JSON must follow it’s syntax

{"employee":{"name":"John", "age":30, "city":"New York"} } an array-Values in JSON can be arrays.
### {"employees":["John", "Anna", "Peter"] }

a boolean-Values in JSON can be true/false {“sale":true} null-Values in JSON can be null
### {"middlename":null}

### JSON values cannot be one of the following data types:

Function & date objects are not allowed, if you need to include then, write it as a “string”(with double quotes) and convert them back. Likewise undefined.
### JSON.parse()

### A common use of JSON is to exchange data to/from a web

server. When receiving data from a web server, the data is always a string. Parse the data(data being the argument) with JSON.parse(), and the data becomes a JavaScript object.
### JSON.stringify()

### A common use of JSON is to exchange data to/from a web

### server. When sending data to a web server, the data has to be a string. Convert

### a JavaScript object into a string with JSON.stringify() (built in function). Any

### JavaScript object can be stringiﬁed (converted to a string) with the JavaScript

function JSON.stringify(), with data as argument
/*JSON.stringify will not stringify() functions. This can be "fixed" if you convert the functions into strings using toString() with function as argument before
### stringifying*/

### Also date strings must be converted suing a reviver as an argument to check it’s

properties and convert it to a JS date object by using a new Date() method, and passing the value as it’s parameter
### JSON From a Server

You can request JSON from the server by using an AJAX request/Fetch.
### As long as the response from the server is written in JSON format, you can

parse() the string into a JavaScript object. Browser Compatibility & Transpilation. In this lesson, you will learn about two important tools for addressing browser compatibility issues.
### caniuse.com — A website that provides data on web browser compatibility for

HTML, CSS, and JavaScript features. You will learn how to use it to look up ES6 feature support.
### Babel — A Javascript library that you can use to convert new, unsupported

JavaScript (ES6), into an older version (ES5) that is recognized by most modern browsers This is called Transpilation.
### ES6 supports backward compatibility

### ES5 supports concatenation(+) for string interpolation , ES6 introduced

### template literals(‘text…… ${expression}….. text’ for string interpolation

### String Interpolation is the process of evaluating string literals containing

### one or more placeholders(expressions, variables…etc) into a `string` to access

### & return their values. We can also use string concatenation in ES6. Automatic

replacing of variables with real values is called string interpolation. Example var pasta = "Spaghetti"; var meat = "Pancetta"; var sauce = "Eggs and cheese"; Concatenation
### “ + variable + “

### var carbonara = "You can make carbonara with " + pasta + ", " + meat + ", "

- " and a sauce made with " + sauce + ".";
Template literals
### ${variable}

let carbonara = `You can make carbonara with ${pasta}, ${meat}, and a sauce made with ${sauce}.`; Review Babel — A JavaScript package that transpiles JavaScript ES6+ code to ES5. npm init — A terminal command that creates a package.json file. package.json — A file that contains information about a JavaScript project.
npm install — A command that installs Node packages. babel-cli — A Node package that contains command line tools for Babel. babel-preset-env — A Node package that contains ES6+ to ES5 syntax mapping information. .babelrc — A file that specifies the version of the JavaScript source code. "build" script — A package.json script that you use to tranpsile ES6+ code to
## Es5.

npm run build — A command that runs the build script and transpiles ES6+ code to ES5.
### How to use Babel

### how to setup a JavaScript project that transpiles code when you run npm run

build from the root directory of a JavaScript project. For future reference, here
### is a list of the steps needed to set up a project for transpilation:

### Initialize your project using npm init and create a directory called src

Install babel dependencies by running syntax npm install babel-cli -D
### npm install babel-preset-env -D

Create a .babelrc file inside your project and add the following code inside it: "presets": ["env"] Add the following script to your scripts object in package.json:
### "build": "babel src -d lib"

Run npm run build whenever you want to transpile your code from your src to lib directories. Don't Use new Object() Use "" instead of new String() Use 0 instead of new Number() Use false instead of new Boolean() Use {} instead of new Object() Use [] instead of new Array()
### Use /()/ instead of new RegExp()

Use function (){} instead of new Function() Example
### let ×1 = "";             // new primitive string

### let ×2 = 0;              // new primitive number

### let ×3 = false;          // new primitive boolean

Declaring objects & arrays with const will prevent any accidential change of type. const x4 = {}; // new object
### const ×5 = [];           // new array object

### const ×6 = /()/;         // new regexp object

### const ×7 = function(){}; // new function object

***************************************************************************
***************************************************************************
*********
//NODE.JS// (https://nodejs.org)
### Introduction

### You’ll sometimes hear front-end development referred to as

### client-side development. Our instinct might be to think of the client as the

### human visitor or user of a website, but when referring to the client in web

### development, we’re usually referring to the non-human requester of content. In

### the case of visiting a website, the client is the browser, but in other

circumstances, a client might be another application, a mobile device, or even a “smart” appliance!
### The collection of programming logic required to deliver dynamic content to a

### client, manage security, process payments, and myriad other tasks is sometimes

known as the “application” or application server(Back-End Dev).
### While the front-end is the part of the website(HTML, CSS & Javascript) that

### makes it to the browser, the back-end consists of all the behind-the-scenes

### processes and data that make a website function and send resources to

clients(I.e like a warehouse of a store).
### A web server is a process running on a computer that listens for incoming

### requests for information over the internet and sends back responses. Each time

### a user navigates to a website on their browser, the browser makes a request to

### the web server of that website.  The speciﬁc format of a request (and the

### resulting response) is called the protocol. I.e When a visitor navigates to a

### website on their browser, they make an HTTP request protocol for the resources

### that make up that site. Modern web applications often cater to the speciﬁc user

rather than sending the same files to every visitor of a webpage. This is known as
### “dynamic content”.w.r.t their relation to constraint

### In order to have consistent ways of interacting with data, a back-end will

### often include a web API. API stands for “Application Program Interface” and can

### mean a lot of different things, but a web API is a collection of predeﬁned ways

of, or rules for, interacting with a web application’s data, often through an HTTP
### request-response cycle

### The type of request indicates how it would like to

interact with a web application’s data (create new data, read existing data, update existing data, or delete existing data), and it receives some data back as a response.
### When building a robust web application back-end, we need to incorporate both

### authentication (Who is this user? Are they who they claim to be?) and

### authorization (Who is allowed to do and see what?) into our server-side logic to

make sure we’re creating secure, personalized, and dynamic content.
### Most developers make use of frameworks which are collections of tools that

### shape the organization of your back-end and provide efﬁcient ways of

### accomplishing otherwise difﬁcult tasks. The collection of technologies used to

### create the front-end(HTML, CSS, Js) and back-end(Java, Python, Javascript, PHP

…etc) of a web application is referred to as a stack. This is where the term full- stack developer comes from. *************************************************************************** *************************************************************************** *********
Node.js is an open source server environment, which allows you to run single- threaded, non-blocking, asynchronously Javascript runtime programming, which is very memory efficient JavaScript on the server. Node.js can create, open, read, write, delete, and close files on the server A “runtime” converts code written in a high-level, human- readable, programming language and compiles it down to code the computer can execute. A runtime environment is where your program will be executed. It determines what global objects your program can access and it can also impact how it runs Node.js can generate dynamic page content Node.js modules/files must be initiated in the “Terminal Shell/Command Prompt Interface" program of your computer. Node.js can collect form data. Node.js can add, delete, modify
### data in your database

### Modules(https://nodejs.org/api/) <—> Cheatsheets(https://overapi.com/

### nodejs) Note: The words “module” and “ﬁle” are often used interchangeably

### Modularity is a software design technique where one program has distinct

### parts, each providing a single piece of the overall functionality. These

### separate modules come together to build a cohesive whole.  Modules are

### reusable pieces of code in a ﬁle that can be exported and then imported for

### use in another ﬁle. A modular program is one whose components can be

separated, used individually, and recombined to create a complex system. Modularity is essential for creating scalable programs which incorporate libraries and frameworks and separate the program’s concerns into manageable chunks. Essentially, a module is a collection of code located in a file. Instead of having an
entire program located in a single file, code is organized into separate files based on the concerns they address. These files can then be included in other files by using the require() function.
### You can create your own modules, Save the code in a ﬁle called

"myfirstmodule.js"and easily export their function, variable values, arrays & objects in other application file.
### Use the module.exports. keyword to make your module properties(variable values,

arrays & objects) and methods(function) available outside the module file. Include your module in the any of the node.js files using the require Keyword.
### To save developers from reinventing the wheel each time, Node.js has several

### built-in modules to perform common tasks efﬁciently. These are known as the core

### modules. The core modules are deﬁned within Node.js’s source code and are

located in the lib/ folder. Core modules can be required by passing a string with
### the name of the module into the require() function:

### In JavaScript, there are two runtime environments and each has a preferred

module implementation. The Node runtime environment and the browser’s
### runtime environment

module.exports is an object that is built-in to the Node.js runtime environment. Another feature that is built-in to the Node.js runtime environment: The require() function accepts a string as an argument. That string provides the file path to the module you would like to import.
### Using Object Destructuring { single functionality }to be more Selective With

require() In many cases, modules will export a large number of functions but only one or two of them are needed. You can use object destructuring to extract only the needed functions.
### module is actually another built-in core module of Node.js. When we require it

and append the builtinModules property, it gives the list of every core module. require('module').builtinModules inside REPL.
### “Below are modules global to the Node.js V8 chrome engine”

__dirname, __filename —>Specifies the file/directory/folder.
### console, exports, global, module, Buffer, process, require(),

### queueMicrotask(callback),  setImmediate(callback[, ...args]),

### setInterval(callback, delay[, ...args]), setTimeout(callback, delay[, ...args]),

### clearImmediate(immediateObject), clearInterval(intervalObject),

clearTimeout(timeoutObject), TextDecoder, TextEncoder, URL, URLSearchParams, WebAssembly
### Understanding setImmediate() process.nextTick() setTimeout() setInterval()

### When we pass a function to process.nextTick(), we instruct the engine to invoke

### this function at the end of the current operation, before the next event loop

### tick starts. The event loop is busy processing the current function code. When

this operation ends, the JS engine runs all the functions passed to nextTick calls
### during that operation. It's the way we can tell the JS engine to process a

function asynchronously (after the current function), but as soon as possible, not queue it. Calling setTimeout(() => {}, 0) will execute the function at the end of next tick,
### much later than when using nextTick() which prioritizes the call and executes it

### just before the beginning of the next tick. Use nextTick() when you want to make

sure that in the next event loop iteration that code is already executed.
### Any function passed as the setImmediate() argument is a callback that's executed

### in the next iteration of the event loop. How is setImmediate() different from

Zero-Delay setTimeout(() => {}, 0) (passing a 0ms timeout), and from
### process.nextTick()

### A function passed to process.nextTick() is going to be executed on the current

iteration of the event loop, after the current operation ends. This means it will always execute before setTimeout and setImmediate.
### A setTimeout() callback with a 0ms delay is very similar to setImmediate(). The

execution order will depend on various factors, but they will be both run in the next iteration of the event loop. Note: Every time the event loop takes a full trip, we call it a tick.
### setInterval is a function similar to setTimeout, with a difference: instead of

running the callback function once, it will run it forever, at the specific time interval you specify (in milliseconds).
### Handling errors in callbacks

### How do you handle errors with callbacks? One very common strategy is to use

what Node.js adopted: the first parameter in any callback function is the error
### object: error-ﬁrst callbacks

### If there is no error, the object is null. If there is an error, it contains some

### description of the error and other information. Asynchronous Operations in

### Node.Js implements error-ﬁrst callback functions, to handle error unlike their

synchronous counterparts, where an error leads to a halt in program execution. ┌──────────────┐ │ dir │ base │ ├──────┬ ├──┤
│ root │ │ name │ ext │ " / home/user/dir / file .txt " └──────┴─────────┘ (All spaces in the "" line should be ignored. They are purely for formatting.) root: '/', // dir: '/home/user/dir', // base: 'file.txt', // ext: '.txt',
### //   name: 'ﬁle'

path.join() method allows us to create cross-platform filepaths. path.join(__dirname, /file.txt) ==> /home/user/dir/file.txt whichIS absolute path I.e x/filextext === relative path
### Node.js Global Console Module

### In Node.js, the terminal is used to send and receive text feedback to and from a

### program, often for debugging purposes. This may sound familiar to how we use

the DOM console. That’s because in Node.js, the built-in console module exports a global console object that gives the terminal similar functionality. console.log() — to print messages to the terminal. console.assert() — to print a message to the terminal if the value is falsy. console.table() — to print out a table in the terminal from an object or array.
### Node.js Global Process Module

### In computer science, a process is the instance of a computer program that is

being executed. Node has a global process object with useful methods and information about the current process.
### process.env -property is an object which stores and controls information about

the environment in which the process is currently running. process.memoryUsage() -returns information on the CPU demands of the current process.
### process.memoryUsage().heapUsed -will return a number representing how

### many bytes of memory the current process is using. Heap can mean different

things in different contexts: a heap can refer to a specific data structure, but it can also refer to the a block of computer memory.
### process.argv property holds an array of command line arguments provided

### when the current process was initiated. The ﬁrst element in the array is the

### absolute path to Node, which ran the process. The second element in the array is

the path to the file that’s running. The following elements will be any command
### line arguments provided when the process was initiated. Command line arguments

are separated from one another with whitespaces.
### Node.js Global Process—>Input/Output Module

Input is data that is given to the computer, while output is any data or feedback
### that a computer provides. In Node,  using the

### stdin.on() method on the process object we can get input from a user. We are

able to use this because .on() is an instance of EventEmitter.
### .stdout.write() method on the process object To give an output, we can use the

as well. This is because console.log() is a thin wrapper on .stdout.write().
### // Recieves an input

process.stdin.on('name of event', listenerCallbackFunction); // Gives an output process.stdout.write();
### Node.Js Global Error Module

### The Node environment’s error module has all the standard JavaScript errors such

### as EvalError, SyntaxError, RangeError, ReferenceError, TypeError, and

URIError as well as the JavaScript Error class for creating new error instances.
### Within our own code, we can generate errors and throw them, and, with

### synchronous code in Node, we can use error handling techniques such as

try...catch statements. However traditional try...catch statements won’t work for errors thrown during asynchronous operations.
### Instead we use error-ﬁrst callback functions >> callback functions which have

### an error as the ﬁrst expected argument and the data as the second argument. If

### the asynchronous task results in an error, it will be passed in as the ﬁrst

argument to the callback function. If no error was thrown, the first argument will be undefined. const api = require('./api.js');
### // An error-ﬁrst callback

let errorFirstCallback = (err, data) => {
### if (err) {

console.log(`Something went wrong. ${err}\n`); } else { console.log(`Something went right. Data: ${data}\n`); api.errorProneAsyncApi('problematic input', errorFirstCallback);
### We require the local api.js module which contains the

### api.naiveErrorProneAsyncFunction() method. This asynchronous method designed

### to work like the asynchronous methods in Node. invoke the

api.errorProneAsyncApi() method with ‘err input' as the first argument and the error-first callback as the second.
### Node.js Global Buffer Module

### In Node.js, the Buffer module is used to handle binary data. A Buffer object

### represents a ﬁxed amount of memory that can’t be resized. Buffer objects are

similar to an array of integers where each element in the array represents a byte of data. The buffer object will have a range of integers from 0 to 255 inclusive. The Buffer module provides a variety of methods to handle the binary data such
### Buffer.alloc()

### method creates a new Buffer object with the size speciﬁed

as the first parameter. .alloc() accepts three arguments:
### Size: Required. The size of the buffer

Fill: Optional. A value to fill the buffer with. Default is 0. Encoding: Optional. Default is UTF-8. .toString() method translates the Buffer object into a human-readable string. It accepts three optional arguments: Encoding: Default is UTF-8. Start: The byte offset to begin translating in the Buffer object. Default is 0.
### End: The byte offset to end translating in the Buffer object. Default is the

### length of the buffer. The start and end of the buffer are similar to the start

and end of an array, where the first element is 0 and increments upwards.
### Buffer.from() method is provided to create a new Buffer object from the

### speciﬁed string, array, or buffer. The method accepts two arguments:

Object: Required. An object to fill the buffer with. Encoding: Optional. Default is UTF-8.
### Buffer.concat() method joins all buffer objects passed in an array into one

Buffer object. .concat() comes in handy because a Buffer object can’t be resized.
### This method accepts two arguments:

Array: Required. An array containing Buffer objects. Length: Optional. Specifies the length of the concatenated buffer. Node.js Readable/Writable Streams const stream = require(‘stream’);
A stream is an abstract interface for working with streaming data in Node.js. The
### stream module provides an API for implementing the stream interface.  All

streams are instances of EventEmitter. Both Writable and Readable streams will store data in an internal buffer.
### There are four fundamental stream types within Node.js:

### Writable: streams to which data can be written —>fs.createWriteStream()

### Readable: streams from which data can be read —>fs.createReadStream()

Duplex: streams that are both Readable and Writable (for example, net.Socket).
### Transform: Duplex streams that can modify or transform the data as it is

written and read (for example, zlib.createDeflate()).
### Additionally, this module includes the utility functions stream.pipeline(),

stream.finished(), stream.Readable.from() and stream.addAbortSignal().
### Node.js OS Module

### const os = require('os'); / import os from ‘os’

### Allows Node.js access to information about the computer, operating system, and

### network on which the program is running. OS module object is not global and

needs to be imported. With the os module saved to the os variable, you can call
### methods like:

os.type() — to return the computer’s operating system. os.arch() — to return the operating system CPU architecture.
### os.networkInterfaces — to return information about the network interfaces of

the computer, such as IP and MAC address. os.homedir() — to return the current user’s home directory. os.hostname() — to return the hostname of the operating system. os.uptime() — to return the system uptime, in seconds. Node.js Util Module
### const util = require('util');

The util module contains methods used to maintain and debug your code.
### Developers sometimes classify outlier functions used to maintain code and debug

certain aspects of a program’s functionality as utility functions. Utility functions don’t necessarily create new functionality in a program, but you can think of them
### as internal tools used to maintain and debug your code. The Node.js util core

### module contains methods speciﬁcally designed for these purposes. One important

object is types, which provides methods for runtime type checking in Node. Returning Boolean.
### .promisify(), which turns callback functions into promises. Since promises are

often preferred over callbacks and especially nested callbacks, Node offers a way
### to turn these into promises. util.Promisify(callbackFunc)

Node.js File System Module Syntax☞ const fs = require('fs');
10.
### The Node.js core module is an API for interacting with the ﬁle system. It was

### modeled after the POSIX standard for interacting with the ﬁlesystem, allows you

### to work with the ﬁle system on your computer.  Each method available through

the fs module has a synchronous version(doesn’t require error-first callback func) and an asynchronous version(requires an error-first-callbackFunc as argument). Common use for the File System module with their methods.
### Read ﬁles || Create ﬁles  || Update ﬁles || Delete ﬁles  || Rename ﬁles

### Writable: streams to which data can be written —>.createWriteStream()

### Readable: streams from which data can be read —>.createReadStream()

.unlink() method to delete files, argument is the file-path to be deleted. .readFileSync() method which reads data from a provided file synchronously.
### It’s 1st arg is the ﬁle-path to read from, 2nd arg is the encoding format

### .writeFileSync() method which writes data into a provided ﬁle synchronously

it’s 1st arg is a new file-path, 2nd arg is the read data. .readFile() method which reads data from a provided file asynchronously.
### fs.readFile('./ﬁle-path’, 'utf-8', err-ﬁrst-Callback);

The first argument is a string that contains a path to the file file.txt. The second argument is a string specifying the file’s character encoding (usually ‘utf-8’ for text files).
### The third argument is an error-ﬁrst callback function to be invoked when

### the asynchronous task(non-blocking) of reading from the ﬁle system is

### complete. The error-ﬁrst callback function which expects an error to be

### passed as the ﬁrst argument and data(contents of ﬁle) as the second. Node

will pass the contents of file.txt into the provided callback as its second argument(data)
### .writeFile()- since the error-ﬁrst callback function is passed the data

### from .readﬁle, & returns this data, we can therefore invoke the .writeFile()

### method within the {code block} of the err-ﬁrst-callbackfunc with It’s 1st

argument—> a new file-path, 2nd argument—> the read data. . Access the promise-based version of the fs module like so:
### const fs = require("fs").promises;

Instead of taking a err-first callback, these methods return a Promise.
### const writePromise = fs.writeFile("./out.txt", "Hello, World");

writePromise.then(() => console.log("success!")).catch(err => console.error(err));
### Node.js Readline Module Syntax☞ const readline = require('readline');

### The Readline module provides an interface for reading data from a Readable

### stream one line at a time. This is what we call streams. Streaming data is

preferred as it doesn’t require tons of RAM and doesn’t need to have all the data on hand to begin processing it. Streams allow us to read or write data piece by
11.
piece instead of all at once.
### .createInterface()- To read ﬁles line-by-line, Instances of the

### readline.Interface class are constructed using the readline.createInterface()

### method. Every instance is associated with a single input Readable stream and a

### single output Writable stream. The output stream is used to print prompts for

### user input that arrives on, and is read from, the input stream. This returns an

EventEmitter set up to emit 'line' events.
### const readline = require('readline’);//use the readline stream module

### const fs = require('fs’);//use the ﬁle system module

const myInterface = readline.createInterface({ input: fs.createReadStream('text.txt') });
### myInterface.on('line', (ﬁleLine) => {

console.log(`The line read: ${fileLine}`); });
### Node.js Events Class Module

### Node.js core API is built around an idiomatic asynchronous event-driven

### architecture in which certain kinds of objects (called "emitters") emit named

events that cause Function objects ("listeners") to be called. Objects in Node.js
### can ﬁre events, Node.js has a built-in module, called "Events", where you can

create-, fire-, and listen for- your own events.
### Node.js has an EventEmitter class which can be accessed by importing the events

### core module by using the require() statement. Each event emitter instance has

an .on() method which assigns a listener callback function to a named event. EventEmitter also has an .emit() method which announces a named event that has occurred. Syntax below. const events = require('events'); //import event module
### Class events Extends EventEmitter { }

### const myEmitter = new events.EventEmitter();//creating an instance of the

events.EventEmitter class constructor using the new keyword & getting access to it’s properties & methods.
### The eventEmitter.on() method is used to register listeners, while the

eventEmitter.emit() method is used to trigger the event.
### Each event emitter instance has an .on(‘events’, callbackfunction) method which

### assigns & register a listener callback function(optional args/data) to a named

### event. The .on() method takes as its ﬁrst argument the name of the event as a

‘string’ and, as its second argument, the listener callback function—>analogous to jQuery Each event emitter instance also has an .emit() method which triggers
12.
13.
### a named event /announces an event has occurred. The .emit() method takes as its

### ﬁrst argument the name of the event as a ‘string’ and, as its second argument,

the optional args/data that should be passed into the listener callback function.
### When a listener is registered using the .on() method, that listener is invoked

every time the named event is emitted. Using the .once() method, it is possible to
### register a listener that is called at most once for a particular event. Once the

event is emitted, the listener is unregistered and then called.
### Node.js Global timers Module

### The global timers module contains scheduling functions such as setTimeout(),

### setInterval(), and setImmediate(). These functions are put into a queue

processed at every iteration of the Node.js event loop. This means that the timer
### functions are scheduled and put into a queue. This queue is processed at every

iteration of the event loop. If a timer function is executed outside of a module, the behavior will be random (non-deterministic).
### The setImmediate() function executes the speciﬁed callback function after the

### current event loop has completed<->The function to call at the end of this turn

### of the Node.js Event Loop. The method accepts a callback function as its ﬁrst

### argument and optionally accepts arguments for the callback function as the

### subsequent arguments. If you instantiate multiple setImmediate() functions, they

will be queued for execution in the order that they were created. If callback is not a function, a TypeError will be thrown.
### The setImmediate(), setInterval(), and setTimeout() methods each return objects

### that represent the scheduled timers. These can be used to cancel the timer and

### prevent it from triggering. clearImmediate(immediateObject),

clearInterval(intervalObject), & clearTimeout(timeoutObject) Node.js HTTP Module
### const http = require('http');

### To process HTTP requests in JavaScript and Node.js, we can use the built-in http

module. This core module is key in leveraging Node.js networking and is extremely
### useful in creating HTTP servers and processing HTTP requests. Allows Node.js to

transfer data over the Hyper Text Transfer Protocol (HTTP).
### The http module comes with various methods that are useful when engaging

### with HTTP network requests. One of the most commonly used methods within the

### http module is the .createServer() method. This method is responsible for doing

### exactly what its namesake implies; it creates an HTTP server. To implement this

method to create a server, the following code can be used. const http = require('http');
### http.createServer(function (req, res) {

code to be executed based on request & response from server
### }).listen(port#, () => {

### Callback function allowing it to carry out a task

after the server has successfully started }); const server = http.createServer((req, res) => { res.end('Server is running!'); });
### server.listen(8080, () => {

### const { address, port } = server.address();

console.log(`Server is listening on: http://${address}:${port}`);
### The .createServer() method takes a single argument in the form of a callback

### function. —>This callback function has two primary arguments; the request

(commonly written as req) and the response (commonly written as res).
### The req object contains all of the information about an HTTP request

### <ingested> by the server. It exposes information such as the HTTP method (GET,

POST, etc.), the url, pathname, headers, body, and so on.
### The res object contains methods and properties pertaining to the generation

### of a response by the HTTP server. This object contains methods such as

### res.setHeader() (sets HTTP headers on the response)

res.statusCode (set the status code of the response) (https://
### developer.mozilla.org/en-US/docs/Web/HTTP/Status#information_responses)

### Once a request is processed, a response must be returned to the client to inform

### it of what happened. To build a response for the client, several pieces of

information are required. One of these pieces of information is the HTTP response
### status code, which is responsible for indicating whether a speciﬁc HTTP request

### has been successfully completed. Each response status code conveys information

### about what happened during the processing of the request, which in turn helps

the client decide how to handle the response and if further action is necessary. res.end() (dispatches the response to the client who made the request).
### Once the .createServer() method has instantiated the server, it must begin

### listening for connections. This ﬁnal step is accomplished by the

### .listen() method on the server instance. This method takes a port# as the 1st

argument, which tells the server to listen for connections at the given port#.
14.
15.
Additionally, the .listen() method takes an optional callback function as a second
### argument, allowing it to carry out a task after the server has successfully

### started. Using this simple .createServer() method, in conjunction with the

callback, provides the ability to process HTTP requests dynamically and dispatch responses back to their callers. Node.js Url Class Module
### const url = require('url');

### Typically, an HTTP server will require information from the request URL to

### accurately process a request. This request URL is located on the url property

### contained within the req object itself. To parse the different parts of this URL

### easily, Node.js provides the built-in url module. The core of the url module

revolves around the URL class. A new URL object can be instantiated using the
### URL class as follows:

### const url = new URL('https://www.example.com/p/a/t/h?query=string);

Once instantiated, different parts of the URL can be accessed and modified via
### various properties, which include:

.hostname: Gets and sets the host name portion of the URL. .pathname: Gets and sets the path portion of the URL.
### .searchParams: Gets the search parameter object representing the query

parameters contained within the URL. Returns an instance of the URLSearchParams class.
### Using these properties, one can break the URL down into easily usable parts for

### processing the request. While the url module can be used to deconstruct a URL

### into its constituent parts, it can also be used to construct a URL

Once all parts of the URL have been added, the composed URL can be obtained using the .toString() method. .toString(); // Creates URL “https://www.example.com/p/a/t/h?query=string”
### Node.js Querystring Module

### const querystring = require(‘querystring’);

### While the url module can handle query strings attached to URLs, it can also be

done with the built-in querystring module. The querystring module is dedicated to providing utilities solely focused on parsing and formatting URL query strings. The querystring module is focused solely on manipulating URL query strings, so it
### requires the query string to have already been isolated from an incoming URL as

### part of a request. This means that some pre-processing of the URL is necessary

before being able to use the module. Such as using the js split() method .split()
### || .split(separator) || .split(separator, limit) —>.split('?')[1]

As such, the module provides a much smaller number of methods to use. The core methods are listed below:
### querystring.parse(): This method is used for parsing a URL query string into a

collection of key-value pairs. The .decode() method does the same.
### querystring.stringify(): This method is used for producing a URL query string

from a given object via iteration of the object’s “own properties.” The .encode() method does the same. .escape(): This method is used for performing percent-encoding on a given query string. .unescape(): This method is used to decode percent-encoded characters within a given query string.
### Anatomy of the Uniform Resource Locator ->Basic Url Syntax<— protocol/

### domain/path/{path_parameter_optional}?query

### A URL can provide a great deal of information about a request and how it is

### expected to behave. A URL is made up of the following parts: Anatomy of a URL

1) Protocol: The protocol of the URL denotes what protocol is being used for this
particular resource. For instance, a URL could have a protocol of HTTP or HTTPS.
### 2) Domain: The domain of the URL is a unique reference that identiﬁes a website

### on the Internet through the domain name system(DNS)

### 3) Path: The path refers to a ./ﬁle or directory on the web server. Paths

oftentimes contain path parameters that APIs can process as a way to provide additional data when processing.
### Path parameters appear as part of the path on a URL

4) Query: The query is commonly found on pages that contain dynamic content.
### Queries are preﬁxed by a ? and appear at the end of a URL. Queries can be

### comprised of multiple key/value pairs, separated by a &, with each key being

### assigned its corresponding value using =. Queries are often used in conjunction

with GET requests to pass filter parameters in order to provide specificity for the requested resource. I.e ?key1=value1&key2=value2….. *************************************************************************** *************************************************************************** *********************************
### HTTP, short for Hypertext Transfer Protocol, is a request-response protocol that

### serves as the foundation of data exchange and communication within the client-

### server computing model. What this means in simpler terms is that HTTP helps

facilitate the exchange of information between a client (i.e. browser, website, mobile app, etc.) and a server.
### 1) The client(browser) submits an HTTP request message to the server. 2) The

server receives the HTTP request, performs some functions on behalf of the
client according to the request. 3) The server returns a response data/message to the client containing important information about the processing of the request. The HTTP module can create an HTTP server object that listens to server ports and gives a response back to the client.
### The Structure of HTTP

### HTTP requests and responses have speciﬁc structures to help facilitate the

### exchange of information between a client and a server. These structures

encapsulate all of the important information required to instruct the recipient of the message on how to react.
1) HTTP Method: The HTTP
method is usually a verb, such as GET and POST, or a noun such as OPTIONS and HEAD. These methods inform the server of the intent of the request and are used in accurately routing and processing requests. For instance, an HTTP request containing a GET method implies that the client wants to fetch a resource. The list of supported HTTP methods can be found using the http.METHODS property.
1) HTTP Protocol Version: The
version of the HTTP protocol, similar to the request.
2) PathName: The path denotes
the path of the resource relative to the root URL. For example, making a GET request to https://codecademy.com/api/ lessons would strip common elements such as the protocol (https://) and domain (codecademy.com), leaving the path of /api/lessons.
2) Status Code: The status
code indicates if the request was successful and, if not, why it wasn’t successful.
3) HTTP Protocol Version: The
version of the HTTP protocol (I.e. HTTP/1.1, HTTP/2, and HTTP/3). We will learn more about this in the next exercise.
3) Status Message: The status
message provides a short description of the corresponding status code.
4) Headers: Headers are
optional and are used to convey additional information that may be important in processing a request by a server. There is an extensive list of standard headers that can be used, as well as custom headers that can be added on a per-application basis.
4) Headers: These response
headers are similar to those provided in a request.
5) Body: The body contains
data required to be sent to the server to process a request. The body is not leveraged for all request types. It is most common to see a body attached to requests with verbs such as POST, PUT, and
## Patch.

5) Body: The body of a
response contains data corresponding to the fetched resource. The body is optional and contains data only when necessary to fulfill the request.
### Routing To process and respond to requests appropriately, servers need to do

### more than look at a request and dispatch a response. Internally, a server needs

### to maintain a way to handle each request based on speciﬁc criteria such as

### method, pathname, etc. The process of handling requests in speciﬁc ways based

on the information provided within the request is known as “Routing”.
### The method is one important piece of information that can be used to route

### requests. Since each HTTP request contains a method such as GET and POST, it is

a great way to discern different classes of requests based on the action intended
### for the server to carry out. Thus, all GET requests could be routed to a speciﬁc

### function for handling, while all POST requests are routed to another function to

be handled. This also allows for the logical co-location of processing code with the specific verb to be handled.
### We can distinguish one request from another of the same method through the

### use of the pathname. The pathname allows the server to understand what

resource is being targeted, allowing the server to handle many different types of requests to different resources. Databases are remote resources to which the server must make a request.
### When this happens, the server—> making the <request> functions as the client—

### >, sending HTTP messages to the <database server>. Databases usually have

### their own Software Development Kits (SDKs) and Object-Relational Mapping

### (ORMs) that can be used to connect to them easily. But with the right

### information, requests could potentially be made in a raw form directly from your

server using something like the HTTP .request() method.
### As seen in the diagram above, a single server often does not represent the ﬁnal

destination in processing a request from a client. Instead, a client sends a request,
### which is then processed partially, generating a separate HTTP request from the

### server to the database. When received, the server waits for the database’s

response and will ultimately relay that information as a response back to the original caller.
### The back-ends of modern web applications include some sort of database, often

more than one. Databases are collections of organized stored information that can be easily accessed, managed and updated.There are many different databases, but we can divide them into two types:
### Relational databases

### store information in tables with columns and rows. SQL,

### Structured Query Language, is a programming language for accessing and

changing data stored in relational databases. Popular relational databases include MySQL and PostgreSQL. Non-Relational databases (also known as NoSQL databases). use other
### systems such as key-value pairs or a document storage model. Non-relational

databases might while popular NoSQL databases include MongoDB and Redis.
### MongoDB, which is a document-oriented NoSQL database. It is crucial to be

### aware of how the data is stored in different types of databases and how

we can connect to these remote database servers and retrieve the desired data. In a document-oriented NoSQL database, the data is organized into a hierarchy of the following levels:
### databases >> collections >> documents

Databases make up the top level of data organization in a MongoDB instance.
### Databases are organized into collections which contain documents. Documents

contain literal data such as strings, numbers, dates, etc. in a JSON-like format.
### Each document consists of key-value pairs which are the basic unit of data in a

### MongoDB database. A single collection can contain multiple documents and they

are schema-less meaning that the size and content of each document can be
### different from each another

### In order to connect to the remote MongoDB server running on the target box, we

will need to install the MongoDB shell utility, which can be done on Debian-based Linux distributions (like Parrot, Kali and Ubuntu) by downloading the following tar
### archive ﬁle We must then extract the contents of the tar archive ﬁle using the

tar utility. Navigate to the location where the mongosh binary is present. Let's now try to connect to the MongoDB server running on the remote host as
### an anonymous user. We can list the

databases present on the MongoDB server using the following command. curl -O https://downloads.mongodb.com/compass/mongosh-2.3.2-linux-x64.tgz tar xvf mongosh-2.3.2-linux-x64.tgz cd mongosh-2.3.2-linux-x64/bin ./mongosh mongodb://{target_IP}:27017 show dbs; Let's list down the collections stored in the sensitive_information database using the following -> show collections; command.
### We can dump the contents of the documents present in the collection name by

### using the db.collectionName.ﬁnd() command. Let's replace the collection

### name ﬂag in the command and also use pretty() in order to receive the output in

### a beautiﬁed format -> db.collectionName.ﬁnd().pretty();

### Redis (REmote DIctionary Server) is an open-source advanced NoSQL key-value

data store used as a database, cache, and message broker. The data is stored in a
### dictionary format having key-value pairs. It is typically used for short term

### storage of data that needs fast retrieval. Redis does backup data to hard drives

to provide consistency. Redis runs as server-side software so its core functionality
### is in its server component. The server listens for connections from clients,

programmatically or through the command-line interface.
### The command-line interface (CLI) is a powerful tool that gives you complete

access to Redis’s data and its functionalities if you are developing a software or tool that needs to interact with it. Now, to be able to interact remotely with the
### Redis server, we need to download the redis-cli utility. It can be downloaded

using the following command : sudo apt install redis-tools && redis-cli -h
### {target_IP}

Alternatively, we can also connect to the Redis server using the netcat utility, but we will be using redis-cli in this write-up as it is more convenient to use. The keyspace section provides statistics on the main dictionary of each database. The statistics include the number of keys, and the number of keys with an expiration. Let us select this Redis logical database by using the select command followed by the index number of the database that needs to be selected : select 0
### We can list all the keys present in the database using the command : keys *

We can view the values stored for a corresponding key using the get command
### followed by the keynote:  get <key>

The database is stored in the server's RAM to enable fast data access. Redis also writes the contents of the database to disk at varying intervals to persist it as a
### backup, in case of failure. The back-end needs a way to programmatically access,

### change, and analyze the data stored. In fact, much of what the back-end entails

is reading, updating, or deleting information stored in a database.
### There are different types of databases and one among them is Redis, which is an

### 'in-memory' database. In-memory databases are the ones that rely essentially on

### the primary memory for data storage (meaning that

### the database is managed in the RAM of the system); in contrast to databases that

store data on the disk or SSDs. As the primary memory is significantly faster than
### the secondary memory, the data retrieval time in the case of 'in-memory'

databases is very small, thus offering very efficient & minimal response times.
### Applications like Redis or databases are designed to operate securely only on

internal/trusted networks and never get exposed over the Internet. This is indeed a secure practice, but it is based on the hypothesis that the
### internal network is

### uncompromised. If a machine that has access to the internal network gets

compromised it is possible to access these instances using tunneling. Overview of Data Brokering with Node.js —>https://heynode.com/tutorial/what- data-brokering/
### Interacting with Another Backend API

### Just like with databases, sometimes servers need to make requests to external

### APIs to accomplish some goal. There are a variety of reasons to reach out to

### external services. Some common situations are payment processing, service

integrations with other products, webhooks, and so on.
### There are a few methods provided by the http module that facilitate making

### HTTP requests to external services. One of these methods is the request()

### method. The request() method takes two arguments; it takes a conﬁguration

object containing details about the request as well as a callback to handle the response.
### const options = {

hostname: 'example.com', port: 8080, path: '/projects', method: 'GET', headers:
{ 'Content-Type': 'application/json' } const request = http.request(options, res => { // Handle response here
### For convenience, the http module provides a convenient method for making GET

### requests in the form of the get() method. This method differs from the request()

method in that it automatically sets the method to GET and calls req.end() automatically.
### The fact that servers can make HTTP requests to other services opens up

possibilities for different architecture designs for back-ends. One example of an architecture made possible by this ability is microservice architectures.
### Microservice architectures divide needs into separate lightweight services that

### communicate via HTTP over a network. As such, a single application can be

### comprised of dozens of microservices, which could all be written in different

programming languages, but work together by communicating over HTTP. *************************************************************************** *************************************************************************** *********
### The Node REPL

### REPL is an abbreviation for read–eval–print loop. It’s a

### program that loops, or repeatedly cycles, through three different states: a read

### state where the program reads input from a user, the eval state where the

### program evaluates the user’s input, and the print state where the program prints

out its evaluation to a console. Then it loops through these states again. The Node
### REPL will evaluate your input line by line. Access the REPL by typing the

### command node (with nothing after it) into the terminal and hitting enter. A >

character will show up in the terminal, indicating the REPL is running and prompting your input. By default, you indicate the input is ready for eval when you hit enter. If you’d
### like to type multiple lines and then have them evaluated at once, you can

### type .editor while in the REPL. Once in “editor” mode, you can type control + d

### when you’re ready for the input to be evaluated. Each session of the REPL has a

single shared memory; you can access any variables or functions you define until you exit the REPL.
### A REPL can be extremely useful for performing calculations, learning a language,

and developing code. It’s a place where you can explore language features and try
things out while receiving immediate feedback. Figuring out how to do this outside of the browser or a website can be really empowering.
### The global object has a lot of useful properties and methods, If you’re familiar

### with running JavaScript on the browser, you’ve likely encountered the Window

### object. Here’s one major way that Node differs: try to access the Window object

### (this will throw an error). The Window object is the JavaScript object in the

browser that holds the DOM, since we don’t have a DOM here, there’s no Window object. What are CJS, AMD, UMD, and ESM in Javascript?
### Common JS- imports modules Synchronously, made for backend, gives you a copy

### of the imported object, doesn’t work in browsers cause it has to be bundled &

### transpired —> const module = require(×/module); <—

Asynchronous Modules Definition- imports modules asynchronously, made for
### front-end exact opposite of CJS

### Universal Modules Deﬁnition- works for both front & back end,

### EcMa-Script Modules- standardized asynchronous import module, works with

### modern browsers runtime environment, best module format thanks to its simple

### syntax, async nature, and tree-shakeability.—> import module from ‘module’ <—

can be used in HTML script tags with the defer keyword however pls specify type=module as an attribute. *************************************************************************** *************************************************************************** *********
### Node Package Manager(npm)—> npm install <pkg>

### npm is an online collection, or registry, of software. Developers can share code

they’ve written to the registry or download code provided by other developers to use in Node.js projects.
### In addition to core Node.js modules, third-party modules(referred to as

dependencies) often solve common problems and simplify the development process.
### Using dependencies is an essential aspect of efﬁciently creating applications—we

don’t have to reinvent the wheel each time we want to include new functionality.
### npm is the default package manager for Node.js and its command-line tool is

### included in the Node.js installation process. This tool enables developers to

interact with the registry via the terminal. Node.js has three main types of modules to work with:
### Built-in modules

Local modules/Personally Customized Modules
### External modules which we install using NPM

### Create a package.json File

Part of learning Node.js is creating a package.json file using npm init. Creating a package.json file is typically the first step in a Node project, and you need one to install dependencies in npm. If you're starting a project from scratch, you create
### a package.json ﬁle to hold important metadata about your project and record your

### dependencies. When you run npm init to generate a package.json, you can accept

the suggested defaults, or fill out your own information. After you've created a package.json, you are free to install dependencies for your
### project using npm install <package>

### Instead of running npm init and then repeatedly hitting the enter key to accept

defaults, you can also generate a package.json without being asked for input. Run npm init -y to generate a package and automatically and accept all the defaults. The package.json created will be shown on the command line, and saved to the current directory.
### The goal of package-lock.json ﬁle is to keep track of the exact version of every

### package that is installed so that a product is 100% reproducible in the same way

even if packages are updated by their maintainers.
### A popular npm package is nodemon. nodemon is a tool used to automatically

restart a program when a file changes, alleviating the need for the node app.js
### command each time you save a ﬁle. npm i nodemon

To install a package of <package name> globally, use the -g flag in the installation
### command by typing: npm -g install <package name>

### Formidable Module—>This is a very good module for working with

client(browser)-side file uploads to the server, called "Formidable".The Formidable
### module can be downloaded and installed using NPM: npm install

### formidable….After you have downloaded the Formidable module, you can include

the module in any application using the require keyword. const formidable = require('formidable'); BIG PICTURE of a Backend In a modern backend:
- **Routes** = “Entry gates”
### * **Controllers** = “Middle managers”

- **Utils / Services** = “Workers doing the actual job (API calls, DB tasks,
### crypto signing, business rules)”

This triangle keeps your code clean, predictable, and scalable. --- ROUTES — *“Entry Points / API Endpoints”* ### **Your description: almost correct** But I’ll refine it. ### ✔ What Routes REALLY do Routes **do NOT do business logic**. Routes **only decide which controller to run**. They define:
- The URL (`/buydata`)
### * The HTTP method (`POST`)

- The middleware to run (`authMiddleware`)
- The controller function to execute
### ✔ Example
```js router.post('/buydata', authMiddleware, buyData); ``` This line means:
### A POST request hits `/buydata`

### Backend checks if user is authenticated

### If OK → execute `buyData` controller

### If NOT OK → reject the request

###
Routes should NOT contain:
- axios calls
- API business logic
- heavy processing
Those belong elsewhere. ---
### CONTROLLERS — *“Logic Orchestrators”*

### ### ✔ Your understanding: **correct and solid**

Controllers receive `(req, res)` because they sit between the **incoming HTTP request** and the backend logic.
### ### ✔ What Controllers actually do:

### **Extract user data from the request**

### (`req.body`, `req.params`, `req.query`)

### **Call the appropriate Utils/Service function**

### **Handle errors gracefully**

### **Send a response back to the frontend**

### ✔ Controllers DO:
- Validate simple things (missing ﬁelds)
- Call utils/services
- Return JSON responses
### ✔ Controllers DO NOT:
- Make direct API calls
- Write business logic
- Know API keys or provider URLs
### * Connect to databases (mostly)

Those belong to **Utils/Services** or **Models**. ### ✔ Using your example: ```js const response = await vtPass.buyData({ phone,
network: `${network}-data`, variationCode, amount }); ``` Controller → passes sanitized values → utils handles the real business. ---
### UTILS / SERVICES — *“The Workers”*

### ### ✔ Your understanding: **correct, with one reﬁnement**

### ✔ What Utils/Services are responsible for:
### * Managing **axios clients**

- Connecting to external providers (VTpass, Zendit, Crypto APIs)
- Handling API keys
- Running business logic
### * Generating request IDs / signatures

- Transforming provider responses before controllers use them
### ✔ They DO NOT:
- Handle HTTP requests
- Know anything about Express
- Deal with req/res
### * Know about users or authentication

They are purely **backend logic modules**, independent of Express. ### ✔ Example ```js return this.request("POST", "/v1/esim/purchases", payload); ``` This sends a POST request to Zendit and returns provider data to the controller. ### ✔ Why Utils use axios
Because utils talk to **other APIs**, not to your frontend. --- Putting It Together (Perfect Relationship Model) ``` ┌─────────────┐ ┌───────────────┐ ┌───────────────┐
## Routes    │  -->  │

## Controller   │

## -->   │   Utils/Service│

└─────────────┘ └───────────────┘ └───────────────┘
### │                        │                        │

### URL + HTTP verb         Extract req.body          External API calls,

attach middleware Validate + call utils business logic, axios ``` ### **Frontend → Routes → Controllers → Utils → Provider API → Controller → Frontend**


---

*Document converted from PDF: :JavaScript Introduction.pdf*
