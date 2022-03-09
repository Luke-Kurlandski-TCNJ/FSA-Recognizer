"""Tests for the finit state automata.

Note that finite state automata that accept the end string as a member of the language will accept
    any string for the endswith and substring task.
"""

from abc import ABC
from copy import deepcopy
from typing import List
from unittest import TestCase

from fsa import FSA


class TestFSA(ABC):

    fsa_simple: FSA
    fsa_full: FSA
    fsa_simple_file: FSA
    fsa_full_file: FSA

    membership_true_inputs: List[str]
    membership_false_inputs: List[str]

    endswith_true_inputs: List[str]
    endswith_false_inputs: List[str]

    substring_true_inputs: List[str]
    substring_false_inputs: List[str]

    def runner(self, recognize, true_inputs, false_inputs):
        for s in true_inputs:
            self.assertTrue(recognize(s), msg=f"Expected True on {s}, but got {recognize(s)}.")
        for s in false_inputs:
            self.assertFalse(recognize(s), msg=f"Expected False on {s}, but got {recognize(s)}.")

    def test_same_simple(self):
        for attr in ("states", "final_states", "start_state", "alphabet", "trans_func"):
            self.assertEqual(
                getattr(self.fsa_simple, attr),
                getattr(self.fsa_simple_file, attr),
                msg=f"{attr} differs between fsas.",
            )

    def test_same_full(self):
        for attr in ("states", "final_states", "start_state", "alphabet", "trans_func"):
            self.assertEqual(
                getattr(self.fsa_full, attr),
                getattr(self.fsa_full_file, attr),
                msg=f"{attr} differs between fsas.",
            )

    def test_recognize_membership_simple(self):
        self.runner(
            self.fsa_simple.recognize_member,
            self.membership_true_inputs,
            self.membership_false_inputs,
        )

    def test_recognize_membership_simple_file(self):
        self.runner(
            self.fsa_simple_file.recognize_member,
            self.membership_true_inputs,
            self.membership_false_inputs,
        )

    def test_recognize_membership_full(self):
        self.runner(
            self.fsa_full.recognize_member,
            self.membership_true_inputs,
            self.membership_false_inputs,
        )

    def test_recognize_membership_full_file(self):
        self.runner(
            self.fsa_full_file.recognize_member,
            self.membership_true_inputs,
            self.membership_false_inputs,
        )

    def test_recognize_endswith_simple(self):
        self.runner(
            self.fsa_simple.recognize_endswith,
            self.endswith_true_inputs,
            self.endswith_false_inputs,
        )

    def test_recognize_endswith_simple_file(self):
        self.runner(
            self.fsa_simple_file.recognize_endswith,
            self.endswith_true_inputs,
            self.endswith_false_inputs,
        )

    def test_recognize_endswith_full(self):
        self.runner(
            self.fsa_full.recognize_endswith,
            self.endswith_true_inputs,
            self.endswith_false_inputs,
        )

    def test_recognize_endswith_full_file(self):
        self.runner(
            self.fsa_full_file.recognize_endswith,
            self.endswith_true_inputs,
            self.endswith_false_inputs,
        )

    def test_recognize_substring_simple(self):
        self.runner(
            self.fsa_simple.recognize_substring,
            self.substring_true_inputs,
            self.substring_false_inputs,
        )

    def test_recognize_substring_simple_file(self):
        self.runner(
            self.fsa_simple_file.recognize_substring,
            self.substring_true_inputs,
            self.substring_false_inputs,
        )

    def test_recognize_substring_full(self):
        self.runner(
            self.fsa_full.recognize_substring,
            self.substring_true_inputs,
            self.substring_false_inputs,
        )

    def test_recognize_substring_full_file(self):
        self.runner(
            self.fsa_full_file.recognize_substring,
            self.substring_true_inputs,
            self.substring_false_inputs,
        )


