'''определить с помощью рекурсии, является ли слово полиндромом'''
# def Palindrom(word, k=0):
#     if word[k]!=word[-(k+1)]:
#         return False
#     else:
#         if k==len(word)//2+1:
#             return True
#         else:
#             return Palindrom(word, k+1)
# print(Palindrom('437734'))
def is_palindrome(word):
    if len(word) == 0:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False
word = input("Введите слово: ")
result = is_palindrome(word.lower())

if result:
    print(f"{word} - палиндром.")
else:
    print(f"{word} - не палиндром.")