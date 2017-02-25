from setuptools import setup

setup(
    name='tcclient',
    version='0.0.1',
    description='Team Cowboy REST API python client.',
    url='https://github.com/bdmartin/tcclient',
    author='Brandon Martin',
    author_email='brandon.d.martin@gmail.com',
    license='MIT',
    packages=['tcclient'],
    install_requires=[
        'requests'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False
)
