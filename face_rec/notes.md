## 1
Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)

Parameters:
image: It is the image on which rectangle is to be drawn.
start_point: It is the starting coordinates of rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
end_point: It is the ending coordinates of rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
color: It is the color of border line of rectangle to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
thickness: It is the thickness of the rectangle border line in px. Thickness of -1 px will fill the rectangle shape by the specified color.

Return Value: It returns an image.
## 2
The waitKey(0) function returns -1 when no input is made whatsoever. As soon the event occurs i.e. a Button is pressed it returns a 32-bit integer.

The 0xFF in this scenario is representing binary 11111111 a 8 bit binary, since we only require 8 bits to represent a character we AND waitKey(0) to 0xFF. As a result, an integer is obtained below 255.

ord(char) returns the ASCII value of the character which would be again maximum 255.

Hence by comparing the integer to the ord(char) value, we can check for a key pressed event and break the loop.