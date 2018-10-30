__author__ = 'Rodrigo Bermudez Schettino'

import helpers.settings as settings
import data.data_miner as data_miner

def get_avg_bitrate(segment_duration_in_ms, representation_id):
  return data_miner.get_value_from_file(data_file_path=settings.path_to_x264_log(segment_duration_in_ms, representation_id), 
                                        start_regex='encoded.*fps, ', 
                                        end_regex=' kb/s')

avg_250ms_240p_low_res   = get_avg_bitrate(segment_duration_in_ms=250, representation_id=1)
avg_250ms_240p_180kbps   = get_avg_bitrate(segment_duration_in_ms=250, representation_id=2)
avg_250ms_360p           = get_avg_bitrate(segment_duration_in_ms=250, representation_id=3)
avg_250ms_480p           = get_avg_bitrate(segment_duration_in_ms=250, representation_id=4)
avg_250ms_720p           = get_avg_bitrate(segment_duration_in_ms=250, representation_id=5)
avg_250ms_1080p          = get_avg_bitrate(segment_duration_in_ms=250, representation_id=6)
avg_250ms_1440p          = get_avg_bitrate(segment_duration_in_ms=250, representation_id=7)
avg_250ms_2160p          = get_avg_bitrate(segment_duration_in_ms=250, representation_id=8)
avg_250ms                = [avg_250ms_240p_low_res, avg_250ms_240p_180kbps, avg_250ms_360p, avg_250ms_480p, avg_250ms_720p, avg_250ms_1080p, avg_250ms_1440p, avg_250ms_2160p]

avg_500ms_240p_low_res   = get_avg_bitrate(segment_duration_in_ms=500, representation_id=1)
avg_500ms_240p_180kbps   = get_avg_bitrate(segment_duration_in_ms=500, representation_id=2)
avg_500ms_360p           = get_avg_bitrate(segment_duration_in_ms=500, representation_id=3)
avg_500ms_480p           = get_avg_bitrate(segment_duration_in_ms=500, representation_id=4)
avg_500ms_720p           = get_avg_bitrate(segment_duration_in_ms=500, representation_id=5)
avg_500ms_1080p          = get_avg_bitrate(segment_duration_in_ms=500, representation_id=6)
avg_500ms_1440p          = get_avg_bitrate(segment_duration_in_ms=500, representation_id=7)
avg_500ms_2160p          = get_avg_bitrate(segment_duration_in_ms=500, representation_id=8)
avg_500ms                = [avg_500ms_240p_low_res, avg_500ms_240p_180kbps, avg_500ms_360p, avg_500ms_480p, avg_500ms_720p, avg_500ms_1080p, avg_500ms_1440p, avg_500ms_2160p]

avg_750ms_240p_low_res   = get_avg_bitrate(segment_duration_in_ms=750, representation_id=1)
avg_750ms_240p_180kbps   = get_avg_bitrate(segment_duration_in_ms=750, representation_id=2)
avg_750ms_360p           = get_avg_bitrate(segment_duration_in_ms=750, representation_id=3)
avg_750ms_480p           = get_avg_bitrate(segment_duration_in_ms=750, representation_id=4)
avg_750ms_720p           = get_avg_bitrate(segment_duration_in_ms=750, representation_id=5)
avg_750ms_1080p          = get_avg_bitrate(segment_duration_in_ms=750, representation_id=6)
avg_750ms_1440p          = get_avg_bitrate(segment_duration_in_ms=750, representation_id=7)
avg_750ms_2160p          = get_avg_bitrate(segment_duration_in_ms=750, representation_id=8)
avg_750ms                = [avg_750ms_240p_low_res, avg_750ms_240p_180kbps, avg_750ms_360p, avg_750ms_480p, avg_750ms_720p, avg_750ms_1080p, avg_750ms_1440p, avg_750ms_2160p]

