import pandas as pd
import scipy
import numpy as np
from damavand.damavand.utils import *

def env(signals):
	"""
	env(signals) - Extracting the envelope of a set of signals

	Arguments:
	signals -- A pd.DataFrame() incuding signals in its rows.

	Return Value:
	A pd.DataFrame() whose rows are the envelopes of the signals stored in the inputted DataFrame.

	Descriptions:
	This function extracts the envelope of signals, stored in a pd.DataFrame() object. This is done through the application of
	Hilbert Transform (https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.hilbert.html); also np.abs() is used
	to calculate the absolute magnitude, from both the imaginery and real parts.
	"""

	return pd.DataFrame(np.abs(scipy.signal.hilbert(signals)))

def fft(signals, freq_filter = None, window = None):
	"""
	fft(signals, freq_filter, window) - Applying the Fast-Fourier Transform algorithim to derive frequency domain representation of a set of signals

	Arguemnts:
	Signals -- A pd.DataFrame() incuding signals in its rows.
	freq_filter -- A frequency filter object from scipy.signal module (e.g. scipy.signal.butter()) to avoid aliasing.
	window -- A window object from scipy.signal.windows module (e.g. scipy.signal.windows.hann()) to encounter the leakage error.

	Return Value:
	A pd.DataFrame whose rows are the frequency representations of the inputted DataFrame. As only the real frequency axis is of importance, the lenght of the frequency domain signals
	is half of the original time domain signal.

	Descriptions:
	This function computes the Discrete Fourier Transform (DFT) of a set of signals, through the application of Fast-Fourier Transform (FFT) algorithm. As it returns only the coeeficients
	correpsonding to real frequency components (not the imaginery ones), lenght of the returned pd.DataFrame() is half of the inputted pd.DataFrame. freq_filter and window are not mandatory 
	arguments and a function call without them is valid, however, we recommend using them to avoid aliasing (and of course near-zero/DC filtering through band-pass filters) and leakage error.
	We encourage you to use frequency axis for the sake of visualization; this can be done using either of the followings: scipy.fft.fftfreq(), np.linspace() and
	damavand.utils.fft_freq_axis().
	"""
	if freq_filter is not None:
		signals = scipy.signal.sosfilt(freq_filter, signals)

	if window is not None:
		signals = signals * window

	return pd.DataFrame(2.0/signals.shape[1] * np.abs(scipy.fft.fft(signals)[:, 0:signals.shape[1]//2]))


def zoomed_fft(signals, f_min, f_max, desired_len, sampling_freq, freq_filter = None, window = None):
	"""
	ZoomedFFT(signals, time_len, f_min, f_max, desired_len, sampling_freq, freq_filter, window) - Applying the ZoomFFT algorithm to derive a fine-grained frequency representation
	in a desired frequency range

	Arguments:
	signals -- A pd.DataFrame() incuding signals in its rows.
	f_min -- Minum of the desired frequency range.
	f_max -- Maximum of the desired frequency range.
	desired_len -- The desired length of the frequency domain representation.
	sampling_freq -- The sampling frequency of the inputted pd.DataFrame().
	freq_filter -- A frequency filter object from scipy.signal module (e.g. scipy.signal.butter()) to avoid aliasing.
	window -- A window object from scipy.signal.windows module (e.g. scipy.signal.windows.hann()) to encounter the leakage error.

	Return Value:
	A pd.DataFrame whose rows are the frequency representations of the inputted DataFrame, in the desired frequency range and with the chosen lenght.

	Descriptions:
	Using this function, one is able to derive a frequency represenation from the time domain signal in a desired frequency range and with the desired length. freq_filter and window are not mandatory 
	arguments and a function call without them is valid, however, we recommend using them to avoid aliasing (and of course near-zero/DC filtering through band-pass filters) and leakage error.
	We encourage you to use frequency axis for the sake of visualization; this can be done using either of the followings: np.linspace() or damavand.utils.ZoomedFFT_freq_axis().

	"""
	if freq_filter is not None:
		signals = scipy.signal.sosfilt(freq_filter, signals)

	if window is not None:
		signals = signals * window

	transform = scipy.signal.ZoomFFT(signals.shape[1], [f_min, f_max], desired_len, fs = sampling_freq)

	return pd.DataFrame((2/signals.shape[1]) * np.abs(transform(signals)))

def stft(signals, window_len, hop_len, freq_filter = None, window = None):
	"""
	STFT(signals, window_len, hop_len, freq_filter = None, window = None) - Application of Short-Time Fourier Transform to derive Time-Frequency representation of the inputted signals

	Arguemnts:
	signals -- A pd.DataFrame() incuding signals in its rows.
	window_len -- Lenght of the desired time segments.
	hop_len -- Length of the feed, used to get forward during the segmentation process.
	freq_filter -- A frequency filter object from scipy.signal module (e.g. scipy.signal.butter()) to avoid aliasing.
	window -- A window object from scipy.signal.windows module (e.g. scipy.signal.windows.hann()) to encounter the leakage error.

	Return Value:
	A np.array(), whose first dimension equals the number of rows included in the input pd.DataFrame; it includes derived Time-Frequency representations of the inputted signals. freq_filter and window are not mandatory 
	arguments and a function call without them is valid, however, we recommend using them to avoid aliasing (and of course near-zero/DC filtering through band-pass filters) and leakage error. Pay attention that unlike
	the case of damavand.signal_processing.fft() or damavand.signal_processing.zoomed_fft(), for this function you have to define freq_filter and window objects with a lenght that suits the segmented signals (equal to
	the window_len argument), instead of the original signals, presented in the inputted pd.DataFrame().

	Descriptions:
	By the application of this function, one is able to derive Time-Frequency representation; this is done by first segmenting the original signals to a series of shorter signals and consecutively FFT is applied on each
	segmented signal to derive the corresponding frequency representation. Results are usually visualized as heatmaps, whose vertical axis is the frequency dimension and the horizontal one is left to time dimension. One
	can use the damavand.utils.STFT_axises() to generate both time and frequency axises needed to visualize the resulting heatmaps.
	"""
	splitted_signals = np.array(signals.apply(splitter, args = (window_len, hop_len, False), axis = 1).to_list())
	if freq_filter is not None:
		splitted_signals = scipy.signal.sosfilt(freq_filter, splitted_signals)

	if window is not None:
		splitted_signals = splitted_signals * window
		
	return 2.0/splitted_signals.shape[2] * np.abs(scipy.fft.fft(splitted_signals)[:, :, 0:splitted_signals.shape[2]//2])