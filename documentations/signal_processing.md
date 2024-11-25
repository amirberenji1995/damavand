# Damavand Documention - Signal Processing Module API Reference

## Transformations Submodule

### ```env(signals)```


#### Extracting the envelope of a set of signals
  
  ##### Arguments:
  - **signals**: A ```pandas.DataFrame``` incuding signals in its rows.
  
  ##### Return Value:
  - A ```pandas.DataFrame``` whose rows are the envelopes of the signals stored in the inputted DataFrame.

  ##### Descriptions:
  This function extracts the envelope of signals, stored in a ```pandas.DataFrame``` object. This is done through the application of Hilbert transform
  ([```scipy.signal.hilbert```](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.hilbert.html)); also ```numpy.abs``` is used
  to calculate the absolute magnitude, from both the imaginery and real parts.


### ```fft(signals, freq_filter = None, window = None)```

#### Applying the Fast-Fourier Transform algorithim to derive frequency domain representation of a set of signals
  
  ##### Arguemnts:
  - **signals**: A ```pandas.DataFrame()``` incuding signals in its rows.
  - **freq_filter**:  A frequency filter object from ```scipy.signal``` module (e.g. [```scipy.signal.butter```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.signal.butter.html#scipy.signal.butter)) to avoid aliasing.
  - **window**: A window object from ```scipy.signal.windows``` module (e.g. [```scipy.signal.windows.hann```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.signal.windows.hann.html#scipy.signal.windows.hann)) to encounter the leakage error.
  
  ##### Return Value:
  A ```pandas.DataFrame``` whose rows are the frequency representations of the inputted DataFrame. As only the real frequency axis is of importance, the lenght of the frequency domain signals is half of the original time domain signal.

  ##### Descriptions:
  This function computes the Discrete Fourier Transform (DFT) of a set of signals, through the application of Fast-Fourier Transform ([```scipy.fft.fft```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.fft.fft.html#scipy.fft.fft)) algorithm. As it returns only the coeeficients correpsonding to real frequency components (not the imaginery ones), lenght of the returned ```pandas.DataFrame``` is half of the inputted ```pandas.DataFrame```. ```freq_filter``` and ```window``` are not mandatory arguments and a function call without them is valid, however, we recommend using them to avoid aliasing (and of course near-zero/DC filtering through band-pass filters) and leakage error. We encourage you to use frequency axis for the sake of visualization; this can be done using either of the followings: [```scipy.fft.fftfreq```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.fft.fftfreq.html#scipy.fft.fftfreq), [```numpy.linspace```](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) and **damavand.utils.fft_freq_axis**.


  ### ```zoomed_fft(signals, f_min, f_max, desired_len, sampling_freq, freq_filter = None, window = None)```

  #### Applying the ZoomFFT algorithm to derive a fine-grained frequency representation in a desired frequency range

  ##### Arguments:
  - **signals**: A ```pandas.DataFrame``` incuding signals in its rows.
  - **f_min**: Minum of the desired frequency range.
  - **f_max**: Maximum of the desired frequency range.
  - **desired_len**: The desired length of the frequency domain representation.
  - **sampling_freq**: The sampling frequency of the signals included in **signals**.
  - **freq_filter**:  A frequency filter object from ```scipy.signal``` module (e.g. [```scipy.signal.butter```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.signal.butter.html#scipy.signal.butter)) to avoid aliasing.
  - **window**: A window object from ```scipy.signal.windows``` module (e.g. [```scipy.signal.windows.hann```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.signal.windows.hann.html#scipy.signal.windows.hann)) to encounter the leakage error.

  ##### Return Value:
  A ```pandas.DataFrame``` whose rows are the frequency representations of the inputted DataFrame, in the desired frequency range and with the chosen lenght.

  ##### Descriptions:
  This function enables one to derive a frequency represenationin a desired frequency range and with the desired length, through the application of [```sicpy.signal.ZoomFFT```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.signal.ZoomFFT.html#scipy.signal.ZoomFFT). ```freq_filter``` and ```window``` are not mandatory arguments and a function call without them is valid, however, we recommend using them to avoid aliasing (and of course near-zero/DC filtering through band-pass filters) and leakage error. We encourage you to use frequency axis for the sake of visualization; this can be done using either of the followings: [```numpy.linspace```](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) or ```damavand.utils.zoomed_fft_freq_axis```.


  ### ```stft(signals, window_len, hop_len, freq_filter = None, window = None)```

  #### Application of Short-Time Fourier Transform to derive Time-Frequency representation of the inputted signals

  ##### Arguemnts:
  - **signals**: A ```pandas.DataFrame``` incuding signals in its rows.
  - **window_len**: Lenght of the desired time segments.
  - **hop_len**: Length of the feed, used to get forward during the segmentation process.
  - **freq_filter**:  A frequency filter object from ```scipy.signal``` module (e.g. [```scipy.signal.butter```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.signal.butter.html#scipy.signal.butter)) to avoid aliasing.
  - **window**: A window object from ```scipy.signal.windows``` module (e.g. [```scipy.signal.windows.hann```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.signal.windows.hann.html#scipy.signal.windows.hann)) to encounter the leakage error.

  ##### Return Value:
  A ```numpy.array```, whose first dimension equals the number of rows included in the input ```pandas.DataFrame```; it includes derived Time-Frequency representations of the inputted signals. ```freq_filter``` and ```window``` are not mandatory arguments and a function call without them is valid, however, we recommend using them to avoid aliasing (and of course near-zero/DC filtering through band-pass filters) and leakage error. Pay attention that unlike the case of ```damavand.signal_processing.FFT``` or ```damavand.signal_processing.ZoomedFFT```, for this function you have to define freq_filter and window objects with a lenght that suits the segmented signals (equal to the ```window_len``` argument), instead of the original signals, presented in the inputted ```pandas.DataFrame```.

  ##### Descriptions:
  By the application of this function, one is able to derive Time-Frequency representation; this is done by first segmenting the original signals to a series of shorter signals and consecutively [**FFT**](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.fft.fft.html#scipy.fft.fft) is applied on each
  segmented signal to derive the corresponding frequency representation. Results are usually visualized as heatmaps.

## Feature Extraction Submodule

### ```feature_extractor(signals, features)```

#### Extracting a number of features from the inpuuted signals

##### Arguments:
- **signals**: A ```pandas.DataFrame``` incuding signals in its rows.
- **features**: A python ```dict``` where:
  - keys are feature names
  - values are tuples of (function, args, kwargs) where:
    * function: the feature extraction function
    * args: tuple of positional arguments (optional)
    * kwargs: dict of keyword arguments (optional)

##### Return Value:
A ```pandas.DataFrame```, including the feature values for the signals in the inputted ```pandas.DataFrame```.

##### Description:
To extract a set of features from the signals presented in a ```pandas.DataFrame```, one can use this function. Features of interest are supposed to be passed as a python ```dict``` where:
  - keys are feature names
  - values are tuples of (function, args, kwargs) where:

    - function: the feature extraction function
    - args: tuple of positional arguments (optional)
    - kwargs: dict of keyword arguments (optional)


### Features to extract

[This study](https://www.sciencedirect.com/science/article/abs/pii/S0888327006002512) introduces 11 time-domain and 13 frequency-domain (24 in total) features for rotating machinery fault diagnosis. Detailed list of them alongside tips on how to extract them using ```feature_extractor(signals, features)``` is included in the table below. It is worth mentioning that $x(n)$, $s(k)$ and $f_k$ correspond to time-domain signal, frequency spectrum and corresponding frequency axis; moreover, TS and FS in the **Description** column stand for time-series and frequency spectra.

| **Number** |                                               **Formula**                                              |                **Description**               |                               **Implementation**                              |
|:----------:|:------------------------------------------------------------------------------------------------------:|:--------------------------------------------:|:-----------------------------------------------------------------------------:|
|     P1     |                                  $P_1 = \frac{\sum_{n=1}^{N} x(n)}{N}$                                 |                    TS Mean                   |                                 ```np.mean```                                 |
|     P2     |                         $P_2 = \sqrt{\frac{\sum_{n=1}^{N} (x(n)-P_1)^2}{N-1}}$                         |             TS Standard Deviation            |                                  ```np.std```                                 |
|     P3     |                    $P_3 = \left(\frac{\sum_{n=1}^{N} \sqrt{\|x(n)\|}}{N}\right)^{2}$                   | TS Squared Mean of Square Roots of Absolutes |       ```damavand.damavand.signal_processing.feature_extraction.smsa```       |
|     P4     |                            $P_4 = \sqrt{\frac{\sum_{n=1}^{N} (x(n))^2}{N}}$                            |              TS Root Mean Square             |        ```damavand.damavand.signal_processing.feature_extraction.rms```       |
|     P5     |                                          $P_5 = \max \|x(n)\|$                                         |                    TS Peak                   |       ```damavand.damavand.signal_processing.feature_extraction.peak```       |
|     P6     |                         $P_6 = \frac{\sum_{n=1}^{N} (x(n)-P_1)^3}{(N-1)P_1^3}$                         |                  TS Skewness                 |                             ```scipy.stats.skew```                            |
|     P7     |                      $P_7 = \sqrt{\frac{\sum_{n=1}^{N} (x(n)-P_1)^4}{(N-1)P_1^4}}$                     |                  TS Kurtosis                 |                           ```scipy.stats.kurtosis```                          |
|     P8     |                                         $P_8 = \frac{p_5}{p_4}$                                        |                TS Crest Factor               |   ```damavand.damavand.signal_processing.feature_extraction.crest_factor```   |
|     P9     |                                         $P_9 = \frac{p_5}{p_3}$                                        |              TS Clearance Factor             | ```damavand.damavand.signal_processing.feature_extraction.clearance_factor``` |
|     P10    |                        $P_{10} = \frac{P_4}{\frac{1}{N}\sum_{n=1}^{N}\|x(n)\|}$                        |                TS Shape Factor               |   ```damavand.damavand.signal_processing.feature_extraction.shape_factor```   |
|     P11    |                        $P_{11} = \frac{P_5}{\frac{1}{N}\sum_{n=1}^{N}\|x(n)\|}$                        |               TS Impulse Factor              |  ```damavand.damavand.signal_processing.feature_extraction.impulse_factor```  |
|     P12    |                                $P_{12} = \frac{\sum_{k=1}^{K} s(k)}{K}$                                |                    FS Mean                   |                                 ```np.mean```                                 |
|     P13    |                      $P_{13} = \sqrt{\frac{\sum_{k=1}^{K} (s(k)-P_{12})^2}{K-1}}$                      |                  FS Variance                 |                                  ```np.var```                                 |
|     P14    |                  $P_{14} = \frac{\sum_{k=1}^{K} (s(k)-P_{12})^3}{K(\sqrt{P_{12}})^3}$                  |                  FS Skewness                 |                             ```scipy.stats.skew```                            |
|     P15    |                       $P_{15} = \frac{\sum_{k=1}^{K} (s(k)-P_{12})^4}{KP_{13}^2}$                      |                  FS Kurtosis                 |                           ```scipy.stats.kurtosis```                          |
|     P16    |                  $P_{16} = \frac{\sum_{k=1}^{K} f_k \cdot s(k)}{\sum_{k=1}^{K} s(k)}$                  |             FS Spectral Centroid             |        ```damavand.damavand.signal_processing.feature_extraction.spectral_centroid```       |
|     P17    |                 $P_{17} = \sqrt{\frac{\sum_{k=1}^{K} (f_k - P_{16})^2 \cdot s(k)}{K}}$                 |                                              |        ```damavand.damavand.signal_processing.feature_extraction.P17```       |
|     P18    |              $P_{18} = \sqrt{\frac{\sum_{k=1}^{K} f_k^2 \cdot s(k)}{\sum_{k=1}^{K} s(k)}}$             |                                              |        ```damavand.damavand.signal_processing.feature_extraction.P18```       |
|     P19    |        $P_{19} = \sqrt{\frac{\sum_{k=1}^{K} f_k^4 \cdot s(k)}{\sum_{k=1}^{K} f_k^2 \cdot s(k)}}$       |                                              |        ```damavand.damavand.signal_processing.feature_extraction.P19```       |
|     P20    | $P_{20} = \frac{\sum_{k=1}^{K} f_k^2 \cdot s(k)}{\sum_{k=1}^{K} s(k) \sum_{k=1}^{K} f_k^4 \cdot s(k)}$ |                                              |        ```damavand.damavand.signal_processing.feature_extraction.P20```       |
|     P21    |                                    $P_{21} = \frac{P_{17}}{P_{16}}$                                    |                                              |        ```damavand.damavand.signal_processing.feature_extraction.P21```       |
|     P22    |                  $P_{22} = \frac{\sum_{k=1}^{K} (f_k-P_{16})^3 \cdot s(k)}{KP_{17}^3}$                 |                                              |        ```damavand.damavand.signal_processing.feature_extraction.P22```       |
|     P23    |                  $P_{23} = \frac{\sum_{k=1}^{K} (f_k-P_{16})^4 \cdot s(k)}{KP_{17}^4}$                 |                                              |        ```damavand.damavand.signal_processing.feature_extraction.P23```       |
|     P24    |             $P_{24} = \frac{\sum_{k=1}^{K} (f_k-P_{16})^{1/2} \cdot s(k)}{K\sqrt{P_{17}}}$             |                                              |        ```damavand.damavand.signal_processing.feature_extraction.P24```       |

```Python
from damavand.damavand.datasets.downloaders import read_addresses, ZipDatasetDownloader
from damavand.damavand.datasets.digestors import KAIST
from damavand.damavand.signal_processing.feature_extraction import *
from damavand.damavand.signal_processing.transformations import fft
from damavand.damavand.utils import *
from zipfile import ZipFile
import os
import pandas as pd
import numpy as np
import scipy

addresses = read_addresses()
downloader = ZipDatasetDownloader(addresses['KAIST'])
downloader.download_extract('KAIST.zip', 'KAIST/')

# using only two channels out of four available ones to avoid RAM oveflow
kaist = KAIST('KAIST/', os.listdir('KAIST/'), list(range(2)))
mining_params = {
    'win_len': 20000,
    'hop_len': 20000,
}
kaist.mine(mining_params)

df = pd.concat(kaist.data[0]).reset_index(drop = True)
signals, metadata = df.iloc[:, : - 3], df.iloc[:, - 3 :]

time_features = {
  'mean': (np.mean, (), {}),
  'std': (np.std, (), {}),
  'smsa': (smsa, (), {}),
  'rms': (rms, (), {}),
  'peak': (peak, (), {}),
  'skew': (scipy.stats.skew, (), {}),
  'kurtosis': (scipy.stats.kurtosis, (), {}),
  'crest_factor': (crest_factor, (), {}),
  'clearance_factor': (clearance_factor, (), {}),
  'shape_factor': (shape_factor, (), {}),
  'impulse_factor': (impulse_factor, (), {}),
}
time_features_df = feature_extractor(signals, features)

window = scipy.signal.windows.hann(signals_env.shape[1])
freq_filter = scipy.signal.butter(25, [5, 12500], 'bandpass', fs = 25600, output='sos')
signals_fft = fft(signals, freq_filter = freq_filter, window = window)
freq_axis = fft_freq_axis(20000, 25600)

freq_features = {
  'mean': (np.mean, (), {}),
  'var': (np.var, (), {}),
  'skew': (scipy.stats.skew, (), {}),
  'kurtosis': (scipy.stats.kurtosis, (), {}),
  'spectral_centroid': (spectral_centroid, (freq_axis,), {}),
  'P17': (P17, (freq_axis,), {}),
  'P18': (P18, (freq_axis,), {}),
  'P19': (P19, (freq_axis,), {}),
  'P20': (P20, (freq_axis,), {}),
  'P21': (P21, (freq_axis,), {}),
  'P22': (P22, (freq_axis,), {}),
  'P23': (P23, (freq_axis,), {}),
  'P24': (P24, (freq_axis,), {}),
}
freq_features_df = feature_extractor(signals, features)

```