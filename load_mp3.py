from pydub import AudioSegment

audio = AudioSegment.from_wav("sayak.wav")

audio = audio +6
audio = audio*2

audio = audio.fade_in(20000)
audio.export("mashup.mp3", format="wav")

audio2= AudioSegment.from_wav("mashup.mp3")
print("done")
