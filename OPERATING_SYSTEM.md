## Operating system 
 * User management - create user profiles( security enforce rules related to the setting of passwords, frequency of change, strength of word - upper, lower and special characters awa  digits. Set different user access rights - fields we  can view access there are 3 levels read, write - edit / amend / full control 
 * Peripheral management of how the OS communicates with other items of hardware. Device drivers each associated piece of hardware has its own processor instruction set, device drivers translate the signals sent from one device to another - send data to different peripherals and buffers - speed of transfer of data. 
 * Memory management - moving data from RAW to VM 2 methods  Paging and segmentation and within primary memory - registers (Immediate Access Store ) to RAM, cache speed of access to files held within
 * Allocation of processor time - 5 scheduling algorithms 1. Queues aka first come first served; 2. Shortest job first, shortest time remaining, Round Robin, Multi level feedback queues. Each process is allocated a portion of processor time, and this is determined by algorithms. Each task has a given priority determined by the algorithm's interrupt - determine the relative importance, place into the stack, program counter changes address to the ISR and this is processed before process tasks are popped off the stack and the program counter address is changed.
 * File management - creates folders, allows files to be moved, copied and archived 

Operating system architecture there are 3 main parts to an OS
1) Kernal - is central component of the coputers os, provides the bridge between applications and the data at the hardware level. The kernal that responds to system calls, ahdlees interrupes and exceptions. This part of the OS control external hardware. Kernal has the ability to manipulate processor state - different processor states across different cores - kernal manages allocation of tasks across different cores - job scheduler within the OS which allocates different sections of the same task - different independent processes across different core processor 

####Kernal provides the ability to different process to access to access files and maintains on the hard drive and in different locations in memory 
Meta Data
Author, file type, permissions and locations in memory. Each file in memory can be located over different secrors, clusters within the ard drivve - nodal address which points to the next part of the file. 

 - Processes ( one task that can be performed one process can be made of meny threads ) 
 - Threads ( is a child of some process which can communicate with the parent process and other process, ecxecute program code.
 - Handles 

###System libraries are special library functions using applications which need to access Kernal fearures - dae / time library and the use of the system clock 
Maintenance of system utilities - organisation of files on the harddrive 









