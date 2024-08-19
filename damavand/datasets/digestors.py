import numpy as np
import pandas as pd
import os
import scipy.io as sio
import gc
from damavand.damavand.utils import *

class KAIST:
  def __init__(self, base_directory, files, channels = list(range(4))):
    self.base_dir = base_directory
    self.files = files
    self.data = {key: [] for key in channels}

  def mine(self, mining_params):
    for file in self.files:
      file_name_split = file.split('_')

      if len(file_name_split) > 2:
        load = list(file_name_split[0])[0]
        state = file_name_split[1]
        severity = file_name_split[2].split('.')[0]
      else:
        load = list(file_name_split[0])[0]
        state = file_name_split[1].split('.')[0]
        severity = '-'

      mat_contents = sio.loadmat(self.base_dir + file)

      for key in self.data.keys():
        temp_df = splitter(mat_contents['Signal'][0][0][1][0][0][0][:, key], mining_params['win_len'], mining_params['hop_len'])
        temp_df['load'], temp_df['state'], temp_df['severity'] = load, state, severity
        self.data[key].append(temp_df)

class MFPT:
  def __init__(self, base_directory, folders):
    self.base_dir = base_directory
    self.folders = folders

    self.data = {
      97656: [],
      48828: [], 
    }

  def mine(self,mining_params):
    for folder in self.folders:
      for file in os.listdir(self.base_dir + folder + '/'):
        if file.split('.')[1] == 'mat':
          mat_data = sio.loadmat(self.base_dir + folder + '/' + file)
          if file.startswith('baseline'):
            Fs = mat_data['bearing'][0][0][0][0][0]
            load = mat_data['bearing'][0][0][2][0][0]
            rot_speed = mat_data['bearing'][0][0][3][0][0]
            state = 'Normal'
            temp_df = splitter(mat_data['bearing'][0][0][1].reshape(-1,), mining_params[Fs]['win_len'], mining_params[Fs]['hop_len'])
            temp_df['Fs'], temp_df['load'], temp_df['rot_speed'], temp_df['state'] = Fs, load, rot_speed, state
            self.data[Fs].append(temp_df)
          elif file.startswith('OuterRaceFault'):
            Fs = mat_data['bearing'][0][0][3][0][0]
            load =  mat_data['bearing'][0][0][1][0][0]
            rot_speed = mat_data['bearing'][0][0][0][0][0]
            state = 'OR'
            temp_df = splitter(mat_data['bearing'][0][0][2].reshape(-1,), mining_params[Fs]['win_len'], mining_params[Fs]['hop_len'])
            temp_df['Fs'], temp_df['load'], temp_df['rot_speed'], temp_df['state'] = Fs, load, rot_speed, state
            self.data[Fs].append(temp_df)
          elif file.startswith('InnerRaceFault'):
            Fs = mat_data['bearing'][0][0][3][0][0]
            load = mat_data['bearing'][0][0][1][0]
            rot_speed = mat_data['bearing'][0][0][0][0][0]
            state = 'IR'
            temp_df = splitter(mat_data['bearing'][0][0][2].reshape(-1,), mining_params[Fs]['win_len'], mining_params[Fs]['hop_len'])
            temp_df['Fs'], temp_df['load'], temp_df['rot_speed'], temp_df['state'] = Fs, load, rot_speed, state
            self.data[Fs].append(temp_df)



class CWRU:
  def __init__(self, base_directory, channels = ['FE', 'DE']):
    self.base_dir = base_directory
    self.channels = channels

    self.data = {channel:{Fs:[] for Fs in set([a.split('.')[0].split('_')[-1] for a in os.listdir(self.base_dir)])} for channel in self.channels}

  def mine(self, mining_params, synchronous_only = False):
    for file in os.listdir(self.base_dir):
      if file.endswith('.mat'):
        file_split = file.split('.mat')[0].split('_')
        if len(file_split) == 3:
          state = file_split[0]
          rot_speed = file_split[1]
          Fs = file_split[2]
          severity = '-'
          defected_bearing = '-'
        else:
          defected_bearing = file_split[0]
          state = file_split[1]
          severity = file_split[2]
          rot_speed = file_split[3]
          Fs = file_split[4]

        mat_data = sio.loadmat(self.base_dir + file)
        available_channels = {key.split('_')[1]: key  for key in mat_data.keys() if key.split('_')[-1] == 'time'}
        if synchronous_only == True:
          if set(available_channels.keys()) >= set(self.channels):
            for channel in self.channels:
              if channel in available_channels.keys():
                temp_df = splitter(mat_data[available_channels[channel]].reshape((-1)), mining_params[Fs]['win_len'], mining_params[Fs]['hop_len'])
                temp_df['state'], temp_df['defected_bearing'], temp_df['severity'], temp_df['rot_speed'], temp_df['Fs'] = state, defected_bearing, severity, rot_speed, Fs
                self.data[channel][Fs].append(temp_df)
        else:
          for channel in self.channels:
            if channel in available_channels.keys():
              temp_df = splitter(mat_data[available_channels[channel]].reshape((-1)), mining_params[Fs]['win_len'], mining_params[Fs]['hop_len'])
              temp_df['state'], temp_df['defected_bearing'], temp_df['severity'], temp_df['rot_speed'], temp_df['Fs'] = state, defected_bearing, severity, rot_speed, Fs
              self.data[channel][Fs].append(temp_df)

