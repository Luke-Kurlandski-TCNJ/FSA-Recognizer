"""Tests for the finit state automata.

Note that finite state automata that accept the end string as a member of the language will accept
    any string for the endswith and substring task.
"""

from abc import ABC
from copy import deepcopy
from typing import List
from unittest import TestCase

from fsa import FSA


class TestLanguage(ABC):
    """Esnure the Finite State Automata correctly models a language.
    
    Tests one language using four equivalent FSA objects. Two FSA created from data structures and
        two created from file-based representations.

    Attributes
    ----------
    fsa_partial : FSA
        FSA using a partial transition function
    fsa_complete : FSA
        FSA using a complete transition function
    fsa_partial_file : FSA
        FSA using a complete transition function, extracted from a file
    fsa_complete_file : FSA
        FSA using a complete transition function, extracted from a file
    membership_true_inputs : List[str]
        Test strings which should evaluate to true for the membership task
    membership_false_inputs : List[str]
        Test strings which should evaluate to false for the membership task
    endswith_true_inputs : List[str]
        Test strings which should evaluate to true for the endswith task
    endswith_false_inputs : List[str]
        Test strings which should evaluate to false for the endswith task
    substring_true_inputs : List[str]
        Test strings which should evaluate to true for the substring task
    substring_false_inputs : List[str]
        Test strings which should evaluate to false for the substring task

    Methods
    -------
    runner
        Performs the assertion for all membership, endswith, and substring tests
    test_same_partial
        Ensure the partial FSA from data structures and files are the same
    test_same_complete
        Ensure the complete FSA from data structures and files are the same
    test_recognize_membership_partial
        Test the partial FSA on membership tasks
    test_recognize_membership_partial_file
        Test the partial FSA from file on membership tasks
    test_recognize_membership_complete
        Test the complete FSA on membership tasks
    test_recognize_membership_complete_file
        Test the complete FSA from file FSA on membership tasks
    test_recognize_endswith_partial
        Test the partial FSA on endswith tasks
    test_recognize_endswith_partial_file
        Test the partial FSA from file on endswith tasks
    test_recognize_endswith_complete
        Test the complete FSA on endswith tasks
    test_recognize_endswith_complete_file
        Test the complete FSA from file FSA on endswith tasks
    test_recognize_substring_partial
        Test the partial FSA on substring tasks
    test_recognize_substring_partial_file
        Test the partial FSA from file on substring tasks
    test_recognize_substring_complete
        Test the complete FSA on substring tasks
    test_recognize_substring_complete_file
        Test the complete FSA from file FSA on substring tasks
    """

    fsa_partial: FSA
    fsa_complete: FSA
    fsa_partial_file: FSA
    fsa_complete_file: FSA

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

    def test_same_partial(self):
        for attr in ("states", "final_states", "start_state", "alphabet", "trans_func"):
            self.assertEqual(
                getattr(self.fsa_partial, attr),
                getattr(self.fsa_partial_file, attr),
                msg=f"{attr} differs between fsas.",
            )

    def test_same_complete(self):
        for attr in ("states", "final_states", "start_state", "alphabet", "trans_func"):
            self.assertEqual(
                getattr(self.fsa_complete, attr),
                getattr(self.fsa_complete_file, attr),
                msg=f"{attr} differs between fsas.",
            )

    def test_recognize_membership_partial(self):
        self.runner(
            self.fsa_partial.recognize_member,
            self.membership_true_inputs,
            self.membership_false_inputs,
        )

    def test_recognize_membership_partial_file(self):
        self.runner(
            self.fsa_partial_file.recognize_member,
            self.membership_true_inputs,
            self.membership_false_inputs,
        )

    def test_recognize_membership_complete(self):
        self.runner(
            self.fsa_complete.recognize_member,
            self.membership_true_inputs,
            self.membership_false_inputs,
        )

    def test_recognize_membership_complete_file(self):
        self.runner(
            self.fsa_complete_file.recognize_member,
            self.membership_true_inputs,
            self.membership_false_inputs,
        )

    def test_recognize_endswith_partial(self):
        self.runner(
            self.fsa_partial.recognize_endswith,
            self.endswith_true_inputs,
            self.endswith_false_inputs,
        )

    def test_recognize_endswith_partial_file(self):
        self.runner(
            self.fsa_partial_file.recognize_endswith,
            self.endswith_true_inputs,
            self.endswith_false_inputs,
        )

    def test_recognize_endswith_complete(self):
        self.runner(
            self.fsa_complete.recognize_endswith,
            self.endswith_true_inputs,
            self.endswith_false_inputs,
        )

    def test_recognize_endswith_complete_file(self):
        self.runner(
            self.fsa_complete_file.recognize_endswith,
            self.endswith_true_inputs,
            self.endswith_false_inputs,
        )

    def test_recognize_substring_partial(self):
        self.runner(
            self.fsa_partial.recognize_substring,
            self.substring_true_inputs,
            self.substring_false_inputs,
        )

    def test_recognize_substring_partial_file(self):
        self.runner(
            self.fsa_partial_file.recognize_substring,
            self.substring_true_inputs,
            self.substring_false_inputs,
        )

    def test_recognize_substring_complete(self):
        self.runner(
            self.fsa_complete.recognize_substring,
            self.substring_true_inputs,
            self.substring_false_inputs,
        )

    def test_recognize_substring_complete_file(self):
        self.runner(
            self.fsa_complete_file.recognize_substring,
            self.substring_true_inputs,
            self.substring_false_inputs,
        )


