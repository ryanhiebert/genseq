from setuptools import setup

setup(
    name='genseq',
    version='1.0',
    description='Lazily Resolving Sequence',
    long_description=open('README.rst', 'rb').read().decode('utf-8'),
    author='Ryan Hiebert',
    author_email='ryan@ryanhiebert.com',
    license='MIT',
    url='https://github.com/ryanhiebert/genseq',
    package_dir={'': 'src'},
    py_modules=['genseq'],
    include_package_data=True,
    zip_safe=False,
    requires=[
        'six',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
