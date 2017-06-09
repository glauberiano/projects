from pylab import *
from scipy.io import wavfile
import malplotlib.pyplot as plt

class audioCharacterization:

	def __init__(self, audioPath):
		self.frequency, self.pressureintensity = wavfile.read(audioPath)
		self.SampleLength = self.pressureIntensity.shape[0]
		self.duration = self.SampleLength / self.frequency
		self.fastFourierTransform = fft(self.pressureIntensity)
		timeArray = timeArray / self.frequency
		self.timeArray = timeArray
		
	def plotTone(self):
		plt.plot(self.timeArray, self.pressureIntensity, color='k')
		ylabel('Amplitude')
		xlabel('Time (s)')
		
	def plotToneSpectrum(self):
		frequencyMagnitude = abs(self.fastFourierTransform)
		frequencyMagnitude = frequencyMagnitude / float(self.SampleLength)
		frequencyMagnitude = frequencyMagnitude ** 2
		
		if (self.SampleLength % 2 > 0):
			frequencyMagnitude[1:len(frequencyMagnitude)] = frequencyMagnitude[1:len(frequencyMagnitude)] * 2
		else:
			frequencyMagnitude[1:len(frequencyMagnitude)-1] = frequencyMagnitude[1:len(frequencyMagnitude)-1] * 2
			
		freqArray = arange(0, self.SampleLength, 1.0) * (self.frequency / self.SampleLength)
		plt.plot(freqArray/1000, 10*log10(frequencyMagnitude), color='k')
		xlabel('Frequency (Hz)')
		ylabel('Power (dB)')
