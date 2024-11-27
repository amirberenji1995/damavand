# Damavand Documention - Datasets Module API Reference
Data is the essential ingridient for any data-driven analysis, including rotating machinery intelligent condition monitoring. On this page, we go through both submodules of the datasets module: 1)Downloaders and 1)Digestors. While the former is focused around downloading the raw dataset from internet, the latter is developed around structurizing the raw data.
## Downloaders Submodule

### ```read_addresses```

#### Loading the addresses of datasets to download them

##### Arguments:
- **This function recieves no argument**

##### Return Value:
- A ```dict``` object whose keys are dataset names and values are download addresses.

##### Description:
Using this function, one is able to load the download addresses of the available datasets, as a python dictionary. For single-file datasets, the value corresponding to the dataset name key, is the download link. For datasets consisting of various files, value corresponding to the dataset name will be another python dictionary whose keys are file names and corresponding values are download links.

#### Usage example:

```Python
# Importing
from damavand.damavand.datasets.downloaders import read_addresses

# Loading the addresses
addresses = read_addresses()
```

### ```ZipDatasetDownloader```

#### Downloading datasets stored in single Zip files

#### Description:

Using this class, one is able to download and extract datasets that are available as single zip files (eg. SEU).

- ##### Instantiation: ```ZipDatasetDownloader(url)```
    - ```url``` is the download link.
- ##### Downloading: ```ZipDatasetDownloader.download(download_file)```
    - ```download_file``` is the directory in which the zip file is downloaded to. This value is stored in ```ZipDatasetDownloader.download_file```, once ```ZipDatasetDownloader.download()``` is called.

- ##### Extraction: ```ZipDatasetDownloader.extract(extraction_path)```
    - ```extraction_path``` is the directory that zip file is extracted to. This value is stored in ```ZipDatasetDownloader.extraction_path```, once ```ZipDatasetDownloader.extract()``` is called.

- ##### Merging downloading and extraction steps: ```ZipDatasetDownloader.download_extract(download_path, extraction_path)```

    - ```download_file``` is the directory in which the zip file is downloaded to. This value is stored in ```ZipDatasetDownloader.download_file```, once ```ZipDatasetDownloader.download()``` is called.
    - ```extraction_path``` is the directory that zip file is extracted to. This value is stored in ```ZipDatasetDownloader.extraction_path```, once ```ZipDatasetDownloader.download_extract()``` is called.


#### Usage example:

```Python
# Importing
from damavand.damavand.datasets.downloaders import read_addresses, ZipDatasetDownloader

# Loading the addresses
addresses = read_addresses()

# Downloading the dataset
downloader = zipDatasetDownloader(addresses['SEU'])
downloader.download_extract('SEU.zip', 'SEU/)
```

### ```CwruDownloader```

#### A custom downloader for CWRU dataset.

#### Description:

- ##### Instantiation: ```CwruDownloader(files)```
    - ```files``` is a python ```dictionary``` whose keys are file names and corresponding values are the download links.
- ##### Downloading: ```CwruDownloader.download(download_path, chunk_size = 512, delay = 1)```

    - ```download_path``` is the directory where desired files are downloaded to. This value is stored in ```CwruDownloader.download_path```, once ```CwruDownloader.download()``` is called.
    - ```chunk_size``` to avoid corrupted downloading, responses are read in chunks; this variable controls the size of the chunks. Default value is 512  Bytes.
    - ```delay``` to avoid server overload, it is better to place a small delay between requesting consecutive files. This argument controls the dealy time interval, in the unit of seconds. The default value is 1 second.

- ##### Redownloading errored downlaods: ```CwruDownloader.redownload(chunk_size = 512, delay = 1)```
    - ```chunk_size``` to avoid corrupted downloading, responses are read in chunks; this variable controls the size of the chunks. Default value is 512 Bytes.
    - ```delay``` to avoid server overload, it is better to place a small delay between requesting consecutive files. This argument controls the dealy time interval, in the unit of seconds. The default value is 1 second.

- ##### Undownloaded files: ```CwruDownloader.undownloaded```
    If a file is not downloaded properly - either during the ```CwruDownloader.download()``` or ```CwruDownloader.redownload()``` - it is added to ```CwruDownloader.undownloaded``` as a pair of key (file name) and value (corresponding error). This can be later used to complete the downloading process.

#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, CwruDownloader

# Loading the addresses
addresses = read_addresses()

