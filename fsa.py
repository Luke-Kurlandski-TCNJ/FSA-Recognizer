"""Finte state automata and recognizer."""

from __future__ import annotations
import argparse
from pathlib import Path
from pprint import pformat
from typing import Dict, Set


class FSA:

    states_file_name = "states.txt"
    final_states_file_name = "finalStates.txt"
    start_state_file_name = "startState.txt"
    alphabet_file_name = "alphabet.txt"
    trans_func_file_name = "transitionTable.txt"

    def __init__(
        self,
        states: Set[str],
        final_states: Set[str],
        start_state: str,
        alphabet: Set[str],
        trans_func: Dict[str, Dict[str, str]],
    ) -> None:

        self.states = states
        self.final_states = final_states
        self.start_state = start_state
        self.alphabet = alphabet
        self.trans_func = trans_func

    def __repr__(self) -> str:
        return (
            f"States({self.states})\n"
            f"Final States({self.final_states})\n"
            f"Start States({self.start_state})\n"
            f"Alphabet({self.alphabet})\n"
            f"Transition Function({self.trans_func})\n"
        )

    def __str__(self) -> str:
        return (
            f"States:-------\n{pformat(self.states)}"
            f"Final States:-------------\n{pformat(self.final_states)}"
            f"Start States:------------\n{pformat(self.start_state)}"
            f"Alphabet:---------\n{pformat(self.alphabet)}"
            f"Transition Function:--------------------\n{pformat(self.trans_func)}"
        )

    # TODO: implement
    def _recognize(self, string: str, *, mode:str) -> bool:

        state = self.start_state
        accept = state in self.final_states
        for c in string:
            if mode == "base" and c not in self.trans_func[state]:
                return False
            elif mode == "ending" or mode == "substring":
                continue
            state = self.trans_func[state][c]
            accept = state in self.final_states

        return accept

    def recognize_membership(self, string):

        return self._recognize(string, mode="base")

    def recognize_endswith(self, string):

        return self._recognize(string, mode="ending")

    def recognize_substring(self, string):

        return self._recognize(string, mode="substring")

    @classmethod
    def from_file(cls: FSA, path: Path) -> FSA:

        states = cls.extract_states(path / cls.states_file_name)
        final_states = cls.extract_final_states(path / cls.final_states_file_name)
        start_state = cls.extract_start_state(path / cls.start_state_file_name)
        alphabet = cls.extract_alphabet(path / cls.alphabet_file_name)
        trans_func = cls.extract_trans_func(path / cls.trans_func_file_name)

        return cls(states, final_states, start_state, alphabet, trans_func)

    # TODO: implement
    @staticmethod
    def extract_states(file: Path) -> Set[str]:
        raise NotImplementedError()

    # TODO: implement
    @staticmethod
    def extract_final_states(file: Path) -> Set[str]:
        raise NotImplementedError()

    # TODO: implement
    @staticmethod
    def extract_start_state(file: Path) -> str:
        raise NotImplementedError()

    # TODO: implement
    @staticmethod
    def extract_alphabet(file: Path) -> Set[str]:
        raise NotImplementedError()

    # TODO: implement
    @staticmethod
    def extract_trans_func(file: Path) -> Dict[str, Dict[str, str]]:
        raise NotImplementedError()


def main(path: Path, test_str: str):

    fsa = FSA.from_file(path)
    result = fsa.recognize(test_str)
    print(f"Our FSA recognizes this string: {result}")

def test():
    f = FSA(
        states={"s0", "s1"},
        final_states={"s0"},
        start_state="s0",
        alphabet={"a", "b"},
        trans_func={
            "s0" : {"a" : "s1"},
            "s1" : {"b" : "s0"}
        }
    )

    true_strings = ["", "ab", "abab", "ababab"]
    false_strings = ["a", "b", "ba", "baba", "aba", "abb", "ababa", "ababb"]

    for s in true_strings:
        print(f.recognize(s))

if __name__ == "__main__":
    
    test()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path", type=Path, help="Enter a path to the directory containing files."
    )
    parser.add_argument("--string", type=str, help="Enter a string to test on the FSA.")
    args = parser.parse_args()

    main(args.path, args.string)
