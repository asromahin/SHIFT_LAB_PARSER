import api.utils.utils as utils
import time
from tqdm import tqdm
import pandas as pd

class YandexParser():
    def __init__(self,save_path,keyword = '_',limit=0,url=None):
        self.save_path=save_path
        self.keyword=keyword
        self.wd=utils.init_wd()
        self.limit=limit
        if(url):
            self.set_url(url)
    def set_url(self,url):
        self.url=url
        if(self.wd.current_url!=self.url):
            self.wd.get(self.url)
            time.sleep(1)
    def get_links_to_images(self):

        last_height = self.wd.execute_script("return document.body.scrollHeight")
        last_len = 0
        print('scroll page with images')
        while (True):
            imgs = self.wd.find_elements_by_class_name('serp-item__thumb')
            print(len(imgs))
            b = self.wd.find_element_by_class_name('more_direction_next')
            try:
                b.click()
            except:
                pass
            time.sleep(1)
            new_height = self.wd.execute_script("return document.body.scrollHeight")
            imgs = self.wd.find_elements_by_class_name('serp-item__link')
            if (last_len == len(imgs)):
                break;
            if (self.limit != 0):
                if (len(imgs) > self.limit):
                    break;
            last_height = new_height
            last_len = len(imgs)

        print('end scroll page with images')

        self.image_links = []
        for im in imgs:
            url = im.get_attribute('href')
            # print(url)
            d = url.split('&')
            for i in range(len(d)):
                if ('img_url' in d[i]):
                    d2 = d[i].split('=')[1]
                    url = d2.split('%3A')
                    url = ':'.join(url)
                    url = url.split('%2F')
                    url = '/'.join(url)
                    self.image_links.append(url)
                    break;
        print('end parse links for images')
        self.pdata = pd.DataFrame(self.image_links, columns=['url'])

    def get_images_by_links(self):

        print('start grab images')
        save_files=[]
        for i in tqdm(range(len(self.image_links))):
            save_name = f'{self.save_path}/{keyword}_{i}.jpg'
            utils.get_image_by_url(self.image_links[i], save_name)
            save_files.append(save_name)
        self.pdata['save_file']=save_files

        print('end grab images')

    def get_by_text(self, text):
        url = "https://yandex.ru/images/search?from=tabbar&text={}".format(text.replace(' ', '%20'))
        self.set_url(url)
        self.get_links_to_images()
        self.get_images_by_links()

    def get_by_url(self, url):
        self.set_url(url)
        self.get_links_to_images()
        self.get_images_by_links()

    def get_by_image(self,image_path=''):
        self.wd.get('https://yandex.ru/images/')
        print('open https://yandex.ru/images/')
        time.sleep(1)
        self.wd.find_element_by_class_name('icon_type_cbir').click()
        time.sleep(1)
        print(f'download image from {image_path}')
        target_panel=self.wd.find_element_by_class_name('cbir-panel__file-input')
        utils.drag_and_drop_file(target_panel,image_path)
        print('wait download')
        start_url=self.wd.current_url
        seconds=0
        limit_seconds=60
        while(True):
            if(self.wd.current_url!=start_url or seconds>=limit_seconds):
                break
            time.sleep(1)
            seconds+=1
            print('while',seconds,'seconds')
        time.sleep(1)

        elem = self.wd.find_element_by_class_name('similar__thumbs')
        elem = elem.find_element_by_tag_name('li')
        elem = elem.find_element_by_tag_name('a')
        start_url=elem.get_attribute('href')
        print('get url:', start_url)
        self.set_url(start_url)
        print('go to page')
        self.get_links_to_images()
        self.get_images_by_links()

    def get_by_image_url(self,image_url='',save_screen='screenshot.png'):
        self.wd.get('https://yandex.ru/images/')
        print('open https://yandex.ru/images/')
        time.sleep(1)
        self.wd.find_element_by_class_name('input__cbir-button').click()
        time.sleep(1)

        print(f'set image url {image_url}')
        cur_elem = self.wd.find_element_by_class_name('cbir-panel__input')
        target_panel=cur_elem.find_element_by_class_name('input__control')
        print(target_panel.get_attribute('value'))
        target_panel.click()
        target_panel.clear()
        target_panel.send_keys(image_url)
        print(target_panel.get_attribute('value'))

        self.wd.get_screenshot_as_file(save_screen)
        time.sleep(2)
        cur_elem.find_element_by_class_name('cbir-panel__search-button').click()
        time.sleep(5)
        print('image is set')
        start_url=self.wd.current_url
        seconds=0
        limit_seconds=60
        #while(True):
        #    if(self.wd.current_url!=start_url or seconds>=limit_seconds):
        #        break
        #    time.sleep(1)
        #    seconds+=1
        #    print('while',seconds,'seconds')
        time.sleep(1)
        self.wd.save_screenshot('test.png')
        elem = self.wd.find_element_by_class_name('cbir-similar__thumbs-inner')
        elem = elem.find_element_by_tag_name('li')
        elem = elem.find_element_by_tag_name('a')
        start_url=elem.get_attribute('href')
        print('get url:', start_url)
        self.set_url(start_url)
        print('go to page')
        self.get_links_to_images()
        self.get_images_by_links()




