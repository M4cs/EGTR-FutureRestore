<p align='center'>
  <a href=''><img src="https://cdn.discordapp.com/attachments/422105201605083136/540718008662753310/unknown.png"></a>
  <h1 align='center'>EGTR - Cross Platform GUI for FutureRestore</h1>
</p>

Developer: [@maxbridgland](https://twitter.com/maxbridgland)

Version: 1.0.2

Release Date: 01/31/2019

License: GPL v3

# Introduction:

EGTR stands for Easy Gui To Restore. I couldn't think of a name so I just went with that acroynm. The tool allows you to specify multiple options and get to restoring a lot easier. **I'm not responsible for any issues this may cause with your device. It works the same as futurerestore so you have the same concequences when using it.** This doesn't include any code from futurerestore or any other program. The program obtains the futurerestore binary from the official s0uthwest release repository [here](https://github.com/s0uthwest/futurerestore/releases).

***USE THE LATEST SEP AND LATEST BASEBAND TO YOUR OWN DISCRECTION. IT HAS BEEN CONFIRMED TO HAVE SOME ISSUES WITH S0UTHWEST'S BUILD***

# Changelog:

### 1.0.5:

- UI Update, Added Exit Recovery Mode, Fixed Some Bugs :)

### 1.0.3 & 1.0.4:

- Removed and then added back Latest SEP and Baseband

### 1.0.2:

- Fix Freezing Bugs in screens.

### 1.0.1:

- Added more flags.


# Instructions:

### Requirements:

- Python 3.6+
- An Internet Connection

### Tk, Qt, and Wx:

You can use different backend libraries for EGTR's GUI. If you would like to do so simple install either `PySimpleGUI` (TKinter), `PySimpleGUIWx` (Wx) or, `PySimpleGUIQt` (Qt5/PySide2) for Qt. After installing these with `pip` just change the imports in `screens.py` to whatever library you'd like to use.

### Steps:

1. Clone or download this repository,

2. Inside the directory of this download run `pip3 install -r requirements.txt`.

3. Run `python3 egtr.py`.

***On first run you are going to be asked to download FutureRestore. Press continue. The program will close after it finishes downloading. Run step 3 over again to get into the program after downloading.***
