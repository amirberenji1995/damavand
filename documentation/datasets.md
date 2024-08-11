# Damavand Documention - Datasets Module API Reference

## Downloaders Submodule

### ```read_addresses```

Using this function, one is able to load the download addresses of the available datasets, as a python dictionary. For single-file datasets, the value corresponding to the dataset name key, is the download link. For datasets consisting of various files, value corresponding to the dataset name will be another python dictionary whose keys are file names and corresponding values are download links.

#### Usage example:

```
addresses = read_addresses()
```

### ```ZipDatasetDownloader```

Using this class, one is able to download and extract datasets that are available as single zip files (eg. SEU).

#### Instantiation: ```ZipDatasetDownloader(url)```
- ```url``` is the download link.
#### Downloading: ```ZipDatasetDownloader.download(download_file)```
- ```download_file``` is the directory in which the zip file is downloaded to. This value is stored in ```ZipDatasetDownloader.download_file```, once ```ZipDatasetDownloader.download()``` is called.

#### Extraction: ```ZipDatasetDownloader.extract(extraction_path)```
- ```extraction_path``` is the directory that zip file is extracted to. This value is stored in ```ZipDatasetDownloader.extraction_path```, once ```ZipDatasetDownloader.extract()``` is called.

#### Merging downloading and extraction steps: ```ZipDatasetDownloader.download_extract(download_path, extraction_path)```

- ```download_file``` is the directory in which the zip file is downloaded to. This value is stored in ```ZipDatasetDownloader.download_file```, once ```ZipDatasetDownloader.download()``` is called.
- ```extraction_path``` is the directory that zip file is extracted to. This value is stored in ```ZipDatasetDownloader.extraction_path```, once ```ZipDatasetDownloader.download_extract()``` is called.


#### Usage example:

```
addresses = read_addresses()
downloader = zipDatasetDownloader(addresses['SEU'])
downloader.download_extract('SEU.zip', 'SEU/)
```

### ```CwruDownloader```

A custom downloader for CWRU dataset.

#### Instantiation: ```CwruDownloader(files)```
- ```files``` is a python ```dictionary``` whose keys are file names and corresponding values are the download links.
#### Downloading: ```CwruDownloader.download(download_path, chunk_size = 512, delay = 1)```

- ```download_path``` is the directory where desired files are downloaded to. This value is stored in ```CwruDownloader.download_path```, once ```CwruDownloader.download()``` is called.
- ```chunk_size``` to avoid corrupted downloading, responses are read in chunks; this variable controls the size of the chunks. Default value is 512  Bytes.
- ```delay``` to avoid server overload, it is better to place a small delay between requesting consecutive files. This argument controls the dealy time interval, in the unit of seconds. The default value is 1 second.

#### Redownloading errored downlaods: ```CwruDownloader.redownload(chunk_size = 512, delay = 1)```
- ```chunk_size``` to avoid corrupted downloading, responses are read in chunks; this variable controls the size of the chunks. Default value is 512 Bytes.
- ```delay``` to avoid server overload, it is better to place a small delay between requesting consecutive files. This argument controls the dealy time interval, in the unit of seconds. The default value is 1 second.

#### Undownloaded files: ```CwruDownloader.undownloaded```
If a file is not downloaded properly - either during the ```CwruDownloader.download()``` or ```CwruDownloader.redownload()``` - it is added to ```CwruDownloader.undownloaded``` as a pair of key (file name) and value (corresponding error). This can be later used to complete the downloading process.

#### Usage example:

```
addresses = read_addresses()
downloader = CwruDownloader(addresses['CWRU'])
downloader.download('CWRU/')
while len(list(downloader.undownloaded.keys())) > 0:
    downloader.redownload()
    print(downloader.undownloaded)
```

### ```PuDownloader```

A custom downloader for PU dataset.

#### Instantiation: ```PuDownloader(files)```
- ```files``` is a python ```dictionary``` whose keys are file names and corresponding values are the download links.

#### Downloading: ```PuDownloader.download(download_path, timeout = 10)```

- ```download_path``` is the directory where rar files are donwloaded to. This value is stored in ```PuDownloader.download_path```, once ```PuDownloader.download()``` is called.
- ```timeout``` is the number of seconds that downloader waits to download a file.

#### Extracting: ```PuDownloader.extract(extraction_path)```
- ```extraction_path``` is the directory that rar files are extracted to. This value is stored in ```PuDownloader.extraction_path```, once ```PuDownloader.extract()``` is called.

