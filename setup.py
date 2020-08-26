from setuptools import setup

setup(
    name="cheap-stock app",
    version='0.1',
    py_modules=['stock-app', 'docopt_config'],
    install_requires=[
        'Click',
        'colorama',
        'tabulate',
    ],
    # scripts =['docopt_config.py']
    entry_points='''
        [console_scripts]
        stock-app=stock:cli
    ''',
)