# yparser

# Необходимо установить для парсера:

1. pip install opencv-python
2. pip install numpy
3. pip install imagededup
4. pip install pandas
5. pip install tqdm
6. pip install requests
7. pip install shutil
8. pip install psutil

# Установка selenium и chrome driver:

apt-get update

apt install chromium-chromedriver

cp /usr/lib/chromium-browser/chromedriver /usr/bin

pip install selenium

// in some python script:

import sys

sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

# Необходимо установить для приложения:

1. pip install PyQt4
2. pip install matplotlib

# Как запускать парсер?

1. Заходите на yandex.ru
2. Выбираете категорию "картинки"
3. Там есть иконка фотоаппарата возле кнопки "найти", жмёте её.
4. Загружаете фотографию электросчётчика
5. На данном этапе должна загрузиться страница с блоком "Похожие фотографии" внизу. Копируем адрес текущей страницы и присваиваем его переменной image_url в tests/test.py.
6. Запускаем скрипт tests/test.py из консоли: python tests/test.py (или Ctrl+Shift+F10 из основного окна PyCharm)
7. Если загрузка быстро прошла, гораздо быстрее часа, это значит, что произошёл "непонятный глюк", который как-то связан с яндексом, пока не разобрался. Лечится перезапуском скрипта. Вообще ожидаемое время порядка 2 часов для 1500 изображений. У вас могут быть другие цифры.
8. Результат лежит в папке 'data'
9. Затем нужно почистить папку от плохо скаченных, а также от дубликатов, для этого запускаете скрипт clean_data.py
10. Появится новая 'clean_data' - это и есть ваши данные, которые надо просмотреть и выбрать уже необходимые
