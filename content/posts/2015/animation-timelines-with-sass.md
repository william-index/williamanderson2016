---
$title@: Curating Animation Timelines with Sass
$slug: animation-timeslines-with-sass
$subtitle: How to curate and time recurring animations sequentially and looped over multiple objects with Sass and not lose your mind.
$dates:
  published: 2015/06/08
excerpt: CSS animations are fantastic, but when it comes to longer sequences over multiple objects that animate in order things get tricky. This tutorial explores creating a timeline for such animations using Sass.
$coverimg: 2015/images/sass_timelines/cover.gif
$public: true
---
<p data-height="373" data-theme-id="0" data-slug-hash="pJPOje" data-default-tab="result" data-user="william-index" class='codepen'>See the Pen <a href='http://codepen.io/william-index/pen/pJPOje/'>Looped animation with delays</a> by William Anderson (<a href='http://codepen.io/william-index'>@william-index</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

Animation in CSS with @keyframes is a powerful feature, but it falls short when it comes to curating timelines over multiple elements. There are often cases where we need to have different elements on the page toggle, or delay the start of one aniamtion until another completes. <code>animation-delay</code>, can be helpful, but quickly the different elements sync up if the animation loops. With Sass, a little bit of math, and some fun logic however, we can start taking better control over these animations.

A good example of this are the popups on the [Bourbon website](http://bourbon.io), but these employ javascript to append classes and thus time animation.

<img src="/static/images/blog/sass_timelines/bourbon.png"  alt='Design mockup for conversation animation.'/>

## The Example.

I'll be building out an example through this article, that I like to think of as an illustration of a conversation. Multiple 'people' markers will each say their own phrases in sequence and then repeat. AND, this will be done with just Sass!

<img src="/static/images/blog/sass_timelines/design_mockup.png"  alt='Design mockup for conversation animation.'/>

## Designing of the Animation

Before going into the overall timeline, we still need to plan the individual animation. <span class="fade">Note* I wont be going over styling in general during this post, but you can see the styling for objects in the [pen](http://codepen.io/william-index/pen/pJPOje) if you want.</span>

In this case I want my word bubbles to grow out from the point, with a bit of a spring action. If I were writing the keyframes for just one it would look something like this.

[sourcecode:ruby]

+keyframes(fade_in)
  0%
    +transform(scale(0.0))
  20%
    +transform(scale(1.0))
  80%
    +transform(scale(1.0))
  100%
    +transform(scale(0.0))
[/sourcecode]

<span class="fade">Here if you aren't familiar with the mixins Im using [Bourbon](http://bourbon.io) which I mentioned earlier. It pre-fixes and simplifies and whatnot, much like compass and a bunch of other things, but I prefer this.</span>

Lets visualize that as actual frames instead of percentages.

<img src="/static/images/blog/sass_timelines/single_object_timeline.png"  alt='Timeline for a single object.'/>

The lighter pink-tone here shows the scale from zero to one, if our animation was linear (no easing). We can see how the object changes in scale for each blocked out frame based on our animation. Most importantly, note that even though there are only 4 percentages given we use **5 frames**, when we draw it out like this. No matter what our frames _MUST_ be equal in size, meaning if you had used 4% size frames, you would need to have 25 of them, even if your animation keyframed at 0%, 4%, 96%, and 100%.

## Understanding the Timeline

When we start to look at this for multiple sequential animations, if it were on one timeline it may look something like this.

<img src="/static/images/blog/sass_timelines/multiple_object_timeline.png" class="full"  alt='Timeline for a multiple objects.'/>

In css, the issue here is that keyframes simply adjust the style properties for an element when they are applied as an animation. Thus, they don't have selectors.

We could apply the keyframes I showed above, and apply a delay, which would result in an animation with a flow something like this:

<img src="/static/images/blog/sass_timelines/undesired_timeline.png" class="full"  alt='Undesired Timeline for a multiple objects.'/>

With <code>animation-repeat</code> applied, after each objects individual timeline (assuming we had well calculated delays <code>atnimation-delay</code>), after each new introduction, all previous would repeat, and introduce one more element. Until all of them where shown and popping in and out in rhythm.

Instead, each object will need its own unique timeline, that persists over duration of all animations.

To do this, we note that every timeline has the same zero and 100% values by default (meaning that there will be 6 percentages in our keyframes declaration 0%, 0%, 20%, 80%, 100% as an example for our first obejct &mdash; the red dot).

<img src="/static/images/blog/sass_timelines/desired_multiple_timelines.png" alt='Desired Timelines for a multiple objects.'/>

We will also then need to have 5 different <code>@keyframes</code> declarations, **one for each object**, which we will create dynamically with Sass in just a moment.

## Setting Up Variables and Calculations

We are going to use some variables for this to make it easier.

[sourcecode:sass]

$object_count: 5
$object_order: 1 2 3 4 5
$duration: 3s
$animation_steps: 5

$frame_count: $animation_steps * $object_count
$frame_length:  100 / $frame_count
$animation_length: $duration * $object_count  
[/sourcecode]

Lets look at each one of these in turn.

- **$object_count** : The number of objects. In our case, 5 dots, means 5 objects.

- **$object_order** : This is the order we want the objects to appear in, its no fine if they are all in a row, but I put them that way to start.

- **$duration** : The duration in seconds for the animation of a single object.

- **$animation_steps** : This is from earlier, when we drew out our animation for a single object. Its the actual number of frames the animation occurs over, and is independent of the number of steps to our <code>keyframes</code> definition.

- **$frame_count** : This is the total number of frames for the entire accumulative timeline. Its equal to the number of frames per object, times all the objects.

- **$frame_length** : Now that we know how many frames, we let Sass convert them to percentages for us, figuring out the exact percent of each frame over the total additive timeline. As easy as 100 divided by the total number.

- **$animation_length** : The length of the entire animation. Another easy calculation, just the number of objects times the length of each objects animation.

## Creating Multiple Keyframe Declarations

With our variables and calculations all in place for the animation, things start to get a bit more complicated, as we have to build out our keyframes.

In Sass, there is a concept called interpolation. <span class="fade">Its actually not unique to Sass at all.</span> Where we can do bits of calculation and have them print out as non-value areas in our compiled stylesheets.

[sourcecode:ruby]

@for $i from 1 through $object_count
  +keyframes(bubble_#{$i})
[/sourcecode]

By using this, we can [loop over](http://thesassway.com/intermediate/if-for-each-while#for) each object and create a set of keyframes for its unique timeline automatically. Here the variable <code>$i</code> is used just to track what spacing the animation has from the 5 timelines drawn above. The <code>#{$i}</code> means to print out the value of <code>$i</code> there when we compile to css.

So this in the end would yield.

[sourcecode:scss]

@keyframes fade_1{

}
@keyframes fade_2{

}
@keyframes fade_3{

}
@keyframes fade_4{

}
@keyframes fade_5{

}
[/sourcecode]

Not so bad. But now we need to create the actual animations. Inside the <code>keyframes</code> inside the loop, we need to do two calculations unique to each object we are iterating over. First, we need to figure out which object we are on from our <code>$object_order</code> variable, and then we need to determine at what percent in the overall additive timeine that object should start animating in at.

[sourcecode:ruby]

$on_object: nth($object_order, $i)
$start_percent: (($on_object - 1)/$object_count) * 100
[/sourcecode]

<code>nth</code> is a [Sass function](http://sass-lang.com/documentation/file.SASS_REFERENCE.html#functions) that gives us the value of an item from a [list](http://sass-lang.com/documentation/file.SASS_REFERENCE.html#lists). Our original sequence was just <code>1 2 3 4 5</code> but you can change that later.

The next calculation, takes which object we are on, and subtracts one (so that we start from 0% instead of 20% into the animation), and divides that by the total number of objects. <span class="fade">zero divided by anything is zero</span> Afterwards we multiple by 100 to change the decimal into a percent!

We can now write out our entire keyframe declaration, we manually set the 0% and 100% value, which should be the same. Then we put in the same steps we had when it was all hand coded, but use interpolation to calculate the percent. The calculation is the start percent, plus the number of frames we want it to move (remember the original single object timeline?), and we multiply those frames by the <code>$frame_length</code> we calculated, so that they turn into percents.

[sourcecode:ruby]

@for $i from 1 through $object_count
  +keyframes(bubble_#{$i})
    $on_object: nth($object_order, $i)
    $start_percent: (($on_object - 1)/$object_count) * 100
    0%
      +transform(scale(0.0))
    #{$start_percent}%
      +transform(scale(0.0))
    #{($start_percent)+($frame_length*1)}%
      +transform(scale(1.0))
    #{($start_percent)+($frame_length*4)}%
      +transform(scale(1.0))
    #{($start_percent)+($frame_length*5)}%
      +transform(scale(0.0))
    100%
      +transform(scale(0.0))
[/sourcecode]

## Applying animations to the DOM Objects

Now that our animations are all defined, we just need to apply them to the actual items.

This has its own bit of calculation to it, but nothing worse than what we have done already.

[sourcecode:ruby]

@for $i from 1 through $object_count
  .conversation__participant:nth-child(#{$i})
    .conversation__participant__bubble
      +animation(bubble_#{$i} $animation_length $ease-in-out-back)
      +animation-iteration-count(infinite)
[/sourcecode]

Here we loop over the same number of objects, and then I select the <code>:nth-child()</code> <span class="fade">meaning the bubbles from the object that is $i in order of how they appear in the DOM</span>.

Then we use interpolation again to pick which <code>@keyframes</code> to use from the ones we made in our previous loop, and set the total duration to the length. Here I am also using one of Bourbon's pre-defined bezier curves to give a  bit of spring to the animation.

Finally the last property makes sure that the animation repeats forever!

## Thats it!

You can view the final product and all its source code here: [http://codepen.io/william-index/pen/pJPOje](http://codepen.io/william-index/pen/pJPOje). There are tons of ways that this could be modified, or even turned into a library or set of Sass functions and mixins to make it even easier, but I think this is a good intro to the theory of how it works.

Let me know if you have any questions, in the comments section.
