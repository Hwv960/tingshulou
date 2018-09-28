from setuptools import setup, find_packages

setup(
    name="tingshulou",
    version="1.0",
    keywords=("tingshu", "tingshulou"),
    description="tingshulou",
    long_description="python tingshulou",
    license="MIT Licence",

    url="http://test.com",
    author="test",
    author_email="test@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[],

    scripts=[],
    entry_points={
        'console_scripts': [
            'test = test.help:main'
        ]
    }


)