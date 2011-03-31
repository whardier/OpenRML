#!/usr/bin/env python

from distutils.core import setup

setup(name='OpenRML',
      version='0.1',
      author='Shane R. Spencer',
      author_email='shane@bogomip.com',
      license='MIT',
      description='ReportLab RML processing and rendering',
      packages = ['openrml'],
      package_dir = {'openrml': 'openrml'},
      scripts = ['scripts/openrml-render'],
      url = 'https://github.com/whardier/OpenRML',
      download_url = 'https://github.com/whardier/OpenRML/tarball/master',
      classifiers = ['Development Status :: 4 - Beta',
                     'Environment :: Console',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Documentation',
                     'Topic :: Software Development :: Libraries :: Python Modules',
                     'Topic :: Text Processing',
                     'Topic :: Utilities',
                    ],
     )


