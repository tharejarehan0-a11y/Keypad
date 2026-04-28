# Keypad
<br>

<img width="1536" height="824" alt="ChatGPT Image Apr 22, 2026, 09_27_56 AM" src="https://github.com/user-attachments/assets/ca69ca86-906f-423e-9ba5-332e965acd4e" style="background-color:black"/>

<br>

# **Keyboard for Beginners**
(_It is Keypad a keyboard designed specifically to make learning touch typing efficient and more easy for beginners_)

<br>

<p align="center">
<img width="475" height="673" alt="Screenshot 2026-04-24 at 2 32 22 AM" src="https://github.com/user-attachments/assets/31bce5ec-4a6b-48a8-b2fe-bfb89ea2f251" />


</p>

<br>

# **Story Behind it/Motivation**
When I started my computer journey I started learning how to do typing fast (_touch typing_). I was made to type only alphabets in the whole course some or the other way for me there was like no use of other keys similarly for many people other keys are just useless when they want to learn typing or practice it **and it is specifically designed for it**

# **Key takeaways**


1. Best for people starting touch typing
2. More portable if only learning to type
3. Mechanical keyboard with MX Cherry Keys
4. Can be customized using the firmware unlike ordinary keyboards

# **Schematics**

# Matrix
<br>
<img width="980" height="373" alt="Screenshot 2026-04-22 at 7 55 31 PM" src="https://github.com/user-attachments/assets/76c8dc9d-9b78-4492-866c-18a3cb44748e" />
<br><br>

**These keys are layed in a matrix of rows and columns. There are 10 columns and 4 rows in the matrix. All the intersection of the rows and columns constitute a key here. The microconttroller that will be attached to these will detect low currect at the key you will press and will have already the columns and rows assigned in the firmware that let it know where the key to detect is. I have attached global labels of rows and columns which can be attached to the microcontroller and help the schematics look a lot cleaner**

<br><br>
# Keys
<br>
<img width="476" height="677" alt="Screenshot 2026-04-22 at 7 51 36 PM" src="https://github.com/user-attachments/assets/5bc727f7-dc75-461e-a285-0a9e8b5f84eb"/>

<br><br>
**The key composes of a keyswitch and a diode these help the microcontroller help detect the lower currect in the matrix of rows and columns**

<br><br>
# Microcontroller
<br>
<img width="616" height="774" alt="Screenshot 2026-04-22 at 7 51 54 PM" src="https://github.com/user-attachments/assets/fa33a21b-1377-4b55-b11d-98e431b98ffe" />

<br><br>
**As a microcontroller we are using the raspberry pi pico which has 22 gpio pins the net lablels or the global net labels are attached to these pins only. The ADC_VREF pin is the analog to digital converter the 3.3v is fed into this pin but has lot of noise that is why we add a capatior of 100nF here. Then we have the 3v3 pin and the run pin . The run pin is connected to a sw_push button with one end of the push button connected to gnd and other end free and the 3v3 pin is essentially the pin that gives out the the 3v3 current it has two capacitors parallely of 100nF and 10µF to reduce the noise you can check out the design at mech_keyboard.kicad_sch**

<br><br>

# **PCB Design**
<br>
<img width="1098" height="554" alt="Screenshot 2026-04-22 at 8 22 37 PM" src="https://github.com/user-attachments/assets/9e567c56-8cc2-434a-990c-5aca457d82d8" />
<br>

**This is the PCB Design of the keyboard having the footprints of keys of MX_Cherry , The Raspberry pi pico, resistors_smd_do35, sw_push_button and capacitors. There are also mounting holes on the pcb for the screws to fit in . We will be using the m2 screws having dimensions 2mm * 6mm and 2mm * 8mm for it . The routing follows the pattern that the capacitors , sw_push and resistors are done in the front chopper layer and the columns in the back chopper layer but there are vias also present in the pcb which make it hetrogeneous.<br><br>We have used to grind one is 19.05mm and other is 2.3813mm. the first was used for the keys which were moved by reference to it's upper right corner and the second was used for resistors which were moved without any resistors. You can check out the design in mech_Keyboard.kicad_pcb**

