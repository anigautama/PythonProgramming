#anil

n = int(input("Enter number:"))
p = str(input("Enter string:"))
print(p[::-1])
rev_no = 0
orig_no = n
while n!=0:
    rem = n%10
    rev_no = rev_no*10+rem
    n = int(n/10)

if(orig_no == rev_no):
    print("no. is pallindrome")
else:
    print("no. is not pallindrome")

if(p[::-1]==p):
    print("String is pallindrome")
else:
    print("String is not pallidrome")
