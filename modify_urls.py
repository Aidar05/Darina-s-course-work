liked = [
    '"http://127.0.0.1:43345/static/gallery/header_img.png"',
    '"http://127.0.0.1:43345/static/gallery/header_img.png"',
    '"http://127.0.0.1:43345/static/gallery/header_img.png"',
    '"http://127.0.0.1:43345/static/gallery/header_img.png"',
    '"http://127.0.0.1:43345/static/gallery/header_img.png"',
    '"http://127.0.0.1:43345/static/gallery/header_img.png"'
]

url = '"http://127.0.0.1:43345/static/gallery/header_img.png"' 

def exclude_chars(str, chars_to_filter):
    result = ''
    for char in str:
        if char not in chars_to_filter:
            result += char
    return result

def exclude_chars_inList(liked):    
    result = []
    for i in liked:
        result.append(exclude_chars(i))

    return result

def remove_base_path(url):
    base_url = 'http://127.0.0.1:43345/'
    return url.replace(base_url, '')

def modify_url(url):
    url = exclude_chars(url, '"')
    url = remove_base_path(url)
    return url 

def filter_liked(liked):
    result = []

    for img_url in liked:
        result.append(modify_url(img_url))
    return result
