---
$title@: Evolutionary Algorithms for Generating Pixel Art Plants
$slug: ea-for-pixel-plants
subtitle: ""
$date: 2016/12/10
curated_next: '/content/posts/2015/logic-and-states-with-css.md'
excerpt: EAs are incredibly powerful and can be implemented in very simple and straight forward ways or in manners that are quite complex, for data science and for art.
$cover_img: 2015/images/tumblr_themes/cover.gif
$public: true
---
<img src="/static/images/blog/pixelplants/cover.png" class="full" />

Machine learning in regards to evolutionary algorithms, neural networks, utilization of natural language processing and other more general concepts has been a really hot topic as of late. As I've had some professional pressure to dive more deeply into these I wanted to find a project aligning with the style of art I enjoy that could effectively utilize one of these technologies.

I have a love for generated art and letting the computer make decisions for certain aspects of visuals, so something along those lines made sense. What came out of that was an evolutionary algorithm (hereafter EA), to evolve pixelart "plants."

## Overview of EAs
EAs are incredibly powerful and can be implemented in very simple and straight forward ways or in manners that are quite complex. The majority  of them can be broken down however into the following cycle:

<img src="/static/images/blog/pixelplants/ea-diagram.png" alt="Basic steps of an Evolutionary Algorithm"/>
<span class="fade">Reference: [Introduction to Evolutionary Algorithms](http://www.ra.cs.uni-tuebingen.de/mitarb/streiche/publications/Introduction_to_Evolutionary_Algorithms.pdf)</span>

The core components from that cycle that affect how the population evolves are how it reproduces and how survival is determined.
I'll dive into how I approached both of these along with pitfalls that I've run into that are altogether rather common.

## Designing plants

For creating the pixel art plants a totally random population is first created. This means grids of randomly placed pixels varying between 16 colors and transparent.

Any pixel placed above the 80% mark represented above ground plant parts and could have 1 of 15 total shades of green and purple/red (the shade and pigmentation are significant later) or transparent.

Pixels placed below that line still had associated values for those 15 but would have different rules applied to them and be flattened to be shown as brown, these are the "roots."

<img src="/static/images/blog/pixelplants/plant-parts.png" alt="core plant parts">

Plant parts above ground would be responsible for energy generation and absorption, while parts below ground would be responsible for nutrients generation.

The key reason for choosing 15 values and a NULL (transparent) was so that each pixel could be represented by a single hex character. This also allowed for me to format the grid into a linear sequence which then resembled something akin to DNA, where each pixel is an "allele".

<img src="/static/images/blog/pixelplants/dna-sequence.png" alt="Diagram showing a grid of 9 pixels broken down intro a linear image" />

## Mechanisms of reproduction

A key part in performing an EA is reproduction. There are two basic ways this can be performed in an EA:

1. Asexual Reproduction - in where children from a parent are imperfect clones

2. Sexual reproduction - where two or more parents combine fragments of their DNA to create a unique offspring that inherits characteristics (seen or unseen) from its parents.

In this case the plants reproduce sexually with 2 parents where each plant selects 2 random other plants from the current population and crossbreeds. This is done by simply splitting each plant's DNA string into N fragments and then essentially flipping a coin to determine which parent the child inherits each segment from.

<img src="/static/images/blog/pixelplants/reproduction.png" alt="Illustration of reproduction of pixel plants" />

This results in a new population size 3m where m is the starting size of the original population. From the new population of the previous parents and newly born offspring the fitness of all individuals is calculated and the most fit M survive.


## Defining fitness

Calculating which members of the population survive comes down to fitness. While in this case how the values are derived is a bit involved, the final score evaluation for any given plant is:

[sourcecode:python]
energyOffset = energyProduced - energyNeeded
nutrientOffset = nutrientsProduced - nutrientsNeeded

score =  energyOffset**2 + nutrientOffset**2
[/sourcecode]

The higher a plant scores the more fit that plant is considered. Let's look at more detail into how I came up with these parameters though.

### Energy produced
The energy produced for each plant is calculated by determining the energy produced by each pixel and adding them together.

For each pixel, if it is above the roots area it can produce energy, if to it can not. Additionally, if it is a blank/transparent cell/pixel then it produces <code>0</code> energy. Otherwise the factors that  determine are as follows:

* Higher and more saturated color pixels generate more
* Pixels closer to the top generate more energy
* If another non-blank pixel is above that pixel, it generates energy only 1/5 as well

### Energy consumed
Energy consumption however is a bit more complex. Part of the reason for this is to help ensure that the full grid of pixels isn't full, as ultimately the null pixels are what creates the perception of shape.

* Null pixels consume <code>0</code> energy
* Cells with only 1 sibling or less (adjacent or diagonal) require significantly more nutrients to sustain their one off sibling
* Roots do not consume energy
* Each cell requires at least <code>1</code> energy for each sibling cell
* For each sibling of the same color, a bonus is awarded and 2 less energy is required
* Each non-blank cell requires a minimum of 1 energy

### Nutrients
The formulas for nutrients are more simple and based solely on pixels being attaches if they are in the roots section of the plant, with additional points being required or awarded with the more breathing room for each cell.

## Population bias and premature convergence

With complex problems such as those plants (each of 16*32 pixels being a variable with 16 possible values all of which shift multiple values depending on the values and quantity of neighboring values), the "landscape" of possible solutions is  quite complex.

Think of it like the below geography:
<img src="/static/images/blog/pixelplants/mountainRange.jpg" />
<span class="fade">[Image sourced from wikipedia](https://en.wikipedia.org/wiki/Mountain_range)</span>

Each time the algorithm is run the evolution trends towards the top of a slope so that it optimizes the lifeforms. The issue here being though that the bias in my system means that peak is most probably not the highest.

In fact in my code by around generation 10 a solid direction has already been chosen and only that hill will be climbed. This is not desirable, and can be seem clearly here where much more subtle changes happen as the evolutionary process progresses.

<img src="/static/images/blog/pixelplants/evolution.gif"/>


Theoretically the mutations set to occur  during reproduction(occasionally random pixels have their values reassigned) lends to the thought that eventually the most optimal peak will be achieved.

However as each pixel relates to each of it's sibling pixels siblings, if one is swapped for what may ultimately be the best, it may be evaluated poorly due to those pixels that surround it and the same for the values of its surrounding pixels.

Ways to fix this include larger population sizes, and also not having only the most fit individuals survive. Survival of the fittest and only the fittest leads to extreme bias of selection based on starting conditions.

## Selection method and survival
>Much like actual biology however, where if too similar a group is selected, they will not be able to change or adapt readily to shifting conditions. In this case then being unable to find the highest mountain.

The greatest issue with this particular algorithm implementation is the selection methods for survival. Here truncated selection is used which essentially just selects the top number of best candidates.

Much like actual biology however, where if too similar a group is selected, they will not be able to change or adapt readily to shifting conditions. In this case then being unable to find the highest mountain. A better approach to refactor or to have used from the start would've been tournament selection where a random individual is selected to compare against and if the initial candidate is stronger it survives.

This mimics to an extent predatory (literally canabalistic) behavior where the most critical function is the luck in finding weaker "prey" from within the species.

Another option is roulette, which despite the name is not inherently random. Here from each generation of plants the parent and the offspring would each be assigned a percentage chance of being chosen based on their score relative to the total value of scores. So while more successful plants would have a higher chance of survival, it would be possible for less optimal members of the species to survive.

## Wrong definition
Where EAs get fun is when patterns emerge from criteria that weren't expected. The definitions for what makes a plant a plant here were a best guess to give a set of rules for drawing a plant. Plant may in fact be a generous term, but none-the-less, a structure following the rules defined evolves and emerges.

Quickly the pattern emerges though of a checkerboard or lattice (which was not expected), most likely from the rules a that plant cells (pixels) gain more points by having more siblings and lose points by having a sibling directly above them.

So after a well-scoring lattice created pixels will be swapped in and out to fill or open portions further optimizing it. This is essentially how the plants "grow" within the confines of this particular EA.

## Conclusion
Ultimately this project was great fun a lot of learning and a lot of new stuff. If you want to find out more of contribute checkout the source code.  [https://github.com/william-index/plantgod](https://github.com/william-index/plantgod)

#### Bibliography:
[http://www.ra.cs.uni-tuebingen.de/mitarb/streiche/publications/Introduction_to_Evolutionary_Algorithms.pdf](http://www.ra.cs.uni-tuebingen.de/mitarb/streiche/publications/Introduction_to_Evolutionary_Algorithms.pdf)

[https://www.goodreads.com/book/show/30211819-evolutionary-computation](https://www.goodreads.com/book/show/30211819-evolutionary-computation)
