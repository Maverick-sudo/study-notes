# - -HyperText Markup Language Tutorial- -

## Summary

Element Syntax <tagname>Content</tagname> The <!DOCTYPE html> declaration defines that this document is an HTML5 document the visible contents, such as headings, paragraphs, images, hyperlinks, tables, lists, etc. The <h1> element defines a large heading Use the HTML <th> element to define a table heading/content of the table values.

## Table of Contents

  - [<!- -HyperText Markup Language Tutorial- ->](#hypertext-markup-language-tutorial)
  - [COmment SYntax. <!--...-->](#comment-syntax)
  - [browser's title bar or in the page's tab)](#browsers-title-bar-or-in-the-pages-tab)
  - [Table<table>/Table Head<th>/Table Body<tbody>/Table Row<tr>/Table Column/](#tabletabletable-headthtable-bodytbodytable-rowtrtable-column)
  - [Use the HTML <table> element to deﬁne a table](#use-the-html-table-element-to-deﬁne-a-table)
  - [Use the HTML <tbody> element to deﬁne table body](#use-the-html-tbody-element-to-deﬁne-table-body)
  - [Use the HTML <tr> element to deﬁne a table row](#use-the-html-tr-element-to-deﬁne-a-table-row)
  - [Use the HTML <td> element to deﬁne a table data](#use-the-html-td-element-to-deﬁne-a-table-data)
  - [Use the colspan attribute to make a cell span many columns](#use-the-colspan-attribute-to-make-a-cell-span-many-columns)
  - [Use the rowspan attribute to make a cell span many rows](#use-the-rowspan-attribute-to-make-a-cell-span-many-rows)
  - [Use the id attribute to uniquely deﬁne one table](#use-the-id-attribute-to-uniquely-deﬁne-one-table)
  - [Use the CSS border property to deﬁne a border](#use-the-css-border-property-to-deﬁne-a-border)
  - [Use the CSS border-collapse property to collapse cell borders](#use-the-css-border-collapse-property-to-collapse-cell-borders)
  - [Use the CSS padding property to add padding to cells](#use-the-css-padding-property-to-add-padding-to-cells)
  - [Use the CSS text-align property to align cell text](#use-the-css-text-align-property-to-align-cell-text)
  - [HTML head Elements](#html-head-elements)
  - [HTML Attributes](#html-attributes)
  - [All HTML elements can have attributes/ HTML elements use attributes to add](#all-html-elements-can-have-attributes-html-elements-use-attributes-to-add)
  - [extra detail or functionality to the element. Some familiar attributes may be](#extra-detail-or-functionality-to-the-element-some-familiar-attributes-may-be)
  - [<img src="url/jpg/gif” alt="alternatetext">](#img-srcurljpggif-altalternatetext)
  - [<audio src=“XXXX.mp3" type="audio/mp3" controls> </audio>](#audio-srcxxxxmp3-typeaudiomp3-controls-audio)
  - [<video src=“XYZ.mp4" controls loop autoplay> Video not supported </video>](#video-srcxyzmp4-controls-loop-autoplay-video-not-supported-video)
  - [Another tag that can be used to incorporate media content into a page is](#another-tag-that-can-be-used-to-incorporate-media-content-into-a-page-is)
  - [Use an Image as a Link](#use-an-image-as-a-link)
  - [“_blank”  - Opens the document in a new window or tab](#_blank-opens-the-document-in-a-new-window-or-tab)
  - [“_parent”  - Opens the document in the parent frame](#_parent-opens-the-document-in-the-parent-frame)
  - [Absolute URLs vs. Relative URLs](#absolute-urls-vs-relative-urls)
  - [Link to an Email Address](#link-to-an-email-address)
  - [Button as a link](#button-as-a-link)
  - [HTML Link Colors](#html-link-colors)
  - [You can change the link state colors, by using CSS:](#you-can-change-the-link-state-colors-by-using-css)
  - [HTML Links - Creating Bookmarks](#html-links-creating-bookmarks)
  - [Use the id attribute (id="value") to deﬁne bookmarks in a page](#use-the-id-attribute-idvalue-to-deﬁne-bookmarks-in-a-page)
  - [HTML Formatting Elements](#html-formatting-elements)
  - [<sup> - Superscript text](#sup-superscript-text)
  - [Use the style attribute for styling HTML elements](#use-the-style-attribute-for-styling-html-elements)
  - [<section class=“XXX”>.WRITE.</section>](#section-classxxxwritesection)
  - [<form action=“XYZ.html” method=“Post” target=“_blank/self/top/parent”>](#form-actionxyzhtml-methodpost-target_blankselftopparent)
  - [<label for=“YYY”>. WRITE. </label>](#label-foryyy-write-label)
  - [</datalist>](#datalist)
  - [submitting the form](#submitting-the-form)
  - [Client-side validations happen in the browser before information is sent to a](#client-side-validations-happen-in-the-browser-before-information-is-sent-to-a)
  - [server. Assigned to the <form> tag.  These quick checks help ensure that input](#server-assigned-to-the-form-tag-these-quick-checks-help-ensure-that-input)
  - [data is correct and safe for our servers. It also helps give users immediate](#data-is-correct-and-safe-for-our-servers-it-also-helps-give-users-immediate)
  - [Semantic HTML VS NON-Semantic HTML](#semantic-html-vs-non-semantic-html)
  - [Semantic elements provide information about the content between the opening](#semantic-elements-provide-information-about-the-content-between-the-opening)
  - [and closing tags.By using Semantic HTML, we select HTML elements based on](#and-closing-tagsby-using-semantic-html-we-select-html-elements-based-on)
  - [their meaning, not on how they are presented. Elements such](#their-meaning-not-on-how-they-are-presented-elements-such)
  - [<div id=“main”></div> VS <main></main>](#div-idmaindiv-vs-mainmain)
  - [<div id=“footer”></div> VS <footer></footer>](#div-idfooterdiv-vs-footerfooter)

---

## Content

### <!- -HyperText Markup Language Tutorial- ->

### The HTML element is everything from the start tag to the end tag:

Element Syntax <tagname>Content</tagname>
### COmment SYntax. <!--...-->

The <!DOCTYPE html> declaration defines that this document is an HTML5 document
### The <html> element is the root element of an HTML page

### The <head> element contains meta information about the HTML page

### The <title> element speciﬁes a title for the HTML page (which is shown in the

### browser's title bar or in the page's tab)

### The <body> element deﬁnes the document's body, and is a container for all

the visible contents, such as headings, paragraphs, images, hyperlinks, tables, lists, etc. The <h1> element defines a large heading
### The <p> element deﬁnes a paragraph

### Table<table>/Table Head<th>/Table Body<tbody>/Table Row<tr>/Table Column/

### Use the HTML <table> element to deﬁne a table

### Use the HTML <tbody> element to deﬁne table body

### Use the HTML <tr> element to deﬁne a table row

### Use the HTML <td> element to deﬁne a table data

Use the HTML <th> element to define a table heading/content of the table values. Use the HTML <caption> element to define a table caption </caption>. Before the <tbody>.
### Use the colspan attribute to make a cell span many columns

### Use the rowspan attribute to make a cell span many rows

### Use the id attribute to uniquely deﬁne one table

### Use the CSS border property to deﬁne a border

### Use the CSS border-collapse property to collapse cell borders

### Use the CSS padding property to add padding to cells

### Use the CSS text-align property to align cell text

Use the CSS border-spacing property to set the spacing between cells
### HTML head Elements

### The HTML <head> element is a container for the following elements :

[ <title>, <style>, <meta>, <link>, <script>, and <base>] or container for metadata (data about data) and is placed between the <html> tag and the <body> tag Metadata is not displayed Tag Description
<head> Defines information about the document <title> Defines the title of a document <base> Defines a default address or a default target for all links on a page(relative URLs) <link> Defines the relationship between a document and an external resource <meta> name=“charset/ description/author/viewport” Defines metadata about an HTML document used to specify the character set, page description, keywords, author of the document, and viewport settings. <script> Defines a client-side external or internal javaScript <style> Defines style information for a document
### HTML Attributes

### All HTML elements can have attributes/ HTML elements use attributes to add

### extra detail or functionality to the element. Some familiar attributes may be

href and src, but there are many more—including class and id!
### The src attribute of <img> speciﬁes the path to the image to be displayed;

alt - Specifies an alternate text for the image.
### <img src="url/jpg/gif” alt="alternatetext">

### <audio src=“XXXX.mp3" type="audio/mp3" controls> </audio>

### <video src=“XYZ.mp4" controls loop autoplay> Video not supported </video>

### Another tag that can be used to incorporate media content into a page is

### the <embed> tag, which can embed any media content including videos, audio ﬁles,

and gifs from an external source. It’s a self closing tag like <img>.
### Use an Image as a Link

<a> <img src=“image filepath” alt=“”> </a> Note: We used the <a> tag for link.
### The width and height attributes of <img> provide size information for images

### The alt attribute of <img> provides an alternate text for an image

The style attribute is used to add styles to an element, such as color, font, size, and more
### The lang attribute of the <html> tag declares the language of the Web page

### The title attribute deﬁnes some extra information about an element

### The href attribute of <a> speciﬁes the URL of the page the link goes to

The target attribute specifies where to open the linked document.
### The target attribute can have one of the following values:

“_self”  - Default. Opens the document in the same window/tab as it was clicked
### “_blank”  - Opens the document in a new window or tab

### “_parent”  - Opens the document in the parent frame

“_top”  - Opens the document in the full body of the window
### Absolute URLs vs. Relative URLs

An absolute URL (a full web https:// address) in the href attribute. A local link (a link to a page within the same website) is specified with a relative URL (without the "https://www" part). HTML Links -
### Link to an Email Address

<a href="mailto:someone@example.com"> Send email </a>
### Button as a link

<button onclick=“document file path”> </button>
### HTML Link Colors

By default, a link will appear like this (in all browsers): An unvisited link is underlined and blue A visited link is underlined and purple
### An active link is underlined and red

### You can change the link state colors, by using CSS:

A link can also be styled as a button, by using CSS: Inline Style Format of Link. <style> a : link/visited/hover/active {color/text-decoration/background-color/}
### HTML Links - Creating Bookmarks

### Use the id attribute (id="value") to deﬁne bookmarks in a page

Use the href attribute (href="#value") to link to the bookmark HTML Tag Reference <p> Defines a paragraph <hr> Defines a thematic change in the content <br> Inserts a single line break
10.
11.
12.
13.
14.
15.
16.
<pre> Defines pre-formatted text HTML Quotation and Citation Elements Tag Description <abbr> Defines an abbreviation or acronym <address> Defines contact information for the author/owner of a document <bdo> Defines the text direction <blockquote> Defines a section that is quoted from another source <cite> Defines the title of a work <q> Defines a short inline quotation
### HTML Formatting Elements

Formatting elements were designed to display special types of text: <b> - Bold text <strong> - Important text <i> - Italic text <em> - Emphasized text <mark> - Marked text <small> - Smaller text <del> - Deleted text <ins> - Inserted text <sub> - Subscript text
### <sup> - Superscript text

### Use the style attribute for styling HTML elements

Use background-color for background color Use color for text colors Use font-family for text fonts Use font-size for text sizes Use text-align for text alignment <!-- Write your comments here --> HTML List Tags Tag Description <ul> Defines an unordered list <ol> add type attribute to define the numbering type Defines an ordered list
<li> Defines a list item <dl> Defines a description list <dt> Defines a term in a description list <dd> Describes the term in a description list HTML Forms
### <section class=“XXX”>.WRITE.</section>

### <form action=“XYZ.html” method=“Post” target=“_blank/self/top/parent”>

The <form> element is a container for different types of input elements, such as: text area fields, checkboxes, radio buttons, submit buttons.
### <label for=“YYY”>. WRITE. </label>

### The for attribute of the <label> tag should be equal to the id attribute of

the <input> element to bind them together. <input type=“***” name=“” id=“yyy” value=“”> <datalist> <option value=“ ”></option>
### </datalist>

<textarea id=“” name=“” rows/col></textarea> Or <textarea></textarea> <input type=“submit” value=“submit”> </form> HTML Form Elements Tag Description <form> Defines an HTML form for user input <input> Defines an input control <textarea> Defines a multiline input control (text area) <label> Defines a label for an <input> element <fieldset> Groups related elements in a form <legend> Defines a caption for a <fieldset> element
<select> Defines a drop-down list <optgroup> Defines a group of related options in a drop-down list <option> Defines an option in a drop-down list <button> Defines a clickable button <datalist> Specifies a list of pre-defined options for input controls <output> Defines the result of a calculation <input type="text"> Displays a single-line text input field <input type="radio"> Displays a radio button (for selecting one of many choices) <input type="checkbox"> Displays a checkbox (for selecting zero or more of many choices) <input type="submit"> Displays a submit button (for submitting the form) <input type="button"> Displays a clickable button List of All <form> Attributes Attribute Description accept-charset Specifies the character encodings used for form submission action Specifies where to send the form- data when a form is submitted autocomplete Specifies whether a form should have autocomplete on or off enctype Specifies how the form-data should be encoded when submitting it to the server (only for method="post") method= Get/Post Specifies the HTTP method to use when sending form-data name Specifies the name of the form novalidate Specifies that the form should not be validated when submitted rel Specifies the relationship between a linked resource and the current document
target Specifies where to display the response that is received after
### submitting the form

### Client-side validations happen in the browser before information is sent to a

### server. Assigned to the <form> tag.  These quick checks help ensure that input

### data is correct and safe for our servers. It also helps give users immediate

feedback on what they need to fix instead of having to wait for a server to send back that information. They Include Required attribute Min & Max input for number attribute MinLength & max length attribute. Pattern attribute.
### Semantic HTML VS NON-Semantic HTML

### Semantic elements provide information about the content between the opening

### and closing tags.By using Semantic HTML, we select HTML elements based on

### their meaning, not on how they are presented. Elements such

as <div> and <span> are not semantic elements since they provide no context as to what is inside of those tags. <div id=“header”></div> VS <header></header> <div id=“nav”></div> VS <nav></nav>
### <div id=“main”></div> VS <main></main>

### <div id=“footer”></div> VS <footer></footer>

<header>, <nav> , <main> and <footer> create the basic structure of the webpage.
### <section> deﬁnes elements in a document, such as chapters, headings, or any

other area of the document with the same theme. <article> holds content that makes sense on its own such as articles, blogs, comments, etc. <aside> contains information that is related to the main content, but not required in order to understand the dominant information.
Below is a list of some of the semantic elements in HTML. Tag Description <article> Defines independent, self- contained content <aside> Defines content aside from the page content <details> Defines additional details that the user can view or hide <figcaption> Defines a caption for a <figure> element <figure> Specifies self-contained content, like illustrations, diagrams, photos, code listings, etc. <footer> Defines a footer for a document or section <header> Specifies a header for a document or section <main> Specifies the main content of a document <mark> Defines marked/highlighted text <nav> Defines navigation links <section> Defines a section in a document <summary> Defines a visible heading for a <details> element
<time> Defines a date/time
### There are two display values: block and inline

A block-level element always starts on a new line and takes up the full width available An inline element does not start on a new line and it only takes up as much
### width as necessary; for instance

The <div> element is a block-level and is often used as a container for other
### HTML elements

The <span> element is an inline container used to mark up a part of a text, or
### a part of a document

Note: An inline element cannot contain a block-level element! Fun Fact: Emojis are characters from the UTF-8 character set:
Emojis look like images, or icons, but they are not. They are letters (characters) from the UTF-8 (Unicode) character set. UTF-8 covers almost all of the characters and symbols in the world.
### A Unifrom Rresource Locator is another word for a web address. A URL can be

composed of words (e.g. w3schools.com), or an Internet Protocol (IP) address (e.g. 192.68.20.50). Most people enter the name when surfing, because names are easier to remember than numbers. Note: Only MP4, WebM, and Ogg video are supported by the HTML standard. Note: Only MP3, WAV, and Ogg audio are supported by the HTML standard.
### Playing a YouTube Video in HTML

To play your video on a web page, do the following:
### Upload the video to YouTube

### Take a note of the video id (like tgbNymZ7vqY)

### Deﬁne an <iframe> element in your web page

### Let the src attribute point to the video URL

### Use the width and height attributes to specify the dimension of the player

### Add any other parameters to the URL such as autoplay=1 & mute=1 &

controls=0 & loop=1 after putting ? Sign Web Address Syntax scheme://prefix.domain:port/path/filename
### Explanation:

scheme - defines the type of Internet service (most common is http or https)
### preﬁx - deﬁnes a domain preﬁx (default for http is www)

### domain - deﬁnes the Internet domain name (#xxyyzz.com .org .eu .uk .ru)

### port - deﬁnes the port number at the host (default for http is 80)

path - defines a path at the server (If omitted: the root directory of the site) filename - defines the name of a document or resource. CSS describes how HTML elements are to be displayed on screen, paper, or in
### other media

CSS can be added to HTML documents in 3 ways: Inline
### by using the style attribute inside HTML elements. <p

style=“color: red;”> </p>. Changes only the paragraph in question.
### Internal stylesheet

by using a <style> element in the <head> element.
### The example below changes the color of all paragraph text to red and

also changes the size of the text to 20 pixels. <style> p {color: red;
### font-size: 20px;} </style>

### External - by using a <link> element to link to an external .CSS file or

### style.css The most common way to add CSS, is to keep the styles in

### external CSS files. Use the HTML <link> element to refer to an external

### CSS file or to link HTML and CSS files together. The <link> element

must be placed within the head of the HTML file.
### The most common way to add CSS, is to keep the styles in external CSS

### files. Use the HTML <link> element to refer to an external CSS file or

to link HTML and CSS files together. The <link> element must be placed within the head of the HTML file.
### NOTE: it’s a self closing tag with attributes of  <link href=“address

URL/relative path to css file” rel=relationship btw HTML file & CSS file “stylesheet”>
### The HTML DOM (Document Object Model)

### (https://www.w3schools.com/js/js_htmldom_document.asp)

### “The Document Object Model (DOM) is a platform and language-neutral

### interface that allows programs and scripts to dynamically access and update

the content, structure, and style of a document.
### separated into 3 different parts”

### Core DOM - standard model for all document types

### XML DOM - standard model for XML documents

### HTML DOM - standard model for HTML documents

### When a web page is loaded, the browser creates a Document Object Model of

the page. With the HTML DOM, JavaScript can access and change all the elements of an HTML document.
### The HTML DOM model is constructed as a tree of Objects:

### With the object model, JavaScript gets all the power it needs to create dynamic

HTML, the DOM programming interface gives it absolute control over the
### properties & methods of each objects:

It defines The HTML elements<x> as objects. It defines The properties as values of HTML Elements that you can get & set/
change it’s content(elements, attributes, & CSS styles) of all HTML elements.
### It deﬁnes The methods as actions you can perform on HTML Elements i.e add

new, delete & remove existing elements & attributes.
### It deﬁnes The events for all HTML elements I.e Javascript can create new

HTML & react to existing HTML events in the page. /*console.log() is for debugging purposes likewise window.alert(), document.write() is for testing only*/ Example <p id="demo"></p> <script>
### document.getElementById("demo")×innerHTML = "Hello World!";

/*objectName . Method(element ID). Property*/ </script> The HTML DOM document object is the owner of all other objects in your web page.
### Finding HTML Elements

### Often, with JavaScript, you want to manipulate HTML

### elements. To do so, you have to ﬁnd the elements ﬁrst. There are several ways to

### do this. The most common way to access an HTML element is to use the id of the

### element. Remember all objects elements in the documents are supposedly in an

### array. To effect change on the ﬁrst <p> tag or ﬁrst className or ﬁrst #id. We

use document.getElementById(id).[0]/document.getElementsByTagName(name)[0]/ document.getElementsByClassName(name)[0] Object .Method Description document.getElementById(id) Find an element by element id document.getElementsByTagNa me(name) /<tag> Find elements by tag name document.getElementsByClassN ame(name) Find elements by class name document.querySelector(css selector) Finding HTML elements by CSS selectors document.querySelectorAll(css selector) Finding all HTML elements with same CSS selectors
### Changing HTML Content

### The easiest way to modify the content of an HTML element(<h1-

### h6>,<p>,<div>,<span>, <title>, <body>)  is by using the innerHTML property. To

change the content of an HTML element, use this syntax:
document.getElementById(id).innerHTML = “new HTML” /new != keyword Example: <p id="p1">Hello World!</p> <script>
### document.getElementById("p1")×innerHTML = "New text!";

</script>//The HTML document above contains a <p> element with id="p1” use the HTML DOM to get the element with id="p1”
### A JavaScript changes the

content (innerHTML) of that element to "New text!" From “Hello World!”
### Changing the Value of an Attribute

### To change the value of an HTML attribute(src, href…), use this syntax:

document.getElementById(id).attribute = new value Example: <img id="myImage" src="smiley.gif"> <script>
### document.getElementById("myImage")×src = "landscape.jpg";

</script>//The HTML document above contains an <img> element with
### id="myImage”

### We use the HTML DOM to get the element with id="myImage”

A JavaScript changes the src attribute of that element from "smiley.gif" to "landscape.jpg" /*element.setAttribute(attribute, value) Change the attribute value of an HTML element*/
### Changing HTML-CSS Style

Property ref(https://www.w3schools.com/jsref/
### dom_obj_style.asp)

### To change the style(property:color, font-size, text,….) of an HTML element, or

### create a new style related to a particular elements ID/Class. Use this syntax:

document.getElementById(id).style.property = new style Example: <p id="p2">Hello World!</p> <script> document.getElementById("p2")xstylexcolor = "blue"; </script>//
### Javascript Reacting to HTML Events

### HTML DOM events allow JavaScript to register different event handlers(function

### codes) on elements in an HTML document. Events are normally used in

### combination with functions, and the function() will not be executed before the

event occurs (such as when a user clicks a button☞onlcick, mousedown, onmouseover….etc
### Events are things that happen in the browser — a button being clicked, a page

loading, a video playing, etc. — in response to which we can run blocks of code. The constructs that listen out for the event happening are called event listeners, and the blocks of code that run in response to the event firing are called event handlers. For a list of all HTML DOM events, look at our complete ref(https:// www.w3schools.com/jsref/dom_obj_event.asp)
### The addEventListener() method

### The addEventListener() method attaches an event handler to the speciﬁed

### element. The addEventListener() method attaches an event handler to an element

without overwriting existing event handlers. You can add many event handlers to one element. You can add many event handlers of the same type to one element, i.e two "click" events. You can add event listeners to any DOM object not only HTML elements. i.e the window object. The addEventListener() method makes it easier to control how the event reacts to bubbling.
### When using the addEventListener() method, the JavaScript is separated from the

HTML markup, for better readability and allows you to add event listeners even when you do not control the HTML markup. You can easily remove an event listener by using the .removeEventListener() method.
## Syntax:

### element.addEventListener(event, function, useCapture);

### The ﬁrst parameter is the type of the event (like "click" or "mousedown" or any

other HTML DOM Event.)the program is listening out for
### Note that you don't use

the "on" prefix for the event; use "click" instead of "onclick".
### The second parameter is the function/block of code to run when the event

### occurs, Note that we don't need to specify the function parentheses when writing

it inside. The third parameter is a boolean value specifying whether to use event bubbling or event capturing. This parameter is optional. Note that you don't use the "on" prefix for the event; use "click" instead of "onclick".
### Event propagation

### useCapture is a way of deﬁning the element order when an

event occurs. If you have a <p> element inside a <div> element, and the user clicks
on the <p> element, which element's "click" event should be handled first?
### In bubbling the inner most element's event is handled ﬁrst and then the outer:

the <p> element's click event is handled first, then the <div> element's click event.
### In capturing the outer most element's event is handled ﬁrst and then the inner:

the <div> element's click event will be handled first, then the <p> element's click
### event. The default value is false, which will use the bubbling propagation, when

the value is set to true, the event uses the capturing propagation. Adding and Deleting Elements Method Description document.createElement(eleme nt) Create an HTML element document.removeChild(element Remove an HTML element document.appendChild(element Add an HTML element document.replaceChild(new, old) Replace an HTML element document.write(text) Write into the HTML output stream
### The Browser Object Model (BOM)

### The Browser Object Model (BOM) allows JavaScript to "talk to" the browser.Since

### modern browsers have implemented (almost) the same methods and properties for

JavaScript interactivity, it is often referred to, as methods and properties of the
## Bom.

### The window object is supported by all browsers. It represents the browser's

window. All global JavaScript objects, functions, and variables automatically become members of the window object. Global variables are properties of the window object. Global functions are methods of the window object. Even the document object (of the HTML DOM) is a property of the window object: window.document.getElementById("header"); is the same as: document.getElementById("header"); What is Web API?
### API stands for Application Programming Interface. APIs are ready-made sets of

### code building blocks that allow a developer to implement programs that would

otherwise be hard or impossible to implement.
### ☞It can extend the functionality of the browser

### ☞It can greatly simplify complex functions

### ☞It can provide easy syntax to complex code

A Web API is an application programming interface for the Web. They generally fall into two categories. A Browser API can extend the functionality of a web browser., are built into your
### web browser, and are able to expose data from the surrounding computer

environment, or do useful complex things. DOM API, Geolocation API, Audio & Video APIs. A Server API can extend the functionality of a web server.
### Data Validation

ref(https://www.w3schools.com/js/js_validation.asp) Data validation is the process of ensuring that user input is clean, correct, and
### useful. Typical validation tasks are:

has the user filled in all required fields? has the user entered a valid date? has the user entered text in a numeric field? Most often, the purpose of data validation is to ensure correct user input. Validation can be defined by many different methods, and deployed in many different ways. Server side validation is performed by a web server, after input has been sent to the server. Client/Browser side validation is performed by a web browser, before input is sent to a web server.
### To summarize:

### <script defer src="js/vendor/jquery.js"></script>

### <script defer src="js/script2.js"></script>

### <script defer src="js/script3.js"></script>

### *scripts with a defer attribute will load in the order they are in and will only

### execute once everything has ﬁnished loading. If your scripts need to wait for

### parsing and depend on other scripts hierachically and/or the DOM being in place,

load them using defer and put their corresponding <script> elements in the order you want the browser to execute them.
versus
### *scripts with an async attribute will execute as soon the download is done. This

blocks in the page does not guarantee any specific execution order. If your scripts should be run immediately and they don't have any dependencies, then use async.
### <script async src="js/vendor/jquery.js"></script>

### <script async src="js/script2.js"></script>

### <script async src="js/script3.js"></script>

async and defer both instruct the browser to download the script(s) in a separate
### thread, while the rest of the page (the DOM, etc.) is downloading, so the page

loading is not blocked during the fetch process.


---

*Document converted from PDF: <!- -HyperText Markup Language Tutorial- ->.pdf*
