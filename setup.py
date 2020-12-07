import setuptools

setuptools.setup(
    name='django-postgres-drop-index',
    version='2020.12.7',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
