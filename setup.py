from distutils.core import setup

REQUIRES = [
    'records',
    'structlog'
]

setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/ValeriyMenshikov/db_client.git',
    license='MIT',
    author='Valeriy Menshikov',
    author_email='-',
    install_requires=REQUIRES,
    description='db client with logger'
)
