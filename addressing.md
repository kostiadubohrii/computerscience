## Addressing 

Addressing modes - refers to the way in which the operating system directs ardretrieves data items held in memory
> There are 4 different addressing modes we need to be aware of:
- machine code instructions consist of 2 items ( Operand - address reference of the instruction 
 * address reference  in memory 
 * literal or constant that needs to be loaded
Operand values are determimed by the individyat instruction set determined by the profcessor manufacrurer:

Immediate addressing refers to the loading of the data item itself into memory 
```
LOAD [321] // load the number 321 into the accumulator 
``` 
Direct addressing refers to the address reference where tge data items in located LOAD 41 the data item 12 lives there.

Inderect Addressing accts as a lookup table pints to an address reference in memory which contains the address of the data item to be fetched. As example of where indirect addressing is used is where the OS is not aware on translation where part of the program file is stored. If we are going to use a library funcion incoperated into the program - indirect addressing would make reference to a look up table to locate tthe address of the library. regex, datetime, random, sqlite3, PyQt are incoperated / linked to in out program 
load the lookup table - looktable refers to another address somewhere and this constains the data iteself - uses 2 direct address regerennces. 
Indexed Addressing 

Relative addressing - refers to changes in the address held at the program counter when a branching condition is activated.