# Downloading the addresses
downloader = CwruDownloader(addresses['CWRU'])
downloader.download('CWRU/')
while len(list(downloader.undownloaded.keys())) > 0:
    downloader.redownload()
```

### ```PuDownloader```

#### A custom downloader for PU dataset.

#### Description:

- ##### Instantiation: ```PuDownloader(files)```
    - ```files``` is a python ```dictionary``` whose keys are file names and corresponding values are the download links.

- ##### Downloading: ```PuDownloader.download(download_path, timeout = 10)```

    - ```download_path``` is the directory where rar files are donwloaded to. This value is stored in ```PuDownloader.download_path```, once ```PuDownloader.download()``` is called.
    - ```timeout``` is the number of seconds that downloader waits to download a file.

- ##### Extracting: ```PuDownloader.extract(extraction_path)```
    - ```extraction_path``` is the directory that rar files are extracted to. This value is stored in ```PuDownloader.extraction_path```, once ```PuDownloader.extract()``` is called.

- ##### Merging downloading and extraction steps: ```PuDownloader.download_extract(download_path, extraction_path)```

    - ```download_path``` is the directory in which the rar files are downloaded to. This value is stored in ```PuDownloader.download_path```, once ```PuDownloader.download_extract()``` is called.
    - ```extraction_path``` is the directory that rar files are extracted to. This value is stored in ```PuDownloader.extraction_path```, once ```PuDownloader.download_extract()``` is called.

#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, PuDownloader

# Loading the addresses
addresses = read_addresses()

# Downloading the dataset
downloader = PuDownloader(addresses['PU'])
PuDownloader(addresses['PU']).download_extract('PU_rarfiles', 'PU/')
```

### ```MaFaulDaDownloader```

#### A custom downloader for MaFaulDa dataset.

#### Description:

- ##### Instantiation: ```MaFaulDaDownloader(files)```
    - ```files``` is a python ```dictionary``` whose keys are file names and corresponding values are the download links.

- ##### Downloading: ```MaFaulDaDownloader.download(download_path)```

    - ```download_path``` is the directory where desired files are donwloaded to. This value is stored in ```MaFaulDaDownloader.download_path```, once ```MaFaulDaDownloader.download()``` is called.

- ##### Extracting: ```MaFaulDaDownloader.extract(extraction_path)```
    - ```extraction_path``` is the directory that zip files are extracted to. This value is stored in ```MaFaulDaDownloader.extraction_path```, once ```MaFaulDaDownloader.extract()``` is called.

- ##### Merging downloading and extraction steps: ```MaFaulDaDownloader.download_extract(download_path, extraction_path)```

    - ```download_path``` is the directory in which the zip file is downloaded to. This value is stored in ```MaFaulDaDownloader.download_path```, once ```MaFaulDaDownloader.download_extract()``` is called.
    - ```extraction_path``` is the directory that zip file is extracted to. This value is stored in ```MaFaulDaDownloader.extraction_path```, once ```MaFaulDaDownloader.download_extract()``` is called.


#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, MaFaulDaDownloader

# Loading the addresses
addresses = read_addresses()
# Downloading the dataset
downloader = MaFaulDaDownloader(addresses['MaFaulDa'])
PuDownloader(addresses['MaFaulDa']).download_extract('MaFaulDa_zipfiles', 'MaFaulDa/')
```

## Digestors Submodule

### ```KAIST```

#### A digestor to mine the dataset by Korea Advanced Institute of Science and Technology (KAIST)

- ##### Original title: Vibration, Acoustic, Temperature, and Motor Current Dataset of Rotating Machine Under Varying Operating Conditions for Fault Diagnosis

- ##### External resources:
    - https://data.mendeley.com/datasets/ztmf3m7h5x/6
    - https://www.sciencedirect.com/science/article/pii/S2352340923001671

#### Description:

- ##### Instantiation: ```KAIST(base_directory, files, channels)```

    - ```base_directory``` is the home directory of the extracted files.
    - ```files``` is the list of files of interest; to include all files, use ```os.listdir(base_directory)```
    - ```channels```is the ist of channels to include; 0, 1, 2 and 3 correspond to x direction - housing A, y direction - housing A, x direction - housing B and y direction - housing B, respectively. Default value is [0, 1, 2, 3].

- ##### Mining: ```KAIST.mine(mining_params)```
    - ```mining_params``` is a python dictonary whose keys are ```win_len``` and ```hop_len``` with their correponding values.

- ##### Accessing data: ```KAIST.data```
    Mined data is presented as a python dictonary whose keys correspond to the ```channels``` and values are list of ```pd.DataFrame``` objects.

#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, ZipDatasetDownloader
from damavand.damavand.datasets.digestors import KAIST

# Downloading the dataset
addresses = read_addresses()
downloader = ZipDatasetDownloader(addresses['KAIST'])
downloader.download_extract('KAIST.zip', 'KAIST/')

# Mining the dataset (using only two channels out of four)
kaist = KAIST('KAIST/', os.listdir('KAIST/'), list(range(2)))
mining_params = {
    'win_len': 20000,
    'hop_len': 20000,
}
kaist.mine(mining_params)
```

