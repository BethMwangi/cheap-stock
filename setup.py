from setuptools import setup

setup(
    name="cheap-stock app",
    version='0.1',
    py_modules=['stock-app'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        stock-app=stock:cli
    ''',
)