# **CAD**
<br>

<img width="1470" height="956" alt="Screenshot 2026-04-22 at 8 37 48 PM" src="https://github.com/user-attachments/assets/211d09b4-7761-42b5-940f-cb7483637d85" />
<br>

**Go to https://www.keyboard-layout-editor.com/ to design a keyboard here we designed it complementing to our pcb and schematics paste this in the raw data tab of the site** 

<br>
<br>

```
  [{ "a": 7 }, "", "", "", "", "", { "x": 3 }, "", "", "", "", ""],
  ["", "", "", "", "", { "x": 3 }, "", "", "", "", ""],
  [{ "x": 1 }, "", "", "", "", { "x": 3 }, "", "", "", ""],
  [{ "x": 3, "w": 7 }, ""]
```


<br>

**then go to https://swillkb.com/ and paste the either the raw data of your design under the raw data tab or paste this onto the website u will get a dxf file which you can also take from the files here**

# shapr3D 

<br>

<img width="1470" height="956" alt="Screenshot 2026-04-22 at 1 04 12 AM" src="https://github.com/user-attachments/assets/98172e3a-b482-4300-97a1-6d5ec6d7a977" />
<br>

**if you want to see the full design . You can go to https://app.shapr3d.com/p/c7965ff8-f383-481d-b931-e097212123b2 . This will lead you to the browser version of the shapr3D where you can download the files if you have the upgraded versions or you can see the through out the design if you don't have it you can take all the stl files from the Assets_3d_printing folder tho and then also do whatever you wanna do with them**

<br>

# **firmware**

<br>

<img width="1470" height="956" alt="Screenshot 2026-04-23 at 7 25 21 PM" src="https://github.com/user-attachments/assets/bd0bb8fa-868b-462b-a88a-9fa4b1cf6fa8" />

<br>

**The firmware is written in Circuit python and has KMK library used to program the keyboard the keymap array is used to assign the keys to the intersection and the rows and columns are denoted by keyboard.row_pins and keyboard.col_pins and we have a name function which loads the code onto the keyboard.**

<br>

# **Assets**
1. **Assets_3d_printing** - it has all the files required for 3d printing
2. **Assets_Kicad** - it has all the kicad resources you will require 3d_models, footprints and symbols
3. **firmware** - it has all the files required for the firmware of the keyboard to program the microcontroller
4. **PCB.step** - it is the 3d model of the pcb

<br>

# **Components**

1. **Raspberry pi pico**
2. **MX Cherry 1.00u Keys and Keycaps**
3. **MX Cherry 7.00u Keycap and stablizer**
4. **PCB**
5. **DO-35 Resistors**
6. **SMD C_0603_1608Metric Capacitors**
7. **SW_Push Button**
8. **USB_A to USB_B wire**
9. **M2 2mm*6mm screws**

<br>

# **files**

<br>

1. **Readme.md** : explanation of all the project <br>
2. **BOM.csv** : Bill of materials used in the project shipping not included <br>
3. **mech_Keyboard.kicad_pcb** : The PCB design used (Kicad file) <br>
4. **mech_Keyboard.kicad_sch** : The schematics used (Kicad file) <br>
5. **mech_keyboard.kicad_pro** : The main kicad file <br>
6. **mech_keyboard-backups** : The folder with the backups of these files <br> 
7. **Archive** : Contains all the fabrication files used in the pcb manufacturing process <br>
8. **firmware** : This contains the firmware for the keyboard to be used <br>
9. **Assets_3d_printing*** : All the assets needed for 3D printing <br>
10. **Assets_Kicad** : All the assets needed for the schematics and pcb design including the 3d models <br>
11. **Zinepage.png** : has the A5 Design for the fallout zine <br>
