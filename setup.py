from setuptools import setup, find_packages


setup(
    name='email_split',
    version='1.0.0',
    description='Split an email address into its local and domain parts',
    long_description=open('README.rst').read(),
    keywords=[
        'split',
        'email',
        'parse',
        'local',
        'domain'
    ],
    author='Todd Wolfson',
    author_email='todd@twolfson.com',
    url='https://github.com/underdogio/python-email-split',
    download_url='https://github.com/underdogio/python-email-split/archive/master.zip',
    packages=find_packages(),
    license='MIT',
    install_requires=open('requirements.txt').readlines(),
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
