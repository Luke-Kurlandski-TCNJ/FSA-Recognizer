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
	- test_fsa.TestFSA1: L = (ab)*
	- test_fsa.TestFSA2: L = a(ba)*
	- test_fsa.TestFSA3: L = a*b*
	- test_fsa.TestFSA4: L = a*bb*
	- test_fsa.TestFSA5: L = (ab*a)|(cd*c)|("")
	- test_fsa.TestFSA6: L = (ab*)|(cd*)
- D5: report.pdf
- D6: README.md
