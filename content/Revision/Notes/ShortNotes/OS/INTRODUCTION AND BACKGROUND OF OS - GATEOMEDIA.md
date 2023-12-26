---
type: ShortNotes
subject: OS
atQ: 0
sr-due: 2024-02-18
sr-interval: 65
sr-ease: 209
---
#note
#card/OS/introduction
what is multiprogramming
?
- ==Multiple programs/jobs== reside in the main memory for execution. The operating system selects and executes one of these jobs on to the CPU.
- If the job in execution requires an I/O operation, ==another== job which is ready for execution is scheduled on the CPU.
- increased CPU utilization.
- Increased throughput of the system. <!--SR:!2024-01-25,65,310-->


what is multitasking
?
- ==Multi-tasking== is a logical extension of multi-programming systems. The jobs are executed on the CPU in time sharing mode.
- The main advantage of multi-tasking systems is good response time. <!--SR:!2023-11-29,6,250-->


Real time operating system::![[Pasted image 20231021220801.png]] <!--SR:!2023-12-12,31,270-->


Long-term scheduler::![[Pasted image 20231021221034.png]] <!--SR:!2024-01-23,63,310-->


Medium-term scheduler::![[Pasted image 20231021221056.png]] <!--SR:!2023-12-06,25,270-->


Short-term scheduler::![[Pasted image 20231021221119.png]] <!--SR:!2024-01-18,58,310-->


##### In multithreading, the threads of the same process share, which of the things
?
- user address space,
- files,
- signal and
- semaphore
- signal handlers etc. <!--SR:!2023-11-24,3,230-->


##### In multithreading, each thread has its own, which of the things
?
- stack,
- thread id,
- CPU state information (control and status registers, stack pointers) and
- scheduling information (thread state, priority etc.). <!--SR:!2023-11-27,6,250-->


User level threads versus kernel level threads::![[Pasted image 20231021221810.png]] <!--SR:!2024-01-17,55,310-->

![[Pasted image 20231215200908.png]]