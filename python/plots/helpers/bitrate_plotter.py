__author__ = 'Rodrigo Bermudez Schettino'

import matplotlib.pyplot as plt
import numpy as np
import settings

bitrate_title_prefix     = 'Bitrate of Sintel movie '
avg_bitrate_title_prefix = 'Average ' + settings.downcase_first_letter(bitrate_title_prefix)
bitrate_label            = 'Bitrate in kbps'

def bitrate_of_representations_in_segment_duration(segment_duration_in_ms, data):
	# Create a new canvas for this plot
	plt.figure()
	# Set title and labels in plot
	plt.title(avg_bitrate_title_prefix + '(' + segment_duration_in_ms + ')')
	plt.ylabel(bitrate_label)
	plt.xlabel(settings.representation_id_label)
	x_start = 0
	x_end   = len(data)+1
	# Set axis scales
	plt.xlim(x_start, x_end)
	# Set labels for x axis
	plt.xticks(np.arange(1,len(data)+1), np.arange(1,len(data)+1))
	plt.yscale('log')
	plt.grid(True)

	# Plot data
	plt.plot(np.arange(1,len(data)+1),data, settings.default_marker)
	# Save figure to system
	plt.savefig(settings.bitrate_figures_directory_path + 'avg_' + segment_duration_in_ms +  '_bitrate' + settings.figures_file_extension)
	# Close current figure
	plt.close()

def bitrate_of_segment_durations_in_representations(data):
	# Get dimensions of data matrix
	# Create a numpy array to achieve this
	data              = np.array(data)
	number_of_rows    = data.shape[0]
	number_of_columns = data.shape[1]
	# Create a new canvas for this plot
	plt.figure()
	# Set title and labels in plot
	plt.title(avg_bitrate_title_prefix + 'representations')
	plt.ylabel(bitrate_label)
	plt.xlabel(settings.segment_duration_label)
	x_start = 0
	x_end   = 2100
	# Set axis scales
	plt.xlim(x_start, x_end)
	plt.yscale('log')
	# Set labels for x axis
	plt.xticks(settings.segment_durations_in_ms, settings.segment_durations_in_ms)
	plt.grid(True)

	# Loop through data elements which are arrays
	for row in range(number_of_rows):
		# Create a new subgraph
		plt.subplot()
		# Plot data
		plt.plot(settings.segment_durations_in_ms,data[row,:], settings.markers[row], label=settings.representations[row])
		# Place a legend to the right of the figure
		plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	# Save figure to system
	# Tight to save figure with legend outside of the box
	plt.savefig(settings.bitrate_figures_directory_path + 'avg_bitrate' + settings.figures_file_extension, bbox_inches='tight')
	# Close current figure
	plt.close()

def boxplot_frame_bitrate(segment_duration_in_ms, data):
	# Create a new canvas for this plot
	plt.figure()
	# Set title and labels in plot
	plt.title(bitrate_title_prefix + 'segments ' + '(' + segment_duration_in_ms + ')')
	plt.ylabel(bitrate_label)
	plt.xlabel(settings.representation_id_label)
	plt.grid(True)
	# Set logarithmic axis
	plt.yscale('log')

	# Boxplot with whiskers of [5,95]
	# whis*0,5
	# 1,8*0,5 = 90%
	# Found on http://stackoverflow.com/a/17726418/2227405
	plt.boxplot(data, whis=1.8)
	plt.savefig(settings.bitrate_figures_directory_path + 'frames_psnr_' + segment_duration_in_ms + settings.figures_file_extension)
	# Close current figure
	plt.close()
