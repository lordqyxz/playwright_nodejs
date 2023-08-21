import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="playwright_nodejs",
    version="0.0.1",
    author="ShiYz",
    author_email="yz.shi@outlook.com",
    description="playwright_nodejs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lordqyxz/playwright_nodejs",
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['playwright'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'foo = spider_engine.engine_running_helper:run'
        ]
    },
)
