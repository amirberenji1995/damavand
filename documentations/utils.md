# Damavand Documention - Utilities Module API Reference
We prefer to include entities that are used in different modules in the utilities (utils for short) module.

## ```splitter(array, win_len, hop_len, return_df = True)```

### Splitting raw data signals into series of segmented signals
  
- #### Arguments:
  - **array** is the original signal, in the form of a column vector ```np.array``` (the array should be one-dimensional).
  - **win_len** is the desired length of the segmented signals.
  - **hop_len** is the forward move of the window.
  - **return_df** determines the output type; the default value is ```True```, meaning that returned type is a ```pandas.DataFrame```. If set to ```False```, the function returns a ```np.array```.
  
- #### Return Value:
  - A ```pandas.DataFrame``` including segmented signals, extracted from the original raw signal.

- #### Descriptions:
  This function helps one to transform the raw signals into a series of segmented signals.

- #### Usage example:

```Python
# Importings
import numpy as np
from damavand.damavand.utils import splitter

# Creating a dummy np.array with the size of (10000)
array = np.random.rand(10000)

# Declaring win_len and hop_len
win_len, hop_len = 1000, 250

# Splitting the original array and returning a Pandas.DataFrame
df = splitter(array, win_len, hop_len)

# Splitting the original array and returning a numpy.array
segmented_array = splitter(array, win_len, hop_len, return_df = False)
```

## ```fft_freq_axis(time_len, sampling_freq)```

### Generating a frequency axis to be used with a frequncy spectrum extracted by signal_processing.transformations.fft

- #### Arguments:
  - **time_len** is the length of time-domain signals, FFT is applied on.
  - **sampling_freq** is the sampling frequency.
  
- #### Return Value:
  - A ```numpy.array``` that includes the frequency bins.

- #### Descriptions:
  This function enables one to generate a frequency axis, corresponding to a Discrete Fourier Transform frequency spectrum.

- #### Usage example:

```Python
# Importing
from damavand.damavand.utils import fft_freq_axis

# Generating a frequency axis for frequency spectrum, extracted from time-series with the length of 10000 and sampling frequency of 5000
freq_axis = fft_freq_axis(10000, 5000)
```

## ```zoomed_fft_freq_axis(f_min, f_max, desired_len)```

### Generating a frequency axis to be used with a frequncy spectrum extracted by signal_processing.transformations.zoomed_fft

- #### Arguments:
  - **f_min** is the minumum frequency covered in the spectrum.
  - **f_max** is the maximum frequency covered in the spectrum.
  - **desired_len** is the length of frequency spectrum, extracted by ```zoomed_fft_freq_axis```.
  
- #### Return Value:
  - A ```numpy.array``` that includes the frequency bins.

- #### Descriptions:
  This function enables one to generate a frequency axis, corresponding to a ZoomedFFT frequency spectrum.

- #### Usage example:

```Python
# Importing
from damavand.damavand.utils import zoomed_fft_freq_axis

# Generating a frequency axis for zoomed frequency spectrum, covering from 0 Hz to 2500 Hz using 2500 points
zoomed_freq_axis = zoomed_fft_freq_axis(0, 2500, 2500)
```