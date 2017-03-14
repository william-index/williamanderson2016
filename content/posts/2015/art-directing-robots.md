---
$title@: Art Directing Robots
$slug: art-directing-robots
subtitle: ""
$date: 2017/03/14
curated_next: '/content/posts/2015/successfully-completing-side-projects.md'
excerpt: TBD
$cover_img: 2015/images/tumblr_themes/cover.gif
$public: true
---
# Code is a description of intent

Generative art, regardless of the intelligence of the algorithm, is a guided process between coder and computer where the coder seeks to instruct a machine in regards to their aesthetic senses so that it may produce varied and pleasing artifacts.

> As a programmer, one takes on the role of the hovering art director at all times, their shoulder over the computer ever instructing and changing instructions at whim.

Descriptively, this feels much more like art direction than engineering. As a programmer, one takes on the role of the hovering art director at all times, their shoulder over the computer ever instructing and changing instructions at whim, when inspired and, most hopefully and more regularly whenever they can draw from past experience.

The code becomes more than a means of production and is a tool for communication. It's a conversation with collaborators, a time capsule to the past, a direct line to the future, and a common language between a person and a machine.  Regardless of what is made code however always reflects the description of intent.

As an engineer one tries their best to transcribe the business logic when working on products and projects: slideshows progress to the next slide, modals appear on click, birds flap on tap. These ideas, concepts and intentions function in efficiency, accuracy and interactivity all in relation to the conciseness and clarity of articulation given in the form of code as interpreted by the machine.


# Framework of ideas vs ideas themselves
> As an artist when I create a drawing/painting, a piece of software or an artifact of sound, I envision it clearly first then refine and groom its complexity

