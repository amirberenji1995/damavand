import numpy as np
import pandas as pd

def gaussian_noise(signals, SNR_level, return_noise = False):
  
  def noise_genaretor(row, SNR_level):

    signal_power = np.sum(np.square(row))
    noise_power = signal_power / np.power(10, (SNR_level/10))
    noise = np.random.normal(0, np.sqrt(noise_power), row.shape)
    
    return noise
  
  noises = []
  noisy_records = []
  for index, row in signals.iterrows():
    noise = noise_genaretor(row, SNR_level)
    noises.append(noise)
    noisy_records.append(row + noise)


  if return_noise:
    return pd.DataFrame(noisy_records), pd.DataFrame(noises)
  else:
    return pd.DataFrame(noisy_records)
  

def masking_noise(signals, ratio, uniformity = False, return_mask = False):
  
  n_mask = int(signals.shape[1] * ratio)

  if uniformity:
    mask = np.ones((signals.shape[1]))
    indices = np.random.choice(np.arange(mask.shape[0]), replace = False, size = n_mask)
    mask[indices] = 0

    if return_mask:
      return pd.DataFrame(signals.to_numpy() * mask), mask
    else:
      return pd.DataFrame(signals.to_numpy() * mask)
  
  else:
    masks = []
    for index, row in signals.iterrows():
      mask = np.ones((row.shape[0]))
      indices = np.random.choice(np.arange(mask.shape[0]), replace = False, size = n_mask)
      mask[indices] = 0
      masks.append(mask)

    if return_mask:
      return pd.DataFrame(signals.to_numpy() * masks), pd.DataFrame(masks)
    else:
      return pd.DataFrame(signals.to_numpy() * masks)
    
def amplitude_shifting(signals, coefficients):
  
  if type(coefficients) == list :
    coefficients = np.repeat(np.array(coefficients).reshape(-1, 1), signals.shape[1], axis = 1)
  
  return signals * coefficients