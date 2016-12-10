---
$title@: Logic and State Management with just CSS
$slug: logic-and-states-with-css
$path: /blog/logic-and-states-with-css/
subtitle: Building interfaces that involve logic with just CSS.
$date: 2015/10/17
excerpt: With a bit of planning and wizardry hover states and forms can handle basic logic in css. This tutorial explores some effective ways of harnessing that power and some aspirational examples.
$coverimg: 2015/images/css_logic/cover.png
$public: true
---
<img src="/static/images/blog/css_logic/banner.png" class="full" />

## Why use logical CSS instead of just JavaScript?
CSS has come a long way, and finally older browsers are starting to fade. In many instances JavaScript, when written well, has performance benefits in animation as well as other areas that far outweigh CSS's convenience.

Limited languages however such as CSS or older platforms such as the NES with 6502 Assembly, inspire inspiration through constraints. It could also be argued that CSS only solutions to problems that would typically be solved with JS offer fallbacks in case JS fails to load, crashes from an error, or is disabled. Mostly I side with the former and think its fun to find solutions within constraints.

## Direct and General Sibling Selectors
The key to handling logic with CSS is understanding *direct* and *sequential* sibling selectors. These are the <code>+</code> and <code>~</code> characters respectively.

When I teach CSS I like to teach students to read the meaning of selectors from right to left so,

[sourcecode:ruby]
.item + .item { }
[/sourcecode]

would be read as any DOM element with a class of <code>item</code> that comes directly after (<code>+</code>) any DOM element with a class of <code>item</code>. Meaning if you were to apply the selector <code>.item + .item</code> to a DOM like,

[sourcecode:html]

<div class="item">1</div>
<div class="item">2</div>
<div class="skip">3</div>
<div class="item">4</div>
<div class="item">5</div>
<div class="item">6</div>
<div class="item">7</div>
[/sourcecode]

It would style the elements with numbers 2,5,6,7. As the first <code>.item</code> does not come after a <code>.item</code> and the 4th element <code>&lt;div class="item"&gt;4&lt;/div&gt;</code> comes after a <code>.skip</code>, **not** a <code>.item</code>.

Using the *General Sibling Selector* (<code>~</code>) however, would also select element 4 (so 2,4,5,6,7). As a selector such as,

[sourcecode:ruby]
.item ~ .item { }
[/sourcecode]

Would mean to select *any* DOM element with a class of <code>item</code> that is nested at the same depth, and comes after (not necessarily directly) another element with a class of <code>item</code>.

## Hover-state logic
The easiest way to use these selectors to get some really interesting results is with hover states. Here the general sibling selector <code>~</code> is the most valuable tool. With it we can for example detect hover over a specific portion of an interface and have other objects react accordingly.

<img src="/static/images/blog/css_logic/hover-areas.gif" alt="Interface with 2 DOM Elements covering half the screen each." />

In the diagram above, we see that there are 2 <code>div</code> elements each styled to occupy either half of their parent container. They are also shown with transparency, and we can see that beneath them (visually) There is another <code>div</code> element. The markup for this comp may look something like:

[sourcecode:ruby]

<div class="parent-container">
  <div class="hover-area-1"></div>
  <div class="hover-area-2"></div>
  <div class="moveable-object"></div>
</div>
[/sourcecode]

Given this markup, we can write the following selectors,

[sourcecode:ruby]

.hover-area-1 ~ .moveable-object {}
.hover-area-2 ~ .moveable-object {}
[/sourcecode]

which would allow us to alter the style of <code>.moveable-object</code> depending on which area is being hovered over. The effect used could be anything, but using <code>translateX</code> for example in addition to <code>transition</code> within our css, could give us an animated object that moves left and right depending on cursor position. If you are reading this on a device with :hover capabilities, you can see a similar use here, where the spaceship moves left and right when the cursor hovers within the play area:

