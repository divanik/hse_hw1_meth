# Мой код приведен в ноутбуке, но просили выделить отдельно - мне не трудно

def draw_hist(name):
  import numpy as np
  import matplotlib.pyplot as plt
  file_name = f's_{name}.deduplicated.bismark.cov'
  with open(file_name, 'r') as file:
    lines = file.readlines()
  data = np.empty(len(lines))
  print(data.shape)
  for idx, line in enumerate(lines):
    if idx % 100000 == 99999:
      print(idx / 100000)
    _, _, _, num, _, _ = line.split()
    data[idx] = float(num)
  print(data)
  fig, ax = plt.subplots(1, 1)
  fig.set_size_inches(18, 14)
  ax.hist(data, bins=20)

  draw_hist('8cell')

  draw_hist('icm')

  draw_hist('epiblast')