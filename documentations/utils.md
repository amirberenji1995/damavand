# Damavand Documention - Utility Module API Reference

## ```splitter(array, win_len, hop_len, return_df = True)```


### Splitting raw data signals into series of segmented signals
  
  #### Arguments:
  - **array** is the original signal, in the form of a ```np.array```.
  - **win_len** is the desired length of the segmented signals.
  - **hop_len** is the forward move of the window.
  - **return_df** determines the output type; the default value is ```True```, meaning that returned type is a ```pandas.DataFrame```. If set to ```False```, the function returns a ```np.array```.
  
  #### Return Value:
  - A ```pandas.DataFrame``` including segmented signals, extracted from the original raw signal.

  #### Descriptions:
  This function helps one to transform the raw signals into a series of segmented signals.

  