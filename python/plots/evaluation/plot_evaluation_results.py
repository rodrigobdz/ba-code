__author__ = 'Rodrigo Bermudez Schettino'

import sys
import settings
import pandas as pd
import matplotlib.pyplot as plt

nr_runs              = 5
adaptation_algorithm = 'lolypop'
lolypop_params       = {'sigma': 1, 'omega': 50}


def plot_delay():
  df = pd.read_csv(settings.delay_log)
  df = df[(df['omega'] == lolypop_params['omega']) & (df['sigma'] == lolypop_params['sigma'])]
  pdata = {'lolypop': []}
  data = df[(df['algo'] == adaptation_algorithm)]
  for i in range(nr_runs):
    d = data[(data['run_nr'] == (i+1))]
    pdata[adaptation_algorithm].append(d['delay'].mean())
  fig, ax = plt.subplots()
  plt.xlabel('Algorithm')
  plt.ylabel('delay (s)')
  plt.title('Average delay')
  plt.boxplot([pdata['lolypop']])
  ax.set_xticklabels(adaptation_algorithm, rotation=45)


if __name__ == '__main__':
  plot_delay()
  plt.show()
  sys.exit(0)