from setuptools import setup

setup(
    name='mylib',
    version='0.1',
    packages=['mylib'],
    package_dir={"mylib": "mylib"},
    url='',
    license='MIT',
    author='Amit Maindola',
    author_email='maindola.amit@gmail.com',
    description='My custom Library of helper methods for ML and DL',
    install_requires=["numpy",
                      "pandas",
                      "matplotlib",
                      "seaborn",
                      "sklearn",
                      "emoji",
                      "nltk"]
)
