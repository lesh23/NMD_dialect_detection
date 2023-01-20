# 주파수 시각화 코드

# 사용 패키지
import numpy as np
import matplotlib.pyplot as plt
import wave

# 파일 열기
file = wave.open('jejugrandma.wav', mode=None)

# 오디오파일 정보 확인
file
print('no of channels:', file.getnchannels())
print('sampling frequency:', file.getframerate())
print('sample width:', file.getsampwidth())
print('frames:', file.getnframes())

sample_freq = file.getframerate()
n_samples = file.getnframes()
n_channels = file.getnchannels()
t_audio = n_samples/sample_freq

signal_wave = file.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

l_channel = signal_array[0::2]
r_channel = signal_array[1::2]

times = np.linspace(0, n_samples/sample_freq, num=n_samples)

# 주파수 시각화
plt.figure(figsize=(15, 5))
plt.plot(times, l_channel)
plt.title('Channel')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()


