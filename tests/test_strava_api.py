#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: test_strava_api.py
#
# Copyright 2019 Oriol Fabregas
#
# Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

"""
test_strava_api
----------------------------------
Tests for `strava_api` module.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

from betamax.fixtures import unittest

__author__ = '''Oriol Fabregas <fabregas.oriol@gmail.com>'''
__docformat__ = '''google'''
__date__ = '''01-03-2019'''
__copyright__ = '''Copyright 2019, Oriol Fabregas'''
__credits__ = ["Oriol Fabregas"]
__license__ = '''Apache Software License 2.0'''
__maintainer__ = '''Oriol Fabregas'''
__email__ = '''<fabregas.oriol@gmail.com>'''
__status__ = '''Development'''  # "Prototype", "Development", "Production".


class TestStrava_api(unittest.BetamaxTestCase):

    def setUp(self):
        """
        Test set up

        This is where you can setup things that you use throughout the tests. This method is called before every test.
        """
        pass

    def tearDown(self):
        """
        Test tear down

        This is where you should tear down what you've setup in setUp before. This method is called after every test.
        """
        pass
