from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dacsspace",
    url="https://github.com/RockefellerArchiveCenter/DACSspace",
    description="Validate data in an ArchivesSpace instance against DACS requirements.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rockefeller Archive Center",
    author_email="archive@rockarch.org",
    version="0.1.0",
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['dacsspace=dacsspace.command_line:main'],
    },
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires=">=3.7",
    install_requires=[
        "jsonschema",
        "requests",
    ],
)
