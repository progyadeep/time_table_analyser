# Documentation
Version 1.0
<br/>

<table>
  <tr>
    <td><h3>Element</h3></td> <td><h3>Type</h3></td> <td><h3>Purpose</h3></td>
  </tr>
  
  <tr>
    <td>slot_state((14,13))</td> <td>Numpy array</td> <td>This stores the state of all the slots (1 = filled, 0 = empty) of the week.</td>
  </tr>
  
  <tr>
    <td>cd</td> <td>Python list</td> <td>Stores the [i,j] coordinates of the slot in <b>slot_state</b> that is to be evaluated currently.</td>
  </tr>
  
  <tr>
    <td>tt</td> <td>Image</td> <td>Holds the image of the timetable that is being analysed.</td>
  </tr>
  
  <tr>
    <td>dim</td> <td>Python list</td> <td>Stores the dimensions of <b>tt</b>: <i>[width, height]</i></td>
  </tr>
  
  <tr>
    <td>isBlack(rgb)</td> <td>Python function</td> <td>Determines whether the pixel, whose RGB values are passed in a <b>tuplet</b> as argument to this function, is a (seemingly) black pixel or not.</td>
  </tr>
  
  <tr>
    <td>isVCP(rgb)</td> <td>Python function</td> <td>Determines whether the pixel, whose RGB values are passed in a tuplet as argument to this function, is part of a horizontal line that divides the cells in the time table as you move down.</td>
  </tr>
  
  <tr>
  <td>updateNPCoord()</td> <td>Python function</td> <td>Updates the values of <b>cd</b> to hold the coordinates of the next slot to be evaluated in <b>slot_state</b></td>
  </tr>
  
  <tr>
  <td>cols</td> <td>tuplet</td> <td>Holds RGB values of the <b>green, yellow & light brown</b> colours that are used to highlight the slots in the time table - each as individual tuplets. <i>This is a 2D tuplet</i>.</td>
  </tr>
  
  <tr>
    <td>start</td> <td>Python list</td> <td>Holds the [i,j] coordinates of the first significant pixel inside the cell of the first <b>A1</b> slot <i>(Monday's 8 'o' clock class slot)</i> in the timetable image. <b>NOTE:</b> <i>A significant pixel is one which is exactly of one of the three standard green/yellow/light brown colours used to highlight slots in the time table.</i>.</td>
  </tr>
</table>