### ```MFPT```

#### A digestor to mine the dataset by Society for Machinery Failure Prevention Technology (MFPT)

- ##### Original title: Condition Based Maintenance Fault Database for Testing of Diagnostic and Prognostics Algorithms - Bearing Fault Dataset

- ##### External resources:
    - https://www.mfpt.org/fault-data-sets/
    - https://mfpt.org/wp-content/uploads/2018/03/MFPT-Bearing-Envelope-Analysis.pdf

#### Description:

- ##### Instantiation: ```MFPT(base_directory, folders)```
    - ```base_directory``` is the home directory of the extracted file.
    - ```folders``` is the list of folders to include; valid elements are *1 - Three Baseline Conditions*, *2 - Three Outer Race Fault Conditions*, *3 - Seven More Outer Race Fault Conditions* and *4 - Seven Inner Race Fault Conditions*.

- ##### Mining: ```MFPT.mine(mining_params)```
    - ```mining_params``` is a nested python dictonary whose keys are 97656 and 48828 (sampling frequencies the dataset is collected by) and the corresponding values are objects of python dictonary. Secondary dictonaries each have two keys: ```win_len``` and ```hop_len``` with correponding values.

- ##### Accessing data: ```MFPT.data```
    Mined data is presented as a python dictonary whose keys are 97656 and 48828. Corresponding values are lists of ```pd.DataFrame``` objects, belonging to the data files recorded to the corresponding sampling frequency.

#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, ZipDatasetDownloader
from damavand.damavand.datasets.digestors import MFPT

# Downloading the dataset
addresses = read_addresses()
downloader = ZipDatasetDownloader(addresses['MFPT'])
downloader.download_extract('MFPT.zip', 'MFPT/')

# Mining the dataset
mfpt = MFPT('MFPT/MFPT Fault Data Sets/', [
    '1 - Three Baseline Conditions',
    '2 - Three Outer Race Fault Conditions',
    '3 - Seven More Outer Race Fault Conditions',
    '4 - Seven Inner Race Fault Conditions',
])
mining_params = {
    97656: {'win_len': 16671, 'hop_len': 2000},
    48828: {'win_len': 8337, 'hop_len': 1000},
}
mfpt.mine(mining_params)
```

### ```CWRU```

#### A digestor to mine the bearing dataset by Case Western Reserve University (CWRU)

#### External resource:
https://engineering.case.edu/bearingdatacenter

#### Description:

- ##### Instantiation: ```CWRU(base_directory, channels)```
    - ```base_directory``` is the home directory of the downloaded files.
    - ```channels``` is a list of strings to include the desired measurement channels; 'FE' and 'DE' corresponding to fan-end acceleration, drive-end acceleration and base acceleration respectively, are available choices. Default value is ['FE', 'DE'].

- ##### Mining: ```CWRU.mine(mining_params, synchronous_only)```
    - ```mining_params``` is a nested python dictonary whose keys are '12K' and '48K' (sampling frequencies used to collect the dataset) and values are again python dictionaries whose keys are ```win_len``` and ```hop_len```.
    - ```synchronous_only``` is a boolean variable to be used as a flag; once this flag is set ```True```, only files which contain all the desired channels are mined and ones missing one of the channels are skipped. Default value is ```False```.

- ##### Accessing data: ```CWRU.data```
    Mined data is organized as a nested python dictonary whose keys are elements of the ```channels```; corresponding values again python dictionaries whose keys are the sampling frequencies; '12K' and '48K'.

#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, CwruDownloader
from damavand.damavand.datasets.digestors import CWRU

# Downloading the dataset
addresses = read_addresses()
downloader = CwruDownloader(addresses['CWRU'])
downloader.download('CWRU/')
while len(list(downloader.undownloaded.keys())) > 0:
  downloader.redownload()

# Mining the dataset
mining_params = {
    '12K': {'win_len': 12000, 'hop_len': 3000},
    '48K': {'win_len': 48000, 'hop_len': 16000},
}
cwru = CWRU('CWRU/')
cwru.mine(mining_params, synchronous_only = True)
```