When setting out to make art or a statement a particular vision is most commonly the goal. As an artist when I create a drawing/painting, a piece of software or an artifact of sound, I envision it clearly first then refine and groom its complexity ([http://williamanderson.io/blog/successfully-completing-side-projects/](http://williamanderson.io/blog/successfully-completing-side-projects/)).

But when making generative art the process varies significantly. Unlike the proverbial sculptor freeing form from stone I free a framework from an idea. Rather than looking to create a particular final product I abstract that idea to a higher level and seek to construct rules for generating like ideas.

Creating a world, crafting its continents, oceans, ice caps and bringing its fauna and flora to life is the power of a deity. But then zooming out beyond the surface we are left with a marbled sphere of abstract shapes and atmosphere. In a recent project ([@fermipastelladox](https://twitter.com/FermiPasteladox)), I explored this very generation. Worlds would have color and shading, all would be spheres. Blobs and blotches would decorate the surface and the sky would be painted in gradients with sparkles and hearts.

<img src="/static/images/blog/artdirecting_robots/pastel_planet.jpg" />

**This is the idea/dream of a planet rather than the description of a particular astronomical object.** I was planning an abstraction of a framework for what defined a planet within this "Pastel Universe." The creation I sought out to make was not a planet itself but a creator of planets, a sculptor of an entire universe, a god.

# Selection of generative process
Depending on what is being made however, how you build and or teach/train your algorithm may differ. Selection of what to use will also largely depend on the amount of control and restriction as well as how curated the desired artifacts will be.

## Random
The most straightforward (though chaotic) method is to embrace randomness. Randomness can be contained and controlled, random within a range and random with  restrictions but it means a surrender of control to that chaos.

When choosing a wholly random generative approach, there must be an acceptance of imperfect output, of mistakes and missteps made by the machine. In exchange, the beauty of using a random approach is that there is a large opportunity for pleasant surprises to offset the upset of failed artifacts.

### Preset components
<img src="/static/images/blog/artdirecting_robots/captains_tweet_1.png" />

One method of creating generative works using a random approach is something akin to a [Mad Libs](https://en.wikipedia.org/wiki/Mad_Libs). This is wildly popular for Twitter bots and I have employed this approach myself in a very literal sense in the creation of [@dorffort_ebooks](https://twitter.com/dorffort_ebooks?lang=en) [@fantasticrealestate](https://twitter.com/FantasyListings) and [@captainsloggame](http://captainsloggame.com/).

The principle concept it to blank out key words within a sentence or piece of written content and allow random works for particular parts of speech to fill those blanks. While this could be used for all fragments of a sentence the fewer places where randomness is introduced the more predictable the system may be. For example:

[sourcecode:text]
The ______ is now your best ____.
[/sourcecode]

The above template allows for a lot of surprises and experiences. In the case that both blanks are nouns you could end up with whimsical phrases:

#### The ballerina is now your best dragon.

morbid scenarios:

#### The baby is now your best cannon-fodder.

or complete nonsense:

#### The Jelly is now your best minivan.

Opening this up to more blank spaces will increase the chances of undesirable outcomes, but that's where the art direction aspect comes in.

If using an API such as [wordnik](https://www.wordnik.com/), you could refine the criteria for what type of word is chosen for each space, or to be even more controlling foregoing the use of an external service and having short curated lists of desirable/tested phrases.

To see the differences between the release of control vs heavy curation  Captain’s Log Game and Fantastic Realestate serve as clear examples. Fantastic Realestate is completely random in its selection (other than grammar) resulting in vastly different tweets being generated many of which are near incomprehensible as seen here:

<img src="/static/images/blog/artdirecting_robots/realestate_tweet-1.png" />

Much the opposite however, Captain’s Log Game has very specifically set lists of words to use, allowing it to maintain a consistent tone across a near infinite number of tweets.

<img src="/static/images/blog/artdirecting_robots/captains_tweet_2.png" />


### Flexible components
Still within the realm of the random one may have more flexible components, or items that adhere to a structured system of design but allow for bits of chaos within.

Where a toy such as the mix and match shown below is much more along the lines of a highly curated phrasal template (commonly: "Mad Lib") system one could create a digital version in which these randomly selected items have additional unrestricted layers of randomness.

[<img src="/static/images/blog/artdirecting_robots/olliblocks.png" />](http://coolmompicks.com/blog/2012/10/21/diy-blocks-stack-mix-and-match/)
<span class="fade">Source: [Coolmompicks.com](http://coolmompicks.com/blog/2012/10/21/diy-blocks-stack-mix-and-match/)</span>

Sticking with the [Ollie Blocks](http://coolmompicks.com/blog/2012/10/21/diy-blocks-stack-mix-and-match/) example above this could mean that whenever a component (head/body/etc) is selected it's color is picked randomly from anything within the spectrum of possibilities for that display. This allows for a highly curated presentation of form with a more chaotic interpretation of color restrictions.

<img src="/static/images/blog/artdirecting_robots/variation-in-randomness.png" />

This is where the real training of the algorithm occurs. The more random a system is the less meaning and intent it has and the less consistent it's feels. Much like when producing artifacts for contract work, the most valuable generative processes are those of consistent quality (not necessarily consistent style or approach).

In Wizard Generator <https://twitter.com/wizardgenerator> this approach us used with very set images of wizards, but replacing color (random) and pattern (random selection of images) to create themes and many whimsical final artifacts.

The below from Wizard Generator are a sampling of one template layout, but its variation with color and pattern show how while the pattern and color selections may be random, constraining those to a single visual template adds consistency.

<img src="/static/images/blog/artdirecting_robots/nose_wizards.gif" />

### Verbally educating a machine with code
Communication is incredibly difficult, and within iterative processes will usually take several rounds of feedback and review for someone to be able to produce an artifact that aligns anywhere near the idea of someone else's vision.

With bots, code becomes the language of critique. The algorithm in the role of the pupil or mentee starts with only the framework it's given pulling in wholly random and unconsidered elements, exploiting and probing edges of possibility found through the vagueness of the engineer’s descriptions. The earliest creations of the algorithm rarely being comparable to the mental template the teacher had in mind.

<img src="/static/images/blog/artdirecting_robots/fossil_compare.jpg" />

Only through further critique and iteration (code refractors) can one instruct the algorithm into how to create something beautiful under the framework of its education. And only through many iterations of this can it learn to explore the vagueness of that education to the benefit of what it sculpts as opposed to the detriment.

## Procedural
While randomness is oft without order, something procedural draws on the power extrapolation. Without diving deeply into different procedural algorithms themselves the core idea is to take some seed or starting value and use that to build and generate something much larger than itself with a series of rules.

I used this approach in creating [@fermipastelladox](https://twitter.com/fermipasteladox) which when given a specifically formatted string of characters such as:

#### 6A5237-53F5-A2625A

Converts those to numbers which are then used to draw a scene from within its universe.

Palettes are chosen instead of colors and even numbers used in a random like manner are handled with the modulo operator to keep them within desired ranges. This allows for generating consistent visuals and also gives the opportunity for a universe of 16 quintillion planets to exist without a database.

## Intelligent
While many approaches in artificial intelligence are possible from a technical level ([Evolutionary Algorithms](http://williamanderson.io/blog/ea-for-pixel-plants/), Deep Learning etc), the ultimate challenge once again comes down to an articulation by the engineer.

When dealing with an intelligent system however it comes back to a more human like approach. Instead of directing the ways in which something should be adjusted tweaked and manipulated or the ways in which different components interact the articulation is of a more vague final image.

# Conclusion
Ultimately, when art directing via algorithms, execution that differs from vision is an inability to articulate aesthetic requirements. This can either be from a lack of refined vision, or a failure in teaching the machine through code. Regardless, as with teaching, directing, mentoring the most satisfying reward is seeing growth in those with whom you work with.
