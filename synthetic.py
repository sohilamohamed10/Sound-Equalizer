import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import wavio


sampleRate = 2000
frequency =[100,200,300,400,500,600,700,800,900,1000]
duration = 1
y=np.zeros(1*sampleRate)
t = np.linspace(0, 1, sampleRate * duration)  #  Produces a 5 second Audio-File
for f in frequency:
	y += np.sin(f * 2 * np.pi*t )  #  Has frequency of 440Hz
plt.plot(t,y)
plt.show()
wavio.write("sound.wav",y,sampleRate,sampwidth=1)
