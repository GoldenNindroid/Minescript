# type: ignore
import minescript as m
import minescript_plus as mp
import time

x,y,z = m.player_position()
x, y, z = int(x), int(y), int(z)
def start(x,y,z):
    m.chat(f"Start Block Position: X={x}, Y={y}, Z={z}")
    m.execute("fill {x} {y} {z} {a} {b} {c} minecraft:black_glazed_terracotta".format(x=x-1, y=y-1, z=z-1, a=x-1, b=y-1,c=z-1))


def player_place_block(x,y,z):
    time.sleep(0.1)
    m.player_press_use(True)
    time.sleep(0.1)
    m.player_press_left(True)
    m.player_press_use(False)
    #time.sleep(0.25)
    #m.player_press_left(False)

def player_made_wall_left():
    m.player_set_orientation(0,45)
    time.sleep(0.01)
    m.player_press_use(True)
    m.player_inventory_select_slot(1)
    time.sleep(0.1)
    m.player_press_use(False)
    time.sleep(0.1)
    m.player_press_left(True)
    m.player_inventory_select_slot(0)
    m.player_press_use(True)
    time.sleep(4)
    m.player_inventory_select_slot(1)
    time.sleep(0.01)
    m.player_press_use(True)
    time.sleep(0.01)
    m.player_press_left(False)
    m.player_press_use(False)
def player_made_wall_back():
    time.sleep(0.1)
    m.player_inventory_select_slot(0)
    m.player_press_use(True)
    m.player_press_backward(True)
    time.sleep(2)
    m.player_press_use(False)
    time.sleep(0.01)
    m.player_press_backward(False)
    m.player_inventory_select_slot(1)
    m.player_set_orientation(0,55)
    m.player_press_use(True)
    m.player_press_backward(True)
    time.sleep(0.01)
    m.player_press_use(False)
    m.player_press_backward(False)
def player_made_wall_right():
    m.player_inventory_select_slot(0)
    m.player_press_right(True)
    m.player_press_use(True)
    time.sleep(1.4)
    m.player_press_use(False)
    m.player_press_right(False)
    time.sleep(0.01)
    m.player_inventory_select_slot(1)
    m.player_press_use(True)
    time.sleep(0.05)
    m.player_press_use(False)
def player_made_wall_foward():
    m.player_press_jump(True)
    m.player_press_forward(True)
    time.sleep(0.1)
    m.player_press_forward(False)
    m.player_press_jump(False)

def get_wood():
    wood_slot = int(mp.Inventory.find_item("minecraft:oak_log"))
    if wood_slot != 1:
        m.player_inventory_select_slot(wood_slot)
    else:
        mp.Inventory.inventory_hotbar_swap(wood_slot, 1)
        m.player_inventory_select_slot(1)
def get_oak_planks():
    planks_slot = int(mp.Inventory.find_item("minecraft:oak_planks"))
    if planks_slot != 0:
        m.player_inventory_select_slot(planks_slot)
    else:
        mp.Inventory.inventory_hotbar_swap(planks_slot, 0)
        m.player_inventory_select_slot(0)
start(x,y,z)


#getting materials
get_wood()
time.sleep(0.1)
get_oak_planks()
time.sleep(0.1)

#walls
player_made_wall_left()
time.sleep(0.2)
player_made_wall_back()
time.sleep(0.2)
player_made_wall_right()
time.sleep(0.2)
player_made_wall_foward()