### ```SEU```

#### A digestor to mine the gearbox dataset from Southeast University

- ##### Original title: **Gearbox dataset** from Highly Accurate Machine Fault Diagnosis Using Deep Transfer Learning

- ##### External resources:
    - https://ieeexplore.ieee.org/abstract/document/8432110
    - https://github.com/cathysiyu/Mechanical-datasets/tree/master/gearbox

#### Description

- ##### Instantiation: ```SEU(base_directory, channels)```
    - ```base_directory``` is the home directory of the downloaded files.
    - ```channels``` is a list of integers (from 0 to 7), corresponding to 8 accelerometers. Default value is [0, 1, 2, 3, 4, 5, 6, 7].

- ##### Mining: ```SEU.mine(mining_params)```
    - ```mining_params``` is a python dictonary whose keys are ```win_len``` and ```hop_len```. 

- ###### Accessing data: ```SEU.data```
    Mined data is organized as a python dictonary whose keys are elements of the ```channels```; corresponding values are lists of ```pd.DataFrame``` objects.

#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, ZipDatasetDownloader
from damavand.damavand.datasets.digestors import SEU

# Downloading the dataset
addresses = read_addresses()
downloader = ZipDatasetDownloader(addresses['SEU'])
downloader.download_extract('SEU.zip', 'SEU/')

# Mining the dataset
mining_params = {'win_len': 10000, 'hop_len': 10000}
seu = SEU('SEU/')
seu.mine(mining_params)
```

### ```MaFaulda```

#### A digestor to mine the Machinery Fault Database (MaFaulDa)

- #### Original title: Machinery Fault Database

- #### External resources:
    - https://www02.smt.ufrj.br/~offshore/mfs/page_01.html

#### Description:

- ##### Instantiation: ```MaFauldDa(base_directory, folders, channels)```
    - ```base_directory``` is the home directory of the extracted folders.
    - ```folders``` is a list to include folders of interest, during the mining process.
    - ```channels``` is a list of integers (from 0 to 7), corresponding to the tachometer, 3 accelerometers on the underhang bearing (axial, radial and tangential), 3 accelerometers on the overhang bearing (axial, radial and tangential) and a microphone.

- ##### Mining: ```MaFaulda.mine(mining_params)```
    - ```mining_params``` is a python dictonary whose keys are ```win_len``` and ```hop_len```. 

- ##### Accessing data: ```MaFaulda.data```
    Mined data is organized as a python dictonary whose keys are elements of the ```channels```; corresponding values are lists of ```pd.DataFrame``` objects.

#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, MaFaulDaDownloader
from damavand.damavand.datasets.digestors import MaFauldDa

# Downloading the dataset
addresses = read_addresses()
downloader = MaFaulDaDownloader({key: addresses['MaFaulDa'][key] for key in ['normal.zip', 'imbalance.zip']})
downloader.download_extract('mafaulda_zip_files/', 'mafaulda/')

# Mining the dataset (using only the third channel)
mafaulda = MaFauldDa('mafaulda/', os.listdir('mafaulda/'), channels = [2])
mining_params = {
    'win_len': 50000,
    'hop_len': 50000
}
mafaulda.mine(mining_params)
```

### ```MEUT```

#### A digestor to mine the dataset by Mehran University of Engineering & Technology

- ##### Original title: Triaxial bearing vibration dataset of induction motor under varying load conditions

- ##### External resources:
    - https://data.mendeley.com/datasets/fm6xzxnf36/2
    - https://www.sciencedirect.com/science/article/pii/S2352340922005170

#### Description:

- ##### Instantiation: ```MUET(base_directory, folders, channels)```
    - ```base_directory``` is the home directory of the extracted folders.
    - ```folders``` is the list of folders to include during the mining process.
    - ```channels```is the list of integers, corresponding to the triaxial acceleration signals; 1, 2 and 3 correspond to X-axis, Y-axis, and Z-axis. The default value is [1, 2, 3].

- ##### Mining: ```MUET.mine(mining_params)```
    - ```mining_params``` is a python dictonary whose keys are ```win_len``` and ```hop_len```. 

