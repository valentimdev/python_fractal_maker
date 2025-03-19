import turtle

# Function to set up the screen
def setup_screen(width, height):
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.screensize(3 * width, 3 * height)
    screen.bgcolor('black')
    screen.delay(0)
    return screen

# Function to set up the turtle
def setup_turtle(color, pensize, speed, pos):
    turtle_instance = turtle.Turtle()
    turtle_instance.pensize(pensize)
    turtle_instance.speed(speed)
    turtle_instance.setpos(pos)
    turtle_instance.color(color)
    return turtle_instance

# Function to apply substitution rules
def apply_rules(axiom, chr_1, rule_1, chr_2, rule_2):
    return ''.join([rule_1 if char == chr_1 else
                    rule_2 if char == chr_2 else char for char in axiom])

# Function to generate the result after multiple generations
def get_result(gens, axiom, chr_1, rule_1, chr_2, rule_2):
    for _ in range(gens):
        axiom = apply_rules(axiom, chr_1, rule_1, chr_2, rule_2)
    return axiom

# Function to draw the fractal
def draw_fractal(turtle_instance, axiom, chr_1, chr_2, step, angle, stack=None):
    for char in axiom:
        if char == chr_1 or char == chr_2:
            turtle_instance.forward(step)
        elif char == '+':
            turtle_instance.right(angle)
        elif char == '-':
            turtle_instance.left(angle)
        elif char == '[':
            if stack is not None:
                angle_, pos_ = turtle_instance.heading(), turtle_instance.pos()
                stack.append((angle_, pos_))
        elif char == ']':
            if stack is not None:
                angle_, pos_ = stack.pop()
                turtle_instance.setheading(angle_)
                turtle_instance.penup()
                turtle_instance.goto(pos_)
                turtle_instance.pendown()

# Function to draw the Pythagoras Tree
def draw_pythagoras_tree(turtle_instance, length, depth):
    if depth == 0:
        return
    turtle_instance.forward(length)
    turtle_instance.left(45)
    draw_pythagoras_tree(turtle_instance, length * 0.7, depth - 1)
    turtle_instance.right(90)
    draw_pythagoras_tree(turtle_instance, length * 0.7, depth - 1)
    turtle_instance.left(45)
    turtle_instance.backward(length)

# Main function
def main():
    # General settings
    WIDTH, HEIGHT = 1600, 900

    # Choice menu
    print("Choose the fractal you want to generate:")
    print("1 - Sierpinski Triangle")
    print("2 - Fractal Tree")
    print("3 - Dragon Curve")
    print("4 - Pythagoras Tree")
    choice = input("Enter the number corresponding to your choice: ")

    if choice == '1':
        # Settings for the Sierpinski Triangle
        screen = setup_screen(WIDTH, HEIGHT)
        turtle_instance = setup_turtle('purple', 3, 0, (-WIDTH // 3, -HEIGHT // 2))
        gens = 7
        axiom = 'F'
        chr_1, rule_1 = 'F', 'F-G+F+G-F'
        chr_2, rule_2 = 'G', 'GG'
        step = 8
        angle = 120
        stack = None
    elif choice == '2':
        # Settings for the Fractal Tree
        screen = setup_screen(WIDTH, HEIGHT)
        turtle_instance = setup_turtle('green', 3, 0, (0, -HEIGHT // 2))
        gens = 6
        axiom = 'XY'
        chr_1, rule_1 = 'F', 'FF'
        chr_2, rule_2 = 'X', 'F[+X]F[-X]+X'
        step = 7
        angle = 22.5
        stack = []
    elif choice == '3':
        # Settings for the Dragon Curve
        screen = setup_screen(WIDTH, HEIGHT)
        turtle_instance = setup_turtle('red', 2, 0, (WIDTH // 4, -HEIGHT // 4 - 25))
        gens = 13
        axiom = 'XY'
        chr_1, rule_1 = 'X', 'X+YF+'
        chr_2, rule_2 = 'Y', '-FX-Y'
        step = 4
        angle = 90
        stack = None
    elif choice == '4':
        # Settings for the Pythagoras Tree
        screen = setup_screen(WIDTH, HEIGHT)
        turtle_instance = setup_turtle('orange', 2, 0, (0, -HEIGHT // 2 + 50))  # Adjusted position for centering
        turtle_instance.left(90)  # Adjust initial orientation
        length = 150  # Initial trunk size (increased to make the tree larger)
        depth = 10  # Recursion depth (increased for more detail)
        stack = None
    else:
        print("Invalid choice. Please run the program again.")
        return

    # Generate the fractal
    turtle.pencolor('white')
    turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
    turtle.clear()
    turtle.write(f'Generation {gens if choice != "4" else depth}', font=('Calibri', 60, 'normal'))

    if choice == '4':
        draw_pythagoras_tree(turtle_instance, length, depth)
    else:
        axiom = get_result(gens, axiom, chr_1, rule_1, chr_2, rule_2)
        if choice == '2':
            turtle_instance.left(90)  # Adjust for the Fractal Tree
        draw_fractal(turtle_instance, axiom, chr_1, chr_2, step, angle, stack)

    screen.exitonclick()

if __name__ == "__main__":
    main()