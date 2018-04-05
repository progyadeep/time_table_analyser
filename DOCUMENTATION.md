# Documentation
This is a documentation of the program.  

<hr/>

<table>
  <tr>
    <td><h3>Element</h3></td> <td><h3>Type</h3></td> <td><h3>Purpose</h3></td>
  </tr>
  
  <tr>
    <td>slot_state((14,13))</td> <td>Numpy array</td> <td>A 14x13 array that holds the states of all the slots of the week: 1 = filled slot, 0 = empty slot</td>
  </tr>
  
  <tr>
    <td>cd</td> <td>Python list</td> <td>This is a list of size 2 that holds the [i,j] coordinates of the <i>next</i> slot in the <i>slot_state</i> array that is to be manipulated.</td>
  </tr>
  
  <tr>
    <td>tt</td> <td>PIL Image</td> <td>This variable holds the image of the time table that is to be analysed.</td>
  </tr>
  
  <tr>
    <td>dim</td> <td>Python list</td> <td>This is a list of size 2 that holds the dimensions of the image in the form: <i>[width, height]</i>.</td>
  </tr>
  
  <tr>
    <td>isBlack(rgb)</td> <td>Python function</td> <td>Determines whether the pixel, whose RGB values are passed as its argument, is a (seemingly) black pixel or not.</td>
  </tr>
  
  <tr>
    <td>isVCP(rgb)</td> <td>Python function</td> <td>Determines whether the pixel, whose RGB values are passed as its argument, is a horizontal line (that separates two adjacent slot cells in the time table) or not.</td>
  </tr>
  
  <tr>
    <td>updateNpCoord()</td> <td>Python function</td> <td>This function updates the values of <b>cd</b> to the next slot in <b>slot_state</b> everytime a cell in <b>slot_state</b> is evaluated.</td>
  </tr>
  
  <tr>
    <td>cols</td> <td>Python tuplet</td> <td>This is a tuplet that holds 3 tuplets. The inner tuplets hold the RGB values of the <b>green</b>, <b>yellow</b> and <b>light brown</b> colour that are used to highlight slots in the VIT time table.</td>
  </tr>
  
  <tr>
    <td>start</td> <td>Python list</td> <td>This is a list of size 2 that holds the [i,j] coordinates of the first <i>significant</i> pixel inside the first slot cell (i.e., A1) in the time table. <i>[A significant pixel is one which is either of the three colours defined by the RGB values stored in <b>cols</b>.]</i></td>
  </tr>
</table>
