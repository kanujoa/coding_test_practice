str = input()

number = ""     # ?«?λ§? ?΄κΈ? ?? κ°μ²΄λ₯? λ§λ€?΄ μ€??€.
for i in str:     # i? str? ????κ°? ??????€.
  if i.isdigit():     # λ¬Έμ iκ°? str type? ?«??Έμ§?λ₯? ??¨
    number += i     # μ°ΈμΌ κ²½μ° number? iλ₯? μΆκ??

for j in number:     # j? number? ????κ°? ?????¨
  if j == "0":     # jκ°? "0"?΄λ©? κ·Έκ²? ?? μ£Όμ΄?Ό ?¨.
    number = number.replace(j, "", 1)     # replaceλ₯? ?¬?©?  ??? ?­? λ³??? ?΄? μ£Όμ΄?Ό ??€. κ·Έλ¦¬κ³? replace? λ¬Έμ?΄ ??? ?΄?Ή?? λ¬Έμ λͺ¨λλ₯? μΉν?κΈ? ?λ¬Έμ 1κ°λ§ λ°κΎΈ?΄ μ£Όκ³  ?Ά?Όλ©? λ§μ??λ§μ κ°μλ₯? ? ?΄ μ£Όμ΄?Ό ??€.
  else:     # 0?΄ ?? ?«?κ°? ??€λ©? μ¦μ break    --> ?μͺ½μ 0λ§? ? κ±°λ  ? ?κ²? ?¨
    break
print(number)     # ?«? μΆλ ₯

number = int(number)      # ?½?λ₯? κ΅¬νκΈ? ??΄ str type? numberλ₯? int type?Όλ‘? ?λ³??
count = 0     # ?½?? κ°μ
for a in range(1, number+1):     # a? numberκΉμ??? ??°?
  if number % a == 0:     # numberκ°? aλ‘? ???΄ ?¨?΄μ§?λ©? κ·? aκ°? number? ?½?κ°? ?¨.
    count += 1     # count 1 μ¦κ??
print(count)     # count μΆλ ₯