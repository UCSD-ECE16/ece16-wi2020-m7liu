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