class TestFSA1(TestCase, TestFSA):
    """Test the language of L = (ab)*"""

    def setUp(self) -> None:

        self.fsa_simple = FSA(
            states={"s0", "s1"},
            final_states={"s0"},
            start_state="s0",
            alphabet={"a", "b"},
            trans_func={"s0": {"a": "s1"}, "s1": {"b": "s0"}},
        )

        self.fsa_full = FSA(
            states={"s0", "s", "s1"},
            final_states={"s0"},
            start_state="s0",
            alphabet={"b", "a"},
            trans_func={
                "s0": {"a": "s1", "b": "s"},
                "s1": {"b": "s0", "a": "s"},
                "s": {"b": "s", "a": "s"},
            },
        )

        self.fsa_simple_file = FSA.from_file("./data/1-simple")

        self.fsa_full_file = FSA.from_file("./data/1-full")

        self.membership_true_inputs = ["", "ab", "abab", "ababab"]
        self.membership_false_inputs = ["a", "b", "ba", "baba", "aba", "abb", "ababa", "ababb"]

        self.endswith_true_inputs = ["", "ab", "abab", "ababab"]
        self.endswith_true_inputs += ["xyz" + s for s in self.endswith_true_inputs]
        self.endswith_false_inputs = []

        self.substring_true_inputs = ["", "ab", "abab", "ababab"]
        self.substring_true_inputs += ["xyz" + s + "xyz" for s in self.substring_true_inputs]
        self.substring_false_inputs = []


class TestFSA2(TestCase, TestFSA):
    """Test the language of L = a(ba)*"""

    def setUp(self) -> None:

        self.fsa_simple = FSA(
            states={"s0", "s1"},
            final_states={"s1"},
            start_state="s0",
            alphabet={"a", "b"},
            trans_func={"s0": {"a": "s1"}, "s1": {"b": "s0"}},
        )

        self.fsa_full = FSA(
            states={"s0", "s", "s1"},
            final_states={"s1"},
            start_state="s0",
            alphabet={"b", "a"},
            trans_func={
                "s0": {"a": "s1", "b": "s"},
                "s1": {"b": "s0", "a": "s"},
                "s": {"b": "s", "a": "s"},
            },
        )

        self.fsa_simple_file = FSA.from_file("./data/2-simple")

        self.fsa_full_file = FSA.from_file("./data/2-full")

        self.membership_true_inputs = ["a", "aba", "ababa", "abababa"]
        self.membership_false_inputs = ["", "b", "ba", "baba", "ab", "abab", "ababab", "abababbb"]

        self.endswith_true_inputs = ["a", "aba", "ababa", "abababa"]
        self.endswith_true_inputs += ["xyz" + s for s in self.endswith_true_inputs]
        self.endswith_false_inputs = ["", "b", "ab", "bab", "abab", "ababab", "abababbb"]
        self.endswith_false_inputs += ["xyz" + s for s in self.endswith_false_inputs]

        self.substring_true_inputs = ["a", "aba", "ababa", "abababa", "ba", "bab", "bbba", "bbbab"]
        self.substring_true_inputs += ["xyz" + s + "xyz" for s in self.substring_true_inputs]
        self.substring_false_inputs = ["", "b", "bb", "bbb"]


