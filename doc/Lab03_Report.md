# ECE16 Lab03 Report
Prepared by Mike Liu
02/11/2020

>Q. Show the code - Starting with a = “Hello World!!!”, come up with a code that will give us b = “Hello” and c = “World” and d = “!!!” . Also, in code, check if “ello” is in a. 

>A. 
```python
    a='Hello World!!!'
    print(a)

    b = ""
    for x in range(0, 5):
        b=b+a[x]
        
    print(b)

    c = ""
    for x in range(6, 11):
        c+=a[x]
        
    print(c)

    d = ""
    for x in range(11, 14):
        d+=a[x]

    print(d)
```
>Q. In the following code, what is the output of the print statement? Why doesn’t original_list = ['hi','how','are','you']?

>A. The output of the print statement is not original_list = ['hi', 'how', 'are', 'you'] is because the print statement prints the original statement that is unchanged while newer_list is the one updated

>Q. Try sending without the .encode. What happens? 

>A. If it is sent without .encode then the Python code will not run. It throws an error since there is not an implicit converter from string to bytes which .write(byte) accepts.

>Q. Identify in the above code, (1) which python command prints to the python’s own console, and (2) which python command prints to the serial port to the MCU?

>A.
(1) There is not code that prints to the python's console. The command that prints to python's console is print() which is not present in the given code.
(2) ser.write(S.encode('utf-8') is the python command that prints to the serial port to the MCU.

>Q. What happens if you take out the \n in the string? Why?

>A. If I take out the \n in the string the OLED does not update from the Serial port because the Serial port is waiting for a newline character (/n) which it does not receive. So the "Hello World" displayed on the OLED is the first "Hello World" even if I continuously update the python file.

>Q. Describe the output you observe on the Python side? 

>A. The output on the Python's side is a part of the of the printed timer statement that the Arduino sends to the serial port. It doesn't hold the whole thing, it prints out exactly 30 characters including \r and \n

>Q. Change the code to read 10 bytes instead of 30. Now what do you get? What are the 10 bytes you received? Remove decode might help you understand

>A. Whe the code is changed to 10 bytes it prints out 10 characters including \r and \n of the timer that the serial is suppose to output from the Arduino. 
Output without decode: b'TIMER:\r\n1\r'
Output with decode: TIMER:
                                    1

>Q. Describe the output you observe on the Python side? Is it the same as before? What does this tell you about the print() function of python? 

>A. The output on the Python side for readSerial2(ser) prints out one character and a newline at a time so all the bytes are shown vertically while readSerial3(ser) outputs everysingle character as an entire array that was appended during execution. The print() function of Python has an automatic conversion to output any string or array, etc based on the type of variable with distinct format. In short it is very flexible in printing to console. 

>Q. We purposely made a few errors above. What were they? 

>A. Try: is suppose to be try: ; s = ser.read(1) is suppose to be s = ser.read(1).decode('utf-8')

>Q. Show the code - Make an Numpy Array called test_array  from a list = [0,10,4,12]. Subtract 20 from the test_array, what do you get? What is the shape of the test_array

>A. If I subtract 20 from the array I get [-20 -10 -16  -8], and the shape of the array is (4,) or 4 columns

>Q. Show the code - Make a 2D array of test_2D_array from [0,10,4,12],[1,20,3,41]

>A.
```python
    test_2D_array = np.array([(0,10,4,12),(1,20,3,41)])
    print(test_2D_array)
```
>Q. Make a 2D array of zeros with shape of 10x20 and then print it out

>A. 
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]

>Q. Show the code - Out of the test_array, create the following using hstack and vstack. 

>A.
```python
    test_hstack_array = np.hstack((test_array, test_array))
    test_vstack_array = np.vstack((test_hstack_array,test_hstack_array,test_hstack_array,test_hstack_array))
    print(test_vstack_array)
```

