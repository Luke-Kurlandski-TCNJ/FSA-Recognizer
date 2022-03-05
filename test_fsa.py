"""Tests for the finit state automata."""

from copy import deepcopy
from unittest import TestCase

from fsa import FSA

# (ab)*
fsa1 = FSA(
    states={"s0", "s1"},
    final_states={"s0"},
    start_state="s0",
    alphabet={"a", "b"},
    trans_func={
        "s0" : {"a" : "s1"},
        "s1" : {"b" : "s0"}
    }
)
fsa4 = deepcopy(fsa1)
fsa4.final_states = {"s1"}

# a*b*
fsa2 = FSA(
    states={"s0", "s1"},
    final_states={"s0", "s1"},
    start_state="s0",
    alphabet={"a", "b"},
    trans_func={
        "s0" : {"a" : "s0",
                "b" : "s1"},
        "s1" : {"b" : "s1"},
    }
)
fsa5 = deepcopy(fsa1)
fsa5.final_states = {"s1"}

# ab*a | cd*c | ""
fsa3 = FSA(
    states={"s0", "s1", "s2"},
    final_states={"s0"},
    start_state="s0",
    alphabet={"a", "b", "c", "d"},
    trans_func={
        "s0" : {"a" : "s2",
                "c" : "s1"},
        "s1" : {"c" : "s0",
                "d" : "s1"},
        "s2" : {"a" : "s0",
                "b" : "s2"}
    }
)
fsa6 = deepcopy(fsa1)
fsa6.final_states = {"s1"}

class TestFSA(TestCase):

    def _test_fsa(self, fsa, mode, true_strings, false_strings):

        for s in true_strings:
            self.assertTrue(fsa._recognize(s, mode=mode))

        for s in false_strings:
            self.assertFalse(fsa._recognize(s, mode=mode))

    def test_recognize_membership(self):

        mode = "base"

        # (ab)*
        fsa = deepcopy(fsa1)
        fsa.final_states = {}
        true_strings = ["", "ab", "abab", "ababab"]
        false_strings = ["a", "b", "ba", "baba", "aba", "abb", "ababa", "ababb"]
        self._test_fsa(fsa, mode, true_strings, false_strings)

        # a*b*
        fsa = fsa2
        true_strings = ["", "a", "aa", "aaa", "b", "bb", "bbb", "ab", "aabb"]
        false_strings = [i + "a" for i in true_strings[4:]]
        self._test_fsa(fsa, mode, true_strings, false_strings)

        # ab*a | cd*c | ""
        fsa = fsa3
        true_strings = ["", "aa", "aba", "abbba", "cc", "cdc", "cdddc"]
        false_strings = ["a", "b", "c", "d", "ab", "abaa", "abb", "cd", "cdd", "cdcc"]
        self._test_fsa(fsa, mode, true_strings, false_strings)

    def test_recognize_endswith(self):

        mode = "ending"

        # (ab)*
        fsa = fsa1
        true_strings = ["", "ab", "abab", "ababab"]
        false_strings = ["a", "b", "ba", "baba", "aba", "abb", "ababa", "ababb"]
        self._test_fsa(fsa, mode, true_strings + false_strings, [])

        # a*b*
        fsa = fsa2
        true_strings = ["", "a", "aa", "aaa", "b", "bb", "bbb", "ab", "aabb"]
        false_strings = [i + "a" for i in true_strings[4:]]
        self._test_fsa(fsa, mode, true_strings + false_strings, [])

        # ab*a | cd*c | ""
        fsa = fsa3
        true_strings = ["", "aa", "aba", "abbba", "cc", "cdc", "cdddc"]
        false_strings = ["a", "b", "c", "d", "ab", "abaa", "abb", "cd", "cdd", "cdcc"]
        self._test_fsa(fsa, mode, true_strings + false_strings, [])
