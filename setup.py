##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.app.exception package

$Id$
"""

import os

from setuptools import setup, find_packages, Extension

setup(name='zope.app.exception',
      version = '3.4.0b1',
      url='http://svn.zope.org/zope.app.exception',
      license='ZPL 2.1',
      author='Zope Corporation and Contributors',
      author_email='zope3-dev@zope.org',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      extras_require=dict(test=[
          'zope.app.securitypolicy',
          'zope.app.testing',
          'zope.app.zcmlfiles',
          'zope.app.zptpage',
      ]),
      namespace_packages=['zope', 'zope.app'],
      install_requires=['setuptools',
                        'zope.app.pagetemplate',
                        'zope.deferredimport',
                        #'zope.formlib',
                        'zope.interface',
                        'zope.publisher',
                        ],
      include_package_data = True,

      zip_safe = False,
      )
