"""Tests for the finit state automata.

Note that finite state automata that accept the end string as a member of the language will accept
    any string for the endswith and substring task.
"""

from copy import deepcopy
from unittest import TestCase

from fsa import FSA


class TestFSA(TestCase):

    # (ab)*
    fsa1 = FSA(
        states={"s0", "s1"},
        final_states={"s0"},
        start_state="s0",
        alphabet={"a", "b"},
        trans_func={"s0": {"a": "s1"}, "s1": {"b": "s0"}},
    )

    # a(ba)*
    fsa2 = deepcopy(fsa1)
    fsa2.final_states = {"s1"}

    # a*b*
    fsa3 = FSA(
        states={"s0", "s1"},
        final_states={"s0", "s1"},
        start_state="s0",
        alphabet={"a", "b"},
        trans_func={
            "s0": {"a": "s0", "b": "s1"},
            "s1": {"b": "s1"},
        },
    )

    # a*bb*
    fsa4 = deepcopy(fsa3)
    fsa4.final_states = {"s1"}

    # ab*a | cd*c | ""
    fsa5 = FSA(
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

    # ab* | cd*
    fsa6 = deepcopy(fsa5)
    fsa6.final_states = {"s1", "s2"}

    def _test_fsa(self, fsa, mode, true_strings, false_strings):

        for s in true_strings:
            self.assertTrue(fsa._recognize(s, mode=mode))

        for s in false_strings:
            self.assertFalse(fsa._recognize(s, mode=mode))

    def test_recognize_membership1(self, mode="member"):
        # (ab)*
        fsa = self.fsa1
        true_strings = ["", "ab", "abab", "ababab"]
        false_strings = ["a", "b", "ba", "baba", "aba", "abb", "ababa", "ababb"]
        self._test_fsa(fsa, mode, true_strings, false_strings)

    def test_recognize_membership2(self, mode="member"):
        # a(ba)*
        fsa = self.fsa2
        true_strings = ["a", "aba", "ababa", "abababa"]
        false_strings = ["", "b", "ba", "baba", "ab", "abab", "ababab", "abababbb"]
        self._test_fsa(fsa, mode, true_strings, false_strings)

    def test_recognize_membership3(self, mode="member"):
        # a*b*
        fsa = self.fsa3
        true_strings = ["", "a", "aa", "aaa", "b", "bb", "bbb", "ab", "aabb"]
        false_strings = ["ba", "bba", "bbba", "aba", "aabba"]
        self._test_fsa(fsa, mode, true_strings, false_strings)

    def test_recognize_membership4(self, mode="member"):
        # a*bb*
        fsa = self.fsa4
        true_strings = ["b", "ab", "bb", "abb", "aabb", "aabbb"]
        false_strings = ["", "a", "ba", "aba", "abba", "bba"]
        self._test_fsa(fsa, mode, true_strings, false_strings)

    def test_recognize_membership5(self, mode="member"):
        # ab*a | cd*c | ""
        fsa = self.fsa5
        true_strings = ["", "aa", "aba", "abbba", "cc", "cdc", "cdddc"]
        false_strings = ["a", "b", "c", "d", "ab", "abaa", "abb", "cd", "cdd", "cdcc"]
        self._test_fsa(fsa, mode, true_strings, false_strings)

    def test_recognize_membership6(self, mode="member"):
        # ab* | cd*
        fsa = self.fsa6
        true_strings = ["a", "ab", "abbb", "c", "cd", "cdd"]
        false_strings = ["", "b", "d", "ba", "dc", "aba", "abc", "abd", "cdc", "cda", "cdb"]
        self._test_fsa(fsa, mode, true_strings, false_strings)

    ################################################################################################

    def test_recognize_endswith1(self, mode="endswith"):
        # (ab)*
        fsa = self.fsa1

        true_strings = ["", "ab", "abab", "ababab"]
        false_strings = []

        true_strings += ["xyz" + s for s in true_strings]
        false_strings += ["xyz" + s for s in false_strings]

        self._test_fsa(fsa, mode, true_strings, false_strings)

    def test_recognize_endswith2(self, mode="endswith"):
        # a(ba)*
        fsa = self.fsa2

        true_strings = ["a", "aba", "ababa", "abababa"]
        false_strings = ["", "b", "ab", "bab", "abab", "ababab", "abababbb"]

        true_strings += ["xyz" + s for s in true_strings]
        false_strings += ["xyz" + s for s in false_strings]

        self._test_fsa(fsa, mode, true_strings, false_strings)

    def test_recognize_endswith3(self, mode="endswith"):
        # a*b*
        fsa = self.fsa3

        true_strings = ["", "a", "aa", "aaa", "b", "bb", "bbb", "ab", "aabb"]
        false_strings = []

        true_strings += ["xyz" + s for s in true_strings]
        false_strings += ["xyz" + s for s in false_strings]

        self._test_fsa(fsa, mode, true_strings, false_strings)

    def test_recognize_endswith4(self, mode="endswith"):
        # a*bb*
        fsa = self.fsa4

        true_strings = ["b", "ab", "bb", "abb", "aabb", "aabbb"]
        false_strings = ["", "a", "ba", "aba", "abba", "bba"]

        true_strings += ["xyz" + s for s in true_strings]
        false_strings += ["xyz" + s for s in false_strings]

        self._test_fsa(fsa, mode, true_strings, false_strings)

    def test_recognize_endswith5(self, mode="endswith"):
        # ab*a | cd*c | ""
        fsa = self.fsa5

        true_strings = ["", "aa", "aba", "abbba", "cc", "cdc", "cdddc"]
        false_strings = []

        true_strings += ["xyz" + s for s in true_strings]
        false_strings += ["xyz" + s for s in false_strings]

        self._test_fsa(fsa, mode, true_strings, false_strings)

    def test_recognize_endswith6(self, mode="endswith"):
        # ab* | cd*
        fsa = self.fsa6

        true_strings = ["a", "ab", "abbb", "c", "cd", "cdd"]
        false_strings = ["", "b", "d", "abd", "cdb"]

        true_strings += ["xyz" + s for s in true_strings]
        false_strings += ["xyz" + s for s in false_strings]

        self._test_fsa(fsa, mode, true_strings, false_strings)
