import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.col_pins = (board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18)
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.keymap = [
                   [KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P],
                   [KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN],
                   [KC.NO, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.BSPC, KC.NO],
                   [KC.NO, KC.NO, KC.NO, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO]
                   ]

if __name__ == '__main__':
    keyboard.go()