from setuptools import find_packages, setup

with open('requirements.txt') as requirements_file:
    REQUIREMENTS = [r.replace('\n', '') for r in requirements_file.readlines()]

setup(
    name='UpyExplorer',
    version='1.0.0',
    description='UpyExplorer API',
    author='UpyExplorer',
    author_email='upyexplorer@gmail.com',
    url='http://www.upyexplorer.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=False
)