```
a = while n < 10: ##b I am trying to assign variable to key word while
  a = a + 12 

Every pease of code has to pass through the 3 grate test.

Compilation sesies 
1) Lexical analyser - get rid of all whitespaces, comments 
Tokenises the code organises them into token 
5 token 
1. Operators ( +, -, //, div,  == ) 
2. Assigment =
3. Key word - case, switch, while , input , for , if , elif, else, , input, ptint, in , enumerate, range
4. Litterals, constants 
5. User defined variables (arrays, variables, lists, data structure) f
Data dictionary aka symbol data where meta data anout the data structures is stored
Token stream - is the order in which the program instructions are going to be executed as defined by the user

Code at this stage is passed through to the syntax analiser
1) Does the code contain any words not matchibng the dictionary of key word? 

Write the set of rules for setting up Natianal Instruction number 
<letter><letter><digit><digit><digit><digit><letter> 
2)
  
  when programs  are executed in a computer they have to unambiguous. At this stage the syntax analyser creates and abstract syntax tree. The syntax tree is a 
  unambiguous struccture which can be guranteed syntacticalluy correct and only reqadvable in one way.
  2*3+4 
  the rules regarding the interpretation of processing is also set down 
  BIDMAS 
  Alsom when interpreting instructions we use a stack and all instructions are interpretaated using RPN Reverse Polish Notation tree structure and post fixed 
  notation 
2 + 3
23+ 
CODE GENERATION this occurs once the AST has been created and checked againsts the rules of the language 
  Convert each line of high lvl code into machine / processor specific machine code consisting of OpCode and Operands. Each line of HHL has a one to many relationship with Macine code allocate registers in the processor - translate logical addresses 
  strMessage 
  spread across different areas on the hard drives each with individual address refferences oprmosies to seek efficient the use of the registers.
  
  
  
  ```
  
  
  
  
  
  
  
  
