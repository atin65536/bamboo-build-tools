from distutils.core import setup

setup(
    name='bamboo-build-tools',
    version='1.0',
    packages=['bamboo'],
    url='http://rutube.ru',
    license='Beer Licence',
    author='tumbler',
    author_email='stikhonov@rutube.ru',
    scripts=[
        'bin/coverage2clover',
        'bin/bbt-deploy'
    ],
    package_data={'bamboo': ['Makefile']},
    description='python build tools for Atlassian Bamboo',
    install_requires=['lxml'],
)
