import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("/Users/wesbroersen 1/Documents/Samples/rhythm-lab.com_amen_vol.1/WAV/cw_amen01_175.wav")
play_obj = wave_obj.play()
play_obj.wait_done()
