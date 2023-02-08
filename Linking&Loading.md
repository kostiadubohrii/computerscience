Compilation and translation of program code 
How jprogram gets granslated  into machine code 
1. Lexical analyser - removes white spancce, comments assigns tokens, 
2. Syntax analyser - tokens are checked to see if they match the rules of the language, Backus Naur form( the  rules  for enforcing the syntex ot the language<br>
Checks the spelling and the grammar rules - estavlich the rules of precedence of a language - ccreated an avstra t syntax tree when a set program insturctino are parsed 
then we use Reverse Polish Notation 
3. Code generation and oprimisation <br>
Starts the process of translating each line of High lvl lenguage into processor specific machine code using the instuction set. <br> 

There is one to many relationships between 1 line of HLL code and machine code <br>
Allocates physical addresses where mach9ine code instructions are stored, reginster usage is opromised 

## Linking and loading

### Linking
A compilation factor is where programs are using external or internal library functrions and how rherse are managed. Linking can be done in 2 ways the library 
itself can be incorporated into the program itself include a complete file for all libraries - tkinter, PyQt, Sqlite, os, datetime, rendom, csv.<br>
<br>
We dont need to use all of them, makes the fiels mush biggeer oonger to load, slowerr access times. We create a link and keep the files seperate - located in close proxmity import not all library functions 

### Loading
Is when the software is installed onto the drive - download, there is a operating system utility program called a loader and ites role is to load the library - incolved DLL - loader will need install the relevant library and create a logical address and read in 


> Some applications can be designed to run on a virtual machine, they represent a generic computer but can emulate the running of soft ware on a given platform. Intermediate code is code produced for a virtual machine is portable and can run across platforms and is ued to test, judge the edxperience of runnign the application on different processor architectues. Intermediate code is the half way house between high lvl code (HLL) and machine code. It is generated as an intermediatte step in the proccess of compiling or interpretating sourcce code.
