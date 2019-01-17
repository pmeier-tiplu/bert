from setuptools import setup

setup(
    name="bert-tiplu",
    version="1.0",
    url="https://github.com/pmeier-tiplu/bert",
    author="Jacob Devlin",
    author_email="jacobdevlin@google.com",
    license="LICENSE",
    description="BERT Bidirectional Encoder Representations from Transformers",
    long_description=open("README.md").read(),
    packages=["bert"],
    install_requires=["tensorflow >= 1.11.0", "six"],
    zip_safe=True,
)
