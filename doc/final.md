# ECE16 Final Report
Prepared by: Mike Liu
Date: 03/19/2020

## Potential Failure Points
### Taps
> Since we have the accelerometer flat on the table we only need to worry about the accelerometer responding to the z dimension. As a result it is unresponsive when the tap is occuring at a different orientation. For example if the accelerometer is held vertically and the tap is going into the accelerometer (like going into the wall) since the direction of acceleration change is going in the y or x direction without a significant change in z. There will be no response from the current algorithm that builds detection off of thresholding on z,x,or y. And each time the orientation of the accelerometer changes, the resting value for each x,y,or z also changes which does not fit the model of thresholding.
>
>![flat_on_table](fig/FINAL_IMAGES/flat_on_table.png)
>
> This is when it is flat on the table. So note the different values for each change in orientation.
>
>![upside_donw](fig/FINAL_IMAGES/upside_down.png)
>
>Upside down
>
>![x_y_front_tilt](fig/FINAL_IMAGES/x_y_front_tilt.png)
>
>I tilted the accelerometer forward and result in a change in overall value of x and y. Note that the same thing happens with side tilts
>
>![x_y_side_tilt](fig/FINAL_IMAGES/x_y_side_tilt.png)
>
>X Y side tilt. So if there are taps the difference in threshold would be different for each value.
>
> If we attempt to detect taps while moving the accelerometer would respond to the x and y axis along with a change in z (just by the nature of walking). When we walk we step out and step back in that results in a change in our z each time taking a step (just watch as a person walks their head will bob slightly) which collects data that is not in spikes of the graph but when x,y,z exceed a "certain" threshold. Let's not account for the swinging motion of the arm if the accelerometer is worn like a watch that results a even more drastic three dimensional movement.

> The threshold algorithm we imposed (without graphical analysis) is extremely prone to see multiple taps, even there was only one, when the change of z lasts for too long. So one tap could become two or three. This was a common error when I was testing the buzzer tap challenge in Lab02. The solution offered at the time was to minimize the detection z threshold. However the method was extremely fickle since people tap at different strenghts and their way of tapping is different each time as well. The model then becomes extremely suited for one person but not applicable for other people.

### Heart Rate Monitor
> A factor that the heart rate monitor does poorly is when it is starting to collect data. That is if the data started recording before a person's hand is on, it will record the extremely large spike and invalidate the data set if we are setting up the machine learning algorithm. It also drags the spike across the recorded heart rate lower if real time analysis is done on counting the BPM.

> Since the heart rate monitor MAX 30105 runs off of a set of IR and RGB LED, it also accepts other wavelengths from the the enviornment. So when it is recording data, a lot of noise is also recorded when it is ran in an enviornment with unstable lighting. In one of my recordings outside, I did it in an area with a lot moving shadows the lighting resulted in some very jumbled data. Below are some examples of me removing a light source (held by my roommate) from my device. Note the deep caves and spikes compared to a normal set of heart beat data

>![Normal_heart_beat](fig/FINAL_IMAGES/Normal_heart_beat.png)
>
>Normal data set
>
>![removing_light_01](fig/FINAL_IMAGES/removing_light_01.png)
>
>Removing Light 01
>
>![removing_light_02](fig/FINAL_IMAGES/removing_light_02.png)
>
>Removing Light 02
>
>![removing_light_03](fig/FINAL_IMAGES/removing_light_03.png)
>
>Removing Light 03

> The heart rate is recorded on a stable platform with an immobile user. When the user starts moving around, ie walking. The collected ehart rate data starts flying all over the place. This is especially prevalent on the action of sitting down and standing up. The current algorithm basically counts the spikes tot he IR change - time graph. Moving around tampers with the consistency of the detected difference. So it results in places with deep caves and high peaks that drown out other signals that can occur at the same period. 

>![Standing_up_and_walking_around](fig/FINAL_IMAGES/Standing_up_and_walking_around.png)
>Standing up and walking around

>![Walking_around](fig/FINAL_IMAGES/Walking_around.png)
>Walking around

## Challenge
### Detect Taps with Different Orientations
The objective is to detect the taps off the accelerometer accurately when it is not just held flat on the table (on wall, upside down, anything really). If this issue is solved then it doesn't matter how the accelerometer is held, it could still detect taps even if it is moved into a different orientation during data collection. This is also a step to improve the algorithm so it can handle movement of when the person wears the accelerometer and taps it.

>So the objective is to combine the directions X, Y, and Z into an algorithm that would handle the situations that when the accelerometer is held stead at any angle and orientation would still find and detect that the taps have happened. However since X,Y,Z are independent variables in a space, resulting in three seperate lines on a graph.
>
>![x_y_z_no_taps](fig/FINAL_IMAGES/x_y_z_no_taps.png)
>
>However trying to define the taps with three seperate lines (three directions) is rather difficult (really it's because I'm lazy) to calculate an accurate occurance of tapping because it tends to look like this
>
>![x_y_z_2_taps](fig/FINAL_IMAGES/x_y_z_2_taps.png)
>
>There were two taps in this situation
>Yes I am aware the original implementation was done entirely on the Arduino IDE. However the graph in Arduino is a bit confusing to read so I am transfering the graphing and implementation to Python instead.
>
>If I tapped the original implementation when I am holding at an angle, in this case how smartphones are normally held, the graph demonstrates changes in X,Y, and Z. 
>
>![angled_orientation_01](fig/FINAL_IMAGES/angled_orientation_01.png)
>
>In the original implementation the taps would be registered around mainly Z and some of the X and Y axis we tap into the accelerometer (like when the chip is a piece of paper and you tap into it). However if the tap occurs while the orientation of the accelerometer is changed then a tap is registered since the original algorithm works off of a baseline + and - threshold which always exceeds it when you move the accelerometer around.
>
>![moving_accelerometer](fig/FINAL_IMAGES/moving_accelerometer.png)
>
>My solution is combining the data sets of all dimensions into one coherent set which requires some elementary algebraic magic. Really I just took the square of each dimension, took the sum of them, and the square root. Which resulted in a graph that looks much nicer and conveys the same information.
>
>![combine_3_taps](fig/FINAL_IMAGES/combine_3_taps.png)
>There were three taps here
>
>![combined_no_taps](fig/FINAL_IMAGES/combined_no_taps.png)
>

