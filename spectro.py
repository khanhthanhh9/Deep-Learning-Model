import matplotlib.pyplot as plt
import wave

import pylab
import glob

allWavFile = glob.glob("*.wav")
allPicFile = glob.glob("*.png")

WavName = [i.rsplit(".",1)[0] for i in allWavFile]
PicName = [i.rsplit(".",1)[0] for i in allPicFile]

diff = [item for item in WavName if item not in PicName]
# for i in diff:
#     print(i)
def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    plt.axis('off') #hide axis
    # pylab.title('spectrogram of %r' % wav_file)
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig(f'{wav_file.rsplit(".",1)[0]}.png')
    plt.cla()
    plt.close('all')
def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.frombuffer(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

for file in diff:
    graph_spectrogram(f'{file}.wav')