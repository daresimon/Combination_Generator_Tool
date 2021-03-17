<!--
 * @Author: Desmond Goh
 * @Date: 2021-03-17 00:21:06
 * @LastEditTime: 2021-03-17 00:31:43
 * @LastEditors: Desmond Goh
 * @FilePath: /Combination_Generator_Tool/README.md
-->
# Combination Generator Tool

A simple tool for generating test cases or test data using one of two methods: All Pairs or Orthogonal Array Testing.\n
Generated test cases will be in the format: Test case {num} of {test_case_statement}: (parameter = variable) ... (n_parameter = n_variable)\n
Generated test data will be in the format: Dataset {num}: {"key": "value" ,..., "n_key": "n_value"}\n

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

## Modifications

To use generated test data directly for other purpose, edit "input_processor.py" to return generated test data list directly instead of formatting & showing as string in text box. Returned list contains each combination of request data in dictionary form
