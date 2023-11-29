# OGC.Engineering
### Demo set for Layered Development - an exploration of micropython
developer contact - dustin ( at ) ogc.engineering

---

### From original readme...
```
This is a MicroPython board

You can get started right away by writing your Python code in 'main.py'.

For a serial prompt:
 - Windows: you need to go to 'Device manager', right click on the unknown device,
   then update the driver software, using the 'pybcdc.inf' file found on this drive.
   Then use a terminal program like Hyperterminal or putty.
 - Mac OS X: use the command: screen /dev/tty.usbmodem*
 - Linux: use the command: screen /dev/ttyACM0

For online docs please visit http://docs.micropython.org/
```
---

### Goals:
* Explore advantages and limitations using different microcontroller programming frameworks

---

### Hardware:
* Baseboard
    - ST Micro NUCLEO-L476RG ( rev. C-04 ) - https://www.st.com/en/evaluation-tools/nucleo-l476rg.html
        * STM32 Nucleo-64 development board with STM32L476RG MCU
        * https://www.st.com/resource/en/schematic_pack/mb1136-default-c04_schematic.pdf
    - STM32L476RG - https://www.st.com/en/microcontrollers-microprocessors/stm32l476rg.html
        * Ultra-low-power with FPU Arm Cortex-M4 MCU 80 MHz with 1 Mbyte of Flash memory, LCD, USB OTG, DFSDM
        * https://www.st.com/resource/en/datasheet/stm32l476rg.pdf
---

### Framework:
* Micropython - Python3 for microcontrollers
    - https://micropython.org/
    - https://micropython.org/download
    - https://micropython.org/stm32/
    - https://github.com/micropython/micropython/tree/master/ports/stm32
    - https://micropython.org/download/NUCLEO_L476RG/

---

### Features/Layers:
* Software Application - hardware independent high level direction of device
    - use libraries, HAL interface defintions and/or run time assignment to provide generalized sequenced activities
    - sw_app__demo.py, walks through all features or a prescribed set of events meant to be similar to all other devices in demo set
* Software Libraries - hardware independent support libraries providing reusable functionality
    - libraries provide self contained functionality
    - use predefined calls provided by the HAL interface or use run time assignments to keep logic general and reusable
    - sw_lib__status_indicator_binary.py providing patterns to be displayed on a generic indicator
    - main.py, adapted from original main file to mimic other systems
        * provides initialization and jump to application
        * may provide framework similar to other systems or jump to app and let it take over full control
* Firmware HAL - collection of defintions used to bring hardware/firmware up to interface needed by software
    - fw_hal.py, defines the interface that makes software truly independent of the underlying firmware/hardware
    - uses drivers, CSP, and hardware descriptions to abstract firmware/hardware from software
* Firmware Drivers - hardware dependent support drivers providing reusable functionality
    - uses CSP and hardware descriptions to provide low level sequenced helper functions
* Firmware CSP - Chip Support Package provided by third parties 
    - boot.py, first thing to run that initializes low level things we probably don't need to worry about at the moment
    - builtin resources provided in MicroPython port:
        * https://github.com/micropython/micropython/tree/master/ports/stm32/boards/NUCLEO_L476RG
        * TODO: build instructions versus download .hex package from https://micropython.org/download/NUCLEO_L476RG/
        * TODO: document machine and other imports provided by this section
* Hardware Description - defintions of hardware capabilities and resources used/needed
    - hw_description.py
---

### Development Notes/Steps:
* Development Machine and programs:
    - Ubuntu 22.04
    - sudo apt install thonny
1. Download Micropython .hex for NUCLEO-L476RG from https://micropython.org/download/NUCLEO_L476RG/
    * at time of documentation, "MicroPython v1.21.0 on 2023-10-06; NUCLEO-L476RG with STM32L476RG"
2. Use STM32CubeProgrammer to connect to, erase, and flash micropython .hex file onto NUCLEO board
    * TODO: add links to programmer GUI tool and command line tools and gui stlink-tools, stlink-gui
3. Use Thonny IDE installed from the command line and connect to your new Micropython device
    * Select Tools > Options... and got to the Interpretor tab
    * Select "MicroPython (generic)" for the interpreter and select the STM32 STLink device in the "Port" dropdown
    * press "OK" and your device should connect withthe MicrPython prompt >>> being seen in the Shell tab
    * Ctrl-D in the console causes device to soft reboot and execute program
    * Ctrl-F2 or click "STOP/RESTART Backend" in the to stop device running in order to save regain control of device for saving files
4. Update "main.py" as the entry point
    * TODO: explore modification of boot.py for additional features/customization