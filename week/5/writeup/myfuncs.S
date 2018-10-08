; STOS = stores string
; rdi = 1st arg (string pointer)
; rsi = 2nd arg (char)
; rdx = 3rd arg (how many letters)

section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous functions stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame
        ;your code goes here!
        mov rcx, rdx  ;moves 3rd argument to counter register       
L1:
        mov [rdi], sil;deref rdi (1st arg) and set it equal to char in sil
        add rdi, 1    ;inc
        loop L1
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous functions stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame


        ;;;;;;;;;;;;;;;;;;;;;
        ;your code goes here!
        ;;;;;;;;;;;;;;;;;;;;;
        mov rcx, rdx
L2:     
        mov al, [rsi] ;deref rsi and move it to temp register
        mov [rdi], al ;deref rdi and move val at temp register in
        add rdi, 1    ;inc
        add rsi, 1    ;inc
        loop L2

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
