"""This is the entry point of the program."""

"""def create_box(height, width, character):
    box = ''
    for i in range(height):
        box_width = ''
        for j in range(width):
            box_width += character
        box_width += '\n'
        box += box_width
    return box"""
    
    #shortened version (commented code is what is added for to create_special_box)
def create_box(height, width, character):
    box = ''
    for i in range(height):
        for j in range(width):
                #if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            box += character
            #else:
                #box += ' '
        box += '\n'
    return box
    
def create_special_box(height, width, character):
    box = ''
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                box += character
            else:
                box += ' '
        box += '\n'
    return box
    
    """while version
def create_box(height, width, character):
    box = ''
    count_height = 0
    count_width = 0
    while count_width < width and count_height < height:
        box += character
        count_width += 1
        if count_width == width:
            box += '\n'
            count_width = 0
            count_height += 1
    return box"""

    
    
"""def create_special_box(height, width, character):
    topbot = width*character + '\n'
    middle_line = character + ((width-2) * " ") + character + '\n'
    middle = middle_line * (height - 2)
    final_box = topbot + middle + topbot
    
    return final_box"""
    
"""Another create_special_box function, by Viet Pham
def create_special_box(height, width, character):
    topbot = width*character + '\n'
    middle = ''
    for i in range(height-2):
 +        box_width = character
 +        for j in range(width-2):
 +            box_width += ' '
 +        box_width += character + '\n'
 +        middle += box_width
 +    
 +    finalbox = topbot + middle + topbot
 +    
 +    return finalbox"""


if __name__ == '__main__':
    create_box(3, 4, '*')
