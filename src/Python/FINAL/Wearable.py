
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
        self.collect_data(200)
        plt.show()
        self.connection.close_connection()
        collected_data = self.connection.data
        fs = int(collected_data.calc_sampling_rate()) #round to nearest int
        np.savetxt("data_file.csv", collected_data.data_array, delimiter=",")
        data_array = np.genfromtxt('data_file.csv', delimiter=',')
        [BPM_Estimate, s_thresh_up] = HR.calc_heart_rate_time(data_array[:,4],fs)
        time = (data_array[:,0] - data_array[0,0])/1e6 #have time start at 0 and in seconds
        #cuml = np.array(data_array[:,1]*data_array[:,1]+data_array[:,2]*data_array[:,1]+data_array[:,3]*data_array[:,1])

        #cuml = np.array(data_array[:,1]*data_array[:,1]+data_array[:,2]*data_array[:,2]+data_array[:,3]*data_array[:,3])
        x_square = np.array(HR.take_square(data_array[:,1]))
        y_square = np.array(HR.take_square(data_array[:,2]))
        z_square = np.array(HR.take_square(data_array[:,3]))
        cuml = np.array(x_square+y_square+z_square)
        sqrt = np.array(HR.take_sqrt(cuml))
        pro = HR.process(sqrt,5)
        #plt.plot(time, cuml)
        
        graph_max = max(pro)
        
        big_peaks, _ = sig.find_peaks(pro, height=0.22*graph_max)
        small_peaks, _ = sig.find_peaks(pro, height = 0)
        results = sig.peak_widths(pro, big_peaks)
        pos_sum = sum(results[0])
        print(big_peaks)
        print(np.size(time))
        plt.clf()
        plt.plot(pro)
        #plt.plot(big_peaks, pro[big_peaks], "o")
        #plt.plot(small_peaks, pro[small_peaks], "x")
        plt.hlines(*results[1:], color="C3")
        
        #pro = -pro
        #graph_min = max(pro)
        
        #peaks, _ = sig.find_peaks(pro, height=0.22*graph_min)
        #results = sig.peak_widths(pro, peaks)
        #neg_sum = sum(results[0])
        #print(peaks)
        #plt.clf()
        #plt.title("Peak length period = " + str(neg_sum+pos_sum))
        #plt.plot(pro)
        #plt.plot(peaks, pro[peaks], "x")
        #plt.hlines(*results[1:], color="C3")
        #plt.show()
        #plt.plot(time, square)
        
        peak_period = 20
        i=0
        temp_pro = np.array([])
        while i < np.size(pro):
            temp_pro = pro[i:i+peak_period]
            some_peaks, _ = sig.find_peaks(temp_pro, height=graph_max*0.22)
            plt.plot(some_peaks+i, pro[some_peaks+i], "x")
            print(some_peaks)
            if np.size(some_peaks) > 0:
                print("tap")
            i+=peak_period
        #x_line = plt.plot(time, data_array[:,1])
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