class SEU:
  def __init__(self, base_directory, channels = list(range(8))):
    self.base_dir = base_directory
    self.channels = channels

    self.data = {key:[] for key in self.channels}

  def mine(self, mining_params):
    for sub_directory in os.listdir(self.base_dir):
      for file in os.listdir(self.base_dir + sub_directory):
        if file.endswith('.csv'):
          file_split = file.split('.csv')[0].split('_')
          test_bed = sub_directory
          state = file_split[0]
          rot_speed = file_split[1]
          with open('SEU/' + sub_directory + '/' + file, 'r', encoding='gb18030', errors='ignore') as f:
            content=f.readlines()
            if file == "ball_20_0.csv":
              arr = np.array([i.split(',')[:-1] for i in content[16:]]).astype(float)
            else:
              arr = np.array([i.split('\t')[:-1] for i in content[16:]]).astype(float)

          print('Mining: ', file)
          for key in self.data.keys():
            temp_df = splitter(arr[:, key], mining_params['win_len'], mining_params['hop_len'])
            temp_df['test_bed'] = test_bed
            temp_df['state'] = state
            temp_df['rot_speed'] = rot_speed
            self.data[key].append(temp_df)
            gc.collect()


class MaFauldDa:
  def __init__(self, base_directory, folders, channels = list(range(8))):
    self.base_dir = base_directory
    self.folders = folders
    self.channels = channels

    self.data = {key: [] for key in self.channels}

  def mine(self, mining_params):
    for folder in self.folders:
      if folder == 'normal':
        state = 'normal'
        sev = '_'
        for file in os.listdir(self.base_dir + folder):
          df = pd.read_csv(self.base_dir + folder + '/' +  file, header = None)
          for key in self.data.keys():
            temp_df = splitter(df[key].values, mining_params['win_len'], mining_params['hop_len'])
            temp_df['state'] = state
            temp_df['severity'] = sev
            self.data[key].append(temp_df)

      elif folder in ['underhang', 'overhang']:
        for subfolder in os.listdir(self.base_dir + folder + '/'):
          state = folder + '_' + subfolder
          for sev in os.listdir(self.base_dir + folder + '/' + subfolder + '/'):
            for file in os.listdir(self.base_dir + folder + '/' + subfolder + '/' + sev + '/'):
              df = pd.read_csv(self.base_dir + folder + '/' + subfolder + '/' + sev + '/' + file, header = None)
              for key in self.data.keys():
                temp_df = splitter(df[key].values, mining_params['win_len'], mining_params['hop_len'])
                temp_df['state'] = state
                temp_df['severity'] = sev
                self.data[key].append(temp_df)
      
      else:
        state = folder
        for sev in os.listdir(self.base_dir + folder + '/'):
          for file in os.listdir(self.base_dir + folder + '/' + sev):
            df = pd.read_csv(self.base_dir + folder + '/' + sev + '/' + file, header = None)
            for key in self.data.keys():
              temp_df = splitter(df[key].values, mining_params['win_len'], mining_params['hop_len'])
              temp_df['state'] = state
              temp_df['severity'] = sev
              self.data[key].append(temp_df)