#### Merging downloading and extraction steps: ```PuDownloader.download_extract(download_path, extraction_path)```

- ```download_path``` is the directory in which the rar files are downloaded to. This value is stored in ```PuDownloader.download_path```, once ```PuDownloader.download_extract()``` is called.
- ```extraction_path``` is the directory that rar files are extracted to. This value is stored in ```PuDownloader.extraction_path```, once ```PuDownloader.download_extract()``` is called.

#### Usage example:

```
addresses = read_addresses()
downloader = PuDownloader(addresses['PU'])
PuDownloader(addresses['PU']).download_extract('PU_rarfiles', 'PU/')
```

### ```MaFaulDaDownloader```

A custom downloader for MaFaulDa dataset.

#### Instantiation: ```MaFaulDaDownloader(files)```
- ```files``` is a python ```dictionary``` whose keys are file names and corresponding values are the download links.

#### Downloading: ```MaFaulDaDownloader.download(download_path)```

- ```download_path``` is the directory where desired files are donwloaded to. This value is stored in ```MaFaulDaDownloader.download_path```, once ```MaFaulDaDownloader.download()``` is called.

#### Extracting: ```MaFaulDaDownloader.extract(extraction_path)```
- ```extraction_path``` is the directory that zip files are extracted to. This value is stored in ```MaFaulDaDownloader.extraction_path```, once ```MaFaulDaDownloader.extract()``` is called.

#### Merging downloading and extraction steps: ```MaFaulDaDownloader.download_extract(download_path, extraction_path)```

- ```download_path``` is the directory in which the zip file is downloaded to. This value is stored in ```MaFaulDaDownloader.download_path```, once ```MaFaulDaDownloader.download_extract()``` is called.
- ```extraction_path``` is the directory that zip file is extracted to. This value is stored in ```MaFaulDaDownloader.extraction_path```, once ```MaFaulDaDownloader.download_extract()``` is called.


#### Usage example:

```
addresses = read_addresses()
downloader = MaFaulDaDownloader(addresses['MaFaulDa'])
PuDownloader(addresses['MaFaulDa']).download_extract('MaFaulDa_zipfiles', 'MaFaulDa/')
```

## Digestors Submodule

### ```KAIST```

#### Original title: Vibration, Acoustic, Temperature, and Motor Current Dataset of Rotating Machine Under Varying Operating Conditions for Fault Diagnosis

#### External resources:
- https://data.mendeley.com/datasets/ztmf3m7h5x/6
- https://www.sciencedirect.com/science/article/pii/S2352340923001671

#### Instantiation: ```KAIST(base_directory, files, channels)```

- ```base_directory```: Home directory of the extracted files.
- ```files```: List of files of interest; to include all the files, use ```os.listdir(base_directory)```
- ```channels```: List of channels to include; 0, 1, 2 and 3 correspond to x direction - housing A, y direction - housing A, x direction - housing B and y direction - housing B, respectively. Default value is [0, 1, 2, 3].

#### Mining: ```KAIST.mine(mining_params)```
- ```mining_params```: a python dictonary whose keys are ```win_len``` and ```hop_len``` with their correponding values.

#### Accessing data: ```KAIST.data```
Mined data is presented as a python dictonary whose keys correspond to the ```channels``` and values are list of ```pd.DataFrame``` objects.

#### Usage example:

```
win_len, hop_len = 20000, 20000
kaist = KAIST('KAIST/', os.listdir('KAIST/'), list(range(2)))
kaist.mine(win_len, hop_len)
```

### ```MFPT```

#### Original title: Condition Based Maintenance Fault Database for Testing of Diagnostic and Prognostics Algorithms - Bearing Fault Dataset

#### External resources:
- https://www.mfpt.org/fault-data-sets/
- https://mfpt.org/wp-content/uploads/2018/03/MFPT-Bearing-Envelope-Analysis.pdf

#### Instantiation: ```MFPT(base_directory, folders)```

- ```base_directory```: Home directory of the extracted folder.
- ```folders```: List of folders to include; valid elements are *1 - Three Baseline Conditions*, *2 - Three Outer Race Fault Conditions*, *3 - Seven More Outer Race Fault Conditions* and *4 - Seven Inner Race Fault Conditions*.

