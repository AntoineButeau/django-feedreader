import os
from setuptools import setup

long_description = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name = 'django-feedreader',
    version = '0.9.0',
    packages = ['feedreader'],
    include_package_data = True,
    license = 'BSD License',
    description = 'A simple Django app to aggregate RSS feeds.',
    long_description = long_description,
    url = 'https://github.com/ahernp/django-feedreader',
    author = 'Paul Ahern',
    author_email = 'ahernp@ahernp.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django==1.6.2',
        'django-braces==1.4.0',
        'feedparser==5.1.3',
        'pytz>=2013.7'
    ],
)
