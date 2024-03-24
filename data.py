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
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{portrait_url}2.png')
        },
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{portrait_url}3.png')
        },
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{portrait_url}4.png')
        },
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{portrait_url}5.png')
        }
    ]

    sunflowers = [
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{sunflower_url}1.png')
        },
        {
        'img_info': 'Self-Portrait in front ofs the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{sunflower_url}2.png')
        },
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{sunflower_url}3.png')
        },
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{sunflower_url}4.png')
        },
    ]

    arl_works = [
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{arl_work_url}.png')
        },
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{arl_work_url}2.png')
        },
        {
        'img_info': 'Self-Portrait in front of the Easel',
        'dimens': '1888 (200 Kb); 65 x 50.5 cm',
        'url': url_for('static', filename=f'{arl_work_url}3.png')
        },
    ]

    author_copies = [
    {
    'img_info': 'Self-Portrait in front of the Easel',
    'dimens': '1888 (200 Kb); 65 x 50.5 cm',
    'url': url_for('static', filename=f'{author_copies_url}1.png')
    },
    {
    'img_info': 'Self-Portrait in front of the Easel',
    'dimens': '1888 (200 Kb); 65 x 50.5 cm',
    'url': url_for('static', filename=f'{author_copies_url}2.png')
    },
    {
    'img_info': 'Self-Portrait in front of the Easel',
    'dimens': '1888 (200 Kb); 65 x 50.5 cm',
    'url': url_for('static', filename=f'{author_copies_url}3.png')
    },
]
