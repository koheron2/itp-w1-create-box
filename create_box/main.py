"""This is the entry point of the program."""

def create_box(height, width, character):
    box = ''
    for i in range(height):
        box_width = ''
        for j in range(width):
            box_width += character
        box_width += '\n'
        box += box_width
    return box
    
    
def create_special_box(height, width, character):
    topbot = width*character + '\n'
    middle_line = character + ((width-2) * " ") + character + '\n'
    middle = middle_line * (height - 2)
    final_box = topbot + middle + topbot
    
    return final_box


if __name__ == '__main__':
    create_box(3, 4, '*')