#### Mining: ```MFPT.mine(mining_params)```
- ```mining_params```: a nested python dictonary whose keys are 97656 and 48828 (sampling frequencies the dataset is collected by) and the corresponding values are objects of python dictonary. Secondary dictonaries each have two keys: ```win_len``` and ```hop_len``` with correponding values.

#### Accessing data: ```MFPT.data```
Mined data is presented as a python dictonary whose keys are 97656 and 48828. Corresponding values are lists of ```pd.DataFrame``` objects, belonging to the data files recorded to the corresponding sampling frequency.

#### Usage example:

```
mining_params = {
    97656: {win_len: 16671, hop_len: 4000},
    48828: {win_len: 8337, hop_len: 2000}, 
}
mfpt = MFPT('MFPT Fault Data Sets/', [
    '1 - Three Baseline Conditions',
    '2 - Three Outer Race Fault Conditions',
    '3 - Seven More Outer Race Fault Conditions',
    '4 - Seven Inner Race Fault Conditions',
])
mfpt.mine({'97656': 16000, '48828': 8000}, {'97656': 4000, '48828': 2000})
```

### ```CWRU```

#### External resources:
- https://engineering.case.edu/bearingdatacenter

#### Instantiation: ```CWRU(base_directory, channels)```

- ```base_directory```: Home directory of the downloaded files.
- ```channels```: List of strings to include the desired measurement channels; 'FE' and 'DE' corresponding to fan-end acceleration, drive-end acceleration and base acceleration respectively, are available choices. Default value is ['FE', 'DE'].

#### Mining: ```CWRU.mine(mining_params, synchronous_only)```
- ```mining_params```: a nested python dictonary whose keys are '12K' and '48K' (sampling frequencies used to collect the dataset) and values are again python dictionaries whose keys are ```win_len``` and ```hop_len```.
- ```synchronous_only``` is a boolean variable to be used as a flag; once this flag is set ```True```, only files which contain all the desired channels are mined and ones missing one of the channels are skipped. Default value is ```False```.

#### Accessing data: ```CWRU.data```
Mined data is organized as a nested python dictonary whose keys are elements of the ```channels```; corresponding values again python dictionaries whose keys are the sampling frequencies; '12K' and '48K'.

#### Usage example:

```
mining_params = {
    '12K': {'win_len': 12000, 'hop_len': 3000},
    '48K': {'win_len': 48000, 'hop_len': 16000},
}

cwru = CWRU('CWRU/')
cwru.mine(mining_params, synchronous_only = True)
```


### ```SEU```

#### Original title: Highly Accurate Machine Fault Diagnosis Using Deep Transfer Learning

#### External resources:
- https://ieeexplore.ieee.org/abstract/document/8432110
- https://github.com/cathysiyu/Mechanical-datasets/tree/master/gearbox

#### Instantiation: ```SEU(base_directory, channels)```

- ```base_directory```: Home directory of the downloaded files.
- ```channels```: List of integers (from 0 to 7), corresponding to 8 accelerometers. Default value is [0, 1, 2, 3, 4, 5, 6, 7].

#### Mining: ```SEU.mine(mining_params)```
- ```mining_params```: a python dictonary whose keys are ```win_len``` and ```hop_len```. 

#### Accessing data: ```SEU.data```
Mined data is organized as a python dictonary whose keys are elements of the ```channels```; corresponding values are lists of ```pd.DataFrame``` objects.

#### Usage example:

```
mining_params = {'win_len': 10000, 'hop_len': 10000}
seu = SEU('SEU/')
seu.mine(mining_params)
```

### ```MaFaulda```

#### Original title: Machinery Fault Database

#### External resources:
- https://www02.smt.ufrj.br/~offshore/mfs/page_01.html

#### Instantiation: ```MaFauldDa(base_directory, folders, channels)```

- ```base_directory```: Home directory of the extracted folders.
- ```folders```:Folders to include during the mining process.
- ```channels```: List of integers (from 0 to 7), corresponding to the tachometer, 3 accelerometers on the underhang bearing (axial, radial and tangential), 3 accelerometers on the overhang bearing (axial, radial and tangential) and a microphone.

#### Mining: ```MaFaulda.mine(mining_params)```
- ```mining_params```: a python dictonary whose keys are ```win_len``` and ```hop_len```. 

#### Accessing data: ```MaFaulda.data```
Mined data is organized as a python dictonary whose keys are elements of the ```channels```; corresponding values are lists of ```pd.DataFrame``` objects.

