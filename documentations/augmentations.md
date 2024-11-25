# Damavand Documention - Augmentations Module API Reference

## ```gaussian_noise(signals, SNR_level, return_noise = False)```


### Augmenting signals with a Signal-to-Noise Ratio level, through adding Gaussian noise
  
#### Arguments:
- **signals** is the Original signals, in the form of a ```pd.DataFrame```.
- **SNR_level** is the desired SNR level (in dB) of the augmented signals.
- **return_noise** is a flag to also return the pure noises; default is ```False``` and you need to set it ```True``` to also return the noises.

#### Return Values:
- A ```pandas.DataFrame``` noise contaminated signals.
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