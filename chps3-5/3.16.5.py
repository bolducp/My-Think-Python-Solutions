def draw_grid():
    draw_horizontal()
    draw_vertical()
    draw_horizontal()
    draw_vertical()
    draw_horizontal()
    
def draw_horizontal():
    print '+ ' + '- '* 4 + '+ ' + '- ' * 4 + '+'
    
def draw_vertical():
    print '|' + ' ' * 9 + '|' + ' ' * 9 + '|'
    
    
draw_grid()