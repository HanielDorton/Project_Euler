
ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def translatenumbers(number):
    answer = ''
    if number == 1000:
        answer = 'onethousand'
        number = 0
    if number > 99:
        answer += ones[int(number/100)-1]
        answer+='hundred'
        number = number%100
        if number > 0:
            answer+='and'
    if number > 19:
        answer += tens[int(number/10)-1]
        number = number%10
    if 0 < number < 20 :
        answer += ones[number-1]
    return len(answer)


solution=0
for i in range(1,1001):
    solution+= translatenumbers(i)
print(solution)
input()









