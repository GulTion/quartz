---
subject: COA
type: ShortNotes
sr-due: 2023-12-17
sr-interval: 1
sr-ease: 130
---

#note



Pin diagram of 8085 microprocessor is as given below: 

![](https://media.geeksforgeeks.org/wp-content/uploads/8085-PIN-1.png)

**1. Address Bus and Data Bus:**   
The address bus is a group of sixteen lines i.e A0-A15. The address bus is unidirectional, i.e., bits flow in one direction from the microprocessor unit to the peripheral devices and uses the high order address bus. 

**2. Control and Status Signals:**   
 

- **ALE –** It is an Address Latch Enable signal. It goes high during first T state of a machine cycle and enables the lower 8-bits of the address, if its value is 1 otherwise data bus is activated. 
    
- **IO/M’ –** It is a status signal which determines whether the address is for input-output or memory. When it is high(1) the address on the address bus is for input-output devices. When it is low(0) the address on the address bus is for the memory. 
    
- **SO, S1 –** These are status signals. They distinguish the various types of operations such as halt, reading, instruction fetching or writing.   
     

|IO/M’|S1|S0|Data Bus Status|
|---|---|---|---|
|0|1|1|Opcode fetch|
|0|1|0|Memory read|
|0|0|1|Memory write|
|1|1|0|I/O read|
|1|0|1|I/O write|
|1|1|1|Interrupt acknowledge|
|0|0|0|Halt|

- **RD’ –** It is a signal to control READ operation. When it is low the selected memory or input-output device is read. 
    
- **WR’ –** It is a signal to control WRITE operation. When it goes low the data on the data bus is written into the selected memory or I/O location. 
    
- **READY –** It senses whether a peripheral is ready to transfer data or not. If READY is high(1) the peripheral is ready. If it is low(0) the microprocessor waits till it goes high. It is useful for interfacing low speed devices.   
     

**3. Power Supply and Clock Frequency:** 

- **Vcc –** +5v power supply 
    
- **Vss –** Ground Reference 
    
- **XI, X2 –** A crystal is connected at these two pins. The frequency is internally divided by two, therefore, to operate a system at 3MHZ the crystal should have frequency of 6MHZ. 
    
- **CLK (OUT) –** This signal can be used as the system clock for other devices.   
     
    
    **4. Interrupts and Peripheral Initiated Signals:**   
    The 8085 has five interrupt signals that can be used to interrupt a program execution. 
    
    (i) INTR   
    (ii) RST 7.5   
    (iii) RST 6.5   
    (iv) RST 5.5   
    (v) TRAP 
    
    The microprocessor acknowledges Interrupt Request by INTA’ signal. In addition to Interrupts, there are three externally initiated signals namely RESET, HOLD and READY. To respond to HOLD request, it has one signal called HLDA. 
    
- **INTR –** It is an interrupt request signal. 
    
- **INTA’ –** It is an interrupt acknowledgement sent by the microprocessor after INTR is received.   
     

**5. Reset Signals:** 

- **RESET IN’ –** When the signal on this pin is low(0), the program-counter is set to zero, the buses are tristated and the microprocessor unit is reset. 
    
- **RESET OUT –** This signal indicates that the MPU is being reset. The signal can be used to reset other devices.   
     

**6. DMA Signals:** 

- **HOLD –** It indicates that another device is requesting the use of the address and data bus. Having received HOLD request the microprocessor relinquishes the use of the buses as soon as the current machine cycle is completed. Internal processing may continue. After the removal of the HOLD signal the processor regains the bus. 
    
- **HLDA –** It is a signal which indicates that the hold request has been received after the removal of a HOLD request, the HLDA goes low.   
     

**7. Serial I/O Ports:**   
Serial transmission in 8085 is implemented by the two signals, 

- **SID and SOD –** SID is a data line for serial input where as SOD is a data line for serial output.   
     

###  Advantages of the 8085 microprocessor pin diagram:

- The pin diagram is easy to understand and remember because of its logical and systematic arrangement.  
     
- It has a simple structure with fewer pins compared to other microprocessors, making it easy to design and implement in electronic circuits.  
     
- It has a dedicated pin for interrupt handling, which makes it easy to interface with external devices that require interrupt-driven communication.  
     

### Disadvantages of the 8085 microprocessor pin diagram:

- It has limited addressing capability due to its 8-bit architecture, which can limit its use in applications that require large amounts of memory.  
     
- It has a limited number of pins, which can be a constraint in designing complex systems that require more input/output devices or peripherals.  
     
- It has separate pins for input/output and memory access, which can make it more difficult to design memory-mapped input/output circuits.
