__author__     = 'Rodrigo Bermudez Schettino'

# Markers
default_marker = '--bo'
markers        = [default_marker, '--go', '--co', '--mo', '--yo', '--ko', '--ro', '--bs']

# Paths
root_path      = '/Users/Rodrigo/Desktop/Bachelorarbeit/'
plot_path      = root_path + 'thesis/figures/evaluation/' # Path were the plots should be saved
results_path   = root_path + 'evaluation/results/'

log_files_path = results_path + 'k=1/client side proxy/1477446886/'
# Files
delay_log      = log_files_path + 'delay_log.csv'
download_log   = log_files_path + 'download_log.csv'
throughput_log = log_files_path + 'throughput_log.csv'
skipped_log    = log_files_path + 'skipped.csv'
