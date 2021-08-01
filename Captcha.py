import random
from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha

image = ImageCaptcha()
audio = AudioCaptcha()

captcha_txt = str(random.randint(1001,9999))

image.generate(captcha_txt)
image.write(captcha_txt,'CAPTCHA.png')

audio.generate(captcha_txt)
audio.write(captcha_txt,"Audio.mp3")