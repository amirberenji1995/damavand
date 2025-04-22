# Damavand Documention - Augmentations Module API Reference

## ```gaussian_noise(signals, SNR_level, return_noise = False)```


### Augmenting signals with a Signal-to-Noise Ratio level, through adding Gaussian noise
  
#### Arguments:
- **signals** is the Original signals, in the form of a ```pd.DataFrame```.
- **SNR_level** is the desired SNR level (in dB) of the augmented signals.
- **return_noise** is a flag to also return the pure noises; default is ```False``` and you need to set it ```True``` to also return the noises.

#### Return Values:
- A ```pandas.DataFrame``` including noise contaminated signals.
- A ```pandas.DataFrame``` including the pure noises (only returned when ```return_noise``` is set to ```True```).

#### Descriptions:
Using this function, one is able to contaminate the original signals with zero-mean Gaussian noises (white noises), through summing each signal with a noise interfere. Noise level is determined using the ```SNR_level```. For each row of ```signals``` a noise interfere with unique power is generated and once all noises are generated, original signals are summed with their corresponding interferes to result in contaminated signals. Noise power for each observation is calculated as below:

$$
SNR_{dB} = 10 \log_{10} \left( \frac{P_{signal}}{P_{noise}} \right)
$$

$$
P_x = \frac{1}{N} \sum_{n=1}^{N} [x(n)]^2
$$

$$
\text{var}(x) = E\left( [x - \mu]^2 \right) \quad \text{(where } x \text{ is white noise, } \mu \text{ would be } 0\text{)}
$$

$$
\text{var}(x) = E(x^2) = \frac{1}{N} \sum_{n=1}^{N} [x(n)]^2
$$

$$
\text{var}(x) = \frac{1}{N} \sum_{n=1}^{N} [x(n)]^2 = P_x
$$

#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, ZipDatasetDownloader
from damavand.damavand.datasets.digestors import MFPT
from damavand.damavand.augmentations import gaussian_noise

# Downloading the MFPT dataset
addresses = read_addresses()
downloader = ZipDatasetDownloader(addresses['MFPT'])
downloader.download_extract('MFPT.zip', 'MFPT/')

mfpt = MFPT('MFPT/MFPT Fault Data Sets/', [
    '1 - Three Baseline Conditions',
    '2 - Three Outer Race Fault Conditions',
    '3 - Seven More Outer Race Fault Conditions',
    '4 - Seven Inner Race Fault Conditions',
])

# Mining the dataset
mining_params = {
    97656: {'win_len': 16671, 'hop_len': 2000},
    48828: {'win_len': 8337, 'hop_len': 1000},
}
mfpt.mine(mining_params)

# Signal/Metadata split
df = pd.concat(mfpt.data[48828]).reset_index(drop = True)
signals, metadata = df.iloc[:, : - 4], df.iloc[:, - 4 :]

# Augmenting the dataset with 20 dB noise
augmented_signals = gaussian_noise(signals, 20)

# Augmenting the dataset with 20 dB noise and returing also the pure noises
augmented_signals, noises = gaussian_noise(signals, 20, return_noise = True)
```

## ```masking_noise(signals, ratio, uniformity = False, return_mask = False)```


### Augmenting signals with binary random masks
  
#### Arguments:
- **signals** is the Original signals, in the form of a ```pd.DataFrame```.
- **ratio** the rate of masks to be set to zeros.
- **uniformity** is a flag to get identical binary masks for all observations; default is ```False``` (meaning that masks unidentical masks) and you need to set it ```True``` to zero-out observations, uniformly.
- **return_mask** is a flag to return masks too; its default value is ```False``` and you need to set it to ```True``` to return masks.

#### Return Values:
- A ```pandas.DataFrame``` including the masked out observations.
- A ```pandas.DataFrame``` (or ```np.array``` if ```uniformity``` is set ```True```) including the masks (only returned when ```return_noise``` is set to ```True```).

#### Descriptions:
Using this function, one is able to mask out original signals using binary masks.

#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, ZipDatasetDownloader
from damavand.damavand.datasets.digestors import MFPT
from damavand.damavand.augmentations import masking_noise

# Downloading the MFPT dataset
addresses = read_addresses()
downloader = ZipDatasetDownloader(addresses['MFPT'])
downloader.download_extract('MFPT.zip', 'MFPT/')

mfpt = MFPT('MFPT/MFPT Fault Data Sets/', [
    '1 - Three Baseline Conditions',
    '2 - Three Outer Race Fault Conditions',
    '3 - Seven More Outer Race Fault Conditions',
    '4 - Seven Inner Race Fault Conditions',
])

# Mining the dataset
mining_params = {
    97656: {'win_len': 16671, 'hop_len': 2000},
    48828: {'win_len': 8337, 'hop_len': 1000},
}
mfpt.mine(mining_params)

# Signal/Metadata split
df = pd.concat(mfpt.data[48828]).reset_index(drop = True)
signals, metadata = df.iloc[:, : - 4], df.iloc[:, - 4 :]

# Augmenting the dataset with a ratio of 0.2 to zero out
augmented_signals = masking_noise(signals, 0.2)

# Augmenting the dataset with a ratio of 0.2 to zero out and returing also the masks
augmented_signals, noises = masking_noise(signals, 0.2, uniformity = False, return_mask = True)
```

