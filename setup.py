#!/usr/bin/env python3
#
# Copyright 2019 Venafi, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import absolute_import, print_function, unicode_literals
from setuptools import setup

import venafi

setup(
    name='openstack-heat-plugin-venafi',
    description='Venafi Inc. OpenStack Heat Plugin',
    license='Apache License, Version 2.0',
    version=venafi.__version__,
    author='Venafi Inc.',
    author_email='opensource@venafi.com',
    url='https://github.com/Venafi/venafi-openstack-heat-plugins/',
    keywords=['venafi', 'openstack', 'heat', 'ssl', 'certificates'],
    install_requires=[
        'vcert >= 0.6.0'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Intended Audience :: System Administrators',
    ]
)
