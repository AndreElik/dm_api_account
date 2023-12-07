from setuptools import setup, find_packages
REQUIRES = [
    'allure-pytest',
    'requests',
    'restclient']

setup(
    name='dm_api_account',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/AndreElik/dm_api_account.git',
    license='MIT',
    author='Andre',
    author_email='',
    install_requires=REQUIRES,
    description='dm_api_account : apis, models,  utilites'
)
