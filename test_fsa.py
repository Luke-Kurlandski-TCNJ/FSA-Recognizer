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

    # (ab*a)|(cd*c)|("")
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

    # (ab*)|(cd*)
    fsa6 = deepcopy(fsa5)
    fsa6.final_states = {"s1", "s2"}

    def _test_fsa(self, fsa, mode, true_strings, false_strings):

        for s in true_strings:
            if mode == "member":
                self.assertTrue(fsa.recognize_member(s))
            elif mode == "endswith":
                self.assertTrue(fsa.recognize_endswith(s))
            elif mode == "substring":
                self.assertTrue(fsa.recognize_substring(s))

        for s in false_strings:
            if mode == "member":
                self.assertFalse(fsa.recognize_member(s))
            elif mode == "endswith":
                self.assertFalse(fsa.recognize_endswith(s))
            elif mode == "substring":
                self.assertFalse(fsa.recognize_substring(s))

    def test_recognize_membership1(self):
        """Test the language of (ab)* for membership recognition."""

        true_strings = ["", "ab", "abab", "ababab"]
        false_strings = ["a", "b", "ba", "baba", "aba", "abb", "ababa", "ababb"]

        self._test_fsa(self.fsa1, "member", true_strings, false_strings)

    def test_recognize_membership2(self):
        """Test the language of a(ba)* for membership recognition."""

        true_strings = ["a", "aba", "ababa", "abababa"]
        false_strings = ["", "b", "ba", "baba", "ab", "abab", "ababab", "abababbb"]

        self._test_fsa(self.fsa2, "member", true_strings, false_strings)

    def test_recognize_membership3(self):
        """Test the language of a*b* for membership recognition."""

        true_strings = ["", "a", "aa", "aaa", "b", "bb", "bbb", "ab", "aabb"]
        false_strings = ["ba", "bba", "bbba", "aba", "aabba"]

        self._test_fsa(self.fsa3, "member", true_strings, false_strings)

    def test_recognize_membership4(self):
        """Test the language of a*bb* for membership recognition."""

        true_strings = ["b", "ab", "bb", "abb", "aabb", "aabbb"]
        false_strings = ["", "a", "ba", "aba", "abba", "bba"]

        self._test_fsa(self.fsa4, "member", true_strings, false_strings)

    def test_recognize_membership5(self):
        """Test the language of (ab*a)|(cd*c)|("") for membership recognition."""

        true_strings = ["", "aa", "aba", "abbba", "cc", "cdc", "cdddc"]
        false_strings = ["a", "b", "c", "d", "ab", "abaa", "abb", "cd", "cdd", "cdcc"]

        self._test_fsa(self.fsa5, "member", true_strings, false_strings)

    def test_recognize_membership6(self):
        """Test the language of (ab*)|(cd*) for membership recognition."""

        true_strings = ["a", "ab", "abbb", "c", "cd", "cdd"]
        false_strings = ["", "b", "d", "ba", "dc", "aba", "abc", "abd", "cdc", "cda", "cdb"]

        self._test_fsa(self.fsa6, "member", true_strings, false_strings)

    ################################################################################################

    def test_recognize_endswith1(self):
        """Test the language of (ab)* for endswith recognition."""

        true_strings = ["", "ab", "abab", "ababab"]
        true_strings += ["xyz" + s for s in true_strings]
        false_strings = []

        self._test_fsa(self.fsa1, "endswith", true_strings, false_strings)

    def test_recognize_endswith2(self):
        """Test the language of a(ba)* for endswith recognition."""

        true_strings = ["a", "aba", "ababa", "abababa"]
        true_strings += ["xyz" + s for s in true_strings]
        false_strings = ["", "b", "ab", "bab", "abab", "ababab", "abababbb"]
        false_strings += ["xyz" + s for s in false_strings]

        self._test_fsa(self.fsa2, "endswith", true_strings, false_strings)

    def test_recognize_endswith3(self):
        """Test the language of a*b* for endswith recognition."""

        true_strings = ["", "a", "aa", "aaa", "b", "bb", "bbb", "ab", "aabb"]
        true_strings += ["xyz" + s for s in true_strings]
        false_strings = []

        self._test_fsa(self.fsa3, "endswith", true_strings, false_strings)

    def test_recognize_endswith4(self):
        """Test the language of a*bb* for endswith recognition."""

        true_strings = ["b", "ab", "bb", "abb", "aabb", "aabbb"]
        true_strings += ["xyz" + s for s in true_strings]
        false_strings = ["", "a", "ba", "aba", "abba", "bba"]
        false_strings += ["xyz" + s for s in false_strings]

        self._test_fsa(self.fsa4, "endswith", true_strings, false_strings)

    def test_recognize_endswith5(self):
        """Test the language of (ab*a)|(cd*c)|("") for endswith recognition."""

        true_strings = ["", "aa", "aba", "abbba", "cc", "cdc", "cdddc"]
        true_strings += ["xyz" + s for s in true_strings]
        false_strings = []
        false_strings += ["xyz" + s for s in false_strings]

        self._test_fsa(self.fsa5, "endswith", true_strings, false_strings)

    def test_recognize_endswith6(self):
        """Test the language of (ab*)|(cd*) for endswith recognition."""

        true_strings = ["a", "ab", "abbb", "c", "cd", "cdd"]
        true_strings += ["xyz" + s for s in true_strings]
        false_strings = ["", "b", "d", "abd", "cdb"]
        false_strings += ["xyz" + s for s in false_strings]

        self._test_fsa(self.fsa6, "endswith", true_strings, false_strings)

    ################################################################################################

    def test_recognize_substring1(self):
        """Test the language of (ab)* for substring recognition."""

        true_strings = ["", "ab", "abab", "ababab"]
        true_strings += ["xyz" + s + "xyz" for s in true_strings]
        false_strings = []

        self._test_fsa(self.fsa1, "substring", true_strings, false_strings)

    def test_recognize_substring2(self):
        """Test the language of a(ba)* for substring recognition."""

        true_strings = ["a", "aba", "ababa", "abababa", "bbba", "bbbab"]
        true_strings += ["xyz" + s + "xyz" for s in true_strings]
        false_strings = ["", "b", "bb"]

        self._test_fsa(self.fsa2, "substring", true_strings, false_strings)

    def test_recognize_substring3(self):
        """Test the language of a*b* for substring recognition."""

        true_strings = ["", "a", "aa", "aaa", "b", "bb", "bbb", "ab", "aabb"]
        true_strings += ["xyz" + s for s in true_strings]
        false_strings = []

        self._test_fsa(self.fsa3, "substring", true_strings, false_strings)

    def test_recognize_substring4(self):
        """Test the language of a*bb* for substring recognition."""

        true_strings = ["b", "ab", "bb", "abb", "aabb", "aabbb"]
        true_strings += ["xyz" + s + "xyz" for s in true_strings]
        false_strings = ["", "a", "aa", "aaa"]

        self._test_fsa(self.fsa4, "substring", true_strings, false_strings)

    def test_recognize_substring5(self):
        """Test the language of (ab*a)|(cd*c)|("") for substring recognition."""

        true_strings = ["", "aa", "aba", "abbba", "cc", "cdc", "cdddc"]
        true_strings += ["xyz" + s + "xyz" for s in true_strings]
        false_strings = []

        self._test_fsa(self.fsa5, "substring", true_strings, false_strings)

    def test_recognize_substring6(self):
        """Test the language of (ab*)|(cd*) for substring recognition."""

        true_strings = ["a", "ab", "abbb", "c", "cd", "cdd", "ac", "ca"]
        true_strings += ["xyz" + s + "xyz" for s in true_strings]
        false_strings = ["", "b", "d", "bd", "db", "bdb", "dbd"]
        false_strings += ["xyz" + s for s in false_strings]

        self._test_fsa(self.fsa6, "substring", true_strings, false_strings)
