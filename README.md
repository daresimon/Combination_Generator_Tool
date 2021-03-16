<!--
 * @Author: Desmond Goh
 * @Date: 2021-03-17 00:21:06
 * @LastEditTime: 2021-03-17 00:31:43
 * @LastEditors: Desmond Goh
 * @FilePath: /Combination_Generator_Tool/README.md
-->
# Combination Generator Tool

A simple tool for generating test cases or test data using one of two methods: All Pairs or Orthogonal Array Testing. 
Generated test cases will be in the format: Test case {num} of {test_case_statement}: (parameter = variable) ... (n_parameter = n_variable)
Generated test data will be in the format: Dataset {num}: {"key": "value" ,..., "n_key": "n_value"}

## Getting Started

    

### Prerequisites

```
AllPairs package
Numpy package
Pandas package
```

### Installing

Clone the project to local 
Run pip install to download required packages

```
pip install -r requirements.txt
```

### Running Program

Run main script to start the program:

```
combination_generator_tool.py
```