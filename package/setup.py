from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="desafios_dio",
    version="0.0.1",
    author="Berg_Gama",
    author_email="berg.cambrainha@gmail.com",
    description="Pacote contendo as principais funções para solucionar os desafios iniciais e intermediários da Dio",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="github.com/berggama/bootcamp_unimed"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)