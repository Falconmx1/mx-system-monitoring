from setuptools import setup, find_packages

setup(
    name="mx-system-monitoring",
    version="1.0.0",
    author="Falconmx1",
    description="Herramienta ligera y multiplataforma para monitoreo de sistema en tiempo real",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Falconmx1/mx-system-monitoring",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "psutil>=5.9.0",
        "rich>=13.0.0",
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "mx-monitor=main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
)
