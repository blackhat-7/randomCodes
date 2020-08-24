.global main

.data
        askName: .string "What's your name?\n"
        .equ askNameLen, askName
        name: .space 10

.text

main:
        mov $1, %rax
        mov $1, %rdi
        mov $askName, %rsi
        mov $askNameLen, %rdx
        syscall
        
        mov $0, %rax
        mov $0, %rdi
        mov $name, %rsi
        mov $10, %rdx
        syscall

        mov $1, %rax
        mov $1, %rdi
        mov $name, %rsi
        mov $10, %rdx
        syscall

        mov $60, %rax
        mov $0, %rdi
        syscall
        ret

