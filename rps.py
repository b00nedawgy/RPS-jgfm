import PySimpleGUI as sg
from PIL import Image
from lib_RPS import bot_rps, bot_drc, rps, drc, rps_battle

sg.theme("Dark Blue 3")

col = [
    [sg.Button("Rock", size = (9,1))],
    [sg.Button("Paper", size = (9,1))],
    [sg.Button("Scissors", size = (9,1))],
]

colr = [
    [sg.Button("Up", size = (5,1), key = "Up")],
    [sg.Button("Left", size = (5,1), key = "Left"),
    sg.Button("Right", size = (5,1), key = "Right")],
    [sg.Button("Down", size = (5,1), key = "Down")]
]

bh = [
    [sg.Image(filename = "imgs/no_one.png", size = (50,50),
    visible = False, key = "bot_hand_img")]
]

ph = [
    [sg.Image(filename = "imgs/no_one.png", size = (50,50),
    visible = False, key = "player_hand_img")]
]

layout = [
    [sg.Image(key="the_image", filename = "imgs/pandaman.png", size = (500, 500))],

    [sg.Frame('',
    [[sg.Column(bh, key = "bh_col", background_color = "black")]],
    size = (60,60), background_color = "white")],

    [sg.Frame('',
    [[sg.Column(bh, key = "ph_col", background_color = "black")]],
    size = (60,60), background_color = "white")],

    [sg.Frame('',
    [[sg.Column(col, key = "col", element_justification = 'c', background_color = "blue")]],
    background_color = "blue", key = "frame", visible = True,
    size = (100, 80), element_justification = 'c'),

    sg.Frame('',
    [[sg.Column(colr, key = "colr", element_justification = 'c', background_color = "red")]],
    background_color = "red", key = "frame2", visible = False,
    size = (100,80), element_justification = 'c')]
]

def toggle_visibility(tof):
    window["frame"].update(visible = tof)
    window["frame2"].update(visible = not tof)

margins = (30, 30)

window = sg.Window("Rock Paper Scissors", layout, margins, 
                    element_justification = 'c', element_padding = 1)
phase = 1
winner = 0
winner2 = 0

while True:
    print("phase: "+str(phase))
    event, values = window.read()
    if event == sg.WIN_CLOSED or winner2 != 0:
        break
    elif (event in rps) and phase == 1: #rock paper scissor phase
        bot_hand = bot_rps()
        battle = rps_battle(str(event), bot_hand)
        print("your hand:"+event)
        print("bot: "+bot_hand)
        print("battle: "+str(battle))
        if battle == 0:
            continue
        elif battle == 1:               #player won move to pointing phase
            winner = 1
            print("won rock paper scissors")
        elif battle == -1:              #bot won move to pointing phase
            winner = 2
            print("lost rock paper scissors")
        phase = 2
        toggle_visibility(False)
    elif (event in drc) and phase == 2: #point in a direction phase
        bot_face = bot_drc()
        battle_drc = bot_face
        print("you pointed: "+event)
        print("bot pointed: "+bot_face)
        if winner == 1 and event == battle_drc:
            winner2 = 1
            break
        elif winner == 2 and event == battle_drc:
            winner2 = 2
            break
        phase = 1
        toggle_visibility(True)
if winner2 == 1:
    print("You Won!")
elif winner2 == 2:
    print("You Lost")
window.close()
