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

