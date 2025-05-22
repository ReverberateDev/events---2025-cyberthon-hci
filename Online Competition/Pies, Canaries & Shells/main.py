from pwn import *
elf = ELF('./pies_canaries_and_shells', checksec=False)

print(f"Offset of print_title: {hex(elf.symbols['print_title'])}")
print(f"Offset of shell:       {hex(elf.symbols['shell'])}")
