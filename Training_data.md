#Load the audio file:
wav = audio.load_wav(wav_path)

#Compute linear-scale and mel-scale spectrograms (float32 numpy arrays):
spectrogram = audio.spectrogram(wav).astype(np.float32)
mel_spectrogram = audio.melspectrogram(wav).astype(np.float32)

#Save the spectrograms to disk:
np.save(os.path.join(out_dir, spectrogram_filename), spectrogram.T, allow_pickle=False)
np.save(os.path.join(out_dir, mel_spectrogram_filename), mel_spectrogram.T,  allow_pickle=False)

#If you're not sure which option to use, you can evaluate the transliteration cleaners like this:
from text import cleaners
cleaners.transliteration_cleaners('hi my name is akanksha')   # Replace with the text you want to try
