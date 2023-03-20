# AP-2 Versuch 86 - Abstandsgesetz

This repository contains the python code used to analyse the data from our college projet on the inverse-square law for gamma radiators. For that we measure the detection rate with and without the radiation source.

## Notes when using juypter

1) Import the libraries except data1 and data2 from 'main.py'.
2) Copy all functions from functions.py into one box.
3) Copy the wanted data (except the imports) from data1.py and/or data2.py into another box. It's easier to use a separate boxes for each data set.
4) Remove 'f.' as a prefix from all function calls (that use this prefix).
5) Run the functions used to create the plots (i.e. 'MakeBasicPlotOne()'. This can be done in the same or a separate box.

Additional notes:

- If the Chi_square function thows 'index out of range' errors, please widen the 'parameter_range'.
- If your data shows unecpected tendencies (value-wise), please make sure that the variables from data1.py and data2.py don't use the same name for different values/value sets.
