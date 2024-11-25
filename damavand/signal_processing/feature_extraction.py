import pandas as pd
import numpy as np

def feature_extractor(signals, features):
    """
    feature_extractor(signals, features) - Extracting features from input signals

    Arguments:
    signals -- A pd.DataFrame() including signals in its rows
    features -- A python dict where:
                - keys are feature names
                - values are tuples of (function, args, kwargs) where:
                  * function: the feature extraction function
                  * args: tuple of positional arguments (optional)
                  * kwargs: dict of keyword arguments (optional)
                Example: {
                    'feature1': (func1, (), {}),
                    'feature2': (func2, (arg1,), {'param1': value1}),
                }

    Return Value:
    A pd.DataFrame() containing the feature values for each signal
    """
    def apply_feature(row, func_tuple):
        func, args, kwargs = func_tuple
        return func(row, *args, **kwargs)

    feature_values = signals.apply(
        lambda row: pd.Series([
            apply_feature(row, feat_info) for feat_info in features.values()
        ]),
        axis=1
    )
    feature_values.columns = features.keys()
    
    return feature_values


# Time domain signals

def smsa(arr):
   return np.square(np.mean(np.sqrt(np.abs(arr))))

def rms(arr):
  return np.sqrt(np.mean(np.square(arr)))

def peak(arr):
   return np.max(np.abs(arr))

def crest_factor(arr):
   return peak(arr) / rms(arr)

def clearence_factor(arr):
   return peak(arr) / smsa(arr)

def shape_factor(arr):
   return rms(arr) / np.mean(np.abs(arr))

def impulse_factor(arr):
   return peak(arr) / np.mean(np.abs(arr))

# Frequency domain features

def spectral_centroid(spectrum, freq_axis):
   return np.sum(np.product(spectrum, freq_axis)) / np.sum(spectrum)

def P17(spectrum, freq_axis):
   return np.sqrt(np.mean(np.product(np.square(np.subtract(freq_axis, spectral_centroid(spectrum, freq_axis))), spectrum)))

def P18(spectrum, freq_axis):
   return np.sqrt(np.sum(np.product(np.square(freq_axis), spectrum)) / np.sum(spectrum))

def P19(spectrum, freq_axis):
   np.sqrt(np.sum(np.product(np.power(freq_axis, 4), spectrum)) / np.sum(np.product(np.square(freq_axis), spectrum)))

def P20(spectrum, freq_axis):
   return np.sum(np.product(np.square(freq_axis), spectrum)) / np.sqrt(np.product(np.sum(spectrum), np.sum(np.product(np.power(freq_axis, 4), spectrum))))

def P21(spectrum, freq_axis):
   return P17(spectrum, freq_axis) / spectral_centroid(spectrum, freq_axis)

def P22(spectrum, freq_axis):
   return np.mean(np.product(np.power(np.subtract(freq_axis, spectral_centroid(spectrum, freq_axis)), 3), spectrum)) / np.power(P17(spectrum, freq_axis), 3)

def P23(spectrum, freq_axis):
   return np.mean(np.product(np.power(np.subtract(freq_axis, spectral_centroid(spectrum, freq_axis)), 4), spectrum)) / np.power(P17(spectrum, freq_axis), 4)

def P24(spectrum, freq_axis):
   return np.mean(np.product(np.sqrt(np.subtract(freq_axis, spectral_centroid(spectrum, freq_axis))), spectrum)) / np.sqrt(P17(spectrum, freq_axis))