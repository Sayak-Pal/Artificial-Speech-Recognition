import wave
obj = wave.open("sayak.wav","rb")
print("Number of channels",obj.getnchannels())
print("sample width",obj.getsampwidth())
print("frame rate",obj.getframerate())
print("Number of Frames",obj.getnframes())
print("parameters",obj.getparams())

t_audio=obj.getnframes()/obj.getframerate()
print(t_audio)
frames = obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames))
obj.close()
obj_new=wave.open("sayak_new.wav","wb")
obj_new.setsampwidth(1)
obj_new.setnchannels(1)
obj_new.setframerate(8000.0)

obj_new.writeframes(frames)
obj_new.close()

      