class TestFSA3(TestCase, TestFSA):
    """Test the language of L = a*b*"""

    def setUp(self) -> None:

        self.fsa_simple = FSA(
            states={"s0", "s1"},
            final_states={"s0", "s1"},
            start_state="s0",
            alphabet={"a", "b"},
            trans_func={
                "s0": {"a": "s0", "b": "s1"},
                "s1": {"b": "s1"},
            },
        )

        self.fsa_full = FSA(
            states={"s0", "s1", "s"},
            final_states={"s0", "s1"},
            start_state="s0",
            alphabet={"b", "a"},
            trans_func={"s1": {"b": "s1"}, "s": {"a": "s", "b": "s"}, "s0": {"a": "s0", "b": "s1"}},
        )

        self.fsa_simple_file = FSA.from_file("./data/3-simple")

        self.fsa_full_file = FSA.from_file("./data/3-full")

        self.membership_true_inputs = ["", "a", "aa", "aaa", "b", "bb", "bbb", "ab", "aabb"]
        self.membership_false_inputs = ["ba", "bba", "bbba", "aba", "aabba"]

        self.endswith_true_inputs = ["", "a", "aa", "aaa", "b", "bb", "bbb", "ab", "aabb"]
        self.endswith_true_inputs += ["a" + s for s in self.endswith_true_inputs]
        self.endswith_true_inputs += ["ba" + s for s in self.endswith_true_inputs]
        self.endswith_true_inputs += ["xyz" + s for s in self.endswith_true_inputs]
        self.endswith_false_inputs = []

        self.substring_true_inputs = ["", "a", "aa", "aaa", "b", "bb", "bbb", "ab", "aabb"]
        self.substring_true_inputs += ["xyz" + s + "xyz" for s in self.substring_true_inputs]
        self.substring_false_inputs = []


class TestFSA4(TestCase, TestFSA):
    """Test the language of L = a*bb*"""

    def setUp(self) -> None:

        self.fsa_simple = FSA(
            states={"s0", "s1"},
            final_states={"s1"},
            start_state="s0",
            alphabet={"a", "b"},
            trans_func={
                "s0": {"a": "s0", "b": "s1"},
                "s1": {"b": "s1"},
            },
        )

        self.fsa_full = FSA(
            states={"s0", "s1", "s"},
            final_states={"s1"},
            start_state="s0",
            alphabet={"b", "a"},
            trans_func={"s1": {"b": "s1"}, "s": {"a": "s", "b": "s"}, "s0": {"a": "s0", "b": "s1"}},
        )

        self.fsa_simple_file = FSA.from_file("./data/4-simple")

        self.fsa_full_file = FSA.from_file("./data/4-full")

        self.membership_true_inputs = ["b", "ab", "bb", "abb", "aabb", "aabbb"]
        self.membership_false_inputs = ["", "a", "ba", "aba", "abba", "bba"]
        self.membership_false_inputs += [s + "a" for s in self.membership_true_inputs]

        self.endswith_true_inputs = ["b", "ab", "bb", "abb", "aabb", "aabbb"]
        self.endswith_true_inputs += ["a" + s for s in self.endswith_true_inputs]
        self.endswith_true_inputs += ["ba" + s for s in self.endswith_true_inputs]
        self.endswith_true_inputs += ["xyz" + s for s in self.endswith_true_inputs]
        self.endswith_false_inputs = ["", "a", "ba", "aba", "abba", "bba"]
        self.endswith_false_inputs += ["xyz" + s for s in self.endswith_false_inputs]

        self.substring_true_inputs = ["b", "ab", "bb", "aab", "abb", "aabb", "aabbb"]
        self.substring_true_inputs += ["xyz" + s + "xyz" for s in self.substring_true_inputs]
        self.substring_false_inputs = ["", "a", "aa", "aaa"]


