section .data
        text1: db "What is ur name?\n"
        text1len: equ $-text1
        text2: db "Hello, "
        text2len: equ $-text2

section .bss
        name: resb 16

section .text
        global _start
        
_start:
        call _printText1
        call _setName
        call _printText2
        call _printName

        mov rax, 60
        mov rdi, 0
        syscall

_printText1:
        mov rax, 1
        mov rdi, 1
        mov rsi, text1
        mov rdx, text1len
        syscall
        ret

_setName:
        mov rax, 0
        mov rdi, 0
        mov rsi, resb
        mov rdx, 16
        syscall
        ret

_printText2:
        mov rax, 1
        mov rdi, 1
        mov rsi, text2
        mov rdx, text2len
        syscall
        ret

_printName:
        mov rax, 1
        mov rdi, 1
        mov rsi, name
        mov rdx, 16
        syscall
        ret
