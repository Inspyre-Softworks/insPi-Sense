from distutils.core import setup

setup(
    name='inspi_sense',
    version='1.0',
    packages=['models', 'models.menus', 'models.windows', 'models.windows.popups', 'helpers', 'inspyred_stats', 'menus',
              'windows', 'windows.popups'],
    package_dir={'': 'bin'},
    url='https://github.com/Inspyre-Softworks/inspi_sense.git',
    license='MIT',
    author='Taylor-Jayde Jasmine Blackstone',
    author_email='t.blackstone@inpsyre.tech',
    description=''
)
