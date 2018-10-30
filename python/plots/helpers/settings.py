__author__ = 'Rodrigo Bermudez Schettino'

# Figure paths
figures_directory_path         = '/Users/Rodrigo/Desktop/Bachelorarbeit/thesis/figures/'
psnr_figures_directory_path    = figures_directory_path + 'psnr/'
bitrate_figures_directory_path = figures_directory_path + 'bitrate/'
# Other paths
tkn_directory_path             = '/Users/Rodrigo/Desktop/.tkn-mounting-point/'
sintel_path                    = tkn_directory_path + 'sintel/'
representation_paths           = ['240p_low_res', '240p/240p_180kbps', '360p', '480p', '720p', '1080p', '1440p', '2160p']
psnr_log_file_name             = 'psnr.txt'
figures_file_extension         = '.png'

# Labels
segment_duration_label         = 'Segment duration in ms'
representation_id_label        = 'Representation ID'

# Encoding configurations
segment_durations_in_ms        = [250, 500, 750, 1000, 2000]
representations                =  ['240p low res', '240p', '360p', '480p', '720p', '1080p', '1440p', '2160p']

# Markers
default_marker                 = '--bo'
markers                        = [default_marker, '--go', '--co', '--mo', '--yo', '--ko', '--ro', '--bs']

# Downcases first letter of string
downcase_first_letter          = lambda s: s[:1].lower() + s[1:] if s else ''

# Returns the full path to the psnr log file 
# from the video encoding
def path_to_x264_log(segment_duration_in_ms, representation_id):
  return sintel_path+str(segment_duration_in_ms)+'ms/'+representation_paths[representation_id-1]+'/'+psnr_log_file_name
