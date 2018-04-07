global main
extern printf


section .data
	RESULT dq 0
	N dq 5


section .text
	main:
		push qword [N]
		call Factorial
		mov rdi, rax
		call printResult
		ret

	message:
	db "%lu", 0x0A, 0x0D, 0


	Factorial:
		push rbp
		mov rbp, rsp
		mov rbx, qword [rbp + 16]
		cmp rbx, 1
		jle move
		mov rcx, rbx
		dec rcx
		push rcx
		call Factorial
		mov rbx, qword [rbp + 16]
		mul rbx
		jmp endCode

	move:
		mov rax, 1
	endCode:
		pop rbp
		ret 8
	
	printResult:
		push rbp
		mov rbp, rsp
		sub rsp, 8
		mov rsi, rdi
		mov rdi, message
		mov qword [rbp - 8], 0
		mov al, 0
		call printf
		mov rsi, 0
		mov rax, rsi
		add rsp, 8
		pop rbp
		ret
