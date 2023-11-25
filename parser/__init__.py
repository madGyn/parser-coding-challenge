"""
<h1>Parser Coding Challenge</h1>
<h2>Exercise</h2>
<span>In this exercise, a C, C++ or Python application should be written that prints the layout of the sample
file (showing how boxes are nested, e.g. with indentation) and extracts the content of the MDAT box.
The application should work in either Linux, macOS or Windows and you are free to use whatever
libraries you see fit, however do not use a library that is already doing the parsing itself as that’s the
point of this exercise.
It should provide the following:
<ul>
<li>Read the sample file from disk</li>
<li>
Iterate through the file and print the size and type of each box found to the console. The
following assumptions can be made:
    <ul>
        <li>A box of type MOOF only contains other boxes</li>
        <li>A box of type TRAF only contains other boxes</li>
        <li>All other boxes don’t contain other boxes</li>
    </ul>
</li>
<li>If the box of type MDAT is found, extract and print the content of that box. It can be assumed
that the content is a UTF8 encoded XML string</li>
</ul>
<br>
Sample output of such an application:<br><br>
Box ID: moof of size 181<br>
&nbsp;&nbsp;&nbsp;&nbsp;Box ID: mfhd of size 16<br>
&nbsp;&nbsp;&nbsp;&nbsp;Box ID: traf of size 157<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Box ID: tfhd of size 24<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Box ID: trun of size 20<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Box ID: uuid of size 44<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Box ID: uuid of size 61<br>
Box ID: mdat of size 17908<br>
Mdat content:<br>
Etc. etc.<br>
<br>
Bonus 1: Which problem can occur if a box has a very large size?<br>
Bonus 2: The MDAT box contains base64 encoded images. Extract those images to files.<br>
</span>
"""
from .app import Parser as Parser
from .box import Box as Box