class MUET():
  def __init__(self, base_directory, folders, channels = list(range(1,4))):
    self.base_dir = base_directory
    self.channels = channels
    self.folders = folders

    self.data = {key: [] for key in self.channels}

  def mine(self, mining_params):
    for folder in self.folders:
      if folder.startswith('Healthy'):
        state = 'healthy'
        severity = '-'
        for file in os.listdir(self.base_dir + folder + '/'):
          if file.endswith('.csv'):
            load = file.split(' ')[1] + ' ' + file.split(' ')[1].split('.')[0]
            df = pd.read_csv(self.base_dir + folder + '/' + file)
            for i in self.data.keys():
              temp_df = splitter(df.iloc[:, i].to_numpy(), mining_params['win_len'], mining_params['hop_len'])
              temp_df['state'], temp_df['severity'], temp_df['load'] = state, severity, load
              self.data[i].append(temp_df)
      else:
        for file in os.listdir(self.base_dir + folder + '/'):
          if file.endswith('.csv'):
            df = pd.read_csv(self.base_dir + folder + '/' + file)
            for i in self.data.keys():
              temp_df = splitter(df.iloc[:, i].to_numpy(), mining_params['win_len'], mining_params['hop_len'])
              severity = folder.split('-')[0]
              state =''.join(list(file.split('-')[0])[3:])
              load = file.split('-')[1].split('.')[0]
              temp_df['state'], temp_df['severity'], temp_df['load'] = state, severity, load
              self.data[i].append(temp_df)

class UoO():
  def __init__(self, base_directory, channels = ['Channel_1', 'Channel_2'], reps = list(range(1,4))):
    self.base_dir = base_directory
    self.channels = channels
    self.reps = reps

    self.data = {key: [] for key in self.channels}

  def mine(self, mining_params):
    for file in os.listdir(self.base_dir):
      if file.endswith('.mat'):
        rep = int(file.split('.')[0].split('-')[-1])
        if rep in self.reps:
          state = file.split('.')[0].split('-')[:-1][0]
          loading = file.split('.')[0].split('-')[:-1][1]
          mat_data = sio.loadmat(self.base_dir + file)
          for channel in self.data.keys():
            temp_df = splitter(mat_data[channel].reshape((-1)), mining_params['win_len'], mining_params['hop_len'])
            temp_df['state'], temp_df['loading'], temp_df['rep'] = state, loading, rep
            self.data[channel].append(temp_df)


class PU():
  def __init__(self, base_directory, folders, channels = ['CP1', 'CP2', 'Vib'], reps = list(range(1, 21))):
    self.base_dir = base_directory
    self.folders = folders
    self.channels = channels
    self.reps = reps
    self.data = {key: [] for key in self.channels}

  def mine(self, mining_params):
    self.corrupted_files = {}
    for folder in self.folders:
      for file in os.listdir(self.base_directory + folder):
        if file.endswith('.mat'):
          if int(file.split('.')[0].split('_')[-1]) in self.reps:
            rot_speed, load_torque, radial_force, code, rep = file.split('.')[0].split('_')
            try:
              mat_data = sio.loadmat(self.base_directory + folder + '/' + file)

              if 'CP1' in self.channels:
                temp_df = splitter(mat_data[file.split('.')[0]]['Y'][0][0][0][1][2].reshape((-1)), mining_params['win_len'], mining_params['hop_len'])
                temp_df['rot_speed'] = rot_speed
                temp_df['load_torque'] = load_torque
                temp_df['radial_force'] = radial_force
                temp_df['code'] = code
                temp_df['rep'] = rep
                self.data['CP1'].append(temp_df)

              if 'CP2' in self.channels:
                temp_df = splitter(mat_data[file.split('.')[0]]['Y'][0][0][0][2][2].reshape((-1)), mining_params['win_len'], mining_params['hop_len'])
                temp_df['rot_speed'] = rot_speed
                temp_df['load_torque'] = load_torque
                temp_df['radial_force'] = radial_force
                temp_df['code'] = code
                temp_df['rep'] = rep
                self.data['CP2'].append(temp_df)

              if 'Vib' in self.channels:
                temp_df = splitter(mat_data[file.split('.')[0]]['Y'][0][0][0][6][2].reshape((-1)), mining_params['win_len'], mining_params['hop_len'])
                temp_df['rot_speed'] = rot_speed
                temp_df['load_torque'] = load_torque
                temp_df['radial_force'] = radial_force
                temp_df['code'] = code
                temp_df['rep'] = rep
                self.data['Vib'].append(temp_df)
            except Exception as e:
              self.corrupted_files[self.base_directory + folder + '/' + file] = e

