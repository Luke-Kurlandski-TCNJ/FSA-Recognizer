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
	- test_fsa.TestFSA.fsa1: L = (ab)*
		- test_fsa.TestFSA.test_recognize_membership1
		- test_fsa.TestFSA.test_recognize_endswith1
		- test_fsa.TestFSA.test_recognize_substring1
	- test_fsa.TestFSA.fsa2: L = a(ba)*
		- test_fsa.TestFSA.test_recognize_membership2
		- test_fsa.TestFSA.test_recognize_endswith2
		- test_fsa.TestFSA.test_recognize_substring2
	- test_fsa.TestFSA.fsa3: L = a*b*
		- test_fsa.TestFSA.test_recognize_membership3
		- test_fsa.TestFSA.test_recognize_endswith3
		- test_fsa.TestFSA.test_recognize_substring3
	- test_fsa.TestFSA.fsa4: L = a*bb*
		- test_fsa.TestFSA.test_recognize_membership4
		- test_fsa.TestFSA.test_recognize_endswith4
		- test_fsa.TestFSA.test_recognize_substring4
	- test_fsa.TestFSA.fsa5: L = (ab*a)|(cd*c)|("")
		- test_fsa.TestFSA.test_recognize_membership5
		- test_fsa.TestFSA.test_recognize_endswith5
		- test_fsa.TestFSA.test_recognize_substring5
	- test_fsa.TestFSA.fsa6: L = (ab*)|(cd*)
		- test_fsa.TestFSA.test_recognize_membership6
		- test_fsa.TestFSA.test_recognize_endswith6
		- test_fsa.TestFSA.test_recognize_substring6
- D5: report.pdf
- D6: README.md
