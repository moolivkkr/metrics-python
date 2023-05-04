import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_metrics",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Python package for collecting and exporting metrics using OpenTelemetry SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/python_metrics",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "opentelemetry-api==1.6.0",
        "opentelemetry-sdk==1.6.0",
        "psutil==5.8.0",
        "prometheus-client==0.11.0",
    ],
    python_requires=">=3.6",
)
