"""Finte state automata and recognizer.

Usage
-----
To run the program:
    > python fsa.py --path=<path> --string=<string> --task=<task>
where
    <path> is a path to a directory containing a FSA in file format
    <string> is a string to run through the FSA
    <task> is a task to run the FSA on. One of {'D1', 'D2', or 'D3'}

For help with the program:
    > python fsa.py -h
"""

from __future__ import annotations
import argparse
from pathlib import Path
from pprint import pformat
from typing import Dict, Set


class FSA:
    """Finite state automata capable of performing string recognition in three variations.

    Class Attributes
    ----------------
    states_file_name : str
        Name and suffix of file containing the FSA states
    final_states_file_name : str
        Name and suffix of file containing the FSA final states
    start_state_file_name : str
        Name and suffix of file containing the FSA start state
    alphabet_file_name : str
        Name and suffix of file containing the FSA alphabet
    trans_func_file_name : str
        Name and suffix of file containing the FSA transition function

    Attributes
    ----------
    states : Set[str]
        FSA states
    final_states : Set[str]
        FSA final states
    start_state : str
        FSA start state
    alphabet : Set[str]
        FSA alphabet of symbols
    trans_func : Dict[str, Dict[str, str]]
        FSA transition function, where trans_func[<state>][<symbol>] is the state the FSA should
            enter if the FSA is currently in state <state> and the input symbol on the tape is
            <symbol>

    Methods
    -------
    from_file(path: Path) -> FSA
        Instantiate a FSA from files inside of the directory, path
    recognize_member(string: str) -> bool
        Determine if a string is a member of the language recognized by the FSA
    recognize_endswith(string: str) -> bool
        Determine if a string ends with a member of the language recognized by the FSA
    recognize_substring(string: str) -> bool
        Determine if a string contains a member of the language recognized by the FSA

    Examples
    --------
    >>> fsa = FSA(
            states={"s0", "s1"},
            final_states={"s0"},
            start_state="s0",
            alphabet={"a", "b"},
            trans_func={
                "s0" : {"a" : "s1"},
                "s1" : {"b" : "s0"}
            }
        )
    >>> fsa.recognize_member("abab")
    True
    >>> fsa.recognize_member("ababa")
    False
    >>> fsa.recognize_endswith("xab")
    True
    >>> fsa.recognize_member("xabx")
    True
    >>> data = Path("./test/data")
    >>> fsa = FSA.from_file(data)
    >>> fsa.recognize_member("abab")
    True
    >>> print(fsa)
    ...
    >>> print(repr(fsa))
    ...
    """

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
        """Construct and

        Parameters
        ----------
        states : Set[str]
            FSA states
        final_states : Set[str]
            FSA final states
        start_state : str
            FSA start state
        alphabet : Set[str]
            FSA alphabet of symbols
        trans_func : Dict[str, Dict[str, str]]
            FSA transition function, where trans_func[<state>][<symbol>] is the state the FSA should
                enter if the FSA is currently in state <state> and the input symbol on the tape is
                <symbol>
        """

        self.states = states
        self.final_states = final_states
        self.start_state = start_state
        self.alphabet = alphabet
        self.trans_func = trans_func

    def __repr__(self) -> str:
        return (
            "FSA(\n"
            f"\tstates={self.states},\n"
            f"\tfinal_states={self.final_states},\n"
            f"\tstart_state={self.start_state},\n"
            f"\talphabet={self.alphabet},\n"
            f"\ttrans_func={self.trans_func},\n"
            ")"
        )

    def __str__(self) -> str:
        return (
            f"States:\n-------\n{pformat(self.states)}\n\n"
            f"Final States:\n-------------\n{pformat(self.final_states)}\n\n"
            f"Start State:\n------------\n{pformat(self.start_state)}\n\n"
            f"Alphabet:\n---------\n{pformat(self.alphabet)}\n\n"
            f"Transition Function:\n--------------------\n{pformat(self.trans_func)}\n\n"
        )

    def recognize_member(self, string: str) -> bool:
        """Determine if a string is a member of the language recognized by the FSA.

        Parameters
        ----------
        string : str
            The string to run through the FSA

        Returns
        -------
        bool
            Whether or not the FSA recognizes the string in member mode
        """

        current_state = self.start_state
        for index in range(len(string) + 1):
            if index == len(string):
                if current_state in self.final_states:
                    return True
                return False

            # Handle FSA rejection for partial transition function
            if string[index] not in self.trans_func[current_state]:
                return False

            current_state = self.trans_func[current_state][string[index]]

    def recognize_endswith(self, string: str) -> bool:
        """Determine if a string ends with a member of the language recognized by the FSA.

        Parameters
        ----------
        string : str
            The string to run through the FSA

        Returns
        -------
        bool
            Whether or not the FSA recognizes the string in endswith mode
        """

        # If the empty string is in the language, the string ends with empty string, so return True
        if self.recognize_member(""):
            return True

        current_state = self.start_state
        for index in range(len(string) + 1):
            # If at the end of string...
            if index == len(string):
                # ... and FSA says to accept...
                if current_state in self.final_states:
                    return True
                # ... if FSA not ready to accept and we cannot perform slicing...
                if string == "":
                    return False
                # ... otherwise trim first character of string and test again
                return self.recognize_endswith(string[1:])

            # If the FSA rejects, trim first character of string and test again
            if string[index] not in self.trans_func[current_state]:
                return self.recognize_endswith(string[1:])

            current_state = self.trans_func[current_state][string[index]]

    def recognize_substring(self, string: str) -> bool:
        """Determine if a string contains a member of the language recognized by the FSA.

        Parameters
        ----------
        string : str
            The string to run through the FSA

        Returns
        -------
        bool
            Whether or not the FSA recognizes the string in substring mode
        """

        # If the empty string is in the language, the empty string is a substring, so return True
        if self.recognize_member(""):
            return True

        current_state = self.start_state
        accept_status = current_state in self.final_states
        for index in range(len(string) + 1):
            # In substring mode, we return True if reaching an accept state at any point
            accept_status = current_state in self.final_states
            if accept_status:
                return True
            # If the string is empty, we cannot perform trimming, so just return current status
            if string == "":
                return accept_status
            # If at the end of string or FSA rejects, trim first character of string and test again
            if index == len(string) or string[index] not in self.trans_func[current_state]:
                return self.recognize_substring(string[1:])

            current_state = self.trans_func[current_state][string[index]]

        return accept_status

    @classmethod
    def from_file(cls: FSA, path: str) -> FSA:
        """Create a FSA from a file-based representation.

        Parameters
        ----------
        path : str
            Directory containing the FSA files

        Returns
        -------
        FSA
            FSA stored in this directory
        """

        path = Path(path)
        states = cls._extract_states(path / cls.states_file_name)
        final_states = cls._extract_final_states(path / cls.final_states_file_name)
        start_state = cls._extract_start_state(path / cls.start_state_file_name)
        alphabet = cls._extract_alphabet(path / cls.alphabet_file_name)
        trans_func = cls._extract_trans_func(path / cls.trans_func_file_name)

        return cls(states, final_states, start_state, alphabet, trans_func)

    @staticmethod
    def _extract_states(file: Path) -> Set[str]:
        """Extract FSA states from a file.

        Parameters
        ----------
        file : Path
            File containing FSA states

        Returns
        -------
        Set[str]
            FSA states
        """

        with open(file) as f:
            states = set(f.read().splitlines())
            return states

    @staticmethod
    def _extract_final_states(file: Path) -> Set[str]:
        """Extract FSA final states from a file.

        Parameters
        ----------
        file : Path
            File containing FSA final states

        Returns
        -------
        Set[str]
            FSA final states
        """

        with open(file) as f:
            final_states = set(f.read().splitlines())
            return set(final_states)

    @staticmethod
    def _extract_start_state(file: Path) -> str:
        """Extract FSA start state from a file.

        Parameters
        ----------
        file : Path
            File containing FSA start state

        Returns
        -------
        str
            FSA start state
        """

        with open(file) as f:
            start_state = f.read().splitlines()[0]
            return start_state

    @staticmethod
    def _extract_alphabet(file: Path) -> Set[str]:
        """Extract FSA alphabet from a file.

        Parameters
        ----------
        file : Path
            File containing FSA alphabet

        Returns
        -------
        Set[str]
            FSA alphabet
        """

        with open(file) as f:
            alphabet = set(f.read().splitlines())
            return alphabet

    @staticmethod
    def _extract_trans_func(file: Path) -> Dict[str, Dict[str, str]]:
        """Extract FSA transition function from a file.

        Parameters
        ----------
        file : Path
            File containing FSA transtion function

        Returns
        -------
        Dict[str, Dict[str, str]]
            FSA transition function
        """

        with open(file) as f:
            trans_func = set(f.read().replace(" ", "").splitlines())
            return_dic = {}
            for item in trans_func:
                if "NULL" not in item:
                    a_list = item.split(",")
                    if a_list[0] not in return_dic:
                        return_dic[a_list[0]] = {a_list[1]: a_list[2]}
                    else:
                        return_dic[a_list[0]][a_list[1]] = a_list[2]
            return return_dic


def main(path: Path, test_str: str, task: str) -> None:
    """Run the tasks described in the project description.

    Parameters
    ----------
    path : Path
        Direcotry containing the FSA files
    test_str : str
        The string to run through the FSA
    task : str
        The task to perform described in the project description. One of {'D1', 'D2', 'D3'}.
    """

    fsa = FSA.from_file(path)

    if task == "D1":
        result = fsa.recognize_member(test_str)
    elif task == "D2":
        result = fsa.recognize_endswith(test_str)
    elif task == "D3":
        result = fsa.recognize_substring(test_str)
    else:
        raise ValueError(
            f"The task {task} was not recognized. The task should be in: {{'D1', 'D2', 'D3'}}."
        )

    print(f"Whether or not our FSA recognizes this string: {result}")


def debug():
    """For development and debugging."""

    pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=Path, help="Enter a path to the directory containing files.")
    parser.add_argument("--string", type=str, help="Enter a string to test on the FSA.")
    parser.add_argument("--task", type=str, help="Enter the task. One of {'D1', 'D2', 'D3'}.")
    parser.add_argument("--debug", action="store_true", default=False, help="For developers.")
    args = parser.parse_args()

    if args.debug:
        debug()
    else:
        main(args.path, args.string, args.task)
