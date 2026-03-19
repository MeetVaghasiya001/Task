# def print_n_nums(n):
#     if n == 0:
#         return 0
#     print(n)
#     print_n_nums(n-1)
# print(print_n_nums(11))


# def range_number(start,end):
#     if start > end:
#         return 
#     print(start)
#     range_number(start+1,end)
# print(range_number(100,110))



# def fibo(n):
#     if n<=1:
#         return n
#     return fibo(n-1) + fibo(n-2)
# print(fibo(10))



# def reverse_str(s):
#     if len(s) == 0:
#         return s
#     return reverse_str(s[1:]) +s[0]
# print(reverse_str('meet'))



# def count_digit(s):
#     if s =='':
#         return 0
#     count = 1 if s[0] in '0123456789' else 0 
#     return count + count_digit(s[1:])
# print(count_digit('meet001'))

# def prime(n,i=2):
#     if n < 1:
#         return 'enter correct number'
#     if i*i=>n:
#         return 'prime'
    
#     if n % i == 0:
#         return 'Not Prime'
    
#     return prime(n,i+1)
# print(prime(2))

# def even(n):
#     if n == 0:
#         return 
#     even(n-1)
#     if n % 2 == 0:
#         print(n)
    
# print(even(10))


# def ele_sum(lst,n):
#     if n == 0:
#         return 0
#     return lst[n-1] + ele_sum(lst,n-1)
# lst=[10,20,30]
# print(ele_sum(lst,len(lst)))
    

# def to_n(n):
#     if n==0:
#         return
#     print(n)
#     to_n(n-1)
# print(to_n(5))

# def sum_n(n):
#     if n == 0:
#         return 0
#     return n + sum_n(n-1)
# print(sum_n(4))

# def print_all(lst,l):
#     if l == 0:
#         return 0
#     print(lst[l-1])
#     print_all(lst,l-1)

# lst=[10,20,30]
# print(print_all(lst,len(lst)))


# prime number with while loop 

# n = 2
# i = 2 
# is_prime = True
# while i < n :
#     if n % i == 0:
#         print('not prime!')
#         is_prime = False
#     i+=1
# if is_prime:
#     print('Prime!')

# def prime_n(n,i=2):
#     if n < 1:
#         return 'enter correct number!'
#     if i > n//2:
#         return 'Prime!'
#     if n % i == 0:
#         return 'Not Prime!'
#     return prime_n(n,i+1)
# print(prime_n(2))


#! Found vowels with recurtion

# s = 'meet'
# i = 0 
# count=0
# while i < len(s):
#     if s[i] in 'aeiouAEIOU':
#         count +=1
#     i+=1
# print(count)

# def vowel(s,i=0,count=0):
#     if i > len(s):
#         return 0
#     if s[i-1] in 'aeiouAEIOU':
#         count += 1
#     return count + vowel(s,i+1)
# print(vowel('meet'))


#! print all element in reverse from given list 


# def print_all(lst,l):
#     if l == 0:
#         return 0
#     print_all(lst,l-1)
#     print(lst[l-1])

# lst=[10,20,30]
# print(print_all(lst,len(lst)))

# recurtion meance function calling it self to perform similar task .
# we use recrtion becaues some problem repeat same pattern inside themself sorecurtion handle it properly .


#! factorial 

# def fact(n):
#     if (n == 0 or n == 1):
#         return 1
#     return n * fact(n-1)
# print(fact(3))

#! print fibonachi series

# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibo(n-1) + fibo(n-2)
# print(fibo(3))

#! Reverse a string

# def reverse(s):
#     if len(s) == 0:
#         return s
    
#     return reverse(s[1:]) + s[0]
# print(reverse('meets'))

#! check string is palindroome or not 

# s = 'meem'
# i=0
# rev = ''
# while i < len(s):
#     rev = s[i] + rev 
#     i+=1

# if s == rev:
#     print('Ok!')
# else:
#     print('No!')

# def palindrome(s):
#     if len(s) <= 1:
#         return s 
#     if s[0] != s[-1]:
#         return 'No'
    
#     return palindrome(s[1:-1])
# print(palindrome('nayan'))


#! find product

# def product(n1,n2):
#     if n2 == 0:
#         return 0
#     print(n1)
#     return n1 + product(n1,n2-1)
# print(product(2,3))


#! print fibonachi

# def fibo(n,a=0,b=1):
#     if n == 0:
#         return 
#     print(a,end=' ')
#     return fibo(n-1,b,a+b)
# print(fibo(11))





def dec_to_bin(n):
    if n==1:
        return '1'
    if n==0:
        return '0'
    return dec_to_bin(n//2) +str(n%2)
print(dec_to_bin(11))


