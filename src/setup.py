from setuptools import setup

setup(
    name='La sombra del Imperio: Guardianes de la paz',
    version='0.1',
    packages=['utils', 'scenes', 'scenes.level_1', 'scenes.level_2', 'game_objects', 'game_objects.level_1',
              'game_objects.level_2'],
    package_dir={'': 'src'},
    url='',
    license='',
    author='javi',
    author_email='javi.rubio.roca@gmail.com',
    description='',
    install_requires=[
        'pygame~=2.5.2',
        'moviepy~=1.0.3'
    ]
)
