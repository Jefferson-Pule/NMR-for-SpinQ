import numpy as np
import matplotlib.pyplot as plt
import os

def format_data(path_to_data,dir_to_save):
    dirname, basename = os.path.split(path_to_data)
    with open(dir_to_save+"new"+basename, 'w') as newdata:
        with open(path_to_data, 'r') as oldfile:
            data=oldfile.read()
            k=0
            line=0
            limits=[]
            for i in data:
                if i=="(":
                    m=k+1
                    while data[m]!=",":
                        newdata.write(data[m])
                        m+=1
                    m+=1
                    newdata.write(" ")
                    while data[m]!=")":
                        newdata.write(data[m])
                        m+=1
                    newdata.write("\n")
                    k+=1
                    line+=1
                elif i=="F":
                    limits.append(line)
                    k+=1
                else:
                    k+=1
            limits=np.unique(np.array(limits))
    return limits 

def divide_data(path_to_data,dir_to_save):
    
    dirname, basename = os.path.split(path_to_data)
    limits=format_data(path_to_data,dir_to_save)
    data=np.loadtxt(dir_to_save+"new"+basename)
    
    FID_RE=data[limits[0]:limits[1],:]
    FID_IM_1=data[limits[1]:limits[2],:]
    FID_IM_2=data[limits[2]:limits[3],:]
    FFT_RE=data[limits[3]:limits[4],:]
    FFT_IM=data[limits[4]:limits[5],:]
    FFT_MOD=data[limits[5]:limits[6],:]
    FFT_FIT=data[limits[6]:,:]
    
    return FID_RE, FID_IM_1, FID_IM_2, FFT_RE, FFT_IM, FFT_MOD, FFT_FIT

def give_plot(name_of_plot):
    x,y=name_of_plot.T
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    FID_RE, FID_IM_1, FID_IM_2, FFT_RE, FFT_IM, FFT_MOD, FFT_FIT=divide_data("C:/Users/japul/source/repos/NMRI/NMRI/data/T2/P/24000.txt","C:/Users/japul/Downloads/")
    give_plot(FFT_RE)
    FID_RE, FID_IM_1, FID_IM_2, FFT_RE, FFT_IM, FFT_MOD, FFT_FIT=divide_data("C:/Users/japul/source/repos/NMRI/NMRI/data/T2/P/432000.txt","C:/Users/japul/Downloads/")
    give_plot(FFT_RE)