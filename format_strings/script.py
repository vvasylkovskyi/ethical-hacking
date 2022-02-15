
from pwn import ELF

elf = ELF('./bin')
target_address = elf.symbols['target']

print("Address: ", target_address)

# 134520896
