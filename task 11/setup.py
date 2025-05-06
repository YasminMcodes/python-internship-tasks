from setuptools import setup, find_packages

setup(
    name="invoice_normalizer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "python-dateutil",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A utility package to normalize messy invoice data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/invoice_normalizer",  # Update if hosting on GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "invoice-normalizer=invoice_normalizer.cli:main",
        ]
    }
)
