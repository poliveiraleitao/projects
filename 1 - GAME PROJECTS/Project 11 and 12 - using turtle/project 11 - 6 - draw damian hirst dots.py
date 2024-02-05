import colorgram
import turtle
import random

# Extract 30 colors from an image.
colors = colorgram.extract('damian hirst dots.jpeg', 30)

# Check if colors were extracted
if colors:
    print(f"Colors were successfully extracted. Number of colors: {len(colors)}")
else:
    print("No colors were extracted.")

# Create a list with the RGB values separating the R, G, and B
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

print(rgb_colors)

# Delete colors with values too similar to 250 for all 3 components (shades of white)
filtered_colors = [color for color in rgb_colors if not all(c > 230 for c in color)]

############## CREATE DAMIAN HIRST PAINT ###############
# Size of dot = 20 x 20
dot_size = 20
# Space between dots
space = 50
# Number of dots in a line
dots_in_line = 20
#number of lines
number_of_lines = 20

# Create a Turtle object
timmy_the_turtle = turtle.Turtle()

# Set the drawing speed
timmy_the_turtle.speed("fastest")

# Draw Damian Hirst-style paint
for line_number in range(number_of_lines):  # number of lines
    # Move to the start position on top of the current line
    timmy_the_turtle.penup()  # stop writing
    starting_x = -665  # Leftmost position
    starting_y = -550 + ((space) * line_number)  # Adjust Y-coordinate for the current line
    timmy_the_turtle.goto(starting_x, starting_y)
    timmy_the_turtle.pendown()

    for _ in range(dots_in_line):  # number of dots per line
        # Set the Turtle's color to a random color from the list
        rgb_color = random.choice(filtered_colors)
        hex_color = "#{:02x}{:02x}{:02x}".format(*rgb_color)
        timmy_the_turtle.color(hex_color)
        # Draw a small dot (20 x 20)
        timmy_the_turtle.dot(dot_size)

        # Move to the next dot
        timmy_the_turtle.penup()  # stop writing
        timmy_the_turtle.forward(space)  # Length of space
        timmy_the_turtle.pendown()  # start writing again

# Keep the window open
turtle.done()

