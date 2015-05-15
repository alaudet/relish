from setuptools import setup

version = 'x.x.x'

setup(name='package_name',
      version=version,
      description='description of package',
      long_description=open("./README.md", "r").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Console",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 2.7",
          "Topic :: Home Automation",
          "License :: OSI Approved :: MIT License",
          ],
      author='Al Audet',
      author_email='alaudet@linuxnorth.org',
      url='https://github.com/alaudet/???',
      download_url='https://github.com/alaudet/???',
      license='MIT License',
      packages=['enter name of package'],
      install_requires=['dependancies']
      )
