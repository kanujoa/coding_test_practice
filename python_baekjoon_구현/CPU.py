n = int(input())     # 명령어의 개수

zero_to_four = {'ADD': '0000', 'SUB': '0001', 'MOV': '0010', 'AND': '0011', 'OR': '0100', 'NOT': '0101', 'MULT': '0110', 'LSFTL': '0111', 'LSFTR': '1000', 'ASFTR': '1001', 'RL': '1010', 'RR': '1011'}

for _ in range(n):
    # 명령어 입력 받기
    command = input().split()
    opcode = command[0]
    rD = int(command[1])
    rA = int(command[2])
    rB = int(command[3])
    
    # opcode 2진수로 알아내기 (위에서 str형의 opcode를 통해)
    if opcode[-1] == 'C':
        opcode = zero_to_four[opcode[:-1]] + '1'
    else:
        opcode = zero_to_four[opcode] + '0'
    
    # rD 알아내기 (rD 입력을 3bit의 이진수로 변환)
    rD_binary = str(bin(rD))[2:]
    rD = '0' * (3 - len(rD_binary)) + rD_binary
    
    # rA 알아내기 (rA를 3bit의 이진수로 변환)
    rA_binary = str(bin(rA))[2:]
    rA = '0' * (3 - len(rA_binary)) + rA_binary

    # rB / C# 알아내기 (opcode의 4번째 bit가 0이면 레지스터 rB(3bit 이진수), 1일 경우 상수 C#(4bit 이진수) 사용)
    if opcode[4] == '0':
        rB_binary = str(bin(rB))[2:]
        rB = '0' * (3 - len(rB_binary)) + rB_binary
        print(opcode + '0' + rD + rA + rB + '0')
    else:
        c_sharp_binary = str(bin(rB))[2:]
        c_sharp = '0' * (4 - len(c_sharp_binary)) + c_sharp_binary
        print(opcode + '0' + rD + rA + c_sharp)