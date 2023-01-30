## Operating system 
 * ***User management*** - create user profiles( security enforce rules related to the setting of passwords, frequency of change, strength of word - upper, lower and special characters awa  digits. Set different user access rights - fields we  can view access there are 3 levels read, write - edit / amend / full control 
 * ***Peripheral management***of how the OS communicates with other items of hardware. Device drivers each associated piece of hardware has its own processor instruction set, device drivers translate the signals sent from one device to another - send data to different peripherals and buffers - speed of transfer of data. 
 * ***Memory management*** - moving data from RAW to VM 2 methods  Paging and segmentation and within primary memory - registers (Immediate Access Store ) to RAM, cache speed of access to files held within
 * ***Allocation of processor time*** - 5 scheduling algorithms 1. Queues aka first come first served; 2. Shortest job first, shortest time remaining, Round Robin, Multi level feedback queues. Each process is allocated a portion of processor time, and this is determined by algorithms. Each task has a given priority determined by the algorithm's interrupt - determine the relative importance, place into the stack, program counter changes address to the ISR and this is processed before process tasks are popped off the stack and the program counter address is changed.
 * ***File management*** - creates folders, allows files to be moved, copied and archived 

Operating system architecture there are 3 main parts to an OS:

1) ***Kernal*** - is central component of the coputers os, provides the bridge between applications and the data at the hardware level. The kernal that responds to system calls, ahdlees interrupes and exceptions. This part of the OS control external hardware. Kernal has the ability to manipulate processor state - different processor states across different cores - kernal manages allocation of tasks across different cores - job scheduler within the OS which allocates different sections of the same task - different independent processes across different core processor 

Kernal provides the ability to different process to access to access files and maintains on the hard drive and in different locations in memory 
Meta Data
Author, file type, permissions and locations in memory. Each file in memory can be located over different secrors, clusters within the ard drivve - nodal address which points to the next part of the file. 

 - ***Processes*** ( one task that can be performed one process can be made of meny threads ) 
 - ***Threads*** ( is a child of some process which can communicate with the parent process and other process, ecxecute program code.
 - ***Handles*** 

System libraries are special library functions using applications which need to access Kernal fearures - dae / time library and the use of the system clock 
Maintenance of system utilities - organisation of files on the harddrive 

Types of operating system:
1) ***Distributed*** - spreads the work of the newtworking OS over a number of servers single process can be split up into several tasks - threads and these can be performed over several systems

2) ***Multitasking*** - that tasks can be performed to run in parallel shared acrosss a number of cores or independent processor units.
Embedded operating systems dedicated to processes which have a limited or single functionality, simple UI, programmed in low level lang.
Real time operating systems must be able to respond to inpiuts and sensors quickly chemical processing systems, self drive.


###Utility program 

***Utility program any program which helps with the mainteance of the computer system in particlar the operating system*** 
1. ***Defragmentation*** - program runs over several passes. It collates proups of related files into a close proxmity to each other in memory. At the end of passes the defragmentation program should have organixed files based on the file type and author and place them into consective places in memory orgonised by pages and segementations. 
2. ***Compretion*** - reduces the size of the file either held on hard drive or tto be transmitted Lossy - permanent loss of data held in the file - image file - dimensions, colour depth audio file time interval that passes between recording could cha nge the amot of data recorded at each moment - bit depth or the numberof channels. 
Lossless - this keeps the data file entire and intact but applies algorithms to reduce the size either when saving to the hard drive or when transmitting.
The algorithms are executed when the file in opened and the data restored. 
1. ***Dictionary encoding*** - works on text files
2. ***Run length encoding*** - used to coimpress image and audio files take small portion of the image and then the image dimensions and colour depth and reacreat the image of transmission eliminate pargs of the file that repeat foe example in audio repeating versus or chorus. 
3. ***Back up*** - full back up the contents of the had drive entire, incremental only files that have been changed since the last full back up.
4. ***Anti malwate*** - cnacs for it representations of files held on tthe harddrive of files off the internet - checks these against a known database of malware, viruses held. Try and clean the infected file, wuarantibbe the file, alert the user that the file exist, delete the file.
Malware / Virus checks have ai capable features installed which involve "heustics" involves the software makingg informed judgements within bounds of the algorithm used to create it. 
- Firewalls perform similar tasksexpect they monitor traffic of the internet. 
5. ***Encryption*** - take an item of data and scremble the date item that is unrecognisible to any intercepring 3rd party. The recipent of the message will need  to be sent a key. An altorithm can be applied to change the dataitem into an unrecognisble format. 
Writing an algorithm for an encryption program - the algorithm needs to input a stringg take each character of the string and shift the charasters along by a predesignated number entered by the user. 

MrTravi
NsUsbwj
Restrict the chatacter combinations of letter only use the asciiletters




