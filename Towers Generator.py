import turtle

# Turtle Aspects
turtle.title('Mini Super Mario Towers')
turtle.shape('turtle')
turtle.speed('fastest') # Makes the turtle move fast
turtle.pensize(1)
                
turtle.getscreen().bgcolor("#a0deae")    # Gives the canvas a green color
turtle.setup(width=1750, height=750)     # Changes the resolution of the turtle console          
turtle.screensize(50000, 50000)          # Enlarges the canvas so big graphics can be viewed
                      
turtle.penup()
turtle.goto(-350, -200)     # Positions turtle at starting point for the tower code   
turtle.Screen().tracer(0)   # Skips drawing animation of turtle

#USER INPUTS#----------------------------------------------------------------------

tower_number = int(turtle.numinput("Tower to Build", "Enter the number of towers you want to build (integer)", minval=1 ))

layer_diff = int(turtle.numinput("Tower Layer Difference", "Enter the number of layer differences between each tower (integer)", minval=2, maxval=5))

tower_distance = int(turtle.numinput("Distance between towers", "Enter the distance between towers (integer)", minval=2, maxval=5))

ftower_layers = int(turtle.numinput("First Tower Layer Amount", "Enter the amount for the first tower layer (integer)", minval=1, maxval=25))

layer_width = int(turtle.numinput("Layer Width", "Enter the width of the layer (integer)", minval=1, maxval=10))

brick_width = int(turtle.numinput("Brick Length", "Enter the length of the brick (integer)", minval=1, maxval=35))

brick_layers = int(turtle.numinput("Brick Width", "Enter the length of the brick width (integer)", minval=1, maxval=25))

# TOWER CODE #----------------------------------------------------------------------

brick_count= 0  # For counting the total number of bricks

for tower in range(tower_number): # Tower Loop

    tower_count = 1      # Undergoes incrementation after each loop for a tower is done
    tower_count += tower # This serves as a tracker of the number of towers for turtle and increases after each loop done for one tower

    for layers in range(ftower_layers + (tower_count -1 )*layer_diff): # Base of the tower and its layers
        for width in range(layer_width): # Width of tower
            brick_count +=1 # Value increases for each loop the variable goes through, tracks total number of bricks
            for sides in range(2): # Makes one brick
                turtle.color('black', '#CA7F65')
                turtle.pendown()
                turtle.begin_fill()
                turtle.fd(brick_width)
                turtle.left(90)
                turtle.fd(brick_layers)
                turtle.left(90)
            turtle.fd(brick_width)
            turtle.end_fill()
        turtle.back(int(layer_width * brick_width)) # Moves turtle to starting point of tower
        turtle.left(90)
        turtle.fd(brick_layers) # Turtle goes up one layer
        turtle.right(90)
    turtle.back(brick_width/2) # Positions turtle for making tower top

    for width in range(layer_width + 1): # Tower top and its width
        brick_count +=1
        for sides in range(2): # Makes one brick
            turtle.color('black', '#693424')
            turtle.begin_fill()
            turtle.fd(brick_width)
            turtle.left(90)
            turtle.fd(brick_layers)
            turtle.left(90)
        turtle.fd(brick_width)
        turtle.end_fill()   
    turtle.penup()


    turtle.left(180) # Mushroom Base
    turtle.fd((layer_width*brick_width/2)+(1.5*brick_width)) # Positions turtle to the middle of the tower
    turtle.right(90)
    turtle.fd(brick_layers)
    turtle.right(90)
    turtle.left(90)
    turtle.color('black', '#f2e0a2')
    turtle.pendown()
    turtle.begin_fill()
    turtle.fd(brick_layers*2)
    turtle.right(90)
    turtle.fd(brick_width*2)
    turtle.right(90)
    turtle.fd(brick_layers*2)
    turtle.right(90)
    turtle.fd(brick_width*2)
    turtle.end_fill()

    turtle.penup()  # Turtle moves to the top of the mushroom
    turtle.right(90)
    turtle.fd(brick_layers*2)
    turtle.left(90)

    turtle.pendown() # Mushroom Cap
    turtle.color('black', 'brown3')
    turtle.right(180)
    turtle.fd(brick_width*2.5)
    turtle.left(90)
    turtle.begin_fill()
    turtle.circle((1.5*brick_width), 180) # Makes a semicircle
    turtle.left(90)
    turtle.fd(brick_width)
    turtle.end_fill()

    turtle.penup() # Mushroom's Eye 1
    turtle.right(90)
    turtle.fd(brick_layers*1.2) # Moves turtle to middle of mushroom
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('black', 'DarkSlateBlue')
    turtle.circle(5, 360) # Makes a big circle
    turtle.end_fill()

    turtle.color('white') # Mushroom Eye 1's shine
    turtle.begin_fill()
    turtle.circle(1.5, 360) # Makes a small circle
    turtle.end_fill()

    turtle.penup() # Mushroom's Eye 2
    turtle.left(90)
    turtle.fd(brick_layers) # Position for next eye
    turtle.right(90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('black', 'DarkSlateBlue')
    turtle.circle(5, 360)
    turtle.end_fill()

    turtle.color('white') # Mushroom Eye 2's shine
    turtle.begin_fill()
    turtle.circle(1.5, 360)
    turtle.end_fill()
    turtle.penup()

    turtle.right(270)       # Makes turtle face the correct direction for making the next tower
    turtle.goto(-350, -200) # Returns turtle to starting position
    turtle.fd( tower_count*((layer_width * brick_width) + (brick_width * tower_distance)) ) # Uniform distance turtle will travel between each tower
    turtle.pendown()

# OUTPUT MESSAGE --------------------------------------------------------------------------

turtle.penup()
turtle.goto(500, -300) # Positions turtle for writing output message
turtle.write( str(tower_number) + " Super Mario Towers have been built with a total of " + str(brick_count) + " bricks", align='right', font=("Arial", 25, "normal"))

turtle.hideturtle()
turtle.exitonclick()