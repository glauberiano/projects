library(plyr)
library(tuneR)
library(seewave)

segment_audio_files <- function(out_path, interval = 30, min_secs = 0, discard_small_audio_files = FALSE,
								cut_audio_start = FALSE) {
								
	in_path <- choose.dir()
	out_path <- paste0(in_path, "\\", out_path
	
	if(dir.exists(out_path) == FALSE {
		dir.create(out_path)
	}
	file_names <- list.files(in_path)
	file_names <- filter(function(f) endswith(f, ".wav"), file_names
	
	for (file_name in file_names) {
		file_path <- file.path(in_path, file_name)
		audio <- readWave(file_path)
		audio_name <- substr(file_name, 1, nchar(file_name)-4)
		freq <- audio@samp.rate
		audio_length <- length(audio)
		seconds <- audio_length / freq
		
		if(seconds <= interval){
			if(discard_small_audio_files ) {
				next
			}
			else {
				small_audio_name <- sprintf("%s_%d.wav", audio_name, round(seconds))
				savewav(audio, file_name=file.path(out_path, small_audio_name))
			}
		} else {
		
			if(cut_audio_start) {
				sliced_audio <- audio[(interval*freq):audio_length]
			} else {
				sliced_audio <- audio[(audio_length - interval*freq):audio_length]
			}
			
			sliced_audio_name <- sprintf("%s_%d.wav", audio_name, interval)
			savewav(audio, file_name=file.path(out_path, sliced_audio_name))
		}
	}
}

segment_audio_files()