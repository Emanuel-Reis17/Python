'''
LIBS: 
    - pytube
    - pyuic5 (do not install)
    - pyinstaller
SCRIPTS:
    - pyuic5 file.ui -o pyFile.py -x
    - pyinstaller --onefile --noconsole fileToConvert.py
'''
from pytube import YouTube
import os

# Download function
def download(self):
    if self.rb_mp4.isChecked() == True:
        url = self.txt_link.text()
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
    elif self.rb_mp3.isChecked() == True:
        try:
            url = self.txt_link.text()
            yt = YouTube(url)
            audio = yt.streams.filter(only_audio=True).first()
            out_file = audio.download()
            # Salvando arquivo formato .mp3
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        except:
            pass
