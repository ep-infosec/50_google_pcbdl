#!/usr/bin/env python3

# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from pcbdl import *

class TestNet(unittest.TestCase):
    def test_create(self):
        """Net creation test"""
        n = Net("test_create")

    def test_duplicate(self):
        Net("create_duplicate")
        with self.assertRaises(Exception):
            Net("create_duplicate")

    def test_str(self):
        """Net naming, both uppercasing and anonymous nets"""
        n = Net("test_str")
        self.assertEqual(str(n), "TEST_STR")

        n = Net()
        self.assertIn("anon", str(n).lower())

    def test_repr(self):
        """Net representations should pretty and contain some info about what's connected"""
        n = Net()
        self.assertIn("unconnected", repr(n))

        r0 = R()
        n << r0
        self.assertIn("connected", repr(n))
        self.assertIn(r0.refdes, repr(n))

        r1 = R()
        n << r1
        self.assertIn(",", repr(n), "there should be a comma separated list of components")
        self.assertIn(r1.refdes, repr(n))

        for i in range(100):
            n << R()
        self.assertIn(str(len(n.connections)), repr(n),
                      "we should show the number of connections after we can't display them all")

    def test_connections(self):
        """Various Net connection tests"""
        n = Net()
        rs = R(), R()

        # Adding by part, chaining
        n << rs[0] << rs[1]

        self.assertEqual({c.part for c in n.connections}, set(rs), "<< failed")

        # Adding by specific pin
        n << R().P1
        self.assertEqual(len(n.connections), 3, "<< on a pin failed")

        # Adding a whole list of things instead of chaining
        n << (R() for i in range(10))

        self.assertEqual(len(n.connections), 13, "<< on a list failed")

        with self.assertRaises(TypeError, msg="this would be silly to work, connecting something of a random type to a net"):
            n << 2

class DefinedAtTest(unittest.TestCase):
    """Make sure all the part/net .defined_at point to this file, not something inside the library proper."""

    def check_defined_at(self, o):
        self.assertIn(__file__, o.defined_at, "%r.defined_at should point to this file, not something inside the library proper." % o)

    def test_created_net(self):
        n = Net()
        self.check_defined_at(n)

    def test_part(self):
        p = Part()
        self.check_defined_at(p)

    def test_implicit_net(self):
        r = R()
        n = r.P1.net
        self.check_defined_at(n)

        tp = TP()
        n = tp.net
        self.check_defined_at(n)

class PartTest(unittest.TestCase):
    def test_automatic_name_collision(self):
        """Can we make a lot of uniquely named resistors"""
        parts = []
        names = set()
        for i in range(1000):
            r = R()
            parts.append(r)
            refdes = r.refdes
            self.assertNotIn(refdes, names)
            names.add(refdes)

    def test_duplicate(self):
        """We shouldn't allow 2 parts with the same refdes."""
        Part(refdes="duplicate_part")
        with self.assertRaises(Exception):
            Part(refdes="duplicate_part")

    def test_part_naming(self):
        p = Part()
        p.refdes = "naming_test"
        self.assertEqual(p.refdes, "NAMING_TEST")

    def test_repr_str(self):
        """Part __repr__ and __str__ contains part refdes"""
        p = Part()
        self.assertIn(p.refdes, str(p))
        self.assertIn(p.refdes, repr(p))

if __name__ == "__main__":
    unittest.main()
