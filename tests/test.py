from api.parser.YandexParser import YandexParser

# Initializing YandexParser
YP = YandexParser('../data')

# Insert the link where Similar Images Block is depicted
image_url = 'https://yandex.ru/images/search?rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F4328953%2FwWv_boU54e26wbJKub6Y-g%2Forig&cbir_id=4328953%2FwWv_boU54e26wbJKub6Y-g&from=tabbar'

# Storing images in the 'data' folder
YP.get_by_image_url(image_url, limit=300)
