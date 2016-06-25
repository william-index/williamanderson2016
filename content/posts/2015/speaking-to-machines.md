---
$title@: Speaking to Machines
$slug: speaking-to-machines
$subtitle: "Writing Collision Detection with Machine Code"
$dates:
  published: 2015/08/28
$excerpt: We tend to be quite removed from how code actually works beyond layers of abstraction. Here we take a look at writing collision detection with zeros and ones.
$cover_img: 2015/images/machine_code/cover.gif
$public: true
---
<img src="/blog/2015/images/machine_code/banner.png" class="full" />
## Degrees of Removal
If you are reading this blog chances are you talk to machines for a living. Of course I'm talking about writing code (probably for the web, maybe for games?) but nonetheless, you deal with quite a few layers of abstraction.

We translate business logic, gameplay and so on into some form of language that some other program can understand and then translate to another program, eventually trickling all the way down to talking to the chips in your computer and making some sort of interaction happen. Being removed so many layers, there is quite a bit of magic between anything we write and what actually happens.

My goal here is to demystify machine code, thats the <code>0</code>s and <code>1</code>s, by looking at a bit of code I wrote for collision detection for an NES game. By the end of this post this sequence of code will actually mean something to you.

**00011000 10101001 00000101 00001011 11001001 00011000 10110000 00011000 10101001 00011000 10000101 00000101 00001011 10000101 00000101 00010111 10101001 00100000 10000101 00000101 00001111 10000101 00000101 00011011 10101001 00101000 10000101 00000101 00010011 10000101 00000101 00011111**

## Counting Systems
Binary itself isn't intimidating. Really it just means a system of 2 things. There are tons of "binary systems" which are basically things that only have two options. When talking about computers we normally are referring to binary numbers represented as something like this <code>10101001</code>.

A classic way of understanding the value of this is assigning a "place value" to each column. So...

```txt

Binary values: 128 64 32 16 8 4 2 1
Our Number   :   1  0  1  0 1 0 0 1
```

Mapping that to our number  is the equivalent of <code>128+32+8+1</code> or <code>169</code> in the system we usually count in. *Code* by Charles Petzold even explains these in terms of how we count. Normally we use a decimal system (so a numeric system based on 10s, where each column represents a increment in the max value —10—). In Binary, this means the column is equal to 2, and furthermore in Hexadecimal, it have a value of 16.

```txt

Binary     :    8   4  2 1
Hexadecimal: 4096 256 16 1
Decimal    : 1000 100 10 1
```

So "<code>11</code>" (pronounced here "one one") actually has the decimal values of 3 and 17, when converted from binary and hexadecimal respectively.

### Maximum Values

When we look at computer code, we talk about bytes, which are 8 bits and a bit is one on/off state. So the maximum value (in binary) for one byte of data is <code>11111111</code> which in decimal is **255**.

