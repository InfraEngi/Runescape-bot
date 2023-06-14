import cv2 as cv
import numpy as np
import os
import pyautogui
import time
import win32gui, win32ui, win32con
from PIL import ImageGrab

#while(True):
windowtocapture = 'RuneLite - Spratus2'
window_handle = win32gui.FindWindow(None, windowtocapture)
if not window_handle:
    raise Exception('Window not found: {}'.format(windowtocapture))
region = win32gui.GetWindowRect(window_handle)

# these are to help calulations below of the specific points in the windows
top_right_corner = region[2], region[1]
top_left_corner = region[0], region[1]
bottom_left_corner = region[0], region[3]
bottom_right_corner = region[2], region[3]

# These are the calulations of the inventory when runelite sidepanel is open
inventory_bottom_right = ((bottom_right_corner[0] - 285), (bottom_right_corner[1] - 45))
inventory_bottom_left = ((bottom_right_corner[0] - 485), (bottom_right_corner[1] - 45))
inventory_top_right = (top_right_corner[0] - 285), (top_right_corner[1] + 652)
inventory_top_left = (top_right_corner[0] - 485), (top_right_corner[1] + 652)
inventory_region_with_side_panel = (inventory_top_left[0], inventory_top_left[1], inventory_bottom_right[0], inventory_bottom_right[1])

# These are the coordinate numbers you can adjust to make sure that the mouse movements are correct when moving to 
# inventory spaces
x_column_1 = 38
x_column_2 = 80
x_column_3 = 122
x_column_4 = 164
y_row_1 = 30
y_row_2 = 65
y_row_3 = 100
y_row_4 = 135
y_row_5 = 170
y_row_6 = 207
y_row_7 = 242

# Locations for the 28 different place in the inventory
# starting from top left to bottom right
Inventory_space_1   =    ((inventory_top_left[0] + x_column_1 ) , (inventory_top_left[1] + y_row_1))
Inventory_space_2   =    ((inventory_top_left[0] + x_column_2 ) , (inventory_top_left[1] + y_row_1))
Inventory_space_3   =    ((inventory_top_left[0] + x_column_3 ) , (inventory_top_left[1] + y_row_1))
Inventory_space_4   =    ((inventory_top_left[0] + x_column_4 ) , (inventory_top_left[1] + y_row_1))
Inventory_space_5   =    ((inventory_top_left[0] + x_column_1 ) , (inventory_top_left[1] + y_row_2))
Inventory_space_6   =    ((inventory_top_left[0] + x_column_2 ) , (inventory_top_left[1] + y_row_2))
Inventory_space_7   =    ((inventory_top_left[0] + x_column_3 ) , (inventory_top_left[1] + y_row_2))
Inventory_space_8   =    ((inventory_top_left[0] + x_column_4 ) , (inventory_top_left[1] + y_row_2))
Inventory_space_9   =    ((inventory_top_left[0] + x_column_1 ) , (inventory_top_left[1] + y_row_3))
Inventory_space_10  =    ((inventory_top_left[0] + x_column_2 ) , (inventory_top_left[1] + y_row_3))
Inventory_space_11  =    ((inventory_top_left[0] + x_column_3 ) , (inventory_top_left[1] + y_row_3))
Inventory_space_12  =    ((inventory_top_left[0] + x_column_4 ) , (inventory_top_left[1] + y_row_3))
Inventory_space_13  =    ((inventory_top_left[0] + x_column_1 ) , (inventory_top_left[1] + y_row_4))
Inventory_space_14  =    ((inventory_top_left[0] + x_column_2 ) , (inventory_top_left[1] + y_row_4))
Inventory_space_15  =    ((inventory_top_left[0] + x_column_3 ) , (inventory_top_left[1] + y_row_4))
Inventory_space_16  =    ((inventory_top_left[0] + x_column_4 ) , (inventory_top_left[1] + y_row_4))
Inventory_space_17  =    ((inventory_top_left[0] + x_column_1 ) , (inventory_top_left[1] + y_row_5))
Inventory_space_18  =    ((inventory_top_left[0] + x_column_2 ) , (inventory_top_left[1] + y_row_5))
Inventory_space_19  =    ((inventory_top_left[0] + x_column_3 ) , (inventory_top_left[1] + y_row_5))
Inventory_space_20  =    ((inventory_top_left[0] + x_column_4 ) , (inventory_top_left[1] + y_row_5))
Inventory_space_21  =    ((inventory_top_left[0] + x_column_1 ) , (inventory_top_left[1] + y_row_6))
Inventory_space_22  =    ((inventory_top_left[0] + x_column_2 ) , (inventory_top_left[1] + y_row_6))
Inventory_space_23  =    ((inventory_top_left[0] + x_column_3 ) , (inventory_top_left[1] + y_row_6))
Inventory_space_24  =    ((inventory_top_left[0] + x_column_4 ) , (inventory_top_left[1] + y_row_6))
Inventory_space_25  =    ((inventory_top_left[0] + x_column_1 ) , (inventory_top_left[1] + y_row_7))
Inventory_space_26  =    ((inventory_top_left[0] + x_column_2 ) , (inventory_top_left[1] + y_row_7))
Inventory_space_27  =    ((inventory_top_left[0] + x_column_3 ) , (inventory_top_left[1] + y_row_7))
Inventory_space_28  =    ((inventory_top_left[0] + x_column_4 ) , (inventory_top_left[1] + y_row_7))






    # These are the calulations of the inventory when runelite sidepanel is NOT open
    #inventory_bottom_right = ((bottom_right_corner[0] - 285), (bottom_right_corner[1] - 45))
    #inventory_bottom_left = ((bottom_right_corner[0] - 485), (bottom_right_corner[1] - 45))
    #inventory_top_right = (top_right_corner[0] - 285), (top_right_corner[1] + 652)
    #inventory_top_left = (top_right_corner[0] - 485), (top_right_corner[1] + 652)
    #inventory_region = (inventory_top_left[0], inventory_top_left[1], inventory_bottom_right[0], inventory_bottom_right[1])


    


    #screenshot = ImageGrab.grab(bbox=(inventory_region))
    #screenshot = np.array(screenshot)
    #screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)


    #cv.imshow('Overview Vision', screenshot1)
    #cv.imshow('Computer Vision', screenshot)
    #if cv.waitKey(1) == ord('q'):
        #cv.destroyAllWindows()
        #break

    #north_iron_ore_image = 'Images\Iron ore 2.png'
    #south_iron_ore_image = 'Images\Iron ore 1.png'
    #west_iron_ore_image = 'Images\Iron ore 3.png'

    