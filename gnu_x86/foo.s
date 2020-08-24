.global main

.data
    hello: .string "Hello\n"
    .equ helloLen, hello
    fmt: .string "%ld\n"
    num1: .long 1234234
    .equ num1Len, num1
    num2: .long 23432
    .equ num2Len, num2


.text

main:
    /*
    push num1
    push num2
    
    call _add
    
    push %rax
    push $fmt
    call printf
    */
    
    push $hello
    push $fmt
    call printf
    call exit

_add:
    pop %rax
    pop %rbx
    add %rbx, %rax
    ret
