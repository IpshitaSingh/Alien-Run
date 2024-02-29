from setuptools import setup, find_packages

setup(
    name='Alien-Run',
    version='0.1.0',
    description='Dodge obstacles!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ipshita Singh',
    author_email='ipshitasingh999@gmail.com',
    url='https://github.com/IpshitaSingh/Alien-Run',
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
)