<p data-height="504" data-theme-id="0" data-slug-hash="qOrXON" data-default-tab="result" data-user="william-index" class='codepen'>See the Pen <a href='http://codepen.io/william-index/pen/qOrXON/'>Qorxon: Cruise Control</a> by William Anderson (<a href='http://codepen.io/william-index'>@william-index</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

## Changing State with checkboxes
You will notice that in the Codepen example above you need to click the "Cruise" button before you can start playing the game. This action there is also performed with just CSS.

Here though in order to use a click action to trigger an event (the removal of the start screen, and the counter in the top right&mdash;Chrome only), we use a checkbox to hold the logic and store the current state of the game (not being played or being played). Checkboxes for forms unfortunately only store binary values, meaning their are either <code>:checked</code> or <code>:not(:checked)</code>.

In its simplest form we can build a toggle for the background color of a div. Lets look at the following markup:

[sourcecode:ruby]

<form class="lightswitch-app">
  <input type="checkbox" class="switch-control"/>
  <div class="room"></div>
</form>
[/sourcecode]

Here we have a form with a checkbox followed by a <code>div</code>. Using the <code>:checked</code> psuedo-class in css we can target the <code>div</code> to change color only when the checkbox is checked.

[sourcecode:ruby]

.room {
  background-color: black;
}

.switch-control:checked + .room {
  background-color: yellow;
}
[/sourcecode]

This gives us an application with two states:

<img src="/static/images/blog/css_logic/select-toggle.png" alt="Diagram of lightswitch css application with 2 states." />

<span class="fade">This is an abstracted representation so that it looks nicer in my blog, you would have to apply more css to get this final styling.</fade>

## Faking Interfaces with labels
Naturally though asking users to click on literal checkboxes for state changes can make the interface seem unnatural or less "designed". Fortunately, checkboxes in html can be paired with label elements, allowing for use to style items in a more friendly manner and hide the original checkboxes.

So expanding upon our previous light-switch example, we could modify our markup to be:

[sourcecode:ruby]

<form class="lightswitch-app">
  <input id="switch"  class="switch-control" type="checkbox" />
  <label for="switch" class="switch-display"></label>
  <div class="room"></div>
</form>
[/sourcecode]

Now clicking on the label will mark the checkbox as checked or uncheck it depending on its state. This gives us a toggle to style with so we can select the room now with.

[sourcecode:ruby]

.switch-control:checked ~ .room {
  background-color: yellow;
}
[/sourcecode]

Notice how we also switched to the general sibling selector <code>~</code>? This accounts for the label which comes in-between the <code>input</code> and the <code>div</code>. Putting the input first is also important so that we can use its state to also style the label. Allowing us to polish up the interface and end with something more like this:

<p data-height="387" data-theme-id="0" data-slug-hash="LpOjrv" data-default-tab="result" data-user="william-index" class='codepen'>See the Pen <a href='codepen.io/william-index/…'>Sample Lightswitch for Blogpost</a> by William Anderson (<a href='codepen.io/william-index'>@william-index</a>) on <a href='codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>


## Complex Selectors
As you experiment with these simple building blocks eventually you will start to have very complex selectors for multiple parts of your css "application." One technique for building these out maintainably is to use something I like to call "Selector Fragments" with a preprocessor such as Sass.

### Writing Selector Fragments with Sass
A selector fragment is any portion of a selector that forms a pattern for selection that you may want to reuse. Lets look some fairly complicated selectors in just plain css:

[sourcecode:ruby]

.control-bit:checked + .display-bit + .control-bit:checked +
 .display-bit + .result-bit .display-bit__value--zero {

}
.control-bit:checked + .display-bit + .control-bit:checked +
 .display-bit + .result-bit + .control-bit:checked +
  .display-bit + .control-bit:not(:checked) + .display-bit +
   .result-bit .display-bit__value--zero {

}
[/sourcecode]

These are from a rather robust css-only application that I made that handled some math-like logic in its interface. We can see from these two selectors however that both have the same first 5 parts.

[sourcecode:ruby]

.control-bit:checked + .display-bit + .control-bit:checked +
 .display-bit + .result-bit {}
[/sourcecode]

Considering that we can have dozens (as was the case here) of selectors of this complexity or higher we can benefit from breaking that out into a fragment. This will make our code easier to follow, but also more maintainable. Our end result in Sass may look more like.

[sourcecode:ruby]

$two-checked: .control-bit:checked + .display-bit +
     .control-bit:checked + .display-bit + .result-bit;

#{$two-checked} .display-bit__value--zero {

}

#{$two-checked} + .control-bit:checked +
  .display-bit + .control-bit:not(:checked) + .display-bit +
   .result-bit .display-bit__value--zero {

}
[/sourcecode]

As we begin to chain multiple fragments together, the code becomes more and more readable while still being able to handle complex logic. Allowing for selectors such as:

[sourcecode:ruby]

#{$value2} + #{$value1a} + #{$value1b} + #{$value0},
#{$value2} + #{$value1b} + #{$value1a} + #{$value0},
#{$value2} + #{$value1a} + #{$value1a} + #{$value0},
#{$value2} + #{$value1b} + #{$value1b} + #{$value0},
#{$value2} + #{$value1a} + #{$value1b} + #{$value2},
#{$value2} + #{$value1b} + #{$value1a} + #{$value2},
#{$value2} + #{$value1a} + #{$value1a} + #{$value2},
#{$value2} + #{$value1b} + #{$value1b} + #{$value2},
#{$value2} + #{$value1a} + #{$value1b} + #{$value1b} + #{$value0},
#{$value2} + #{$value1a} + #{$value1b} + #{$value1a} + #{$value0},
#{$value2} + #{$value1a} + #{$value1a} + #{$value1a} + #{$value0},
#{$value2} + #{$value1a} + #{$value1a} + #{$value1b} + #{$value0},
#{$value2} + #{$value1b} + #{$value1a} + #{$value1a} + #{$value0},
#{$value2} + #{$value1b} + #{$value1a} + #{$value1b} + #{$value0},
#{$value2} + #{$value1b} + #{$value1b} + #{$value1b} + #{$value0},
#{$value2} + #{$value1b} + #{$value1b} + #{$value1a} + #{$value0} {

}
[/sourcecode]

Which can be used to perform complex logical operations purely in the interface using css alone, such as can be seen here:

<p data-height="649" data-theme-id="0" data-slug-hash="jbwggX" data-default-tab="result" data-user="william-index" class='codepen'>See the Pen <a href='http://codepen.io/william-index/pen/jbwggX/'>Half-byte Calculator (CSS-only)</a> by William Anderson (<a href='http://codepen.io/william-index'>@william-index</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

## Conclusion
Some of this may be a bit too complex or convoluted to go into production, but the basic principles should also allow for the simplification of many interactions and animated pleasantries. At a minimum its fun to play with limited systems building things up from scratch.
