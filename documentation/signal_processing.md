# Damavand Documention - Signal Processing Module API Reference

## ```env(signals)```


### Extracting the envelope of a set of signals
  
  #### Arguments:
  - **signals**: A ```pandas.DataFrame``` incuding signals in its rows.
  
  #### Return Value:
  - A ```pandas.DataFrame``` whose rows are the envelopes of the signals stored in the inputted DataFrame.

  #### Descriptions:
  This function extracts the envelope of signals, stored in a ```pandas.DataFrame``` object. This is done through the application of Hilbert transform
  ([```scipy.signal.hilbert```](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.hilbert.html)); also ```numpy.abs``` is used
  to calculate the absolute magnitude, from both the imaginery and real parts.


## ```fft(signals, freq_filter = None, window = None)```

### Applying the Fast-Fourier Transform algorithim to derive frequency domain representation of a set of signals
  
  #### Arguemnts:
  - **signals**: A ```pandas.DataFrame()``` incuding signals in its rows.
  - **freq_filter**:  A frequency filter object from ```scipy.signal``` module (e.g. [```scipy.signal.butter```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.signal.butter.html#scipy.signal.butter)) to avoid aliasing.
  - **window**: A window object from ```scipy.signal.windows``` module (e.g. [```scipy.signal.windows.hann```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.signal.windows.hann.html#scipy.signal.windows.hann)) to encounter the leakage error.
  
  #### Return Value:
  A ```pandas.DataFrame``` whose rows are the frequency representations of the inputted DataFrame. As only the real frequency axis is of importance, the lenght of the frequency domain signals is half of the original time domain signal.

  #### Descriptions:
  This function computes the Discrete Fourier Transform (DFT) of a set of signals, through the application of Fast-Fourier Transform ([```scipy.fft.fft```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.fft.fft.html#scipy.fft.fft)) algorithm. As it returns only the coeeficients correpsonding to real frequency components (not the imaginery ones), lenght of the returned ```pandas.DataFrame``` is half of the inputted ```pandas.DataFrame```. ```freq_filter``` and ```window``` are not mandatory arguments and a function call without them is valid, however, we recommend using them to avoid aliasing (and of course near-zero/DC filtering through band-pass filters) and leakage error. We encourage you to use frequency axis for the sake of visualization; this can be done using either of the followings: [```scipy.fft.fftfreq```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.fft.fftfreq.html#scipy.fft.fftfreq), [```numpy.linspace```](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) and **damavand.utils.fft_freq_axis**.


  ## ```zoomed_fft(signals, f_min, f_max, desired_len, sampling_freq, freq_filter = None, window = None)```

  ### Applying the ZoomFFT algorithm to derive a fine-grained frequency representation in a desired frequency range

  #### Arguments:
  - **signals**: A ```pandas.DataFrame``` incuding signals in its rows.
  - **f_min**: Minum of the desired frequency range.
  - **f_max**: Maximum of the desired frequency range.
  - **desired_len**: The desired length of the frequency domain representation.
  - **sampling_freq**: The sampling frequency of the signals included in **signals**.
  - **freq_filter**:  A frequency filter object from ```scipy.signal``` module (e.g. [```scipy.signal.butter```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.signal.butter.html#scipy.signal.butter)) to avoid aliasing.
  - **window**: A window object from ```scipy.signal.windows``` module (e.g. [```scipy.signal.windows.hann```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.signal.windows.hann.html#scipy.signal.windows.hann)) to encounter the leakage error.

  #### Return Value:
  A ```pandas.DataFrame``` whose rows are the frequency representations of the inputted DataFrame, in the desired frequency range and with the chosen lenght.

  #### Descriptions:
  This function enables one to derive a frequency represenationin a desired frequency range and with the desired length, through the application of [```sicpy.signal.ZoomFFT```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.signal.ZoomFFT.html#scipy.signal.ZoomFFT). ```freq_filter``` and ```window``` are not mandatory arguments and a function call without them is valid, however, we recommend using them to avoid aliasing (and of course near-zero/DC filtering through band-pass filters) and leakage error. We encourage you to use frequency axis for the sake of visualization; this can be done using either of the followings: [```numpy.linspace```](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) or ```damavand.utils.zoomed_fft_freq_axis```.


  ## ```stft(signals, window_len, hop_len, freq_filter = None, window = None)```

  ### Application of Short-Time Fourier Transform to derive Time-Frequency representation of the inputted signals

  #### Arguemnts:
  - **signals**: A ```pandas.DataFrame``` incuding signals in its rows.
  - **window_len**: Lenght of the desired time segments.
  - **hop_len**: Length of the feed, used to get forward during the segmentation process.
  - **freq_filter**:  A frequency filter object from ```scipy.signal``` module (e.g. [```scipy.signal.butter```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.signal.butter.html#scipy.signal.butter)) to avoid aliasing.
  - **window**: A window object from ```scipy.signal.windows``` module (e.g. [```scipy.signal.windows.hann```](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.signal.windows.hann.html#scipy.signal.windows.hann)) to encounter the leakage error.

  #### Return Value:
  A ```numpy.array```, whose first dimension equals the number of rows included in the input ```pandas.DataFrame```; it includes derived Time-Frequency representations of the inputted signals. ```freq_filter``` and ```window``` are not mandatory arguments and a function call without them is valid, however, we recommend using them to avoid aliasing (and of course near-zero/DC filtering through band-pass filters) and leakage error. Pay attention that unlike the case of ```damavand.signal_processing.FFT``` or ```damavand.signal_processing.ZoomedFFT```, for this function you have to define freq_filter and window objects with a lenght that suits the segmented signals (equal to the ```window_len``` argument), instead of the original signals, presented in the inputted ```pandas.DataFrame```.

  #### Descriptions:
  By the application of this function, one is able to derive Time-Frequency representation; this is done by first segmenting the original signals to a series of shorter signals and consecutively [**FFT**](https://docs.scipy.org/doc/scipy-1.11.0/reference/generated/scipy.fft.fft.html#scipy.fft.fft) is applied on each
  segmented signal to derive the corresponding frequency representation. Results are usually visualized as heatmaps.

## ```feature(signals, features)```

### Extracting a number of features from the inpuuted signals

#### Arguments:
- **signals**: A ```pandas.DataFrame``` incuding signals in its rows.
- **features**: A python ```dict``` including the features of interest and corresponding column labels of them.

#### Return Value:
A ```pandas.DataFrame```, including the feature values for the signals in the inputted ```pandas.DataFrame```.

#### Description:
To extract a set of features from the signals presented in a ```pandas.DataFrame```, one can use this function. Features of interest are supposed to be passed as a python ```dict``` whose keys and values are desired label and corresponding python ```functions```. 