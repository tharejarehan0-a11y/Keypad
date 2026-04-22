# KMK Keyboard Firmware for Raspberry Pi Pico

This project contains the firmware for a custom mechanical keyboard with a 4x10 matrix, built using KMK (Keyboard Maker) on a Raspberry Pi Pico.

## Hardware Setup

- **MCU**: Raspberry Pi Pico
- **Matrix**: 4 rows x 10 columns
- **Row Pins**: GP0, GP1, GP2, GP3
- **Column Pins**: GP6, GP7, GP8, GP9, GP10, GP19, GP20, GP21, GP22, GP23
- **Diode Orientation**: COL2ROW (diodes on columns)
- **Additional**: SW push button on RUN pin (for reset), capacitors (not affecting firmware)

## Keymap Layout

- Row 1: Q W E R T Y U I O P
- Row 2: A S D F G H J K L ;
- Row 3: Z X C V B N M ,
- Row 4: Spacebar (positioned in column 7)

## Setup Instructions

1. **Install CircuitPython on Raspberry Pi Pico**:
   - Download the latest CircuitPython UF2 file for Raspberry Pi Pico from [circuitpython.org](https://circuitpython.org/board/raspberry_pi_pico/).
   - Put the Pico into bootloader mode by holding BOOTSEL while plugging in.
   - Drag the UF2 file onto the RPI-RP2 drive.

2. **Download KMK Library**:
   - Clone or download the KMK firmware repository: `git clone https://github.com/KMKfw/kmk_firmware.git`
   - Copy the `kmk/` folder from the repository to the root of the Pico's CIRCUITPY drive.

3. **Upload Firmware**:
   - Copy `code.py` to the root of the Pico's CIRCUITPY drive.
   - The keyboard should now be recognized as a USB HID device.

4. **Testing**:
   - Connect the keyboard and test the keys.
   - Use a key tester or text editor to verify the layout.

## Customization

- Edit `code.py` to change the keymap or pin assignments.
- Refer to KMK documentation for advanced features like layers, combos, etc.

## Notes

- The SW push button on the RUN pin can be used to reset the Pico if needed.
- Ensure proper wiring and diode orientation for the matrix.