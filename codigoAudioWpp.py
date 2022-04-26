from gtts import gTTS
from playsound import playsound

audio="audio.mp3"
lingua="pt-br"

sp = gTTS(
  text="E aí pessoal? Uma Feliz Páscoa para todos vocês!",
  lang=lingua
)

sp.save(audio)
playsound(audio)