#### Usage example:

```
mining_params = {'win_len': 50000, 'hop_len': 50000}
mafaulda = MaFauldDa('mafaulda/', ['normal', 'horizontal_misalignment'], channels = [2])
mafaulda.mine(50000, 50000)
```

### ```MEUT```

#### Original title: Triaxial bearing vibration dataset of induction motor under varying load conditions

#### External resources:
- https://data.mendeley.com/datasets/fm6xzxnf36/2
- https://www.sciencedirect.com/science/article/pii/S2352340922005170

#### Instantiation: ```MUET(base_directory, folders, channels)```

- ```base_directory```: Home directory of the extracted folders.
- ```folders```:Folders to include during the mining process.
- ```channels```: List of integers, corresponding to the triaxial acceleration signals; 1, 2 and 3 correspond to X-axis, Y-axis, and Z-axis.

#### Mining: ```MUET.mine(mining_params)```
- ```mining_params```: a python dictonary whose keys are ```win_len``` and ```hop_len```. 

#### Accessing data: ```MUET.data```
Mined data is organized as a python dictonary whose keys are elements of the ```channels```; corresponding values are lists of ```pd.DataFrame``` objects.

#### Usage example:

```
mining_params = {'win_len': 50000, 'hop_len': 50000}
meut = MEUT('fm6xzxnf36-2/', os.listdir('fm6xzxnf36-2/'), channels = [2])
mafaulda.mine(10000, 5000)
```

### ```UoO```

#### Original title: Bearing vibration data collected under time-varying rotational speed conditions

#### External resources:
- https://www.sciencedirect.com/science/article/pii/S2352340918314124
- https://data.mendeley.com/datasets/v43hmbwxpm/1

#### Instantiation: ```UoO(base_directory, channels, reps)```

- ```base_directory```: Home directory of the extracted folders.
- ```channels```: List of strings, specifying to the desired channels; available choices are 'channel_1' and 'channel_2', corresponding to the acceleration and the rotational speed. Default value is ['channel_1', 'channel_2'].
- ```reps```: To enrich the dataset, measurements are repeated three times. ```reps``` is a list that specifies the number of repetitions (1, 2 and 3), to include. Default value is [1, 2, 3].

#### Mining: ```UoO.mine(mining_params)```
- ```mining_params```: a python dictonary whose keys are ```win_len``` and ```hop_len```. 

#### Accessing data: ```UoO.data```
Mined data is organized as a python dictonary whose keys are elements of the ```channels```; corresponding values are lists of ```pd.DataFrame``` objects.

#### Usage example:

```
mining_params = {'win_len': 50000, 'hop_len': 50000}
uoo = UoO('UoO/', channels = ['Channel_1', 'Channel_2'], reps = list(range(1,4)))
uoo.mine(10000, 10000)
```

### ```PU```

#### Original title: Bearing vibration data collected under time-varying rotational speed conditions

#### External resources:
- https://www.papers.phmsociety.org/index.php/phme/article/view/1577
- https://mb.uni-paderborn.de/kat/forschung/kat-datacenter/bearing-datacenter/data-sets-and-download

#### Instantiation: ```PU(base_directory, folders, channels, reps)```

- ```base_directory```: Home directory of the extracted folders.
- ```folders```: List of the extracted folders, to include.
- ```channels```: List of strings, specifying to the desired channels; available choices are 'CP1', 'CP2' and 'Vib' corresponding to the current phases (1 and 2) and acceleration. Default value is ['CP1', 'CP2', 'Vib'].
- ```reps```: To enrich the dataset, measurements are repeated twenty times. ```reps``` is a list that specifies the number of repetitions (1, 2 and 3), to include. Default value is [1, 2, 3, ... , 19, 20].

#### Mining: ```PU.mine(mining_params)```
- ```mining_params```: a python dictonary whose keys are ```win_len``` and ```hop_len```. 

#### Accessing data: ```PU.data```
Mined data is organized as a python dictonary whose keys are elements of the ```channels```; corresponding values are lists of ```pd.DataFrame``` objects.

#### Usage example:

```
mining_params = {'win_len': 50000, 'hop_len': 50000}
pu = PU('PU/', os.listdir('PU/), channels = ['CP1', 'CP2', 'Vib'], reps = list(range(0,5)))
pu.mine(10000, 10000)
```