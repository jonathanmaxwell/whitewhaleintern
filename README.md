# Intern challenge for White Whale

**Code Challenge: Gibberish Algorithm**
---------------------------------------

Challenge Overview
------------------

We are exticed taht you are intsereted in joiinng Wihte Wahle for the smumer.  Weoclme to yuor fsrit prommarging chanellge.  Yuor chnellage is to courtsnct a prrgoam taht tekas an Enilgsh txet snirtg as iupnt and rerutns rebadale giirebbsh lkie tihs.  It dseno’t mtaetr in waht oerdr the ltteres in a wrod are, but an iproamtnt tihng is taht the frsit and lsat ltteer be in the rghit pclae. The rset can be a taotl mses and you can sitll raed it whotuit a pboerlm.  Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe.

**The Basics:**
  
  - You may use *almost any* programming language... it's your choice.  See the supported options [here](http://ideone.com/).
  - Your program should leave the first and last letter of each word in place and scramble the rest.
  - Your program should not scamble punctuation (.,-'...etc.), numbers, or upper-case abbreviations.
  - See the [/text_files] folder for sample text files. 

**Input/Output:**
 
  - Name your program as follows: `gibgen.xx` (where xx is variable based on the language you choose)
  - Your program should be able to read text input from a string passed into STDIN
      - `gibgen.xx "This is a String"`
      - `cat mystringfile.txt | gibgen.xx`
  - Your program should output to the console.

_Note: This challenge is based on a popular word gibberish meme. You can improve the readability by looking at a [researcher's take](http://www.mrc-cbu.cam.ac.uk/people/matt.davis/cmabridge/) on the truths/myths of this meme, but this is not required._

What to do
----------
1. [Download](http://git-scm.com/downloads) & install Git on your machine

2. <a href="https://github.com/trentgillham/whitewhaleintern#fork-destination-box" class="btn grouped" data-method="POST" rel="nofollow" title="Fork">Fork</a> this project - Go [here](https://github.com/trentgillham/whitewhaleintern) and click the "Fork" button (located on the upper-right side of the screen)

2. Clone your new fork'd repository to your local machine - `git clone https://github.com/trentgillham/whitewhaleintern.git`
3. Complete the code challenge and fill out the Quick Start & Questions in the the README (see below)
4. `git add` and `git commit` your local repository as you go
4. Push your code and README back to Github occasionally - `git push origin master`
5. Email [gillham@whitewhaleanalytics.com](mailto:gillham@whitewhaleanalytics.com) with the Commit URL to your fork'd repository that you want reviewed. It should include at least 2 files: (1) your updated README with Coding Questions answered, and (2) your program (gibgen.xx)
   - Copy and paste the URL into the email along with your name... it should look something like this:
       - https://github.com/YOUR_USERNAME_HERE/whitewhaleintern.git

_Note: If you have any questions, email [gillham@whitewhaleanalytics.com](mailto:gillham@whitewhaleanalytics.com)._

Judging Criteria
----------------

Your responses to the **Coding Questions** at the bottom of this README are the *Most Important* part of this challenge. A working, fully fault-tolerant program that we just can't break, albeit awesome, is the least important.  Why is that?  Remember, we don't expect you to be expert programmers (just yet)... We want to see how you think through a problem.  


For completion by applicant
===========================

Quick Start
-----------

* The program can be run using the commandline. Use "python gibgen.py < textfile.txt" without the quotes, where textfile.txt is the name of whichever textfile you want to give the program. It is designed to handle to the specific input given with this challenge, but can handle any text file with a single line of text.
* Python 3 was used to write this program
* The code has comments to explain its use. No additional information is required to run the program.


Coding Questions
----------------

Question 1: "How did you approach the problem?" (500 words or less)

Pre-Programming: My first step was to write a framework. I detailed it out in English, and in the rough format I expected to use – the way I would write the program. I included different functions I’d want split up from the main function, added comments, and ended up with a framework to translate into another language. I then detailed a plan (test that I had Python working with “hello world”, test read/write functionality with different input, test the tracking of character positions, test simplified scrambling, etc.). I referred to the plan as I coded in order to stay on track and tackle tasks in the bets order.

Language: I chose Python as my language because I remembered it being simple and forgiving. This program seemed relatively simple in its demands, so I assumed Python could handle it. I need to refresh myself on how things worked, so I wanted and easy introduction. No sense in making extra work for myself. During this challenge, I looked up dozens of things online, mostly using Stack Overflow and Python design docs to figure out things I need to learn.

Programming: After installing Python and Git, then testing basic reading/printing, I made a main function and worked with lists and strings. I had the program print strings at several points so I could see how it was receiving and manipulating data. After I was sure it was reading things correctly, and that my system of variables that tracked character positions in lists was tracking properly, I had the program replace every letter inside a word with an ‘x’. This way I could see how new functions interacted with the lists before I wrote the more complicated scramble function. I wrote the program discern word size and punctuation after that to narrow down my targets, all the while just replacing everything between the first and last letters with an ‘x’. 

Now that I had a working foundation, I wrote the scramble feature. I first sketched out how it would work visually, on paper. I was able to follow the plan I had made earlier, making the task simpler and easier to integrate into my program. Satisfied that I understood where different variables had to be referencing and how many loops and if statements I’d need, I wrote the scramble function.

Once that was working, I looked for instances of error. I identified the abbreviations and situations where a scrambled word ended up the same as it started. I wrote a separate function to address abbreviations, and implemented a loop to repeat the scrambling if the word wasn’t scrambled the first (or any) time. I used print-tracking as per before to check when the program addressed and fixed a poorly scrambled word.

I then emailed you about input style, something I hadn’t be able to make match the specifications precisely. With confirmation given, I wrote up this piece based on observations and notes I had made along the way and submitted it.

Question 2: "What was the most difficult aspect of the solution?" (500 words or less)

The most difficult aspect of the solution was handling the input. Having to reteach myself most of what I knew about Python (and learn many new things), I had to figure out how information could be received, read, and changed. Different methods handled things differently, and different methods could only read certain input types (command line vs. user input, string vs. file, etc.)

Handling certain input in limited ways had to be addressed too. For the main function, I ended up with a for loop going through each element in a list made from the input text file. I had to reread and adjust my plan for instances where I need track things. I ended up with increasing variable to track where the element was, for example. I wouldn’t have had to do that if I had made a loop that followed the position of the list instead of the element (and I could have used that position to base other code off of). Once I had an understanding of how Python liked to sort data (or at least how I had figured it out) I found I could change input and reading techniques more easily, and plan ahead better.

Another difficult aspect was how Python uses functions. I had forgotten until it came up that Python doesn’t have pass-by-reference functions. This limited what processes I could remove from the main function to keep the code more streamlined and simple. I had to keep the scramble process, for example, in the main function (I think I may have been able to do it separately by appending new items to growing lists even though a list couldn’t be edited, but the rest of the program isn’t built around that approach). This caused me to have to slow down and change where different pieces of code were placed to accommodate for code in the main function.

