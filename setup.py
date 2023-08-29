from setuptools import find_namespace_packages, setup

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gitruck-flet-search-bar",
    version="0.0.1",
    author="Colsrch",
    author_email="colsrch@foxmail.com",
    description="A search bar for flet",
    license="Apache-2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gitruck/flet-search-bar",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    install_requires=[
        "flet",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    include_package_data=True,
    python_requires=">=3.9",
)
