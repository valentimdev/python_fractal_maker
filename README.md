# Fractal Generator with Python Turtle

This Python script generates various fractals using the `turtle` module. It allows the user to choose from four different fractals and customize their appearance. The script is designed to be simple, interactive, and visually appealing.

## Available Fractals

1. **Sierpinski Triangle**  
   A classic fractal that creates a triangular pattern through recursive subdivisions.

2. **Fractal Tree**  
   A tree-like structure that branches out recursively, creating a natural and organic pattern.

3. **Dragon Curve**  
   A fractal that generates an intricate, dragon-like curve by folding a strip of paper repeatedly.

4. **Pythagoras Tree**  
   A fractal tree based on the Pythagorean theorem, where squares are recursively added to form a tree-like structure.

## Requirements

- Python 3
- The `turtle` module (included in Python's standard library)

## How to Run

1. **Clone or download the script**:
   - Save the script to your local machine as `fractal_generator.py`.

2. **Run the script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is saved.
   - Run the script using the following command:
     ```bash
     python fractal_generator.py
     ```

3. **Choose a fractal**:
   - The script will display a menu with four options. Enter the number corresponding to the fractal you want to generate.

4. **View the fractal**:
   - The selected fractal will be drawn on the screen using the `turtle` graphics module.
   - Click on the screen to exit the program after the fractal is drawn.

## Customization

You can customize the fractals by modifying the following parameters in the script:

- **Generations/Depth**: Controls the level of detail in the fractal.
- **Step Size**: Controls the length of each line segment.
- **Angle**: Controls the angle of branching or rotation.
- **Colors**: Change the color of the fractal by modifying the `color` parameter in the `setup_turtle` function.

For example, to make the Pythagoras Tree larger, you can increase the `length` and `depth` values in the `elif choice == '4'` block.
