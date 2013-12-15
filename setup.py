#/*******************************************************************************
# * Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *       http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.
# *******************************************************************************/

__author__ = 'ran'

from setuptools import setup

version = '0.1.0'

setup(
    name='cosmo-cli',
    version=version,
    author='ran',
    author_email='ran@gigaspaces.com',
    packages=['cosmo_cli','cosmo_rest_client', 'cosmo_rest_client.swagger', 'cosmo_rest_client.swagger.models'],
    license='LICENSE',
    description='the cosmo cli',
    package_data={'cosmo_cli': ['cosmo-config.json']},
    entry_points={
        'console_scripts': ['cosmo = cosmo_cli.cosmo_cli:main']
    },
    install_requires=[
        "python-novaclient",
        "python-keystoneclient",
        "python-neutronclient",
        "scp",
        ]
)