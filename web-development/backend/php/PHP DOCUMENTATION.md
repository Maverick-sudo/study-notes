# PHP DOCUMENTATION

## Summary

VARIABLE declaration rules:
### 1.start with dollar sign($)

## Table of Contents

- [Php Documentation](#php-documentation)
  - [1.start with dollar sign($)](#1start-with-dollar-sign)
  - [2.ﬁrst letter of variable name comes from a-zA-z_](#2ﬁrst-letter-of-variable-name-comes-from-a-za-z_)
  - [4.no space,no syntex](#4no-spaceno-syntex)
  - [2.variable variables](#2variable-variables)
  - [3.static variable](#3static-variable)
  - [do? section:](#do-section)
  - [Desktop (GUI) applications](#desktop-gui-applications)
  - [In order to create this dynamic behavior, PHP was designed to work closely with](#in-order-to-create-this-dynamic-behavior-php-was-designed-to-work-closely-with)
  - [HTML. PHP can be used directly in-line with an HTML document. When the web](#html-php-can-be-used-directly-in-line-with-an-html-document-when-the-web)
  - [and added to the HTML to form one HTML document. The start of in-line PHP is](#and-added-to-the-html-to-form-one-html-document-the-start-of-in-line-php-is)
  - [3.short tag(<? ?>)](#3short-tag)
  - [Note: short tag are bydefault available but can be disabled by short_open_tag =](#note-short-tag-are-bydefault-available-but-can-be-disabled-by-short_open_tag)
  - [Note: If PHP is embeded within XML or XHTML the normal PHP <?php ?> must be](#note-if-php-is-embeded-within-xml-or-xhtml-the-normal-php-php-must-be)
  - [Adding [] changes the variable $username to an array, which means that](#adding-changes-the-variable-username-to-an-array-which-means-that)
  - [see that if the comparison succeeds and returns 0 , the login is successful. If](#see-that-if-the-comparison-succeeds-and-returns-0-the-login-is-successful-if)
  - [we convert those variables into empty arrays ( $username[] & $password[] ),](#we-convert-those-variables-into-empty-arrays-username-password)
  - [to intercept the login request in BurpSuite. To do so ﬁre up BurpSuite and](#to-intercept-the-login-request-in-burpsuite-to-do-so-ﬁre-up-burpsuite-and)
  - [conﬁgure the browser to use it as a proxy, either with the FoxyProxy plugin](#conﬁgure-the-browser-to-use-it-as-a-proxy-either-with-the-foxyproxy-plugin)
  - [or the Browser conﬁguration page. Then send a login request with a random](#or-the-browser-conﬁguration-page-then-send-a-login-request-with-a-random)
  - [set of credentials and catch the request in Change the POST data as follows](#set-of-credentials-and-catch-the-request-in-change-the-post-data-as-follows)
  - [to bypass the login. This converts the variables to arrays and after](#to-bypass-the-login-this-converts-the-variables-to-arrays-and-after)
- [# <** Snip **>](#snip)
  - [if (strcmp($username, $_POST['username']) == 0) {](#if-strcmpusername-_postusername-0)
  - [PHP echo and print Statements](#php-echo-and-print-statements)
  - [It uses echo to add text to the HTML. This practice is so common that PHP](#it-uses-echo-to-add-text-to-the-html-this-practice-is-so-common-that-php)
  - [printf - Output a formatted string](#printf-output-a-formatted-string)
  - [compound types(arrays, objects etc…)](#compound-typesarrays-objects-etc)
  - [//echo("This would NOT work", "\n");](#echothis-would-not-work-n)
  - [echo "Buuuut!", " ", "This", " ", "does!", "\n";](#echo-buuuut-this-does-n)
  - [PHP INCLUDE & REQUIRE STATEMENTS - It is possible to insert the content of](#php-include-require-statements-it-is-possible-to-insert-the-content-of)
  - [one PHP ﬁle into another PHP ﬁle (before the server executes it), with the](#one-php-ﬁle-into-another-php-ﬁle-before-the-server-executes-it-with-the)
  - [So, if you want the execution to go on and show users the output, even if the](#so-if-you-want-the-execution-to-go-on-and-show-users-the-output-even-if-the)
  - [we do the same example using the require statement, the echo statement will not](#we-do-the-same-example-using-the-require-statement-the-echo-statement-will-not)
  - [returned a fatal error](#returned-a-fatal-error)
  - [Otherwise, in case of FrameWork, CMS, or a complex PHP application coding,](#otherwise-in-case-of-framework-cms-or-a-complex-php-application-coding)
  - [Including ﬁles saves a lot of work. This means that you can create a standard](#including-ﬁles-saves-a-lot-of-work-this-means-that-you-can-create-a-standard)
  - [header, footer, or menu ﬁle for all your web pages. Then, when the header needs](#header-footer-or-menu-ﬁle-for-all-your-web-pages-then-when-the-header-needs)
- [Resource & Null](#resource-null)
  - [at runtime by PHP depending on the context in which that variable is used. To](#at-runtime-by-php-depending-on-the-context-in-which-that-variable-is-used-to)
  - [To get a human-readable representation of a type for debugging, use the](#to-get-a-human-readable-representation-of-a-type-for-debugging-use-the)
  - [variables will be parsed which means the computer will read the variables as the](#variables-will-be-parsed-which-means-the-computer-will-read-the-variables-as-the)
  - [value they hold rather than see them as just a sequence of characters.  PHP also](#value-they-hold-rather-than-see-them-as-just-a-sequence-of-characters-php-also)
  - [During variable assignment or reassignment, the variable on the left of the](#during-variable-assignment-or-reassignment-the-variable-on-the-left-of-the)
  - [assignment operator is treated as a variable (named storage for holding a value)](#assignment-operator-is-treated-as-a-variable-named-storage-for-holding-a-value)
  - [When we create a variable assigned to another variable, the computer ﬁnds a](#when-we-create-a-variable-assigned-to-another-variable-the-computer-ﬁnds-a)
  - [new space in memory which it associates with the left operand, and it stores a](#new-space-in-memory-which-it-associates-with-the-left-operand-and-it-stores-a)
  - [copy of the right operand’s value there. This new variable holds a copy of the](#copy-of-the-right-operands-value-there-this-new-variable-holds-a-copy-of-the)
  - [name which points to the same spot in memory. We use a different operator for](#name-which-points-to-the-same-spot-in-memory-we-use-a-different-operator-for)
  - [this—the reference assignment operator (=&). When we assign by reference we’re](#thisthe-reference-assignment-operator-when-we-assign-by-reference-were)

---

## Content

## Php Documentation

VARIABLE declaration rules:
### 1.start with dollar sign($)

### 2.ﬁrst letter of variable name comes from a-zA-z_

3.next letters of variable name comes from a-zA-Z0-9_
### 4.no space,no syntex

classification of VARIABLES: Variable are mainly Two types 1.Predefined Variable/Constants 2.User Define Variable User Define VARIABLE are 3 types 1.variable scope
### 2.variable variables

3.reference variable / Variables From External Sources
VARIABLE scope are 3 types 1.local scope 2.global scope
### 3.static variable

There are three main fields you can use PHP, as described in the What can PHP
### do? section:

Websites and web applications (server-side scripting) Command line scripting
### Desktop (GUI) applications

### In order to create this dynamic behavior, PHP was designed to work closely with

### HTML. PHP can be used directly in-line with an HTML document. When the web

site is delivered from the back-end to the front-end, the PHP content is executed
### and added to the HTML to form one HTML document. The start of in-line PHP is

denoted with <?php and the end is denoted with ?>. Three types of tag are available in php 1.normal tag(<?php ?>) 2.short echo tag(<?= ?>)
### 3.short tag(<? ?>)

### Note: short tag are bydefault available but can be disabled by short_open_tag =

Off and also disabled bydefault if php will built with --disabe--short--tags()
Note: The closing tag of a PHP block at the end of a file is optional, and in some cases omitting it is helpful when using include or require, so unwanted whitespace will not occur at the end of files, and you will still be able to add headers to the response later.
### Note: If PHP is embeded within XML or XHTML the normal PHP <?php ?> must be

used to remain compliant with the standards. Note: PHP requires instructions to be terminated with a semicolon ; at the end of each statement.
### Adding [] changes the variable $username to an array, which means that

strcmp() will compare the array instead of a string. In the above code we
### see that if the comparison succeeds and returns 0 , the login is successful. If

### we convert those variables into empty arrays ( $username[] & $password[] ),

### the comparison will return NULL , and NULL == 0 will return true, causing

### the login to be successful. In order to exploit this vulnerability, we will need

### to intercept the login request in BurpSuite. To do so ﬁre up BurpSuite and

### conﬁgure the browser to use it as a proxy, either with the FoxyProxy plugin

### or the Browser conﬁguration page. Then send a login request with a random

### set of credentials and catch the request in Change the POST data as follows

### to bypass the login. This converts the variables to arrays and after

forwarding the request, strcmp() returns true and the login is successful. username[]=admin&password[]=pass
## # <** Snip **>

session_start(); if (!empty($_POST['username']) && !empty($_POST['password'])) { require('config.php');
### if (strcmp($username, $_POST['username']) == 0) {

if (strcmp($password, $_POST['password']) == 0) { $_SESSION['user_id'] = 1; header("Location: /upload.php"); } else { print("<script>alert('Wrong Username or Password')</script>"); } else { print("<script>alert('Wrong Username or Password')</script>");
## # <** Snip **>

### PHP echo and print Statements

echo and print are more or less the same. They are both used to output data to the screen. When we use echo within HTML we’re no longer printing to the terminal, rather we’re outputting to the HTML document. The PHP opening (<?php) and closing (?>) tags to insert PHP code in HTML pages.
### It uses echo to add text to the HTML. This practice is so common that PHP

provides a shorthand syntax. Instead of using <?php echo to begin the statement, you can simply use <?=. The differences are small: echo has no return value while print has a return value of 1 so it can be used in expressions. echo can take multiple parameters (although such usage is rare) while print can take one argument. echo is marginally faster than print. print - Output a string
### printf - Output a formatted string

print_r - Prints human-readable information about a variable mostly used for
### compound types(arrays, objects etc…)

echo is NOT a function (it’s a “language construct”). But can be used as a function echo("This works!\n"); echo "This also works!\n";
### //echo("This would NOT work", "\n");

### echo "Buuuut!", " ", "This", " ", "does!", "\n";

### PHP INCLUDE & REQUIRE STATEMENTS - It is possible to insert the content of

### one PHP ﬁle into another PHP ﬁle (before the server executes it), with the

include or require statement. The include (or require) statement takes all the text/ code/markup that exists in the specified file and copies it into the file that uses the include statement.
### The include and require statements are identical, except upon failure:

require will produce a fatal error (E_COMPILE_ERROR) and stop the script include will only produce a warning (E_WARNING) and the script will continue
### So, if you want the execution to go on and show users the output, even if the

include file is missing, use the include statement. when a file is included with the include statement and PHP cannot find it, the script will continue to execute, If
### we do the same example using the require statement, the echo statement will not

be executed because the script execution dies after the require statement
### returned a fatal error

### Otherwise, in case of FrameWork, CMS, or a complex PHP application coding,

always use the require statement to include a key file to the flow of execution. This will help avoid compromising your application's security and integrity, just in- case one key file is accidentally missing.
### Including ﬁles saves a lot of work. This means that you can create a standard

### header, footer, or menu ﬁle for all your web pages. Then, when the header needs

to be updated, you can only update the header include file. PHP supports ten primitive types. Four scalar types: scalar values are values that you can't 'break' into smaller pieces, unlike arrays, for instance) bool int float string Four compound types: array object callable iterable And finally two special types:
## Resource & Null

The type of a variable is not usually set by the programmer; rather, it is decided
### at runtime by PHP depending on the context in which that variable is used. To

forcibly convert a variable to a certain type, either cast the variable or use the settype() function on it. Note: To check the type and value of an expression, use the var_dump() function.
### To get a human-readable representation of a type for debugging, use the

gettype() function. To check for a certain type, do not use gettype(), but rather the is_type functions i.e is_int(), is_string(), is_bool(). STRINGS PHP strings allow us to place variables directly into double quoted strings. These
### variables will be parsed which means the computer will read the variables as the

### value they hold rather than see them as just a sequence of characters.  PHP also

has a concept of leading numeric strings. This is simply a string which starts like a numeric string followed by any characters. Note: Any string that contains the letter E (case insensitive) bounded by numbers will be seen as a number expressed in scientific notation. This can produce unexpected results. <?php var_dump("0D1" == "000"); // false, "0D1" is not scientific notation var_dump("0E1" == "000"); // true, "0E1" is 0 * (10 ^ 1), or 0
var_dump("2E1" == "020"); // true, "2E1" is 2 * (10 ^ 1), or 20
### During variable assignment or reassignment, the variable on the left of the

### assignment operator is treated as a variable (named storage for holding a value)

while a variable on the right of the operator is treated as the value it stores.
### When we create a variable assigned to another variable, the computer ﬁnds a

### new space in memory which it associates with the left operand, and it stores a

### copy of the right operand’s value there. This new variable holds a copy of the

value held by the original variable, but it’s an independent entity; changes made to either variable won’t affect the other. We can also create an alias, or nickname, for a variable. Instead of a copy of the original variable’s value, we create a new
### name which points to the same spot in memory. We use a different operator for

### this—the reference assignment operator (=&). When we assign by reference we’re

saying that the variable on the left of the operator should point, or refer, to the
### exact same data as the variable on the right. With assignment by reference,

changes made to one variable will affect the other.
### There are two ways to assign one variable to another:

By value—this creates two variables that hold copies of the same value but remain independent entities.
### By reference—this creates two variable names (aliases) which point to the

same space in memory. They cannot be modified separately! INTEGERS
### Integer overﬂow ¶

### If PHP encounters a number beyond the bounds of the int type, it will be

### interpreted as a ﬂoat instead. Also, an operation which results in a number

beyond the bounds of the int type will return a float instead. Like with addition and subtraction, when we perform multiplication or division, the computer will return an integer whenever the operation evaluates to a whole number. Warning -1 is considered true, like any other non-zero (whether negative or positive) number! ints can be specified in decimal (base 10), hexadecimal (base 16), octal (base 8) or binary (base 2) notation. The negation operator can be used to denote a negative int. To use octal notation, precede the number with a 0 (zero). As of PHP 8.1.0, octal notation can also be preceded with 0o or 0O. To use hexadecimal notation precede
the number with 0x. To use binary notation precede the number with 0b. BOOLEAN When converting to bool, the following values are considered false: the boolean false itself the integer 0 (zero) the floats 0.0 and -0.0 (zero) the empty string, and the string "0"
### an array with zero elements

### the special type NULL (including unset variables)

### SimpleXML objects created from attributeless empty elements, i.e. elements

which have neither children nor attributes. Every other value is considered true (including any resource and NAN). ARRAY
### An array in PHP is actually an ordered map. A map is a type that associates

### values to keys. An array can be created using the array() language construct. It

### takes any number of comma-separated key => value pairs as arguments. To change

a certain value, assign a new value to that element using its key. To remove a key/ value pair, call the unset() function on it.
### Note: A short array syntax exists which replaces array() with []. The array()

### function returns an array. Each of the arguments with which the function

was invoked becomes an element in the array (in the order they were passed in). <?php $array = array( "foo" => "bar", "bar" => "foo", // Using the short array syntax $array = [ "foo" => "bar", "bar" => "foo", This example includes all variations of type casting of keys and overwriting of elements. <?php $array = array(
### 1  => 'a',

### '1'  => 'b', // the value "a" will be overwritten by "b"

1.5 => 'c', // the value "b" will be overwritten by "c"
-1 => 'd',
'01' => 'e', // as this is not an integer string it will NOT override the key for '1.5' => 'f', // as this is not an integer string it will NOT override the key for true => 'g', // the value "c" will be overwritten by "g" false => 'h',
### '' => 'i',

### null => 'j', // the value "i" will be overwritten by "j"

'k', // value "k" is assigned the key 2. This is because the largest integer key
### before that was 1

2 => 'l', // the value "k" will be overwritten by "l" var_dump($array);
### As mentioned above, if no key is speciﬁed, the maximum of the existing int

indices is taken, and the new key will be that maximum value plus 1 (but at least 0). If no int indices exist yet, the key will be 0 (zero).
### Note that the maximum integer key used for this need not currently exist in the

array. It need only have existed in the array at some time since the last time the array was re-indexed.
### We add elements to the end of an array by taking the variable name and

appending square brackets ([]), the assignment operator (=), and the element we
### want to add:

Associative arrays are collections of key=>value pairs. The key in an associative
### array must be either a string or an integer. The values held can be any type. We

use the => operator to associate a key with its value. We can remove a key=>value pair entirely using the PHP unset() function. Note: if the key used doesn’t exist in the array, then nothing happens.
### When we add an element to an array without specifying a key (e.g. using

array_push()), PHP will associate it with the “next” integer key. If no integer keys have been used, it will associate it with the key 0, otherwise it will associate it
### one more than the largest integer used thus far

### The union (+) operator takes two array operands and returns a new array with

any unique keys from the second array appended to the first array. However due
### to the tricky nature of the union operator, if the arrays been combined have

same keys or index, the operand from the left takes precedence.
ITERABLES
### Iterable can be used as a parameter type to indicate that a function requires a

set of values, but does not care about the form of the value set since it will be used with foreach. If a value is not an array or instance of Traversable, a TypeError will be thrown.
### An iterable is any value which can be looped through with a foreach() loop. The

### iterable pseudo-type was introduced in PHP 7.1, and it can be used as a data

type for function arguments and function return values. All arrays are iterables, so any array can be used as an argument of a function that requires an iterable.
### Iterators - Any object that implements the Iterator interface can be used as an

argument of a function that requires an iterable. An iterator contains a list of items and provides methods to loop through them. It
### keeps a pointer to one of the elements in the list. Each item in the list should

have a key which can be used to find the item. An iterator must have these methods: current() - Returns the element that the pointer is currently
### pointing to. It can be any data type

key() Returns the key associated with the current element in
### the list. It can only be an integer, ﬂoat, boolean or string

next() Moves the pointer to the next element in the list rewind() Moves the pointer to the first element in the list valid() If the internal pointer is not pointing to any element
### (for example, if next() was called at the end of the list), this

### should return false. It returns true in any other case

Example #1 Iterable parameter type example <?php function foo(iterable $iterable) { foreach ($iterable as $value) { // ... Example #2 Iterable parameter default value example <?php function foo (iterable $iterable = []) { // ... } Example #3 Return an iterable <?php
function getIterable() :iterable { return ["a", "b", "c"]; $myIterable = getIterable(); foreach($myIterable as $item) { echo $item; } //prints abc
### Iterable can also be used as a return type to indicate a function will return an

iterable value. If the returned value is not an array or instance of Traversable, a TypeError will be thrown. Parameters declared as iterable may use null or an array as a default value.
### RESOURCES - A resource is a special variable, holding a reference to an external

resource. Resources are created and used by special functions. NULL The special null value represents a variable with no value. null is the only possible value of type null. A variable is considered to be null if: it has been assigned the constant null. it has not been set to any value yet. it has been unset(). Syntax There is only one value of type null, and that is the case-insensitive constant null. <?php $var = NULL; ?> OPERATORS
### Operations have an order of precedence meaning that certain types of operations

### in a chain will be evaluated before others: ﬁrst evaluated will be any operation

### wrapped in parenthesis (()), next exponents (**), then multiplication (*) and

division (/), and finally addition (+) and subtraction (-). The acronym PEMDAS can be a helpful way of remembering the order. Operation: Long Syntax: Short Syntax: Add $x = $x + $y $x += $y Subtract $x = $x - $y $x -= $y Multiply $x = $x * $y $x *= $y Divide $x = $x / $y $x /= $y
### Mod $x = $x % $y $x %= $y

Note: The increment/decrement operators only affect numbers and strings. Arrays,
objects, booleans and resources are not affected. Decrementing null values has no effect too, but incrementing them results in 1. Increment/decrement Operators Example Name Effect ++$a Pre-increment Increments $a by one, then returns $a. $a++ Post-increment Returns $a, then increments $a by one. --$a Pre-decrement Decrements $a by one, then returns $a. $a-- Post-decrement Returns $a, then decrements $a by one.
### Postﬁx form of X++, X— operator follows the rule  [ use-then-change ],

### Preﬁx form (++X, —X) follows the rule [ change-then-use ].

<?php $n = 3; echo $n--; // 3 echo --$n; //1 echo $n; //1
### Note : Pre-increment, which is written ++$variable, evaluates to the

### incremented value (PHP increments the variable before reading its value, thus

### the name 'pre-increment'). Post-increment, which is written $variable++

### evaluates to the original value of $variable, before it was incremented (PHP

increments the variable after reading its value, thus the name 'post- increment'). Note: The Argument spread operator (...) is not supported in assignments. // Show all errors error_reporting(E_ALL);
### Type Juggling - Automatic by PHP’s Parser

PHP does not require explicit type definition in variable declaration. In this case, the type of a variable is determined by the value it stores. That is to say, if a string is assigned to variable $var, then $var is of type string. If afterwards an int value is assigned to $var, it will be of type int.
### PHP may attempt to convert the type of a value to another automatically in

### certain contexts. The different contexts which exist are:

Numeric - This is the context when using an arithmetical operator. In this context if either operand is a float (or not interpretable as an int), both
### operands are interpreted as ﬂoats, and the result will be a ﬂoat. Otherwise, the

operands will be interpreted as ints, and the result will also be an int. String - This is the context when using echo, print, string interpolation, or the string concatenation operator. In this context the value will be interpreted as string.
### Logical -  This is the context when using conditional statements, the ternary

operator, or a logical operator. In this context the value will be interpreted as bool. Integral and string - This is the context when using a bitwise operators. In this context if all operands are of type string the result will also be a string. Otherwise, the operands will be interpreted as ints, and the result will also be an int. Comparative Function Note: When a value needs to be interpreted as a different type, the value itself does not change types.
### Type Casting - Manually by the User

### Type casting converts the value to a chosen type by writing the type within

parentheses before the value to convert. To force a variable to be evaluated as a certain type, see the section on Type casting. To change the type of a variable, see the settype() function. <?php
### $foo = 10;   // $foo is an integer

$bar = (bool) $foo; // $bar is a boolean The casts allowed are: (int) - cast to int (bool) - cast to bool (float) - cast to float (string) - cast to string (array) - cast to array (object) - cast to object
### (unset) - cast to NULL

### Type declarations can be added to function arguments, return values, and

class properties. They ensure that the value is of the specified type at call time, otherwise a TypeError is thrown.
### Note: When overriding a parent method, the child's method must match any

return type declaration on the parent. If the parent doesn't define a return type, then the child method may do so. Single types ¶ Type Description
Class/interface name The value must be an instanceof the given class or interface. self The value must be an instanceof the same class as the one in which the type declaration is used. Can only be used in classes. parent The value must be an instanceof the parent of the class in which the type declaration is used. Can only be used in classes. array The value must be an array. callable The value must be a valid callable. Cannot be used as a class property type declaration. bool The value must be a boolean value. float The value must be a floating point number. int The value must be an integer. string The value must be a string. iterable The value must be either an array or an instanceof Traversable. object The value must be an object. mixed The value can be any value.
## Php Functions & Return Statements

### Whenever a function is assigned to a variable, we are indirectly assigning the

return value of the function to that variable.
Function myFunction() { return “value”;}
### $thisMyFunction = myFunction();

### We deﬁned the function myFunction(). Next, we deﬁned the variable

$thisMyFunction and assigned as its value the result of invoking the myFunction() function. This actually did two things. It executed the function and also assigned
### “The return value of the myFunction().” to $thisMyFunction variable. Assigning a

function to a variable is indirectly assigning the return value of that said function to the variable declared.
### X The return keyword immediately stops a function. This means that any code

### after a return won’t run. When a computer encounters a function invocation, it

### will execute the code in the function’s body and then evaluate to the function’s

### returned value. We need to think of functions as both what they do (the

instructions in their code block) and what they return.
### X Returning NULL - Any function without a return statement returns a special

value NULL. NULL is a special data type that stands for the absence of a value.
### X Deﬁning Parameters & Arguments -  When we deﬁne a function, we can also

### deﬁne parameters. A parameter is a variable which serves as a placeholder

### throughout the function’s code block. When the function is invoked, it’s invoked

### with a speciﬁc value. As the computer executes the function, it replaces each

occurrence of the parameter with the value that was passed in. The actual value passed in is known as an argument.
### X Default Arguments - If we tried to invoke a function declared with a

parameter without an argument, it would cause an error; therefore we use default arguments to curb such errors. function myFunction($param = “argument”) { }.
### X Pass By Reference - We can invoke functions with variables or with values

directly. When we invoke a function with a variable as its argument, it’s as if we’re assigning the value held by that variable to the function’s parameter. We assign a
### copy of the value held by the argument variable. The variable argument and the

### parameter are distinct entities; changes made inside the function to the

### parameter will not affect the variable that was passed in. If we do want to make

### permanent changes to a variable within a function, we can prepend the parameter

### name with the reference sign (&). In this way, we assign the parameter to be an

### alias for the argument variable. Both will refer to the same spot in memory, and

changes to the parameter within the function will permanently affect the argument variable. function addX ($param) function addXPermanently (&$param) $param = $param . "X"; $param = $param . "X"; echo $param; echo $param; $word = "Hello"; $word = "Hello"; addX($word); // Prints: HelloX addXPermanently($word); // Prints: HelloX echo $word; // Prints: Hello
### echo $word; // Prints: HelloX

X Variable Scope - The scope of a variable is the context within which it is defined. In PHP global variables must be declared global inside a function if they are going to be used in that function. An error (Undefined variable). This is due to variable scope. Each function has its
### own local scope. This means that any variables deﬁned within the function’s code

block can only be accessed within the code block itself.
### However, if many functions depend on the same piece of information, it can be

### beneﬁcial to have a variable that can be accessed anywhere without being passed

in. To do this, we have to use the global keyword to tell PHP to look in the global scope for the variable, instead of the local scope of the function. When using this
### pattern, it becomes slightly more difﬁcult to determine what information this

function depends on. Make sure to consider this trade-off when implementing your own functions.
### Note that the global keyword is not used when invoking functions. Once a

function has been defined, it can be used within the same code block or even
within other function code blocks.
### Intro to Built-in PHP Functions

### *gettype() function takes a variable as its argument and returns a string value

representing the data type of the argument.
### *var_dump() function also takes a variable argument. It prints details about the

argument it receives. I call it dump details of variables.
- strrev() function takes in a string as its argument and returns a string with all
of the characters of the original string in reverse order.
- strtolower() function to transform an argument string into all lowercase letters
*str_repeat(stringVariable, #) function takes a string as its first argument and a
number as its second. It returns a string containing the argument string repeated the argument number of times.
### *substr_count() function returns the number of instances of a substring within a

### string. It takes two arguments, the string to search through—sometimes called

### the haystack— and the string to search for—sometimes called the needle

### *abs() function returns the absolute value of its number argument:

### *round() function which returns the nearest integer to its number argument

### *The rand() function returns a random integer. We have some ﬂexibility with how

### we invoke it. Invoking rand() with no arguments will return a number between 0

and the largest number our current environment will allow;
### Predeﬁned VARIABLE / SUPERGLOBALS

### There are 12 predeﬁned variables in php 8

### Some predeﬁned variables in PHP are "superglobals", which means that they are

### always accessible, regardless of scope - and you can access them from any

### function, class or ﬁle without having to do anything special. When the front end

### client makes a request to a backend PHP server, several superglobals related to

### the request are available to the PHP script. Superglobals are automatic global

variables which are available in all scopes throughout a script.
## 1.$Globals 2.$_Server 3.$_Request 4.$_Files

## 5.$_Env 6.$_Session 7.$_Cookie 8.$_Get

### 9.$_POST *10.$http_response_header *11.$argc *12.$argv

### $GLOBALS — References all variables available in global scope. An associative

### array containing references to all variables which are currently deﬁned in the

global scope of the script. The variable names are the keys of the array.
### $_SERVER is an array containing information such as headers, paths, and

### script locations. The entries in this array are created by the web server,

### therefore there is no guarantee that every web server will provide any of

### these; servers may omit some, or provide others not listed here. Note: When

running PHP on the command line most of these entries will not be available
or have any meaning. $_GET is an ASSOCIATIVE array of variables passed to the current script via the URL parameters.
### $_POST is an ASSOCIATIVE array of variables passed to the current script

### via the HTTP POST method when using application/x-www-form-urlencoded or

### multipart/form-data as the HTTP Content-Type in the request.  GET vs. POST

### Both GET and POST create an associative array (e.g. array( key1 => value1,

### key2 => value2, key3 => value3, ...)). This array holds key/value pairs, where

### keys are the names of the form controls and values are the input data from

### the user. Both GET and POST are treated as $_GET and $_POST. These are

### superglobals, which means that they are always accessible, regardless of

### scope - and you can access them from any function, class or ﬁle without

### having to do anything special. Using the Action Attribute - Action attribute

specifies a relative URL, you can also enter the name of a PHP file in the same directory as the current one.
### $_REQUEST - HTTP Request variables is a PHP super global variable which is

used to collect data after submitting an HTML form. This contains the contents of $_GET, $_POST, and $_COOKIE.
### $_COOKIE — HTTP Cookies An associative array of variables passed to the

### current script via HTTP Cookies. A cookie is created with the setcookie()

### function. Syntax -> setcookie(name, value, expire, path, domain, secure,

### httponly); Only the name parameter is required. All other parameters are

optional. Note: The setcookie() function must appear BEFORE the <html> tag.
### Note: The value of the cookie is automatically URLencoded when sending the

cookie, and automatically decoded when received (to prevent URLencoding, use setrawcookie() instead).
### $_ENV — Environment variables, An associative array of variables passed to

### the current script via the environment method. These variables are imported

### into PHP's global namespace from the environment under which the PHP

### parser is running. Many are provided by the shell under which PHP is running

### and different systems are likely running different kinds of shells, a deﬁnitive

### list is impossible. Please see your shell's documentation for a list of deﬁned

### environment variables. Other environment variables include the CGI variables,

placed there regardless of whether PHP is running as a server module or CGI processor.
### $argc — The number of arguments passed to script, Contains the number of

arguments passed to the current script when running from the command line.
### Note: The script's ﬁlename is always passed as an argument to the script,

### therefore the minimum value of $argc is 1. This is also available as

$_SERVER['argc'] when using php on web server.
### $argv — Array of arguments passed to script, Contains an array of all the

arguments passed to the script when running from the command line. Note:
10.
11.
### The ﬁrst argument $argv[0] is always the name that was used to run the

script. This is also available as $_SERVER['argv’] when using php on web server.
### $_Files - This feature lets people upload both text and binary ﬁles. With

### PHP's authentication and ﬁle manipulation functions, you have full control over

who is allowed to upload and what is to be done with the file once it has been uploaded.
### <!-- The data encoding type[enctype] MUST be speciﬁed as below -->

### <form enctype="multipart/form-data" action="__URL__" method="POST">

### <!-- MAX_FILE_SIZE must precede the ﬁle input ﬁeld -->

### <input type="hidden" name="MAX_FILE_SIZE" value="30000" />

### <!-- Name of input element determines name in $_FILES array -->

### Send this ﬁle: <input name="userﬁle" type="ﬁle" />

<input type="submit" value="Send File" /> </form> Note: Be sure your file upload form has attribute enctype="multipart/form-data" otherwise the file upload will not work.
### The global $_FILES will contain all the uploaded ﬁle information. Its contents

### from the example form is as follows. Note that this assumes the use of the ﬁle

upload name userfile, as used in the example script above. This can be any name.
### The __URL__ in the above example should be replaced, and point to a PHP ﬁle

### $_SESSION - This PHP global variable is used to set session variables. A

### session is a way to store information (in variables) to be used across multiple

pages. Unlike a cookie, the information is not stored on the users computer.
### When you work with an application, you open it, do some changes, and then

### you close it. This is much like a Session. The computer knows who you are. It

### knows when you start the application and when you end. But on the internet

### there is one problem: the web server does not know who you are or what you

### do, because the HTTP address doesn't maintain state. Session variables solve

this problem by storing user information to be used across multiple pages (e.g. username, favorite color, etc). By default, session variables last until the user
### closes the browser. So; Session variables hold information about one single

### user, and are available to all pages in one application. A session is started

### with the session_start() function, and must be the very ﬁrst thing in your

### document. Before any HTML tags. All session variable values are stored in the

### global $_SESSION variable. To remove all global session variables and destroy

the session, use session_unset() and session_destroy()
## Classes And Objects

A class may contain its own constants, variables (called "properties"), and functions (called "methods").
### Once the class is deﬁned, we can create speciﬁc instances of it—as many as we

### want! These instances of the class are called objects. Since objects are speciﬁc

instances of a class, the process of creating them is called instantiation. In PHP, objects are instantiated using the new keyword followed by the class name and parentheses. We interact with an object’s properties using the object operator (->) followed by the name of the property (without the dollar sign, $), THIS SYNTAX CAN BE
## Used To Assign Values And Access Existing Values Of Object

## Properties.

### The pseudo-variable $this refers to the current object and it’s available when a

### method is called from within an object context; when we invoke this method,

$this refers to the specific object that called the method, $this is the value of the calling object.
### where property is the name of the property, Within class methods non-static

properties may be accessed by using -> (Object Operator): $this->property.
### Declaring class properties or methods as static makes them accessible without

needing an instantiation of the class. These can also be accessed statically within an instantiated class object { }.
### Because static methods are callable without an instance of the object created,

the pseudo-variable $this is not available inside methods declared as static. Static
### properties & methods are accessed by using the scope resolution operator

(Double Colon :: ) self::$property from inside the class definition { }, and cannot be accessed through the object operator (->). To call a static method from a child class, use the parent:: keyword inside the
### child class { }

Class Constants - Constants cannot be changed once it is declared.
### Class constants can be useful if you need to deﬁne some constant data within a

### class. A class constant is declared inside a class with the const keyword. Class

constants are case-sensitive. However, it is recommended to name the constants in all uppercase letters. We can access a constant from outside the class { } by using
### the class name followed by the scope resolution operator (::) followed by the

### constant name. Or, we can access a constant from inside the class by using the

self keyword followed by the scope resolution operator (::) followed by the constant name.
### PHP - class instanceof

You can use the instanceof keyword to check if an object belongs to a specific class: <?php
$apple = new Fruit(); var_dump($apple instanceof Fruit); Class Methods are frequently used to interact with an object’s properties in a defined manner.
### Methods are deﬁned with the same syntax we use when declaring functions

### (except they are deﬁned within the curly brackets of a class).  Methods are

accessed in a similar fashion to properties, using the object operator (->), but in order to invoke them, use parentheses () at the end.
### Class Constructor Method - Constructors are ordinary methods which are called

### during the instantiation of their corresponding object. As such, they may deﬁne

### an arbitrary number of arguments, which may be required, may have a type, and

### may have a default value. Constructor arguments are called by placing the

### arguments in parentheses after the class name. . This method is automatically

### called when an object is instantiated. A constructor method is deﬁned with the

### special method name __construct(). Which can also have parameters, and

### correspond to arguments passed when using the new keyword.  Note: Keep in

### mind that the number of arguments used when instantiating the object must

### match the number of parameters in the constructor deﬁnition otherwise PHP will

### throw an error. Note: If there are no arguments to be passed to the class's

constructor, parentheses after the class name may be omitted.
### The __destruct Function

### A destructor is called when the object is destructed or the script is stopped or

exited. If you create a __destruct() function, PHP will automatically call this function at the end of the script. Notice that the destruct function starts with two underscores (__)!
### Class Inheritance - To deﬁne a class that inherits from another, we use the

### keyword extends. It is not possible to extend multiple classes; a class can only

inherit from one base class. when extending a class, the subclass inherits all of the public and protected methods, properties and constants from the parent class.
### Unless a class overrides those methods, they will retain their original

functionality. Private methods of a parent class are not accessible to a child class. As a result, child classes may reimplement a private method themselves without regard for normal inheritance rules. class ChildClass extends ParentClass {
Class Overriding / Overloading Methods - Sometimes, we want to change how
### methods behave for subclasses from the original parent deﬁnition. This is called

### overriding a method. To do this, deﬁne a new method within the subclass with the

### same name as the parent method. We can call the parent’s deﬁnition of the

method within the subclass using parent:: followed by the method name. The inherited constants, methods, and properties can be overridden by redeclaring
### them with the same name deﬁned in the parent class. However, if the parent

### class has deﬁned a method or constant as ﬁnal, they may not be overridden. It is

possible to access the overridden methods or static properties by referencing
### them with parent::

Note: The final keyword can be used to prevent class inheritance or to prevent method overriding.
### Class Visibility - There are three levels of visibility for class members:

### public (default) - accessible from outside of the class

### protected - only accessible within the class { } or its descendants

### private - only accessible within the deﬁning class { }

A property or method declared without a Visibility modifier will be declared as public.
### A public visibility means members can be accessed from within the object or from

### outside it. But sometimes we’ll want a member to only be accessible from within

### the object. To do this, we can declare this member private, However A class’s

### private members can only be accessed using methods within that parent class

### itself. This isn’t usually the desired effect when we have subclasses. To allow

members to be accessed from within child classes, we can set the visibility within
### the parent class to protected rather than private. This enables child classes to

access these properties and methods internally { } while still preventing them from being accessed externally.
### Class Getters and Setters

The concept of only accessing properties through methods is commonly referred to as using getters and setters.
### We can add logic to the setter to ensure that the value being passed in is

formatted properly, We can also use the getter to format values as they are passed out of the object. For example: class Pet { private $name; function setName($name) { $this->name = $name; function getName() {
return $this->name;
### Scope Resolution Operator (::) or in simpler terms, the double colon. - is a

token that allows access to static, constant, and overridden properties or methods of a class.
### Three special keywords -> self, parent and static are used to access properties

or methods from inside the class definition.
### EXCEPTIONS - An exception is an object that describes an error or

### unexpected behaviour of a PHP script. Exceptions are thrown by many PHP

### functions and classes. User deﬁned functions and classes can also throw

exceptions. Exceptions are a good way to stop a function when it comes across data that it cannot use.
### The throw statement allows a user deﬁned function or method to throw an

### exception. When an exception is thrown, the code following it will not be

executed. If an exception is not caught, a fatal error will occur with an "Uncaught Exception" message.
### To avoid the error from the example above, we can use the try...catch statement

to catch exceptions and continue the process. Syntax -> try { code that can throw exceptions
### } catch(Exception $e) {

code that runs when an exception is caught
### The catch block indicates what type of exception should be caught and the name

### of the variable which can be used to access the exception. In the syntax above,

the type of exception is Exception and the variable name is $e.
### Syntax -> new Exception(message, code, previous)

### The Exception Object contains information about the error or unexpected

### behaviour that the function encountered. Exceptions are used by functions and

methods to send information about errors and unexpected behaviour. Parameter && Description message Optional. A string describing why the exception was thrown
code Optional. An integer that can be used used to easily distinguish this exception from others of the same type previous Optional. If this exception was thrown in a catch block of another exception, it is recommended to pass that
### exception into this parameter

### Methods - When catching an exception, the following table shows some of the

methods that can be used to get information about the exception: Method && Description getMessage() Returns a string describing why the exception was thrown getPrevious() If this exception was triggered by another one, this method returns the previous exception. If not, then it returns null getCode() Returns the exception code getFile() Returns the full path of the file in which the exception was thrown getLine() Returns the line number of the line of code which threw the exception
### PHP & MySQL Database - With PHP, you can connect to and manipulate

### databases. MySQL is the most popular database system used with PHP. The data

in a MySQL database are stored in tables. A table is a collection of related data, and it consists of columns and rows. Databases are useful for storing information categorically. Prepared Statements protect from SQL injection, and are very important for web application security. Three ways of working with PHP and MySQL: MySQLi (object-oriented) MySQLi (procedural) PDO (PHP Data Objects)
### Prepared Statements and Bound Parameters

### A prepared statement is a feature used to execute the same (or similar) SQL

statements repeatedly with high efficiency.
### Prepared statements basically work like this:

Prepare: An SQL statement template is created and sent to the database. Certain values are left unspecified, called parameters (labeled "?"). Example:
### INSERT INTO MyGuests VALUES(?, ?, ?)

### The database parses, compiles, and performs query optimization on the SQL

### statement template, and stores the result without executing it

### Execute: At a later time, the application binds the values to the parameters,

### and the database executes the statement. The application may execute the

### statement as many times as it wants with different values

Compared to executing SQL statements directly, prepared statements have three
### main advantages:

### Prepared statements reduce parsing time as the preparation on the query is

### done only once (although the statement is executed multiple times)

### Bound parameters minimize bandwidth to the server as you need send only

### the parameters each time, and not the whole query

### Prepared statements are very useful against SQL injections, because

parameter values, which are transmitted later using a different protocol, need not
### be correctly escaped. If the original statement template is not derived from

external input, SQL injection cannot occur.


---

*Document converted from PDF: 🔐PHP DOCUMENTATION.pdf*