## ```amplitude_shifting(signals, coefficients)```


### Augmenting signals by amplitude shifting
  
#### Arguments:
- **signals** is the Original signals, in the form of a ```pd.DataFrame```.
- **coefficients** the coefficients to multiply signals by; to multiply all signals with an identical coefficient, pass a ```float``` or ```int```. Alternatively, pass a ```list``` with a length identical to the numbers of rows in ```signals``` to multiply each row with an identical coefficient.

#### Return Values:
- A ```pandas.DataFrame``` including the scaled observations.

#### Descriptions:
By this function, one can augment signals by scaling their amplitudes using a scaler. Scalers can be identical for all signals (if the ```coefficients``` is either a ```float``` or an ```int```) or unique for each row of signal by passing a ```list```.

#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, ZipDatasetDownloader
from damavand.damavand.datasets.digestors import MFPT
from damavand.damavand.augmentations import masking_noise

# Downloading the MFPT dataset
addresses = read_addresses()
downloader = ZipDatasetDownloader(addresses['MFPT'])
downloader.download_extract('MFPT.zip', 'MFPT/')

mfpt = MFPT('MFPT/MFPT Fault Data Sets/', [
    '1 - Three Baseline Conditions',
    '2 - Three Outer Race Fault Conditions',
    '3 - Seven More Outer Race Fault Conditions',
    '4 - Seven Inner Race Fault Conditions',
])

# Mining the dataset
mining_params = {
    97656: {'win_len': 16671, 'hop_len': 2000},
    48828: {'win_len': 8337, 'hop_len': 1000},
}
mfpt.mine(mining_params)

# Signal/Metadata split
df = pd.concat(mfpt.data[48828]).reset_index(drop = True)
signals, metadata = df.iloc[:, : - 4], df.iloc[:, - 4 :]

# Augmenting the dataset with by scaling all the signals by 5
augmented_signals = amplitude_shifting(signals, 5)

# Augmenting the first 5 signals by 5 different coefficients
augmented_signals = amplitude_shifting(signals.iloc[:5, :], [1, 2, 3, 4, 5])
```

## ```resampling(signals, target_len)```


### Resample signals to a target length
  
#### Arguments:
- **signals** is the Original signals, in the form of a ```pd.DataFrame```.
- **target_len** the target length of the resampled signals, as an ```int```.

#### Return Values:
- A ```pandas.DataFrame``` including the resampled signals.

#### Descriptions:
By this function, one can resample signals to a desired (lower or higher than the original) length.

#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, ZipDatasetDownloader
from damavand.damavand.datasets.digestors import MFPT
from damavand.damavand.augmentations import resampling

# Downloading the MFPT dataset
addresses = read_addresses()
downloader = ZipDatasetDownloader(addresses['MFPT'])
downloader.download_extract('MFPT.zip', 'MFPT/')

mfpt = MFPT('MFPT/MFPT Fault Data Sets/', [
    '1 - Three Baseline Conditions',
    '2 - Three Outer Race Fault Conditions',
    '3 - Seven More Outer Race Fault Conditions',
    '4 - Seven Inner Race Fault Conditions',
])

# Mining the dataset
mining_params = {
    97656: {'win_len': 16671, 'hop_len': 2000},
    48828: {'win_len': 8337, 'hop_len': 1000},
}
mfpt.mine(mining_params)

# Signal/Metadata split
df = pd.concat(mfpt.data[48828]).reset_index(drop = True)
signals, metadata = df.iloc[:, : - 4], df.iloc[:, - 4 :]

# Augmenting the dataset by resampling the original signals (8337 points) to 10000
signals_upsampled = resampling(signals, 10000)
```