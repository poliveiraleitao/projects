#get the x and y coordinates of each state
def get_mouse_click_coor(x,y):
    print(x,y)

#call the get mouse click coor function
turtle.onscreenclick(get_mouse_click_coor)
#keep the screen open
turtle.mainloop()