class TestFSA5(TestCase, TestFSA):
    """Test the language of L = (ab*a)|(cd*c)|("")"""

    def setUp(self) -> None:

        self.fsa_simple = FSA(
            states={"s0", "s1", "s2"},
            final_states={"s0"},
            start_state="s0",
            alphabet={"a", "b", "c", "d"},
            trans_func={
                "s0": {"a": "s2", "c": "s1"},
                "s1": {"c": "s0", "d": "s1"},
                "s2": {"a": "s0", "b": "s2"},
            },
        )

        self.fsa_full = FSA(
            states={"s0", "s1", "s", "s2"},
            final_states={"s0"},
            start_state="s0",
            alphabet={"b", "d", "a", "c"},
            trans_func={
                "s0": {"c": "s1", "b": "s", "d": "s", "a": "s2"},
                "s1": {"c": "s0", "a": "s", "d": "s1", "b": "s"},
                "s": {"b": "s", "a": "s", "c": "s", "d": "s"},
                "s2": {"a": "s0", "c": "s", "b": "s2", "d": "s"},
            },
        )

        self.fsa_simple_file = FSA.from_file("./data/5-simple")

        self.fsa_full_file = FSA.from_file("./data/5-full")

        self.membership_true_inputs = ["", "aa", "aba", "abbba", "cc", "cdc", "cdddc"]
        self.membership_false_inputs = [
            "a",
            "b",
            "c",
            "d",
            "ab",
            "abaa",
            "abb",
            "cd",
            "cdd",
            "cdcc",
        ]

        self.endswith_true_inputs = ["", "aa", "aba", "abbba", "cc", "cdc", "cdddc"]
        self.endswith_true_inputs += ["b" + s for s in self.endswith_true_inputs]
        self.endswith_true_inputs += ["d" + s for s in self.endswith_true_inputs]
        self.endswith_true_inputs += ["xyz" + s for s in self.endswith_true_inputs]
        self.endswith_false_inputs = []

        self.substring_true_inputs = ["", "aa", "aba", "abbba", "cc", "cdc", "cdddc"]
        self.substring_true_inputs += ["b" + s + "d" for s in self.substring_true_inputs]
        self.substring_true_inputs += ["d" + s + "b" for s in self.substring_true_inputs]
        self.substring_true_inputs += ["xyz" + s + "xyz" for s in self.substring_true_inputs]
        self.substring_false_inputs = []


class TestFSA6(TestCase, TestFSA):
    """Test the language of L = (ab*)|(cd*)"""

    def setUp(self) -> None:

        self.fsa_simple = FSA(
            states={"s0", "s1", "s2"},
            final_states={"s1", "s2"},
            start_state="s0",
            alphabet={"a", "b", "c", "d"},
            trans_func={
                "s0": {"a": "s2", "c": "s1"},
                "s1": {"c": "s0", "d": "s1"},
                "s2": {"a": "s0", "b": "s2"},
            },
        )

        self.fsa_full = FSA(
            states={"s0", "s1", "s", "s2"},
            final_states={"s1", "s2"},
            start_state="s0",
            alphabet={"b", "d", "a", "c"},
            trans_func={
                "s0": {"c": "s1", "b": "s", "d": "s", "a": "s2"},
                "s1": {"c": "s0", "a": "s", "d": "s1", "b": "s"},
                "s": {"b": "s", "a": "s", "c": "s", "d": "s"},
                "s2": {"a": "s0", "c": "s", "b": "s2", "d": "s"},
            },
        )

        self.fsa_simple_file = FSA.from_file("./data/6-simple")

        self.fsa_full_file = FSA.from_file("./data/6-full")

        self.membership_true_inputs = ["a", "ab", "abbb", "c", "cd", "cdd"]
        self.membership_false_inputs = [
            "",
            "b",
            "d",
            "ba",
            "dc",
            "aba",
            "abc",
            "abd",
            "cdc",
            "cda",
            "cdb",
        ]

        self.endswith_true_inputs = ["a", "ab", "abbb", "c", "cd", "cdd"]
        self.endswith_true_inputs += ["b" + s for s in self.endswith_true_inputs]
        self.endswith_true_inputs += ["d" + s for s in self.endswith_true_inputs]
        self.endswith_true_inputs += ["xyz" + s for s in self.endswith_true_inputs]
        self.endswith_false_inputs = ["", "b", "d", "abd", "cdb"]
        self.endswith_false_inputs += ["xyz" + s for s in self.endswith_false_inputs]

        self.substring_true_inputs = ["a", "ab", "abbb", "c", "cd", "cdd", "ac", "ca"]
        self.substring_true_inputs += ["b" + s + "d" for s in self.substring_true_inputs]
        self.substring_true_inputs += ["d" + s + "b" for s in self.substring_true_inputs]
        self.substring_true_inputs += ["xyz" + s + "xyz" for s in self.substring_true_inputs]
        self.substring_false_inputs = ["", "b", "d", "bd", "db", "bdb", "dbd"]
