About
=====
A basic site, which builds articles from static Markdown (.md) files. No database is needed, runs on `Django 1.9`

Implementation is largely based on description in book: [Lightweight Django](http://shop.oreilly.com/product/0636920032502.do)
So Kudos to the authors, I've just made implementation useful for myself
and maybe someone will find it usefull as well.

Installation
============
- Create virtualenv - `virtualenv venv`

- Enter it `source venv/bin/activate`

- Install required packages `pip install -r requirements.txt`

- Run it: `python app.py runserver`

- For more - reference Django documentation

Usage
=====
Content can be edited in `content` folder by adding new Markdown files
Template can be found in `main/templates/base.html`
