from api.src.utils.utils import get_chunks
from api.src.utils.logger import Logger
import os
import asyncio

import aiohttp
import aiofiles
import threading
import requests


async def fetch(session, image_link, save_path):
    async with session.get(image_link) as resp:
        if resp.status == 200:
            f = await aiofiles.open(save_path, mode='wb')
            await f.write(await resp.read())
            await f.close()


async def download_images_async(image_links, save_dir):
    async with aiohttp.ClientSession() as session:
        for i, image_link in enumerate(image_links):
            try:
                await fetch(session, image_link, os.path.join(save_dir, str(i) + '.jpg'))
            except:
                pass


class Downloader:
    def __init__(self, n_threads=16, logger=Logger(), thread_id=0):
        self.n_threads = n_threads
        self.logger = logger
        self.thread_id = thread_id

    # def log(self, *args):
    #     self.logger.append([*args])

    def save_image_by_response(self, response, savename, url):
        if not response.ok:
            # print(response, url)
            self.logger.log(f'{response}, {url}', thread_id=self.thread_id)
            # pass
        else:
            with open(savename, 'wb') as handle:
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)

    def get_image_by_url(self, url, savename, use_async=True):
        """
        Getting image by a given url using requests library
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/39.0.2171.95 Safari/537.36'}
        try:
            response = requests.get(
                url,
                timeout=5,
                stream=True,
                headers=headers,
            )
            self.save_image_by_response(response, savename, url)

        except Exception as e:
            # print(e, url)
            self.logger.log(f'{e}, {url}', thread_id=self.thread_id)
            # pass

    def download_images_sync(self, images_links, save_path, thread_id):
        # if not os.path.exists(save_dir):
        #     os.mkdir(save_dir)
        for i, image_link in (enumerate(images_links)):
            # save_path = os.path.join(save_dir, str(i) + '.jpg')
            self.get_image_by_url(image_link, save_path.format(thread_id, i + 1))

    def download_images(self, images_links, save_dir, download_type=0):
        if download_type == 0:
            self.download_images_sync(images_links, save_dir)
        elif download_type == 1:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(download_images_async(images_links, save_dir))
        elif download_type == 2:
            if not os.path.exists(save_dir):
                os.mkdir(save_dir)
            chunks = get_chunks(images_links, self.n_threads)
            threads = []
            for i, chunk in enumerate(chunks):
                sub_path = os.path.join(save_dir, '{}_{}.jpg')
                if len(chunk) > 0:
                    x = threading.Thread(target=self.download_images_sync, args=(chunk, sub_path, i + 1))
                    x.start()
                    threads.append(x)
            for thread in threads:
                thread.join()
