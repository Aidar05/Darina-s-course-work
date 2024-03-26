from flask import Flask, url_for

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:43345'

with app.app_context():
    portrait_url = 'gallery/self_portraits/self_portrait'
    sunflower_url = 'gallery/block2/sunflowers'
    arl_work_url = 'gallery/arl_works/asdf'
    author_copies_url = 'gallery/author_copies/asdf'

    self_portraits = [
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{portrait_url}.png')
        },
        {
        'img_info': 'Self-Portrait Dedicated to Paul Gauguin 1888 (130 Kb); Oil on canvas',
        'dimens': '60.5 x 49.4 cm (23 3/4 x 19 1/2 in)',
        'url': url_for('static', filename=f'{portrait_url}2.png')
        },
        {
        'img_info': 'Self-Portrait with Bandaged Ear 1889 (250 Kb); Oil on canvas',
        'dimens': '60 x 49 cm;',
        'url': url_for('static', filename=f'{portrait_url}3.png')
        },
        {
        'img_info': 'Self-Portrait 1889 (250 Kb); Oil on canvas,',
        'dimens': '65 x 54 cm (25 1/2 x 21 1/4 in)',
        'url': url_for('static', filename=f'{portrait_url}4.png')
        },
        {
        'img_info': 'Self-Portrait 1889 (250 Kb); Oil on canvas,',
        'dimens': '65 x 54 cm (25 1/2 x 21 1/4 in',
        'url': url_for('static', filename=f'{portrait_url}5.png')
        }
    ]

    sunflowers = [
        {
        'img_info': 'Подсолнухи. Холст, масло',
        'dimens': 'высота  43,2 см ширина 61 см',
        'url': url_for('static', filename=f'{sunflower_url}1.png')
        },
        {
        'img_info': 'Четыре увядших подсолнуха. Холст, масло',
        'dimens': 'высота 60 см ширина 100 см',
        'url': url_for('static', filename=f'{sunflower_url}2.png')
        },
        {
        'img_info': 'Два срезанных подсолнуха. холст, масло',
        'dimens': 'высота 21 см ширина 27 см',
        'url': url_for('static', filename=f'{sunflower_url}3.png')
        },
        {
        'img_info': 'Два срезанных подсолнуха. Холст, масло',
        'dimens': 'высота 50 см ширина 60 см',
        'url': url_for('static', filename=f'{sunflower_url}4.png')
        },
    ]

    arl_works = [
        {
        'img_info': 'Ваза с двенадцатью подсолнухами. Холст, масло',
        'dimens': 'высота 91 см ширина 72 см',
        'url': url_for('static', filename=f'{arl_work_url}.png')
        },
        {
        'img_info': 'Три подсолнуха («Лозанские» подсолнухи). Холст, масло',
        'dimens': 'высота 73 см ширина 58 см',
        'url': url_for('static', filename=f'{arl_work_url}2.png')
        },
        {
        'img_info': 'Ваза с пятью подсолнухами. Холст, масло',
        'dimens': 'высота 98 см ширина 69 см',
        'url': url_for('static', filename=f'{arl_work_url}3.png')
        },
    ]

    author_copies = [
    {
    'img_info': 'Ваза с пятнадцатью подсолнухами. Холст, масло',
    'dimens': 'высота 95 смширина 73 см',
    'url': url_for('static', filename=f'{author_copies_url}1.png')
    },
    {
    'img_info': 'Ваза с двенадцатью подсолнухами. Холст, масло',
    'dimens': 'высота 92,4 см ширина 71,1 см',
    'url': url_for('static', filename=f'{author_copies_url}2.png')
    },
    {
    'img_info': 'Ваза с пятнадцатью подсолнухами. Холст, масло',
    'dimens': 'высота 100,5 см ширина 76,5 см',
    'url': url_for('static', filename=f'{author_copies_url}3.png')
    },
]
