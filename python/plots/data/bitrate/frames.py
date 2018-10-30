__author__ = 'Rodrigo Bermudez Schettino'

import helpers.settings as settings
import data.data_miner as data_miner

frame_bitrate_start_pattern = 'frame=.* size='
frame_bitrate_end_pattern   = ' bytes'

def get_frame_bitrate_values(segment_duration_in_ms, representation_id):
  return data_miner.get_bitrate_from_segments(data_file_path=settings.path_to_x264_log(segment_duration_in_ms, representation_id), 
                                              start_regex=frame_bitrate_start_pattern, 
                                              end_regex=frame_bitrate_end_pattern,
                                              segment_duration_in_ms=segment_duration_in_ms)

frames_250ms_240p_low_res = get_frame_bitrate_values(segment_duration_in_ms=250, representation_id=1)
frames_250ms_240p_180kbps = get_frame_bitrate_values(segment_duration_in_ms=250, representation_id=2)
frames_250ms_360p         = get_frame_bitrate_values(segment_duration_in_ms=250, representation_id=3)
frames_250ms_480p         = get_frame_bitrate_values(segment_duration_in_ms=250, representation_id=4)
frames_250ms_720p         = get_frame_bitrate_values(segment_duration_in_ms=250, representation_id=5)
frames_250ms_1080p        = get_frame_bitrate_values(segment_duration_in_ms=250, representation_id=6)
frames_250ms_1440p        = get_frame_bitrate_values(segment_duration_in_ms=250, representation_id=7)
frames_250ms_2160p        = get_frame_bitrate_values(segment_duration_in_ms=250, representation_id=8)
frames_250ms              = [frames_250ms_240p_low_res, frames_250ms_240p_180kbps, frames_250ms_360p, frames_250ms_480p, frames_250ms_720p, frames_250ms_1080p, frames_250ms_1440p, frames_250ms_2160p]

frames_500ms_240p_low_res = get_frame_bitrate_values(segment_duration_in_ms=500, representation_id=1)
frames_500ms_240p_180kbps = get_frame_bitrate_values(segment_duration_in_ms=500, representation_id=2)
frames_500ms_360p         = get_frame_bitrate_values(segment_duration_in_ms=500, representation_id=3)
frames_500ms_480p         = get_frame_bitrate_values(segment_duration_in_ms=500, representation_id=4)
frames_500ms_720p         = get_frame_bitrate_values(segment_duration_in_ms=500, representation_id=5)
frames_500ms_1080p        = get_frame_bitrate_values(segment_duration_in_ms=500, representation_id=6)
frames_500ms_1440p        = get_frame_bitrate_values(segment_duration_in_ms=500, representation_id=7)
frames_500ms_2160p        = get_frame_bitrate_values(segment_duration_in_ms=500, representation_id=8)
frames_500ms              = [frames_500ms_240p_low_res, frames_500ms_240p_180kbps, frames_500ms_360p, frames_500ms_480p, frames_500ms_720p, frames_500ms_1080p, frames_500ms_1440p, frames_500ms_2160p]

frames_750ms_240p_low_res = get_frame_bitrate_values(segment_duration_in_ms=750, representation_id=1)
frames_750ms_240p_180kbps = get_frame_bitrate_values(segment_duration_in_ms=750, representation_id=2)
frames_750ms_360p         = get_frame_bitrate_values(segment_duration_in_ms=750, representation_id=3)
frames_750ms_480p         = get_frame_bitrate_values(segment_duration_in_ms=750, representation_id=4)
frames_750ms_720p         = get_frame_bitrate_values(segment_duration_in_ms=750, representation_id=5)
frames_750ms_1080p        = get_frame_bitrate_values(segment_duration_in_ms=750, representation_id=6)
frames_750ms_1440p        = get_frame_bitrate_values(segment_duration_in_ms=750, representation_id=7)
frames_750ms_2160p        = get_frame_bitrate_values(segment_duration_in_ms=750, representation_id=8)
frames_750ms              = [frames_750ms_240p_low_res, frames_750ms_240p_180kbps, frames_750ms_360p, frames_750ms_480p, frames_750ms_720p, frames_750ms_1080p, frames_750ms_1440p, frames_750ms_2160p]

frames_1000ms_240p_low_res = get_frame_bitrate_values(segment_duration_in_ms=1000, representation_id=1)
frames_1000ms_240p_180kbps = get_frame_bitrate_values(segment_duration_in_ms=1000, representation_id=2)
frames_1000ms_360p         = get_frame_bitrate_values(segment_duration_in_ms=1000, representation_id=3)
frames_1000ms_480p         = get_frame_bitrate_values(segment_duration_in_ms=1000, representation_id=4)
frames_1000ms_720p         = get_frame_bitrate_values(segment_duration_in_ms=1000, representation_id=5)
frames_1000ms_1080p        = get_frame_bitrate_values(segment_duration_in_ms=1000, representation_id=6)
frames_1000ms_1440p        = get_frame_bitrate_values(segment_duration_in_ms=1000, representation_id=7)
frames_1000ms_2160p        = get_frame_bitrate_values(segment_duration_in_ms=1000, representation_id=8)
frames_1000ms              = [frames_1000ms_240p_low_res, frames_1000ms_240p_180kbps, frames_1000ms_360p, frames_1000ms_480p, frames_1000ms_720p, frames_1000ms_1080p, frames_1000ms_1440p, frames_1000ms_2160p]

frames_2000ms_240p_low_res = get_frame_bitrate_values(segment_duration_in_ms=2000, representation_id=1)
frames_2000ms_240p_180kbps = get_frame_bitrate_values(segment_duration_in_ms=2000, representation_id=2)
frames_2000ms_360p         = get_frame_bitrate_values(segment_duration_in_ms=2000, representation_id=3)
frames_2000ms_480p         = get_frame_bitrate_values(segment_duration_in_ms=2000, representation_id=4)
frames_2000ms_720p         = get_frame_bitrate_values(segment_duration_in_ms=2000, representation_id=5)
frames_2000ms_1080p        = get_frame_bitrate_values(segment_duration_in_ms=2000, representation_id=6)
frames_2000ms_1440p        = get_frame_bitrate_values(segment_duration_in_ms=2000, representation_id=7)
frames_2000ms_2160p        = get_frame_bitrate_values(segment_duration_in_ms=2000, representation_id=8)
frames_2000ms              = [frames_2000ms_240p_low_res, frames_2000ms_240p_180kbps, frames_2000ms_360p, frames_2000ms_480p, frames_2000ms_720p, frames_2000ms_1080p, frames_2000ms_1440p, frames_2000ms_2160p]