- ##### Accessing data: ```MUET.data```
    Mined data is organized as a python dictonary whose keys are elements of the ```channels```; corresponding values are lists of ```pd.DataFrame``` objects.

#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, ZipDatasetDownloader
from damavand.damavand.datasets.digestors import MUET

# Downloading the dataset
addresses = read_addresses()
downloader = ZipDatasetDownloader(addresses['MEUT'])
downloader.download_extract('MEUT.zip', 'MEUT/')

# Mining the dataset
dataset = MUET('MEUT/fm6xzxnf36-2/', os.listdir('MEUT/fm6xzxnf36-2/'), [3])
mining_params = {
    'win_len': 10000,
    'hop_len': 5000
}
dataset.mine(mining_params)
```

### ```UoO```

#### A digestor to mine the bearing dataset from University of Ottawa

- ##### Original title: Bearing vibration data collected under time-varying rotational speed conditions

- ##### External resources:
    - https://www.sciencedirect.com/science/article/pii/S2352340918314124
    - https://data.mendeley.com/datasets/v43hmbwxpm/1

#### Description:

- ##### Instantiation: ```UoO(base_directory, channels, reps)```
    - ```base_directory``` is the home directory of the extracted folders.
    - ```channels``` is a list of strings, specifying the desired channels; available choices are 'channel_1' and 'channel_2', corresponding to the acceleration and the rotational speed, respectively. The default value is ['channel_1', 'channel_2'].
    - ```reps``` is a list of integers that specifies the number of measurement repetitions (1, 2 and 3), to include. Default value is [1, 2, 3].

- ##### Mining: ```UoO.mine(mining_params)```
    - ```mining_params``` is a python dictonary whose keys are ```win_len``` and ```hop_len```. 

- ##### Accessing data: ```UoO.data```
    Mined data is organized as a python dictonary whose keys are elements of the ```channels```; corresponding values are lists of ```pd.DataFrame``` objects.

#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, ZipDatasetDownloader
from damavand.damavand.datasets.digestors import UoO

# Downloading the dataset
addresses = read_addresses()
downloader = ZipDatasetDownloader(addresses['UoO'])
downloader.download_extract('UoO.zip', 'UoO/')

# Mining the dataset
dataset = UoO('UoO/', ['Channel_1', 'Channel_2'], [1])
mining_params = {'win_len': 10000, 'hop_len': 10000}
dataset.mine(mining_params)
```

### ```PU```

#### A digestor to mine the bearing dataset by Paderborn University

- #### Original title: Condition Monitoring of Bearing Damage in Electromechanical Drive Systems by Using Motor Current Signals of Electric Motors: A Benchmark Data Set for Data-Driven Classification

- #### External resources:
    - https://www.papers.phmsociety.org/index.php/phme/article/view/1577
    - https://mb.uni-paderborn.de/kat/forschung/kat-datacenter/bearing-datacenter/data-sets-and-download

#### Description:

- ##### Instantiation: ```PU(base_directory, folders, channels, reps)```
    - ```base_directory``` is the home directory of the extracted folders.
    - ```folders``` is the list of the extracted folders, to include.
    - ```channels``` is the ist of strings, specifying the desired channels; available choices are 'CP1', 'CP2' and 'Vib' corresponding to the current phases (1 and 2) and acceleration. The default value is ['CP1', 'CP2', 'Vib'].
    - ```reps``` is a list of integers that specifies the number of repetitions (from 1 to 20), to include. The default value is [1, 2, 3, ... , 19, 20].

- ##### Mining: ```PU.mine(mining_params)```
    - ```mining_params``` is a python dictonary whose keys are ```win_len``` and ```hop_len```. 

##### Accessing data: ```PU.data```
    Mined data is organized as a python dictonary whose keys are elements of the ```channels```; corresponding values are lists of ```pd.DataFrame``` objects.

#### Usage example:

```Python
# Importings
from damavand.damavand.datasets.downloaders import read_addresses, PuDownloader
from damavand.damavand.datasets.digestors import PU

# Downloading the dataset
addresses = read_addresses()
addresses['PU'].pop('real_damage')
downloader = PuDownloader(addresses['PU'])
downloader.download_extract(download_path = 'PU_compressed/', extraction_path = 'PU/', timeout = 10)

#Mining the dataset
mining_params = {'win_len': 16000, 'hop_len': 16000}
pu = PU('PU/', os.listdir('PU/'), ['Vib'],reps = [1])
pu.mine(mining_params)
```