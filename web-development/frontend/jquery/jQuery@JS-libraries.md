# jQuery@JS-libraries

## Summary

jQuery@JS-libraries What is jQuery. jQuery is a lightweight, "write less, do more", JavaScript library. The jQuery reference contains a list of all jQuery selectors, methods, properties and events, along with examples. accomplish, and wraps them into methods that you can call with a single line of code.

## Table of Contents

  - [(https://overapi.com/jquery)](#httpsoverapicomjquery)
  - [jQuery takes a lot of common tasks that require many lines of JavaScript code to](#jquery-takes-a-lot-of-common-tasks-that-require-many-lines-of-javascript-code-to)
  - [Let’s use Legos as an analogy for understanding how jQuery works. With an](#lets-use-legos-as-an-analogy-for-understanding-how-jquery-works-with-an)
  - [inﬁnite number of Legos, you could build an entire city — of course, this would](#inﬁnite-number-of-legos-you-could-build-an-entire-city-of-course-this-would)
  - [take a long time. What if you were given pre-made Lego buildings, Lego roads,](#take-a-long-time-what-if-you-were-given-pre-made-lego-buildings-lego-roads)
  - [jQuery CDN](#jquery-cdn)
  - [Google is an example of someone who host jQuery](#google-is-an-example-of-someone-who-host-jquery)
  - [Ref(https://developers.google.com/speed/libraries)](#refhttpsdevelopersgooglecomspeedlibraries)
  - [<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/](#script-srchttpscodejquerycomjquery-360minjs-integritysha256)
  - [crossorigin="anonymous"></script>](#crossoriginanonymousscript)
  - [If your website contains a lot of pages, and you want your jQuery functions to](#if-your-website-contains-a-lot-of-pages-and-you-want-your-jquery-functions-to)
  - [<script src="my_jquery_functions.js"></script>](#script-srcmy_jquery_functionsjsscript)
  - [some action on the element(s). It has become common practice to link the main](#some-action-on-the-elements-it-has-become-common-practice-to-link-the-main)
  - [JavaScript ﬁle at the bottom of the HTML document because a good deal of the](#javascript-ﬁle-at-the-bottom-of-the-html-document-because-a-good-deal-of-the)
  - [content of the script will require that the dependencies, style sheets and](#content-of-the-script-will-require-that-the-dependencies-style-sheets-and)
  - [elements exist before the browser can run the JavaScript that uses and](#elements-exist-before-the-browser-can-run-the-javascript-that-uses-and)
  - [references those things It is good practice to wait for the document(DOM) to be](#references-those-things-it-is-good-practice-to-wait-for-the-documentdom-to-be)
  - [fully loaded and ready before working with it. This also allows you to have your](#fully-loaded-and-ready-before-working-with-it-this-also-allows-you-to-have-your)
  - [JavaScript code in between <script> tags before the body of your document, in](#javascript-code-in-between-script-tags-before-the-body-of-your-document-in)
  - [jQuery uses CSS syntax to](#jquery-uses-css-syntax-to)
  - [jQuery - The noConﬂict() Method](#jquery-the-noconﬂict-method)
  - [jQuery uses the $ sign as a shortcut for jQuery….However if other frameworks/](#jquery-uses-the-sign-as-a-shortcut-for-jqueryhowever-if-other-frameworks)
  - [libraries use the same shortcut, one might stop working..this can be bypassed](#libraries-use-the-same-shortcut-one-might-stop-workingthis-can-be-bypassed)
  - [choosing…var jq = $.noConﬂict();](#choosingvar-jq-noconﬂict)
  - [If you have a block of jQuery code which uses the $ shortcut and you do not](#if-you-have-a-block-of-jquery-code-which-uses-the-shortcut-and-you-do-not)
  - [want to change it all, you can pass the $ sign in as a parameter to the ready](#want-to-change-it-all-you-can-pass-the-sign-in-as-a-parameter-to-the-ready)
  - [jQuery Events](#jquery-events)
  - [$(“ “).event(function() { *action/execution/effects to perform(effects, DOM](#eventfunction-actionexecutioneffects-to-performeffects-dom)
  - [jQuery Effects](#jquery-effects)
  - [Ref(https://www.w3schools.com/jquery/jquery_ref_effects.asp)](#refhttpswwww3schoolscomjqueryjquery_ref_effectsasp)
  - [$(selector).effects(speed, callback); The optional speed parameter speciﬁes the](#selectoreffectsspeed-callback-the-optional-speed-parameter-speciﬁes-the)
  - [speed of the hiding/showing, and can take the following values: "slow", "fast”](#speed-of-the-hidingshowing-and-can-take-the-following-values-slow-fast)
  - [(with quotes), or milliseconds(no quotes), The optional callback parameter is a](#with-quotes-or-millisecondsno-quotes-the-optional-callback-parameter-is-a)
  - [properties to be animated as a parameter. {params}](#properties-to-be-animated-as-a-parameter-params)
  - [$(selector).animate({params}, speed, callback);](#selectoranimateparams-speed-callback)
  - [By default, all HTML elements have a static position, and cannot be moved. To](#by-default-all-html-elements-have-a-static-position-and-cannot-be-moved-to)
  - [manipulate the position, remember to ﬁrst set the CSS position property of the](#manipulate-the-position-remember-to-ﬁrst-set-the-css-position-property-of-the)
  - [element to: “relative”, “ﬁxed”, or “absolute”! All property names must be](#element-to-relative-ﬁxed-or-absolute-all-property-names-must-be)
  - [camel-cased when used with the animate() method just like in Vanilla Javascript](#camel-cased-when-used-with-the-animate-method-just-like-in-vanilla-javascript)
  - [DOM manipulation……..jQuery comes with queue functionality for animations. This](#dom-manipulationjquery-comes-with-queue-functionality-for-animations-this)
  - [jQuery Callback Functions](#jquery-callback-functions)
  - [JavaScript statements are executed line by line. However, with effects, the next](#javascript-statements-are-executed-line-by-line-however-with-effects-the-next)
  - [line of code can be run even though the effect is not ﬁnished. This can create](#line-of-code-can-be-run-even-though-the-effect-is-not-ﬁnished-this-can-create)
  - [executed after the current effect is 100% ﬁnished. A callback function is](#executed-after-the-current-effect-is-100-ﬁnished-a-callback-function-is)
  - [jQuery Method Chaining](#jquery-method-chaining)
  - [Chaining allows us to run multiple jQuery methods (on the same element) within a](#chaining-allows-us-to-run-multiple-jquery-methods-on-the-same-element-within-a)
  - [Ref(https://www.w3schools.com/jquery/jquery_ref_html.asp)](#refhttpswwww3schoolscomjqueryjquery_ref_htmlasp)
  - [jQuery methods for DOM manipulation](#jquery-methods-for-dom-manipulation)
  - [(excluding HTML markup)](#excluding-html-markup)
  - [HTML markup)](#html-markup)

---

## Content

jQuery@JS-libraries What is jQuery? jQuery is a lightweight, "write less, do more", JavaScript library. The jQuery reference contains a list of all jQuery selectors, methods, properties and events, along with examples. (https://www.w3schools.com/jquery/jquery_ref_overview.asp) Cheatsheets
### (https://overapi.com/jquery)

The purpose of jQuery is to make it much easier to use JavaScript on your website.
### jQuery takes a lot of common tasks that require many lines of JavaScript code to

accomplish, and wraps them into methods that you can call with a single line of code. jQuery also simplifies a lot of the complicated things from JavaScript, like AJAX calls and DOM manipulation.
### Let’s use Legos as an analogy for understanding how jQuery works. With an

### inﬁnite number of Legos, you could build an entire city — of course, this would

### take a long time. What if you were given pre-made Lego buildings, Lego roads,

Lego parks, etc? You could build a city much faster. The jQuery library contains the following features: HTML/DOM manipulation CSS manipulation HTML event methods Effects and animations AJAX Utilities
### The Downloaded jQuery library is a single JavaScript ﬁle, and you reference

it with the HTML <script> tag (notice that the <script> tag should be inside the <head> section): <head> <script src="jquery-3.6.0.min.js"></script> </head> Tip: Place the downloaded file in the same directory as the pages where you wish to use it.
### jQuery CDN

If you don't want to download and host jQuery yourself, you can include it from a CDN (Content Delivery Network).
### Google is an example of someone who host jQuery

### Ref(https://developers.google.com/speed/libraries)

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/ jquery.min.js"></script> Or https://code.jquery.com/ itself.
### <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/

xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
### crossorigin="anonymous"></script>

### The integrity and crossorigin properties in the example ensure the ﬁle is

delivered without any third-party manipulation.
### If your website contains a lot of pages, and you want your jQuery functions to

be easy to maintain, you can put your jQuery functions in a separate .js file. However, sometimes it is preferable to place them in a separate file, like this (use
### the src attribute to refer to the .js ﬁle)

### <script src="my_jquery_functions.js"></script>

### The jQuery syntax is tailor-made for selecting HTML elements and performing

### some action on the element(s). It has become common practice to link the main

### JavaScript ﬁle at the bottom of the HTML document because a good deal of the

### content of the script will require that the dependencies, style sheets and

### elements exist before the browser can run the JavaScript that uses and

### references those things It is good practice to wait for the document(DOM) to be

### fully loaded and ready before working with it. This also allows you to have your

### JavaScript code in between <script> tags before the body of your document, in

### the head section. However This method allows us to execute our functions

when the document is fully loaded and can be included before the body. $(document).ready(function(){ // jQuery methods go here... }); The method above can be used in between<script> tags in HTML file, or separate main.js file. jQuery Syntax Basic syntax is $(selector).action() which is based on document.querySelector(“ ”)
$ sign to define/access jQuery $("*") Selects all elements
$(this) Selects the current HTML element
### this keyword

A (selector) to "query (or find)" HTML elements
### jQuery uses CSS syntax to

select elements(their name, id, classes, types, attributes, values of attributes and much more.) Check the reference link below. Ref(https://www.w3schools.com/jquery/jquery_ref_selectors.asp)
### jQuery - The noConﬂict() Method

### jQuery uses the $ sign as a shortcut for jQuery….However if other frameworks/

### libraries use the same shortcut, one might stop working..this can be bypassed

using noConfilct() method which releases the hold on the $ shortcut, You can still use the jQuery as $ in your code or simply swap it to any variable name of your
### choosing…var jq = $.noConﬂict();

this should be written before the $(document).ready(function(){ });.
### If you have a block of jQuery code which uses the $ shortcut and you do not

### want to change it all, you can pass the $ sign in as a parameter to the ready

method. This allows you to access jQuery using $, inside this function - outside of it, you will have to use "jQuery":
### jQuery Events

jQuery Effects are a group of methods in the jQuery library that are responsible for adding dynamic behavior to websites. jQuery events act as higher-order functions taking functions as arguments. $(“ “).on(“event”, function() {*action/execution/effects to perform(effects, DOM manipulation) });
### $(“ “).event(function() { *action/execution/effects to perform(effects, DOM

manipulation)*}); //if event hasn’t been specified in the HTML. Ref(https://www.w3schools.com/jquery/jquery_ref_events.asp) Mouse Events Keyboard Events Form Events Document/ Window Events click keypress submit load dblclick keydown change resize mouseenter keyup focus scroll mouseleave
blur unload
### jQuery Effects

Hide, Show, Toggle, Slide, Fade, and Animate
### Ref(https://www.w3schools.com/jquery/jquery_ref_effects.asp)

### $(selector).effects(speed, callback); The optional speed parameter speciﬁes the

### speed of the hiding/showing, and can take the following values: "slow", "fast”

### (with quotes), or milliseconds(no quotes), The optional callback parameter is a

function to be executed after the effect method completes. Some effects have an optional parameter of opacity from 0-1.
### The jQuery animate()  method however requires Single CSS or multiple CSS

### properties to be animated as a parameter. {params}

### $(selector).animate({params}, speed, callback);

### By default, all HTML elements have a static position, and cannot be moved. To

### manipulate the position, remember to ﬁrst set the CSS position property of the

### element to: “relative”, “ﬁxed”, or “absolute”! All property names must be

### camel-cased when used with the animate() method just like in Vanilla Javascript

### DOM manipulation……..jQuery comes with queue functionality for animations. This

means that if you write multiple animate() calls after each other, jQuery creates an "internal" queue with these method calls. Then it runs the animate calls ONE by ONE.
### The jQuery stop() method is used to stop animations or effects before it is

finished. It works for all jQuery effect functions, including sliding, fading and custom animations. $(selector).stop(stopAll, goToEnd);
### jQuery Callback Functions

### JavaScript statements are executed line by line. However, with effects, the next

### line of code can be run even though the effect is not ﬁnished. This can create

errors. To prevent this, you can create a callback function. A callback function is
### executed after the current effect is 100% ﬁnished. A callback function is

executed after the current effect is finished.
### jQuery Method Chaining

With jQuery, you can chain together actions/methods.
### Chaining allows us to run multiple jQuery methods (on the same element) within a

single statement. that allows us to run multiple jQuery commands, one after the other, on the same element(s). Tip: This way, browsers do not have to find the same element(s) more than once. To chain an action, you simply append the action to the previous action. jQuery DOM Manipulation
### Ref(https://www.w3schools.com/jquery/jquery_ref_html.asp)

One very important part of jQuery is the possibility to manipulate the DOM. jQuery comes with a bunch of DOM related methods that make it easy to access and manipulate elements and attributes. Just Like Vanilla javascript, where we had .innerHTML, .innerTextContent, .value…..
### jQuery methods for DOM manipulation

text() - Sets or returns the text content of selected elements
### (excluding HTML markup)

html() - Sets or returns the content of selected elements (including
### HTML markup)

val() - Sets or returns the value of form fields attr() method is used to get attribute values. Also allows you to set multiple attributes at the same time. Put them in { } curly braces.
### All of the also come with a callback function.The callback function has two

### parameters: the index-i of the current element in the list of elements selected

and the original (old) value. You then return the string you wish to use as the new value from the function.
### Add New HTML Content

append() - Inserts content at the end of the selected elements prepend() - Inserts content at the beginning of the selected elements after() - Inserts content after the selected elements before() - Inserts content before the selected elements Both the append() and prepend() methods can take an infinite number of new elements as parameters Remove Elements/Content
### To remove elements and content, there are mainly two jQuery methods:

remove() - Removes the selected element (and its child elements) empty() - Removes the child elements from the selected element
### The jQuery remove() method also accepts one parameter, which allows you to

filter the elements to be removed. The parameter can be any of the jQuery selector syntaxes.
### jQuery Manipulating CSS

jQuery has several methods for CSS manipulation. We will look at the following
methods:
### addClass() - Adds one or more classes to the selected elements

removeClass() - Removes one or more classes from the selected elements toggleClass() - Toggles between adding/removing classes from the
### selected elements

css("propertyname") - returns the value of the specified property css("propertyname","value”) - sets the style attribute & properties
### for the selected elements to the second parameter -“value”

css({"propertyname":"value","propertyname":"value",...}); curly braces.
### jQuery Dimension Methods

### jQuery has several important methods for working with dimensions:

To set dimensions using this methods below, their parameters are the specified values. The width() method sets or returns the width of an element (excludes padding, border and margin). The height() method sets or returns the height of an element (excludes padding, border and margin). The innerWidth() method returns the width of an element (includes padding). The innerHeight() method returns the height of an element (includes padding). The outerWidth() method returns the width of an element (includes padding and border). The outerHeight() method returns the height of an element (includes padding and border). What is Traversing? ref(https://www.w3schools.com/jquery/jquery_ref_traversing.asp)
### jQuery traversing, which means "move through", are used to "ﬁnd" (or select)

HTML elements based on their relation to other elements. Start with one selection
### and move through that selection until you reach the elements you desire. jQuery

### provides a variety of methods that allow us to traverse the DOM. The largest

category of traversal methods are tree-traversal. jQuery - AJAX Introduction
### Ref(https://www.w3schools.com/jquery/jquery_ref_ajax.asp)

### AJAX is the art of exchanging data with a server asynchronously, and updating

parts of a web page - without reloading the whole page. jQuery provides several methods for AJAX functionality.
### With the jQuery AJAX methods, you can request text, HTML, XML, or JSON from

### a remote server using both HTTP Get and HTTP Post - And you can load the

external data directly into the selected HTML elements of your web page! Method Description $.ajax() Performs an async AJAX request $.ajaxPrefilter() Handle custom Ajax options or modify existing options before each request is sent and before they are processed by $.ajax() $.ajaxSetup() Sets the default values for future AJAX requests $.ajaxTransport() Creates an object that handles the actual transmission of Ajax data $.get() Loads data from a server using an AJAX HTTP GET request $.getJSON() Loads JSON-encoded data from a server using a HTTP GET request $.parseJSON() Deprecated in version 3.0, use JSON.parse() instead. Takes a well-formed JSON string and returns the resulting JavaScript value $.getScript() Loads (and executes) a JavaScript from a server using an AJAX HTTP GET request $.param() Creates a serialized representation of an array or object (can be used as URL query string for AJAX requests) $.post() Loads data from a server using an AJAX HTTP POST request ajaxComplete() Specifies a function to run when the AJAX request completes ajaxError() Specifies a function to run when the AJAX request completes with an error
ajaxSend() Specifies a function to run before the AJAX request is sent ajaxStart() Specifies a function to run when the first AJAX request begins ajaxStop() Specifies a function to run when all AJAX requests have completed ajaxSuccess() Specifies a function to run when an AJAX request completes successfully load() Loads data from a server and puts the returned data into the selected element serialize() Encodes a set of form elements as a string for submission serializeArray() Encodes a set of form elements as an array of names and values


---

*Document converted from PDF: 🔐jQuery@JS-libraries.pdf*
