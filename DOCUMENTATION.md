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
    <td>cd[,]</td> <td>Python list</td> <td>Stores the [i,j] coordinates of the slot in <b>slot_state</b> that is to be evaluated currently.</td>
  </tr>
  
  <tr>
    <td>tt</td> <td>Image</td> <td>Holds the image of the timetable that is being analysed.</td>
  </tr>
  
  <tr>
    <td>dim</td> <td>Python list</td> <td>Stores the dimensions of <b>tt</b>: <i>[width, height]</i></td>
  </tr>
</table>