avg_1000ms_240p_low_res  = get_avg_bitrate(segment_duration_in_ms=1000, representation_id=1)
avg_1000ms_240p_180kbps  = get_avg_bitrate(segment_duration_in_ms=1000, representation_id=2)
avg_1000ms_360p          = get_avg_bitrate(segment_duration_in_ms=1000, representation_id=3)
avg_1000ms_480p          = get_avg_bitrate(segment_duration_in_ms=1000, representation_id=4)
avg_1000ms_720p          = get_avg_bitrate(segment_duration_in_ms=1000, representation_id=5)
avg_1000ms_1080p         = get_avg_bitrate(segment_duration_in_ms=1000, representation_id=6)
avg_1000ms_1440p         = get_avg_bitrate(segment_duration_in_ms=1000, representation_id=7)
avg_1000ms_2160p         = get_avg_bitrate(segment_duration_in_ms=1000, representation_id=8)
avg_1000ms               = [avg_1000ms_240p_low_res, avg_1000ms_240p_180kbps, avg_1000ms_360p, avg_1000ms_480p, avg_1000ms_720p, avg_1000ms_1080p, avg_1000ms_1440p, avg_1000ms_2160p]

avg_2000ms_240p_low_res  = get_avg_bitrate(segment_duration_in_ms=2000, representation_id=1)
avg_2000ms_240p_180kbps  = get_avg_bitrate(segment_duration_in_ms=2000, representation_id=2)
avg_2000ms_360p          = get_avg_bitrate(segment_duration_in_ms=2000, representation_id=3)
avg_2000ms_480p          = get_avg_bitrate(segment_duration_in_ms=2000, representation_id=4)
avg_2000ms_720p          = get_avg_bitrate(segment_duration_in_ms=2000, representation_id=5)
avg_2000ms_1080p         = get_avg_bitrate(segment_duration_in_ms=2000, representation_id=6)
avg_2000ms_1440p         = get_avg_bitrate(segment_duration_in_ms=2000, representation_id=7)
avg_2000ms_2160p         = get_avg_bitrate(segment_duration_in_ms=2000, representation_id=8)
avg_2000ms               = [avg_2000ms_240p_low_res, avg_2000ms_240p_180kbps, avg_2000ms_360p, avg_2000ms_480p, avg_2000ms_720p, avg_2000ms_1080p, avg_2000ms_1440p, avg_2000ms_2160p]

avg_240p_low_res         = [avg_250ms_240p_low_res, avg_500ms_240p_low_res, avg_750ms_240p_low_res, avg_1000ms_240p_low_res,  avg_2000ms_240p_low_res]
avg_240p_180kbps         = [avg_250ms_240p_180kbps, avg_500ms_240p_180kbps, avg_750ms_240p_180kbps, avg_1000ms_240p_180kbps,  avg_2000ms_240p_180kbps]
avg_360p                 = [avg_250ms_360p,         avg_500ms_360p,         avg_750ms_360p,         avg_1000ms_360p,          avg_2000ms_360p]
avg_480p                 = [avg_250ms_480p,         avg_500ms_480p,         avg_750ms_480p,         avg_1000ms_480p,          avg_2000ms_480p]
avg_720p                 = [avg_250ms_720p,         avg_500ms_720p,         avg_750ms_720p,         avg_1000ms_720p,          avg_2000ms_720p]
avg_1080p                = [avg_250ms_1080p,        avg_500ms_1080p,        avg_750ms_1080p,        avg_1000ms_1080p,         avg_2000ms_1080p]
avg_1440p                = [avg_250ms_1440p,        avg_500ms_1440p,        avg_750ms_1440p,        avg_1000ms_1440p,         avg_2000ms_1440p]
avg_2160p                = [avg_250ms_2160p,        avg_500ms_2160p,        avg_750ms_2160p,        avg_1000ms_2160p,         avg_2000ms_2160p]

avg_of_all_representations_in_each_segment_duration = [avg_240p_low_res, avg_240p_180kbps, avg_360p, avg_480p, avg_720p, avg_1080p, avg_1440p, avg_2160p]
