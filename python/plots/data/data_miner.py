__author__ = 'Rodrigo Bermudez Schettino'

import re



# Returns the value between both strings given in line if found
# Otherwise if no math was found, an empty string is returned
#
# Parameters:
#   line        
#   start_regex Regex to find starting point to trim line
#   end_regex  String up to which trim ends
#
# Returns:
#   value       Value between start_regex and end_regex
#
def extract_value_from_line(line, start_regex, end_regex):
  # Search for start string in line
  start_index = re.search(start_regex,line)

  # Return if nothing found
  if not(start_index):
    return False

  # Store index of final character in search match
  start_index = start_index.end()

  # Get index of end string in line
  # end_index = line.find(end_regex)
  end_index = re.search(end_regex,line).start()

  # Error handling if at least one string was not found
  if end_index == -1:
    return False

  return line[start_index:end_index]



# Parameters
#   data_file_path          Path to x264 log file
#   start_regex, end_regex  Parameters for extract_value_from_line
#   singleVal               Switch to return an array of values or
#                           first occurrence of search.
#
# Returns:
#   array of values or a single value if specified so
def get_values_from_file(data_file_path, start_regex, end_regex, singleVal=False):
  # Store the values as array only if specified so
  if not(singleVal):
    values_array = '['
    
  # Get lines of file
  with open(data_file_path) as data_file:
    # Loop through file lines
    for line in data_file:
      # Extract value using regex
      value = extract_value_from_line(line, start_regex, end_regex)
      if value:
        # If value was found stop searching
        if singleVal:
          break
        # Append a semmicolon to format the data in the array
        value        += ','
        # Store value in array
        values_array += value
  
  # Return a single value and not an array of values
  if singleVal:
    return eval(value)

  # Remove last semmicolon in order to close array
  last_semmicolon_index = values_array.rfind(',')
  values_array          = values_array[:last_semmicolon_index]
  # Close array
  values_array          += ']'

  # Convert string to array
  return eval(values_array)



def get_value_from_file(data_file_path, start_regex, end_regex):
  return get_values_from_file(data_file_path, start_regex, end_regex, singleVal=True)


# Sums up frames to segments in the x264 log 
# and adds segment bitrates to an array.
# Segments are recognized because they begin
# with an i-frame (GOP).
#
# Parameters
#   data_file_path Path to x264 log file
#   
# Returns:
#   array with bitrates kbps from segments in encoded video
def get_bitrate_from_segments(data_file_path, start_regex, end_regex, segment_duration_in_ms):
  # Initialize array
  bitrates_from_segments = []
  
  # Variable for counting bits in segment
  segment   = -1
  
  # Get lines of file
  with open(data_file_path) as data_file:

    # Loop through file lines
    for line in data_file:
      # Extract frame_size using regex
      frame_size = extract_value_from_line(line, start_regex, end_regex)
      # Get frame/slice type
      frame_type = extract_value_from_line(line, 'frame=.* Slice:',' Poc:')
      if frame_size:
        # Convert frame_size in bytes to bits
        frame_size   = eval(frame_size) * 8
        # Reset segment size when i-frame is found and
        # append segment size to bitrates array
        #
        # Ignore first loop when the segment variable
        # was not initialized yet
        if frame_type == 'I' and not(segment == -1):
          # Convert segment duration in milliseconds to seconds
          segment_duration_in_s = segment_duration_in_ms / float(1000)
          # Convert bits in segment's size to bits/second
          # Segment's duration in second is given as function argument
          segment = segment / float(segment_duration_in_s)
          # Convert from bps to kbps
          segment = segment / float(1000)
          # Append segment's bitrate to bitrates array
          bitrates_from_segments.append(segment)
          segment = 0

        # Initialize segment size properly
        if segment == -1:
          segment = 0

        # Add frame size to current segment
        segment += frame_size

  # Append last segment to bitrates array
  #
  # It has to be manually appended because 
  # the algorithm waits for the next i-frame
  # to append the segment to the array
  bitrates_from_segments.append(segment)

  return bitrates_from_segments


