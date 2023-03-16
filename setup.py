from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dinteractions_Talarator",
    version="2.0.2",
    description="Official interactions.py talarator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xnrado/talarator",
    author="XnraD",
    author_email="xnrad123@gmail.com",
    license="GNU",
    packages=["interactions.ext.talarator"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=["discord-py-interactions", "interactions-wait-for"],
)
