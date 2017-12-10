# SlidingWindow
It is __STOP AND WAIT__ Protocol in python. With minute changes you can use it for __Selective Repeat__ and __GO-Back N__ Protocol.


Author : Syed Alfran Ali

Used: Python 3 and pygame library

## Instructions to run the python file:
For Windows:
````
	1) Install python:
		https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation
	2) Install Pygame
````	
For Linux:
````
	1) Use ./sliding_window.py in the current directory or chmod to change the permissions.
````
## After running the sliding_window.py file :
Give the following parameters:
````
a) Sliding Window Size
b) Speed of packets transfer
````

To give these values simply click on the GUI Window's black block corresponding to the parameter , enter the value and than press enter.
After pressing enter the value will be shown in the corresponding block. Do this both for sliding window size and speed.
Or for default just click start button. Default window size = 4 and speed =4
The window would wrap around after visiting the entire screen.
To stop the window stop hovering the mouse.
Otherwise keep hovering after window finishes the ack. process. 
So to kill the process task manager has to be used to end process.
