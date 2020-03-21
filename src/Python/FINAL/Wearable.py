
from Libraries.Connection import Connection
from Libraries.Visualize import Visualize
from Libraries.HR import HR
from scipy import signal
from scipy import signal as sig
import matplotlib.pyplot as plt
import numpy as np
import math


class Wearable:

    def __init__(self, serial_name, baud_rate):
        self.connection = Connection(serial_name, baud_rate)
    
    def collect_data(self, num_samples):
        self.connection.end_streaming()
        self.connection.start_streaming()
        while self.connection.data.get_num_samples() < num_samples:
            
            try:
                self.connection.receive_data()
            except(KeyboardInterrupt):
                self.connection.end_streaming()
                self.connection.close_connection()
                print("Exiting program due to KeyboardInterrupt")
                break
        self.connection.end_streaming()
    
    def main(self):
        self.collect_data(10)
        plt.show()
        self.connection.close_connection()
        collected_data = self.connection.data
        fs = int(collected_data.calc_sampling_rate()) #round to nearest int
        np.savetxt("data_file.csv", collected_data.data_array, delimiter=",")
        data_array = np.genfromtxt('data_file.csv', delimiter=',')
        [BPM_Estimate, s_thresh_up] = HR.calc_heart_rate_time(data_array[:,4],fs)
        time = (data_array[:,0] - data_array[0,0])/1e6 #have time start at 0 and in seconds
        #cuml = np.array(data_array[:,1]*data_array[:,1]+data_array[:,2]*data_array[:,1]+data_array[:,3]*data_array[:,1])

        cuml = np.array(data_array[:,1]*data_array[:,1]+data_array[:,2]*data_array[:,2]+data_array[:,3]*data_array[:,3])
        square = np.array(HR.take_square(cuml))
        pro = HR.process(square,5)
        #plt.plot(time, cuml)
        plt.show()
        pro = -pro
        peaks, _ = sig.find_peaks(pro, height=0.15)
        print(np.size(peaks))
        print(np.size(time))
        cuml = HR.take_sqrt(cuml)
        plt.clf()
        #plt.plot(pro)
       # plt.plot(peaks, pro[peaks], "x")
        plt.show()
        #plt.plot(time, square)
        plt.show()
        
        
       # x_line = plt.plot(time, data_array[:,1])
        #y_line = plt.plot(time, data_array[:,2])
        #z_line = plt.plot(time, data_array[:,3])
        #plt.legend(('X','Y','Z'))
        #plt.plot(time, HR.normalize_signal(HR.detrend(-data_array[:,4],fs)))
        #plt.plot(time, s_thresh_up)
        plt.show()
        print("BPM = "+ str(BPM_Estimate))       

def main():
    wearable = Wearable('/dev/cu.usbserial-14310',115200)
    wearable.main()


if __name__== "__main__":
    main()