class TestLanguage1(TestCase, TestLanguage):
    """Test the language of L = (ab)*"""

    def setUp(self) -> None:

        self.fsa_partial = FSA(
            states={"s0", "s1"},
            final_states={"s0"},
            start_state="s0",
            alphabet={"a", "b"},
            trans_func={"s0": {"a": "s1"}, "s1": {"b": "s0"}},
        )

        self.fsa_complete = FSA(
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

        self.fsa_partial_file = FSA.from_file("./data/1-partial")

        self.fsa_complete_file = FSA.from_file("./data/1-complete")

        self.membership_true_inputs = ["", "ab", "abab", "ababab"]
        self.membership_false_inputs = ["a", "b", "ba", "baba", "aba", "abb", "ababa", "ababb"]

        self.endswith_true_inputs = ["", "ab", "abab", "ababab"]
        self.endswith_true_inputs += ["xyz" + s for s in self.endswith_true_inputs]
        self.endswith_false_inputs = []

        self.substring_true_inputs = ["", "ab", "abab", "ababab"]
        self.substring_true_inputs += ["xyz" + s + "xyz" for s in self.substring_true_inputs]
        self.substring_false_inputs = []


class TestLanguage2(TestCase, TestLanguage):
    """Test the language of L = a(ba)*"""

    def setUp(self) -> None:

        self.fsa_partial = FSA(
            states={"s0", "s1"},
            final_states={"s1"},
            start_state="s0",
            alphabet={"a", "b"},
            trans_func={"s0": {"a": "s1"}, "s1": {"b": "s0"}},
        )

        self.fsa_complete = FSA(
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

        self.fsa_partial_file = FSA.from_file("./data/2-partial")

        self.fsa_complete_file = FSA.from_file("./data/2-complete")

        self.membership_true_inputs = ["a", "aba", "ababa", "abababa"]
        self.membership_false_inputs = ["", "b", "ba", "baba", "ab", "abab", "ababab", "abababbb"]

        self.endswith_true_inputs = ["a", "aba", "ababa", "abababa"]
        self.endswith_true_inputs += ["xyz" + s for s in self.endswith_true_inputs]
        self.endswith_false_inputs = ["", "b", "ab", "bab", "abab", "ababab", "abababbb"]
        self.endswith_false_inputs += ["xyz" + s for s in self.endswith_false_inputs]

        self.substring_true_inputs = ["a", "aba", "ababa", "abababa", "ba", "bab", "bbba", "bbbab"]
        self.substring_true_inputs += ["xyz" + s + "xyz" for s in self.substring_true_inputs]
        self.substring_false_inputs = ["", "b", "bb", "bbb"]


class TestLanguage3(TestCase, TestLanguage):
    """Test the language of L = a*b*"""

    def setUp(self) -> None:

        self.fsa_partial = FSA(
            states={"s0", "s1"},
            final_states={"s0", "s1"},
            start_state="s0",
            alphabet={"a", "b"},
            trans_func={
                "s0": {"a": "s0", "b": "s1"},
                "s1": {"b": "s1"},
            },
        )

        self.fsa_complete = FSA(
            states={"s0", "s1", "s"},
            final_states={"s0", "s1"},
            start_state="s0",
            alphabet={"b", "a"},
            trans_func={"s1": {"b": "s1"}, "s": {"a": "s", "b": "s"}, "s0": {"a": "s0", "b": "s1"}},
        )

        self.fsa_partial_file = FSA.from_file("./data/3-partial")

        self.fsa_complete_file = FSA.from_file("./data/3-complete")

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


class TestLanguage4(TestCase, TestLanguage):
    """Test the language of L = a*bb*"""

    def setUp(self) -> None:

        self.fsa_partial = FSA(
            states={"s0", "s1"},
            final_states={"s1"},
            start_state="s0",
            alphabet={"a", "b"},
            trans_func={
                "s0": {"a": "s0", "b": "s1"},
                "s1": {"b": "s1"},
            },
        )

        self.fsa_complete = FSA(
            states={"s0", "s1", "s"},
            final_states={"s1"},
            start_state="s0",
            alphabet={"b", "a"},
            trans_func={"s1": {"b": "s1"}, "s": {"a": "s", "b": "s"}, "s0": {"a": "s0", "b": "s1"}},
        )

        self.fsa_partial_file = FSA.from_file("./data/4-partial")

        self.fsa_complete_file = FSA.from_file("./data/4-complete")

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


class TestLanguage5(TestCase, TestLanguage):
    """Test the language of L = (ab*a)|(cd*c)|("")"""

    def setUp(self) -> None:

        self.fsa_partial = FSA(
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

        self.fsa_complete = FSA(
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

        self.fsa_partial_file = FSA.from_file("./data/5-partial")

        self.fsa_complete_file = FSA.from_file("./data/5-complete")

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


class TestLanguage6(TestCase, TestLanguage):
    """Test the language of L = (ab*)|(cd*)"""

    def setUp(self) -> None:

        self.fsa_partial = FSA(
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

        self.fsa_complete = FSA(
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

        self.fsa_partial_file = FSA.from_file("./data/6-partial")

        self.fsa_complete_file = FSA.from_file("./data/6-complete")

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
