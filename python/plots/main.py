__author__ = 'Rodrigo Bermudez Schettino'

# Data imports
# PSNR data
import data.psnr.average as avg_psnr_data
import data.psnr.frames as frames_psnr_data
# Bitrate data
import data.bitrate.average as avg_bitrate_data
import data.bitrate.frames as frames_bitrate_data
# Helper imports
import helpers.psnr_plotter as psnr_plotter
import helpers.bitrate_plotter as bitrate_plotter

# Average psnr values in each segment size
psnr_plotter.psnr_of_representations_in_segment_duration(segment_duration_in_ms= '250ms', data= avg_psnr_data.avg_250ms)
psnr_plotter.psnr_of_representations_in_segment_duration(segment_duration_in_ms= '500ms', data= avg_psnr_data.avg_500ms)
psnr_plotter.psnr_of_representations_in_segment_duration(segment_duration_in_ms= '750ms', data= avg_psnr_data.avg_750ms)
psnr_plotter.psnr_of_representations_in_segment_duration(segment_duration_in_ms= '1000ms', data= avg_psnr_data.avg_1000ms)
psnr_plotter.psnr_of_representations_in_segment_duration(segment_duration_in_ms= '2000ms', data= avg_psnr_data.avg_2000ms)

# Average values in all segment sizes and all representations
psnr_plotter.psnr_of_segment_durations_in_representations(data= avg_psnr_data.avg_of_all_representations_in_each_segment_duration)

# Boxplots of psnr per frame
psnr_plotter.boxplot_frame_psnr(segment_duration_in_ms= '250ms', data= frames_psnr_data.frames_250ms)
psnr_plotter.boxplot_frame_psnr(segment_duration_in_ms= '500ms', data= frames_psnr_data.frames_500ms)
psnr_plotter.boxplot_frame_psnr(segment_duration_in_ms= '750ms', data= frames_psnr_data.frames_750ms)
psnr_plotter.boxplot_frame_psnr(segment_duration_in_ms= '1000ms', data= frames_psnr_data.frames_1000ms)
psnr_plotter.boxplot_frame_psnr(segment_duration_in_ms= '2000ms', data= frames_psnr_data.frames_2000ms)

# Average bitrates in each segment size
bitrate_plotter.bitrate_of_representations_in_segment_duration(segment_duration_in_ms= '250ms', data= avg_bitrate_data.avg_250ms)
bitrate_plotter.bitrate_of_representations_in_segment_duration(segment_duration_in_ms= '500ms', data= avg_bitrate_data.avg_500ms)
bitrate_plotter.bitrate_of_representations_in_segment_duration(segment_duration_in_ms= '750ms', data= avg_bitrate_data.avg_750ms)
bitrate_plotter.bitrate_of_representations_in_segment_duration(segment_duration_in_ms= '1000ms', data= avg_bitrate_data.avg_1000ms)
bitrate_plotter.bitrate_of_representations_in_segment_duration(segment_duration_in_ms= '2000ms', data= avg_bitrate_data.avg_2000ms)

# Average bitrates in all segment sizes and all representations
bitrate_plotter.bitrate_of_segment_durations_in_representations(data= avg_bitrate_data.avg_of_all_representations_in_each_segment_duration)

# Boxplots of bitrates per frame
bitrate_plotter.boxplot_frame_bitrate(segment_duration_in_ms= '250ms', data= frames_bitrate_data.frames_250ms)
bitrate_plotter.boxplot_frame_bitrate(segment_duration_in_ms= '500ms', data= frames_bitrate_data.frames_500ms)
bitrate_plotter.boxplot_frame_bitrate(segment_duration_in_ms= '750ms', data= frames_bitrate_data.frames_750ms)
bitrate_plotter.boxplot_frame_bitrate(segment_duration_in_ms= '1000ms', data= frames_bitrate_data.frames_1000ms)
bitrate_plotter.boxplot_frame_bitrate(segment_duration_in_ms= '2000ms', data= frames_bitrate_data.frames_2000ms)
