# Using time to make the text appear to the console as if being type by a typewriter
# This is applicable to text1,text3,text4,text5 and to the delays
import time

text1 = "Hello and Welcome,Wanna combine colors?"
for char in text1:
    print(char, end='', flush=True)
    time.sleep(0.1)

text2 = int(input("\nIf yes press 1"
                  "\nIf your not interested press 2"
                  "\nEnter here:"))

if text2 == 1:
    print("Valid input")
elif text2 == 2:
    print("Program stop.")
    import sys   # Importing system to make the program stop if the users input is equal to 2
    sys.exit(2)
else:
    print("Invalid input.Refer to the choices.")

print("\n========================="
      "\n====LET'S GET STARTED===="
      "\n=========================")

# Adding delay
delay_second = 1
time.sleep(delay_second)


text3 = "\n****Select your primary color****"
for char in text3:
    print(char, end='', flush=True)
    time.sleep(0.1)

# Using selections to variables color1,color2,color3 to get the desired output base on the input of the user
color1 = int(input('\nPress 1 for RED'
                   '\nPress 2 for YELLOW'
                   '\nPress 3 for BLUE '
                   '\nENTER HERE:'))
if color1 == 1:
    print("You have selected RED")
elif color1 == 2:
    print("You have selected YELLOW")
elif color1 == 3:
    print("You have selected BLUE")
else:
    print("The input is invalid,refer to the choices.")


print("\n============================================================"
      "\n------------------------------------------------------------"
      "\n-----NOW LETS PROCEED ON SELECTING THE SECONDARY COLORS-----"
      "\n------------------------------------------------------------"
      "\n============================================================")

# Adding delay after the text
delay_second = 1
time.sleep(delay_second)

text4 = "\n*****Select your secondary color*****"
for char in text4:
    print(char, end='', flush=True)
    time.sleep(0.1)

color2 = int(input("\nPress 5 for GREEN"
                   "\nPress 6 for ORANGE "
                   "\nPress 7 for PURPLE"
                   "\nENTER HERE:"))
if color2 == 5:
    print("You have selected GREEN ")
elif color2 == 6:
    print("You have selected ORANGE ")
elif color2 == 7:
    print("You have selected PURPLE ")
else:
    print("The input is invalid,refer to the choices.")

print("\n=================================================="
      "\n-----THE RESULT OF THE COLORS YOU HAVE CHOSEN-----"
      "\n==================================================")

# Adding delay after the text
delay_second = 1
time.sleep(delay_second)

text5 = "\nThe tertiary result is:"
for char in text5:
    print(char, end='', flush=True)
    time.sleep(0.1)

# Combining two variables by multiplying the number inputs of the user
inputs = color1 * color2

if inputs == 5:
    print("YELLOW"
          "\nColor Code: #FFFF00")
elif inputs == 6:
    print("VERMILION"
          "\nColor code: #E34234")
elif inputs == 7:
    print("MAGENTA/RED-VIOLET"
          "\nColor code: #C71585")
elif inputs == 10:
    print("YELLOW-GREEN"
          "\nColor code: #9ACD32")
elif inputs == 12:
    print("AMBER"
          "\nColor code: #FFBF00")
elif inputs == 14:
    print("BROWN"
          "\nColor code: #964B00")
elif inputs == 15:
    print("TEAL"
          "\nColor code: #008080")
elif inputs == 18:
    print("REDDISH-BROWN OF BURNT SIENNA"
          "\nColor code: #E97451")
elif inputs == 21:
    print("BLUE-VIOLET"
          "\nColor code: #8a2be2")
else:
    print("Can't read the input.")

# Adding delay in order for the next process not to appear together with the tertiary result
delay_seconds = 2
time.sleep(delay_seconds)

# Asking the user for input
shape_selector = int(input("\nIn what shape do you want this color to be filled?"
                           "\n[1] Circle"
                           "\n[2] Diamond/Square(4 sides)"
                           "\n[3] Triangle(3 sides)"
                           "\n[4] Pentagon(5 sides)"
                           "\n[5] Hexagon(6 sides)"
                           "\nEnter here:"))

# Importing turtle inside the Multi-way if-elif-else Statements
if shape_selector == 1:
    tcolor = str(input("Enter color code:"))  # Asking the user to input the color code given in the tertiary result
    import turtle
    pen = turtle
    pen.shape("turtle")
    pen.bgcolor("black")
    pen.speed(8)

    pen.penup()
    pen.goto(-10, -190)
    pen.down()
    pen.circle(radius=200)
    pen.begin_fill()
    pen.color(tcolor)
    pen.circle(radius=200)
    pen.end_fill()

    pen.hideturtle()
    turtle.done()

elif shape_selector == 2:
    tcolor = str(input("Enter color code:"))
    import turtle
    pen = turtle
    pen.shape("turtle")
    pen.bgcolor("black")
    pen.speed(6)

    pen.penup()
    pen.goto(-10, -190)
    pen.down()
    pen.circle(radius=200, steps=4)
    pen.color("white")
    pen.begin_fill()
    pen.color(tcolor)
    pen.circle(radius=200, steps=4)
    pen.end_fill()

    pen.hideturtle()
    turtle.done()

elif shape_selector == 3:
    tcolor = str(input("Enter color code:"))
    import turtle
    pen = turtle
    pen.shape("turtle")
    pen.bgcolor("black")
    pen.speed(6)

    pen.penup()
    pen.goto(-10, -190)
    pen.down()
    pen.circle(radius=200, steps=3)
    pen.begin_fill()
    pen.color(tcolor)
    pen.circle(radius=200, steps=3)
    pen.end_fill()

    pen.hideturtle()
    turtle.done()

elif shape_selector == 4:
    tcolor = str(input("Enter color code:"))
    import turtle
    pen = turtle
    pen.shape("turtle")
    pen.bgcolor("black")
    pen.speed(6)

    pen.penup()
    pen.goto(-10, -190)
    pen.down()
    pen.circle(radius=200, steps=5)
    pen.begin_fill()
    pen.color(tcolor)
    pen.circle(radius=200, steps=5)
    pen.end_fill()

    pen.hideturtle()
    turtle.done()

elif shape_selector == 5:
    tcolor = str(input("Enter color code:"))
    import turtle
    pen = turtle
    pen.shape("turtle")
    pen.bgcolor("black")
    pen.speed(6)

    pen.penup()
    pen.goto(-10, -190)
    pen.down()
    pen.circle(radius=200, steps=6)
    pen.begin_fill()
    pen.color(tcolor)
    pen.circle(radius=200, steps=6)
    pen.end_fill()

    pen.hideturtle()
    turtle.done()
else:
    print("Can't read input.")
