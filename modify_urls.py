# Пример того как будет выглядеть список вытащенный из бд
liked = [
    '"http://127.0.0.1:43345/static/gallery/header_img.png"',
    '"http://127.0.0.1:43345/static/gallery/header_img.png"',
    '"http://127.0.0.1:43345/static/gallery/header_img.png"',
    '"http://127.0.0.1:43345/static/gallery/header_img.png"',
    '"http://127.0.0.1:43345/static/gallery/header_img.png"',
    '"http://127.0.0.1:43345/static/gallery/header_img.png"'
]

url = '"http://127.0.0.1:43345/static/gallery/header_img.png"' 

# Убирает лишние символы в строке
def exclude_chars(str, chars_to_filter):
    result = ''
    for char in str:
        if char not in chars_to_filter:
            result += char
    return result

# base url удаляет, оставльняя релитивный путь
def remove_base_path(url):
    base_url = 'http://127.0.0.1:43345/static/'
    base_url_two = 'http://localhost:43345/static/'
    
    result = url.replace(base_url, '')
    result = result.replace(base_url_two, '')
    return result

# Делает все на урл чтобы он был готов для использования
def modify_url(url):
    url = exclude_chars(url, '"')
    url = remove_base_path(url)
    return url 

# Делает все урл usable.
# Примерный результат: ['gallery/self_portraits/self_portrait5.png', 'gallery/self_portraits/self_portrait2.png']
def filter_liked(liked):
    result = []

    for img_url in liked:
        # modified_url = modify_url(img_url)
        result.append(modify_url(img_url))
    return result[0].split()
