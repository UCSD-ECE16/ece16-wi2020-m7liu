# ECE16 Lab04 Report
Prepared by Mike Liu
02/10/2020

>Q. Note that you can connect both the heart rate sensor and your OLED at the same time, both of which use the I2C SDA and SCL lines. Why does this work?

>A. If I connect the I2C SDA and SCL lines at the same time because the I2C can allow the communication of multiple devices at the same time through the same line (121) as each device has a different address to communicate through the I2C can save up to 121 of them and talk through at the same time.

>Q. Notice the while(1) statement. What happens if the device is not connected? What happens if the error is printed and then you connect the device? Will the code proceed? Try it and describe the behavior.

>A. When the device is not connected it prints out an error that says device is not connected. Even if the device is connect later on the while(1) leaves the process in an infinite loop that will not break out until the code is roloaded. Instead the Arduino must be recompiled and reloaded for a new set of inputs. 

>Q. what would the settings look like if you were to: set the led brightness to 25mA, use only the Red + IR LED, Sample at 200Hz, and use an ADC range of 8192? 

>A. The settings would look like a red led at 50%, that samples at 200Hz so the plot would look more detailed, with a larger range the input can be read (ADC range)

>Q. What are the units of the pulse width? Would the bigger the pulseWidth result in a more intense or less intense measurement? Why?

>A. According to the data sheet the unit of the pulse width is microseconds. The bigger pulse width results in a more inense measurement because the LED is brighter to it takes in more measurements since the light is on more.

>Q. How many bits are needed for an ADC range of 16384?

>A. 14 bits are needed for an ADC range of 16384.

>Q. What is the peak wavelength of the R, IR, and G LEDs? 

>A. 1.49*10^6 m I guess. I'm just using the frequency = C/lambda.

>Q. If you want to read the Green value, what Mode do you need the setting to be in and what function will you need to use to get the green signal?

>A. To read the Green value I need to the mode to be able to read the light from the Green LED and I would be using getGreen to get theg reen signal

>Q. What was plotted? What does this tell you about how plt.plot interprets the input? 

>A. Four different lines are plotted with the first array as the x and second as a y, then it uses it to plot a slope. That means for plt.plot inteprets the 2D np.array as sets of slopes.

>Q. Try different n_avg and document, with plots, the result for a few different n_avg and describe which n_avg worked well in emphasizing the taps? 

>A. The result from 10, 100, 1000, and 10000 the n_avg that worked well emphasizing the taps is when the moving average is large but not extremely large. (guess)


