# This file is part of WritheM's Caption Contest, intended for use with MuggleNet's CC.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

import cc

setup(name='django-captioncontest',
      version=cc.__version__,
      description='a django driven caption contest',
      long_description=open('README.md').read(),
      author=cc.__author__,
      author_email=cc.__email__,
      license=cc.__license__,
      url=cc.__url__,
      
      packages=find_packages(exclude=['demo']),
      include_package_data=True,
      zip_safe=False)