# 오디오 파일을 텍스트로 변환하는 코드

# 사용 패키지
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

# wav 파일을 열어서 청크 자르기
r = sr.Recognizer()
sound_file = AudioSegment.from_wav(r'wavfile.wav')
audio_chunks = split_on_silence(sound_file, 
    min_silence_len=500,
    silence_thresh=-40
)

len(audio_chunks)

# 청크 파일 저장
for i, chunk in enumerate(audio_chunks):

    out_file = "C:/Users/Desktop/chunkfiles/chunk{0}.wav".format(i)
    print("exporting", out_file)
    chunk.export(out_file, format="wav")

# 청크 파일 열기
test = sr.AudioFile(r'C:\Users\Desktop\chunkfiles\chunk1.wav')
type(test)

# wav 파일을 오디오데이터로 변환
recognizer = sr.Recognizer()
with test as source:
    audiodata = recognizer.record(test)
type(audiodata)

# 구글정보 가져오기
test_audio = r.recognize_google(audiodata, language="ko-KR") 

# 텍스트로 변환한 결과
print("Your speech thinks like\n " + test_audio)      