You can play around with the values in different number systems using the calculator here: [http://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html](http://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html)

## The Value of Numbers
**So all code is just math then? How the heck does 18 + 173 + 11 actually make something happen?**

The cool part is that it doesn't! Different processors actually do different things with different numbers, so <code>A9</code> in hexadecimal can do completely different things depending on the processor (chip) running a computer.

Basically chips have different reserved values that perform certain actions. In additional there are different "addresses" in which data can be stored. Those addresses are also conveniently numbers. So while code may translate to numerical/counting values, the chip that is running the code actually uses those to refer to machine level action and storage locations.

**Writing assembly for the web would translate (compile) into very different values!**

## Looking At Our Code
The code sample Im going to be using is from a game I wrote in 6502 Assembly for the NES. From what we already know that means that the 6502 processor chip here may be different from other chips and understand different commands. Assembly is one layer of abstraction away from the machine code so it gets us pretty damn close, but it still uses a compiler.

```txt

CLC

LDA $050B
CMP #$18

BCS CheckRight

LDA #$18
STA $050B
STA $0517
LDA #$20
STA $050F
STA $051B
LDA #$28
STA $0513
STA $051F


CheckRight:
```

These lines of code are part of the subroutine (kinda like a function, but more just like a segment of lines of code) I wrote for my game's collision detection.

<img src="/blog/2015/images/machine_code/gameview.gif" class="full" alt="Crabtastic lower play field"/>

The "protagonist" is a crab whose mission in life is to catch birthday cakes. His world is limited though. Rather than having free reign over the ocean, giant carrots block his path.

The code here is called whenever the left button is pressed on the controller and then AFTER we have moved the crab over 1 pixel to the left. So to detect the bounds of his world, we need to do a bit of work.

Ignoring the code above, the logic for that looks like this

```txt

If the crab's new intended location is beyond the left edge
Set the crabs location to be at its minimum left value instead
```

### Loading the Crabs Location

Lines 3, 4 and 6 of the assembly code are where the real meat happens. The <code>LDA</code> opcode (<span class="fade">OpCode, or operation code, is a code (value) for an operation that the processor can perform.</span>) means that we are looking to load a value stored in the chip accumulator.

```txt

LDA $050B
```

The $ after that indicates that we are going to use hexadecimal (the absence of any other symbol has meaning as well, which is that we are giving a memory address). The memory address is given as 2 hex(hexadecimal) values in order, each 2 characters long (as we are talking to a machine we only use 2 digits in hex so the max value is 255, keeping it within one byte of data).

I'm using the location <code>$050B</code> in my code to store the leftmost location of the crab in regards to where I want to draw it on the screen.

<img src="/blog/2015/images/machine_code/crabtastic_movement.gif" alt="Crabtastic bounds animation"/>

### Checking the Crabs Left Side Against the Screen

Line 4 is where we start to compare values:

```txt

CMP #$18
```

The right side of this line should look somewhat familiar. We see the <code>$</code> so we know we are using hex, but there is also a <code>#</code>. The <code>#</code> sign here means we are talking about an actual numerical value, so literally <code>18</code> in hex, which is the equivalent to 24 in the decimal system. This number is the left most coordinate on the screen that I want to allow the leftmost part of the crab to hit.

<code>CMP</code> compares the value currently in the accumulator (which we set in the preivous line to the value stored at location <code>$050B</code>) to another value, so in this case the value of <code>#$18</code> - <code>$050B</code>.

Like in most computer systems the grid works in value increasing from zero (#$00) to #$ff going from left to right on the screens matrix.

<img src="/blog/2015/images/machine_code/screensizing.png" alt="NES Crabtastic Grid" class="full"/>

So for <code>CMP</code> here, if <code>$050B</code> is greater than <code>#$18</code> then the value for the subtraction would be "negative" meaning there is no remainder. If they are equal there is also no remainder, but if the opposite is true and <code>#$18</code> is grater than <code>$050B</code>, something called a "carry" is set. The carry doesn't actually store the remainder, only the fact that there is one. Meaning that it itself is binary (true or false), or what we would call in most modern languages a Boolean.

As there is only one "carry", the first line you see of the code here is actually being used to clear anything that may have been in there before this. It stands for "CLear Carry" <code>CLC</code>.

### Conditional Logic
Line 6,

```txt

BCS CheckRight
```

is the true conditional for checking whats happened. <code>BCS</code> is the opcode for "Branch if Carry Set". Which means that if there is a value in the carry (a remainder from the math we did before), jump to another location in our code. Here I use "CheckRight" which the compiler will them use to look for where I put "CheckRight", grab the differences in hex values and use that numerical difference to indicate where to jump to in the code. CheckRight for me is simply the next subroutine after the current one, so it really just means, ignore the rest of this, and keep chugging along.

### Updating the Crab

<img src="/blog/2015/images/machine_code/pixelview.gif" alt="Crab Sprite Sections"/>

For the NES's PPU, each unit is 8x8 pixels wide and called a sprite (commonly), so my crab is actually 3x2 sprites, that move in unison. If the crab has passed the left edge of the screen, each of its six part locations is updated to equal what it's left most bounds should be. Lines 8 through 16 load the values I manually set as limits (note the <code>#</code>s), and store them in the memory addresses that keep the sprite locations on the screen.


```txt

LDA #$18
STA $050B
STA $0517
LDA #$20
STA $050F
STA $051B
LDA #$28
STA $0513
```

## The Meaning Behind OpCodes
So each of the 3 letter opcodes we use is actually supposed to be a human readable way of referencing the hex value for one of the processor commands with <code>LDA</code> standing for "LoaD Accumulator" as an example.

The 6502 chip in the NES actually uses hex values though which the compiler would convert these to. So <code>LDA</code> for example actually has a value of <code>A9</code> for the NES/Famicom. So translating our code one step away from abstraction we get this:

```txt

$18

$A9 $050B
$C9 #$18

$B0 CheckRight

$A9 #$18
$85 $050B
$85 $0517
$A9 #$20
$85 $050F
$85 $051B
$A9 #$28
$85 $0513
$85 $051F


CheckRight:
```
<span class="fade">If you are interested in where these came from, or what other OpCodes are you can check out this fantastic online reference: [6502.org](http://www.6502.org/tutorials/6502opcodes.html).</span>

And removing the human friendly type reminders <code>$</code> and <code>#</code> leaves us with the even more simple:

```txt

18

A9 05 0B
C9 18

B0 CheckRight

A9 18
85 05 0B
85 05 17
A9 20
85 05 0F
85 05 1B
A9 28
85 05 13
85 05 1F


CheckRight:
```

I mentioned before how the compiler would handle <code>CheckRight</code> by seeing where <code>CheckRight:</code> was relative to it in the code. If we count the hex numbers between lines 6 and 18, there are 24 (decimal) number pairs, meaning that to get from lines 6 to 18 we need to skip 24 hex codes, 24 converted from decimal to hex is <code>18</code>. We are also going to lose line 19 in this next translation as it was just a placeholder for the compiler.

```txt

18

A9 05 0B
C9 18

B0 18

A9 18
85 05 0B
85 05 17
A9 20
85 05 0F
85 05 1B
A9 28
85 05 13
85 05 1F
```

This is the equivalent of our original code, but now all in hex. Lets clean it up a bit, by arbitrarily grouping them into rows of 4 (the lines don't matter now that its just hex).

```txt

18 A9 05 0B
C9 18 B0 18
A9 18 85 05
0B 85 05 17
A9 20 85 05
0F 85 05 1B
A9 28 85 05
13 85 05 1F
```

## Binary
Now that we have a purely numeric representation of our code, in hex pairs (which we know all have a maximum value of 255) we can convert the hex to binary, which gives us:

```txt

00011000 10101001 00000101 00001011
11001001 00011000 10110000 00011000
10101001 00011000 10000101 00000101
00001011 10000101 00000101 00010111
10101001 00100000 10000101 00000101
00001111 10000101 00000101 00011011
10101001 00101000 10000101 00000101
00010011 10000101 00000101 00011111
```

Cool right? We just wrote collision detection in machine code!!

Oh, and if you want to play the game, you can download it here:
<a href="/blog/2015/downloads/crabtastic.nes" target="\_blank">Crabtastic</a>.


**References:**

- [*Code: The Hidden Language of Computer Hardware and Software* Charles Petzold](https://www.goodreads.com/book/show/44882.Code)
- [*I Am Error: The Nintendo Family Computer / Entertainment System Platform* Nathan Altice](https://www.goodreads.com/book/show/23461364-i-am-error)
- [http://www.6502.org/tutorials/6502opcodes.html](http://www.6502.org/tutorials/6502opcodes.html)
- [http://skilldrick.github.io/easy6502/#first-program](http://skilldrick.github.io/easy6502/#first-program)
- [http://www.dwheeler.com/6502/oneelkruns/asm1step.html](http://www.dwheeler.com/6502/oneelkruns/asm1step.html)
