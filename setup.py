import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='guoku-notifications',
    version='0.1',
    install_requires = [
        'django>=1.4',
        'django-model-utils>=2.2',
    ],
    packages=[
        'notifications',
        'notifications.urls',
        'notifications.templatetags',
    ],
    package_data={'notifications': [
                                    'templates/notifications/messages/*.html',
                                    'templates/notifications/messages/partial/*.html'
                                 ]},
    # include_package_data=True,
    license='BSD License',  # example license
    description='A  Django app to notifications.',
    # long_description=README,
    zip_safe=False,
    url='http://www.guoku.com/',

    author='jiaxin',
    author_email='jiaxin@guoku.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Notifications',
    ],
)
