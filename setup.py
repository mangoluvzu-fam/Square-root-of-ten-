from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="square-root-of-ten",
    version="10.0.0",
    author="Travis C. Ortiz",
    author_email="cruisetravers@gmail.com",
    description="The 10th Ignition Engine - Unified Algebraic Resonance Framework with √10 Prime Distribution Discovery",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mangoluvzu-fam/Square-root-of-ten-",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Security :: Cryptography",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.19.0",
        "scipy>=1.5.0",
        "sympy>=1.6",
        "matplotlib>=3.3.0",
    ],
)
