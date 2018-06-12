## TIME TABLE ANALYSER

This is a program that analyses the image of a VITian's time table and determines the filled and free slots of the week. It's writen in Python 3.

## DEPENDENCIES
> Numpy<br/>
> PIL<br/>
> json

## INPUT
As of 12th June, 2018, the program takes in a PNG image of a VITian's time table.<br/><br/>

<b>The image must contain all the slots completely. You need not include the entire time table image: only the part showing your filled slots may be included. BUT, all the boxes (cells) of the time table, starting from MONDAY 08:00 till your last class should be enclosed entirely, i.e., the individual green boxes that show your slots should not be cropped.<br/><br/>

See the file "minimum.png". This file shows the minimum information needed in the image. THE FILE SHOWS CLASSES FROM MONDAY TO FRIDAY.<br/><br/>

A time table that does not contain the black demarcation lines (like the file "dead_tt.jpg") won't be accepted.</b>

## OUTPUT
A one-dimensional JSON array containing all slots' info for all days of the week, one after the other.
For each day, there are 13 values, as there are 13 time slots everyday (TH + LAB)<br/>
1 = Filled slot<br/>
0 = Empty slot<br/>
<br/>
The first 13 values of the JSON array are the time slot values for Monday, the next 13 for Tuesday, and so on.

## CONSTRAINTS
It can only work upon PNG files right now. It can take in JPG/JPEG files too but there's a high possibility of errors, as there's no fixed compression threshold for JPG/JPEG files and the pixel values vary largely.
