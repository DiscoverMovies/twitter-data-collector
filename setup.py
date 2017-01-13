from distutils.core import setup

setup(
    name='twitter-data-collector',
    author="Sherin Ann Thomas",
    author_email="sherinannthomas1@gmail.com",
    description="A tool to collect data from twitter using tweepy",
    version='0.1dev',
    packages=['twitter-data-collector', ],
    license='GNU General Public License',
    long_description=open('README.md').read(),
)
