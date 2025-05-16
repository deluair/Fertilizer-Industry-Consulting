"""Package configuration for the Fertilizer Industry Simulation Framework."""

from pathlib import Path
from setuptools import setup, find_packages

# Read the contents of README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read requirements from requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    requirements = [
        line.strip()
        for line in f.read().splitlines()
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="fertilizer-sim",
    version="0.1.0",
    author="Fertilizer Industry Consulting Team",
    author_email="contact@fertilizer-consulting.com",
    description=(
        "A comprehensive simulation framework for modeling the evolution "
        "of the fertilizer industry (2025-2040)"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deluair/Fertilizer-Industry-Consulting",
    project_urls={
        "Bug Tracker": "https://github.com/deluair/Fertilizer-Industry-Consulting/issues",
        "Documentation": "https://fertilizer-industry-consulting.readthedocs.io",
        "Source Code": "https://github.com/deluair/Fertilizer-Industry-Consulting",
    },
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={
        "": ["*.yaml", "*.yml", "*.json"],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-mock>=3.0.0",
            "black>=23.0.0",
            "isort>=5.10.0",
            "mypy>=1.0.0",
            "flake8>=6.0.0",
            "pre-commit>=3.3.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "nbsphinx>=0.8.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "fertilizer-sim=main:main",
        ],
    },
    zip_safe=False,
)
