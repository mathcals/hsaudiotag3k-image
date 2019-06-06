from setuptools import setup
LONG_DESC = open('README', 'rt').read()

setup(
    name='hsaudiotag3k-image',
    version='1.1.5',
    packages=['hsaudiotag'],
    scripts=[],
    install_requires=[],
    license='BSD License',
    description='Modfied version of hsaudiotag (added support for images). Read metdata (tags) of mp3, mp4, wma, ogg, flac and aiff files.',
    long_description=LONG_DESC,
)
