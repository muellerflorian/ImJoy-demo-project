from setuptools import setup, find_packages

setup(
      name='imjoydemoproject',
      version='0.1.0',
      description='What is going on.',
      url='http://whatever',
      author='Florian MUELLER',
      author_email='muellerf.research@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
        'numpy'
      ],
      zip_safe=False)
