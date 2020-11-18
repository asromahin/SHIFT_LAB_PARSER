# SHIFT_LAB_PARSER

### Python script to download images from 'Yandex Pictures'. Inspired by google-images-download

## Clone the repo

git clone https://github.com/asromahin/SHIFT_LAB_PARSER.git

### Libs that are necessary to install for the parser(if you don't have it installed yet):

pip install opencv-python

pip install numpy

pip install imagededup

pip install pandas

pip install tqdm

pip install requests

pip install shutil

pip install psutil

### Install selenium and chrome driver:

apt-get update

apt install chromium-chromedriver

cp /usr/lib/chromium-browser/chromedriver /usr/bin

pip install selenium

### In python script:

import sys

sys.path.insert (0, '/ usr / lib / chromium-browser / chromedriver')

### Install for the application:

pip install PyQt4
pip install matplotlib

### How to use the parser?

1. Go to yandex.ru / yandex.com and select the category "pictures".
2. There is a camera icon next to the "find" button, click it.
3. Upload an image of the item you would like to parse.
4. The resulting page should contain "Similar images" at its bottom. Copy URL of the current page.
5. Proceed to the tests/test.py script and assign the URL to image_url variable.
6. Run the script from the console: python tests/test.py (or Ctrl+Shift+F10 when using PyCharm).
7. If the download went quickly, much faster than an hour, this means that there has been an "incomprehensible glitch", which is somehow connected with Yandex, I haven't figured it out yet. Restarting the script usually fixes the problem. In general, the expected time is about 2 hours for 1500 images. Your capacity may differ.
8. The result is in the 'data' folder.
9. Then you can clean the folder from some broken images that were downloaded, as well as from duplicates. Run the script clean_data.py to accomplish the task.
10. Processed images will apppear in a new 'clean_data' folder.
