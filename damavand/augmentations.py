import numpy as np
import pandas as pd
from scipy.signal import resample

def gaussian_noise(signals, SNR_level, return_noise = False):
  
  """
  Adding Gaussian noise to a set of signals.

  Parameters
  ----------
  signals: pandas.DataFrame
    A DataFrame whose rows are the signals to be augmented.
  SNR_level: float
    The desired signal-to-noise ratio (in dB) of the augmented signals.
  return_noise: bool, optional
    Whether to return the pure noises as a secondary output; defaults to False.

  Returns
  -------
  noisy_signals: pandas.DataFrame
    A DataFrame whose rows are the augmented signals.
  noises: pandas.DataFrame, optional
    A DataFrame whose rows are the pure noises; only returned when return_noise is set to True.
  """
  
  def noise_genaretor(row, SNR_level):
    """
    Generate Gaussian noise for a given signal row based on the desired SNR level.

    Parameters
    ----------
    row : np.ndarray
      The signal data for which noise is to be generated.
    SNR_level : float
      The desired signal-to-noise ratio in decibels.

    Returns
    -------
    np.ndarray
      An array of Gaussian noise with the same shape as the input signal row.
    """

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
  
  """
  Masking a given set of signals with a certain ratio of its elements zeroed out.

  Parameters
  ----------
  signals : pandas.DataFrame
    A DataFrame whose rows are the signals to be masked.
  ratio : float
    A float in the range [0, 1) that determines the ratio of elements of each signal to be zeroed out.
  uniformity : bool, optional
    A boolean flag to determine whether to generate identical masks for all observations or not. Defaults to False.
  return_mask : bool, optional
    A boolean flag to determine whether to return the masks as well or not. Defaults to False.

  Returns
  -------
  pandas.DataFrame
    A DataFrame including the augmented signals with the desired ratio of zeroed out elements.
  pandas.DataFrame, optional
    A DataFrame including the binary masks that have been used to zero out the elements of signals. Only returned if return_mask is set to True.
  """
  
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
  
  """
  Shift the amplitude of a set of signals by a set of coefficients
  
  Parameters
  ----------
  signals : pd.DataFrame
    Signals to be rescaled
  coefficients : float or list of floats
    Coefficients to be multiplied to the signals. If a float, all signals will be rescaled with that coefficient. If a list of floats, each signal will be rescaled with the corresponding coefficient in the list
  
  Returns
  -------
  pd.DataFrame
    Rescaled signals
  """
  if type(coefficients) == list :
    coefficients = np.repeat(np.array(coefficients).reshape(-1, 1), signals.shape[1], axis = 1)
  
  return signals * coefficients

def resampling(signals, target_len):
  """
  Resample signals to a target length

  Parameters
  ----------
  signals : pd.DataFrame
    Signals to be resampled
  target_len : int
    Target length of the resampled signals

  Returns
  -------
  pd.DataFrame
    Resampled signals
  """
  return pd.DataFrame(resample(signals, target_len, axis = 1))