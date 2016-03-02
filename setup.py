from setuptools import setup

setup(
    name = 'ls branch',
    description = 'List all directories with .git subdirectory and show current branch for each.',
    version = "0.1",
    url = 'https://github.com/arrrlo/lsbranch',

    author = 'Ivan Arar',
    author_email = 'ivan.arar@gmail.com',

    packages = ['lsbranch'],
    install_requires = [
        'click==6.3',
    ],

    entry_points = {
        'console_scripts': [
            'lsbranch=lsbranch.cli:cli'
        ],
    },
)