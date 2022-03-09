# Instructions

As dev1@elsa.hpc.tcnj.edu,
```
module add python/3.7.5
cd project1
```

To run the program:
```
python3 fsa.py --path=<path> --string=<string> --task=<task>
```

where
- `<path>` is a path to the directory containing the FSA files, e.g., './data/1-complete',
- `<string>` is a string to test the above FSA on, e.g., 'ababab', and
- `<task>` is used to determine which deliverable should be run, one of 'D1', 'D2', or 'D3'.

For help with the program:
```
python3 fsa.py -h
```

To run unit tests:
```
python3 -m unittest
```

# Deliverables

- D1: fsa.FSA.recognize_member
- D2: fsa.FSA.recognize_endswith
- D3: fsa.FSA.recognize_substring
- D4:
	- L = `<regex>`
		- `<equivalent FSA using a complete transition function (mathematical FSA definition)>`
		- `<equivalent FSA using a partial transition function (convenient FSA definition)>`
		- `<unit tests class testing the language>`
	- L = (ab)*
		- data/1-complete
		- data/1-partial
		- test_fsa.TestFSA1
	- L = a(ba)*
		- data/2-complete
		- data/2-partial
		- test_fsa.TestFSA2
	- L = a*b*
		- data/3-complete
		- data/3-partial
		- test_fsa.TestFSA3
	- L = a*bb*
		- data/4-complete
		- data/4-partial
		- test_fsa.TestFSA4
	- L = (ab*a)|(cd*c)|("")
		- data/5-complete
		- data/5-partial
		- test_fsa.TestFSA5
	- L = (ab*)|(cd*)
		- data/6-complete
		- data/6-partial
		- test_fsa.TestFSA6
- D5: report.pdf
- D6: README.md
