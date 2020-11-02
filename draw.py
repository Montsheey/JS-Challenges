

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():

    while True :
        input_shape = input("Shape?: ")
        input_shape = input_shape.lower()

        if input_shape == "pyramid" :
            shape = input_shape
            break
        elif input_shape == "square" :
            shape = input_shape
            break
        elif input_shape == "triangle" :
            shape = input_shape
            break
    
    return shape


# TODO: Step 1 - get height (it must be int!)
def get_height():

    while True :
        height = input("Height?: ")
        if height.isdigit():
            height=int(height)
            if height <= 80 and height < 0:
                print("invalid height")
            else:
                return height
        """else:
            print("enter number only")"""
     

# TODO: Step 2
def draw_pyramid(height, outline):
    # print('pyramid')

    if outline == True :
        # for r in range (1, height+1):
        #     for c in range (1, 2*height) :
        #         if r == height or r+c == height+1 or c-r == height -1 :
        #             print("*", end="")
        #         else :
        #             print(end=" ")
        #     print()

        # for r in range(height):
        #     for c in range(height - r):
        #         print("",end =" ")
        #     for c in range(2*r + 1):
        #         if r ==  0 or c == 0 or r == height - 1 or c == 2*r:
        #             print("*", end="")
        #         else:
        #             print(end = " ")
        #     print("")

        for r in range(height):
            for c in range((height-r)-1):
                print(end = " ")
            for c in range(2*r+1):
                if (r == 0 or c == 0 or r == height - 1 or c == 2*r):
                    print("*", end="")
                else:
                    print(end = " ")
            print("")

    else :
        for r in range(height):
            for c in range((height-r)-1):
                print(end=" ") 
            for c in range(2*r+1):
                print("*", end="")
            print("")


# TODO: Step 3
def draw_square(height, outline):
    # print('square')

    if outline == True :
        for r in range (height) :
            for c in range (height) :
                if c == 0 or r == 0 or r == height -1 or c == height -1 :
                    print("*", end="")
                else :
                    print(" ", end="")
            print("")

    else :
        for r in range (height) :
            for c in range(height) :
                print("*", end="")
            print("")   
    

# TODO: Step 4
def draw_triangle(height, outline):
    # print('triangle')

    if outline == True :
        for r in range (height) :
            for c in range  (r+1) :
                if c == 0 or r == (height -1) or r == c or r == 0:
                    print("*", end="")
                else :
                    print(end=" ")
            print("")

    else:
        for r in range(height):
            for c in range(r+1):
                print("*", end="")
            print("")


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "square" :
        draw_square(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)
    pass
    


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input('Outline only? (y/N): ')
    outline = outline.lower()
    if outline == 'y':
        return True
    elif outline == 'n':
        return False
    else:
        return get_outline()


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

