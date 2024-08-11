import numpy as np
import pandas as pd
import scipy

def splitter(array, win_len, hop_len, return_df = True):
   N = array.shape[0]
   m = 0
   ids = []
   while m + win_len < N:
      ids.append([m, m + win_len])
      m = m + hop_len
      
   if return_df:
      return pd.DataFrame([array[i[0]: i[1]] for i in ids])
   else:
      return np.array([array[i[0]: i[1]] for i in ids])
    
def fft_freq_axis(time_len, sampling_freq):
   return scipy.fft.fftfreq(time_len, 1/float(sampling_freq))[0 : time_len // 2]

def zoomed_fft_freq_axis(f_min, f_max, desired_len):
   return np.linspace(f_min, f_max, desired_len)

def rms(arr):
  return np.sqrt(np.mean(np.square(arr)))