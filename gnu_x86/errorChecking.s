mov $100, 100
movb $100, 100
movl $100, 100
movl $100, 100(%eax, %edx, 8)
add $100, 100(%eax, %edx, 8)
addw $100, 100(%eax, %edx, 8)
add $100, %eax
add %eax, %ecx
lea %eax, %eax
lea (%eax), %eax
lea 100(%eax), %eax
lea %eax, 100(%eax)
ret
jmp 0x100
jmpw 0x100
jmp *0x100
jmpb *0x100
jmpw *0x100
cmp %eax, (%eax)
cmp $100, (%eax)
cmpb $100, (%eax)
je 0x100
je *0x100
jne 0x100
ja 0x100
jb 0x100
jae 0x100
call 0x100
call *0x100
callb *0x100
and %eax, (%eax)
and %eax, %ecx
pushb %al
pushw %ax
push %eax
shl $12, %eax
shr $12, %eax
or $0x100, %eax
xor $100, %eax
xchg %eax, %ecx
xchg %eax, (%ecx)
xadd %eax, (%ecx)
pushfl
popfl
lahf
sahf
rdtsc

