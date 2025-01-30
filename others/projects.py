# I understand that this isn't Grepper's primary use but here are some 
# fun little projects that I've found (self taught) to be really fun and
# educational!

def beginner():
  # Beginner Projects
  
  beginner_proj ="""
  Everyone has to start somewhere!
  
  Understand functions with a simple math function
  - Takes in an input, makes it an integer, multiplies it by 2, returns/prints result
  
  Same string checker
  - Takes in two strings and compares them. If they're the same, print("Same!")
  
  String character counter
  - Takes in a string and outputs the length of the string
  -- Bonus points if you can make it not count spaces!
  
  Coinflipper
  - Use Python's random module to select a random num between 0-1. If it's 0, it's tails else it's heads
  -- Bonus points if you can take in a user input of heads/tails and compare that to
  -- the flip, letting them know if they won or not
  
  Test percentage calculator
  - Take in test result and total test score then do simple maths to find the percentage
  -- Bonus points if you can find out how to round the percentage
  
  Number guessing game
  - Generate number from 0-100 and ask the user to guess the number
  -- Many bonus points if you can create a points system!
  
  Make a random person picker for a party game
  - Using Python's random module, choose a random person from a list of names
  -- Bonus points if you make a menu at the beginning of the game
  -- which allows users to add many names 
  """
  print(beginner_proj)
  

def intermediate():
  # Intermediate Projects
  
  intermediate_proj ="""
  Well done, you're doing well!
  
  Create a quadratic equation solver
  - Sounds difficult but just google quadratic equation and take in the values a, b and c
  - This will teach you about Python's math module
  
  Make a benchmark
  - Using pythons time module, start a timer on the first line, make the program do many complex
  - calculations (e.g multiply all numbers from 0-1mil by 2) and when finished, stop the timer.
  - print out the time taken
  
  Make a morse code translator
  - Test your knowledge of dictionaries with a dictionary that compares
  - {"letter":"more_code"}. Then loop through an inputted string and convert it into morse
  
  Make your first API call
  - Using the Requests module, send a request to "https://api.genderize.io/?name=your_name"
  - and by using formatted strings, replace your_name with an inputted name! Output the guessed gender.
  
  Make an information generator
  - Make a program that will generate a: name, email, address, tel num, height, ethnicity, eye colour etc.
  -- Bonus points if you can store the generated person in a dictionary so that you can access information about
  -- them at any time
  
  Make a complete casino
  - Coinflip, roulette, slots etc.
  -- Bonus points if you can integrate a deposit money feature (Obviously fake money!)
 """
  
  print(intermediate_proj)
  
def expert():
  # Expert projects
  
  expert_proj = """
  Ah, I see you're bored and want some ideas on what to do next
  
  Create a Discord bot using discord.py
  - The community is incredibly supportive and it's something that can be quite fun!
  - Make a bot that can: ban, kick, warn, say anything, change nicknames etc.
  
  Create your own PYPI package
  - Making a python module is an impressive feat, why not try it out?
  - Think it's too hard? I managed to make mine when I was just 16 and trust me, I just followed
  - the official documentation line by line!
  
  Make a text based game
  - Include minigames and an interesting story
  
  Make an edge detection algorithm
  - This one is quite tough but I'm 17 and have managed so I'm sure you can too!
  - An edge is detected by getting the average of the neighbouring pixels to a pixel
  - and then finding the average of those pixels. Subtract that average from the current pixel.
  -- For a solution visit my method (Definitely not the best way of doing it)
  -- https://github.com/pTinosq/Edge-Detection-Algorithm
  
  Make a noise reduction algorithm
  - Also quite difficult but possible
  - Noise is reduced in a very similar way but instead of subtracting the mean, you replace the 
  - current pixel with the mean you just calculated
  -- Answer also available at https://github.com/pTinosq/Noise-Reduction-Algorithm
  
  I know you won't particularly like this one but, try something new!
  If you think you've mastered python well enough, try and expand your horizons.
  Here are some languages you might consider:
  Javascript, HTML/CSS, LUA, C#, Kotlin, Rust, GO, Swift
  
  """
  
  print(expert_proj)
  

def final_notes():
  thank_you = """
  Thanks for taking the time to read this, I hope it gave some of you some good ideas to work with!
  If you're interested in seeing some of the projects being put to use, check out my Github
  https://github.com/pTinosq where I will post most of my new projects (Unless they're private).
  
  """
  
  print(thank_you)

