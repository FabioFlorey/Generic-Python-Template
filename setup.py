#! /usr/bin/env python3
# *-* mode: python; coding: utf-8 *-*
'''
=============================================================================
                           ____ ____ ___ _  _ ___
                           [__  |___  |  |  | |__]
                           ___] |___  |  |__| |
                      Build and distribute your code. 
=============================================================================
Author: Fabio Craig Wimmer Florey                             Version: 0.0.1
=============================================================================
                                  ~ NOTICE ~
 
 Project, Copyright © 2022, Fabio Craig Wimmer Florey - All Rights Reserved.

     Unless required by applicable law or agreed to in writing, software      
      distributed under the License is distributed on an "AS IS" BASIS,       
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   

       See the License for the specific language governing permissions        
                      and limitations under the License.
 
 License: MIT-0                          Terms and Conditions: ./LICENSE.md
=============================================================================
'''

from pathlib import Path
from setuptools import setup, find_packages

from toml import loads

CWD : Path   = Path(__file__).parent

config: dict = loads((CWD / 'setup.toml').read_text())
version  : str  = config['version']
fullname : str  = f'{config["name"]} - v{config["version"]}'
readme   : str  = (CWD / 'README.md').read_text()

setup(
       name = config['name'], version=version,
       description = config['description'], license = config['license'],
       url = config['url'], download_url = config['download_url'],

       fullname = fullname, long_description = readme,
       long_description_content_type = config['content_type'],

       keywords = config['keywords'], classifiers = config['classifiers'],

       author           = config['author'],
       author_email     = config['author_email'],
       maintainer       = config['maintainer'],
       maintainer_email = config['maintainer_email'],
       
       packages         = find_packages(),
       python_requires  = config['python_requires'],
       install_requires = config['install_requires'],
       extras_require   = config['extras_require'],
       
       entry_points = config['entry_points']
     )

if __name__ == '__main__':
    pass
