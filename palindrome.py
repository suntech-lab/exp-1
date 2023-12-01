palindrome = str(input('enter your palindrome: '))

small_index = 0
large_index = -1

for i in range(len(palindrome)//2):
    
    if palindrome[small_index] != palindrome[large_index]:
        print('this is not a palindrome')
        break

    elif palindrome[small_index] == palindrome[large_index]:
        small_index += 1
        large_index = large_index - 1
        print('this is a palindrome')
        break