>However looking at the ML code we had before. I wondered if I can use machine learning for learning to find the taps but the result was rather diastrous. I collected a bunch of data and ran it through the gauntlet but the problem was that when I used the testing set, it would only find the large taps but could do nothing about smaller taps that were not as obvious. This might be due to the way I detrended the data which favored strong taps strongly (not a pun) and is rather insensitive to smaller taps.
>The next step to my potential solution was using Pxx,Freqs psd from heart beat sensor and now looking back. I don't even know why I attempted that. Tapping is not a regular pace like heart beat. But here is some nonsense graphs I got as output
>
>![Pxx_Freq_no_taps](fig/FINAL_IMAGES/Pxx_Freq_no_taps.png)
>
>no tap
>
>![Pxx_Freq_01](fig/FINAL_IMAGES/Pxx_Freq_01.png)
>
>one tap
>
>![Pxx_Freq_02](fig/FINAL_IMAGES/Pxx_Freq_02.png)
>
>two tap
>

>After those solutions didn't work I took the older route and that started with detrending the data set so the noise and other randomness could be taken out for an analysis.
>
>![process_01](fig/FINAL_IMAGES/process_01.png)
>
>![process_02](fig/FINAL_IMAGES/process_02.png)
>
>![process_03](fig/FINAL_IMAGES/process_03.png)
>
```python
def take_sqrt(s):
    i=0
    while i < np.size(s):
        s[i] = math.sqrt(s[i])
        i+=1
    return s
def take_square(s):
    i=0
    while i<np.size(s):
        s[i] = s[i]*s[i]
        i+=1
    return s

def process(s, n_avg):
    s = HR.signal_diff(s)
    s = HR.normalize_signal(s)
    s = HR.detrend(s, n_avg)
    return s
    
cuml = np.array(data_array[:,1]*data_array[:,1]+data_array[:,2]*data_array[:,2]+data_array[:,3]*data_array[:,3])

square = np.array(HR.take_square(cuml))

pro = HR.process(cuml,5)
```
>At this point I have noticed that the taps no matter if I tap really hard or really lightly. There tends to be a lingering period of taps. That is when we are tapping the data is being taken at 50Hz (I set it) which means there is a data set coming every 0.02 seconds. So no matter how fast I tap the accelerometer there will be an extended period that my finger/hand is on the accelerometer. I'm not Kirby who can dish out punches 8 per second (I counted with approximation since one hit is 1%). 
>
>![heavy_tap_01](fig/FINAL_IMAGES/heavy_tap_01.png)
>![light_tap_01](fig/FINAL_IMAGES/light_tap_01.png)
>

>The solution was to section off the taps into smaller chunks of data sets that I can further analyze. After collecting a large number of samples I discovered the peak periods of single taps (across 3 different people) tend to be around 6 to 7 (*0.02 s). Double taps and triple taps also tend to stay around this number, so the implementation takes advantage of this to split the incoming data streams further into smaller chunks of 20 (*0.02 s). It's not exactly 6 or 7 because the algorithm needs space to react to the changing data sets, if the chunks are too small. The algorithm would not be able to find peaks as accurately (actually it tends to fail). The sampling period is 4 times larger than the actual period so the algorithm can accurately access the number of taps within a localized time period. This allows for some exceptionally large taps but doesn't drown out all of the smaller taps. If it is in the same sampling period it would drown out the smaller taps but not as easily as sampling with the entire data set. 
>The result is a lovely set of graphs like these
>
>![chunk_data_01](fig/FINAL_IMAGES/chunk_data_01.png)
>![chunk_data_02](fig/FINAL_IMAGES/chunk_data_02.png)
>![chunk_data_03](fig/FINAL_IMAGES/chunk_data_03.png)
>
>So really what is left at this time is to make the code right now work when the data is being fed in. The difficulty is knowing when and where to actually start sampling the data so things don't look completely messed up when it is ran through the algorithm. Because right now all the detrending and signal_difference is done after the data collection is done. Analyzing the data while it is coming in is more difficult because there is no longer a large set of data that can approximate the baseline. The possible solution that I implemented is to delay the actual data collection. Meaning the device artifically creates a baseline intially by taking in as much data as possible in the beginning before the user is allowed to start tapping.

>The intended sectioning was implemented and achieved a 80% accuracy when it comes to multidirectional tapping. However doing the movement while still remains as an insurmountable barrier. Below are two graphs of accelerometer data. The first one is when the accelerometer is just moved upwards, the second is when it experiences an actual tap.
>
>![move_02](fig/FINAL_IMAGES/move_02.png)
>
>![tap_01](fig/FINAL_IMAGES/tap_01.png)
>
>The two sets of accelerometer data looks basically identical. If I don't normalize the signal then the the difference between tapping and moving is strongly emphasised, with tapping significantly stronger than moderate movement. However if there is violent movement, the algorithm still registers it as a tap since there is a drastic change in acclereation and the period is similar to a tapping motion.
>![move_03](fig/FINAL_IMAGES/move_03.png)
>















