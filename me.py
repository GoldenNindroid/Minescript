# type: ignore
import minescript as m
import minescript_plus as mp
import time

x,y,z = m.player_position()
x, y, z = int(x), int(y), int(z)
def start(x,y,z):
    m.chat(f"Start Block Position: X={x}, Y={y}, Z={z}")
    m.execute("fill {x} {y} {z} {a} {b} {c} minecraft:black_glazed_terracotta".format(x=x-1, y=y-1, z=z-1, a=x-1, b=y-1,c=z-1))


#simpifing functions
def open_inventory():
    m.press_key_bind("key.inventory", True)
    time.sleep(0.1)
    m.press_key_bind("key.inventory", False)
    time.sleep(0.1)
def hotbar_swap(x):
    m.player_inventory_select_slot(x)

def player_place_block(x,y,z):
    time.sleep(0.1)
    m.player_press_use(True)
    time.sleep(0.1)
    m.player_press_left(True)
    m.player_press_use(False)
    #time.sleep(0.25)
    #m.player_press_left(False)

#walls
def player_made_wall_left():
    #set the orientation
    m.player_set_orientation(0,45)
    time.sleep(0.01)
    m.player_press_use(True)
    #place the wood
    m.player_inventory_select_slot(1)
    time.sleep(0.1)
    m.player_press_use(False)
    time.sleep(0.1)
    m.player_press_left(True)
    #place the planks
    m.player_inventory_select_slot(0)
    m.player_press_use(True)
    time.sleep(4)
    #back to wood
    m.player_inventory_select_slot(1)
    time.sleep(0.01)
    m.player_press_use(True)
    time.sleep(0.01)
    #stopping
    m.player_press_left(False)
    m.player_press_use(False)
def player_made_wall_back():
    # the wood is already there, so we just place the planks
    time.sleep(0.1)
    m.player_inventory_select_slot(0)
    m.player_press_use(True)
    m.player_press_backward(True)
    time.sleep(2)
    m.player_press_use(False)
    time.sleep(0.01)
    m.player_press_backward(False)
    #back to wood
    m.player_inventory_select_slot(1)
    m.player_set_orientation(0,55)
    m.player_press_use(True)
    # just a tiny mirco adjustment to make sure the block places correctly
    m.player_press_backward(True)
    time.sleep(0.1)
    m.player_press_use(False)
    m.player_press_backward(False)
def player_made_wall_right():
    # the wood is already there, so we just place the planks
    m.player_inventory_select_slot(0)
    m.player_press_right(True)
    m.player_press_use(True)
    # the goal is to make the this leg of the wall one-third of the main wall, so we wait less time
    time.sleep(1.4)
    m.player_press_use(False)
    m.player_press_right(False)
    time.sleep(0.01)
    #back to wood
    m.player_inventory_select_slot(1)
    m.player_press_use(True)
    time.sleep(0.05)
    m.player_press_use(False)
def player_made_wall_foward():
    # because the wood is in the way, we need to jump to place the planks
    m.player_press_jump(True)
    m.player_press_forward(True)
    time.sleep(0.3)
    m.player_press_forward(False)
    m.player_press_jump(False)
    #we have to face down to place the planks because the log would be in the way
    m.player_set_orientation(0,60)
    time.sleep(0.1)
    m.player_inventory_select_slot(0)
    m.player_press_use(True)
    m.player_press_forward(True)
    time.sleep(0.66)
    m.player_press_use(False)
    m.player_press_forward(False)

#material gathering
def get_wood():
    plank_slot = int(mp.Inventory.find_item("minecraft:oak_log"))
    m.echo(plank_slot)
    if plank_slot != 1:
        # You cannot move an item from the inventory to hotbar without the Inventory being open
        # So, we open the Inventory
        m.press_key_bind("key.inventory", True)
        time.sleep(0.5)
        m.press_key_bind("key.inventory", False)
        time.sleep(0.5)

        mp.Inventory.inventory_hotbar_swap(plank_slot, 1)
    else:
        m.player_inventory_select_slot(1)
def get_oak_planks():
    plank_slot = int(mp.Inventory.find_item("minecraft:oak_planks"))
    m.echo(plank_slot)
    if plank_slot != 0:
        # You cannot move an item from the inventory to hotbar without the Inventory being open
        # So, we open the Inventory
        m.press_key_bind("key.inventory", True)
        time.sleep(0.5)
        m.press_key_bind("key.inventory", False)
        time.sleep(0.5)

        mp.Inventory.inventory_hotbar_swap(plank_slot, 0)
    else:
        m.player_inventory_select_slot(0)



# actual execution

#               o                   o                
#___________________________________________________#
#(heh look, i make a face)


#gets starting position and places a marker block
start(x,y,z)
#getting materials
open_inventory()
time.sleep(0.1)
get_wood()
time.sleep(0.1)
get_oak_planks()
time.sleep(0.1)
mp.Screen.close_screen()
time.sleep(0.2)

#walls
player_made_wall_left()
time.sleep(0.2)
player_made_wall_back()
time.sleep(0.2)
player_made_wall_right()
time.sleep(0.2)
player_made_wall_foward()