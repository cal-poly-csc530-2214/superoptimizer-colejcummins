# superoptimizer-colejcummins
superoptimizer-colejcummins created by GitHub Classroom

I ultimately decided to try and create a super-optimizer from scratch in Python, which, given the search space and slower speed of Python as a language,
was much more difficult than expected. I used a significantly reduced 8086 instruction set, only 6 registers, and immediate values only between 15 and -15.
Given that Python also gives the user very little access to underlying aspects of a system such as binary values and opcodes, translating 8086 operations
and binary instruction took up most of my time. The un-optimized and prunes search space of this set is 10 instructions, 6 registers, 32 immediate values
and 6 registers for the second operand of most instructions giving a total of approximately 2000 possible instructions per line. With each line adding 
another power, the total unpruned search space for just 4 lines is 2000 ^ 4 or 1.6 * 10 ^ 13 possible programs, a ludicrous number to compute in a reasonable 
time frame given the program is running in python. Ultimately, with optimizations if the total number of possible instructions is brought down to about <100
per line, the search space becomes much more reasonable. I would love to have progressed more on adding optimizations but became too bogged down in implimentation
details. 
