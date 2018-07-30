from setuptools import setup, find_packages

setup(
    name='wallappaer',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click','random','bs4','apscheduler','os','sys','requests','ctypes','flickrapi'
    ],
    entry_points='''
        [console_scripts]
        yourscript=wallpaper:main
    ''',
)
