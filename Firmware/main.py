# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()

# Add the macro extension if needed (not required for simple 1–9 output)
macros = Macros()
keyboard.modules.append(macros)

# Define your pin order here — make sure it matches your wiring!
PINS = [
    board.D3,  # key 1
    board.D4,  # key 2
    board.D2,  # key 3
    board.D1,  # key 4
    board.D5,  # key 5
    board.D6,  # key 6
    board.D7,  # key 7
    board.D8,  # key 8
    board.D9,  # key 9
]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Keymap: each item corresponds to each pin in order
keyboard.keymap = [
    [
        KC.N1,  # pin 1
        KC.N2,  # pin 2
        KC.N3,  # pin 3
        KC.N4,  # pin 4
        KC.N5,  # pin 5
        KC.N6,  # pin 6
        KC.N7,  # pin 7
        KC.N8,  # pin 8
        KC.N9,  # pin 9
    ]
]

if __name__ == '__main__':
    keyboard.go()
