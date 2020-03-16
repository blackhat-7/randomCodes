global printResult
global maxof3

section .data
    
    num: db 0
    numLen: equ $-num

section .text
    
maxof3:
    mov rax, rdi
    cmp rax, rsi
    cmovl rax, rsi
    cmp rax, rdx
    cmovl rax, rdx
    mov [num], rax
    syscall
    call printResult

    mov rax, 60
    mov rdi, 0
    syscall

printResult:
    mov rax, 1
    mov rdi, 1
    mov rsi, [num]
    mov rdx, numLen
    syscall
    ret


