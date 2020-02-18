import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsis-pkg",
    version="0.0.1",
    author="Pulkit Gupta",
    author_email="guptapulkit48@gmail.com",
    description="A package for TOPSIS analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gupta-pulkit/topsis-pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data = True,
    install_requires=["numpy", "pandas"],
    entry_points={
        "console_scripts": [
            "topsis-pkg=topsis_pkg.topsis:main",
        ]
    },
)
