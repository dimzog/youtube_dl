import os
import sys
import zipfile
import glob

print('Youtube downloader using youtube_dl\n')
print('Checking for Updates\n')
os.system('pip install --upgrade youtube-dl')

SAVE_PATH = '/tracks'
LINKS_PATH = 'list.txt'

if 'ffmpeg' not in os.environ['PATH']:
    print('FFMPEG needs to be in path')

    # Windows 64-bit latest static build
    FFMPEG_URL = 'https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-latest-win64-static.zip'
    FFMPEG_PATH = 'ffmpeg-latest-win64-static.zip'

    files = [file for file in glob.glob('*.zip')]
    if FFMPEG_PATH not in files:
        print('Downloading..')

        request = requests.get(FFMPEG_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with open(FFMPEG_PATH, 'wb') as f:
            f.write(request.content)

    print('Extracting..')
    with zipfile.ZipFile(FFMPEG_PATH, 'r') as zip:
        zip.extractall('C:/FFmpeg')

    BIN_PATH = 'C:\FFmpeg\\ffmpeg-latest-win64-static\\bin'
    print(f'Done.. Add "{BIN_PATH}" to path')


with open(LINKS_PATH, 'r') as links:
    for link in links:
        cmd = (
                f'youtube-dl -f best --no-warnings --extract-audio --audio-format mp3 '
                f'--audio-quality 0 --embed-thumbnail --add-metadata  -o '
                f'{SAVE_PATH}/%(title)s.%(ext)s {link}'
                )

        os.system(cmd)
