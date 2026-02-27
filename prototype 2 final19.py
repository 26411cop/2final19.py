import random

print("ยินดีต้อนรับสู่โปรแกรมทายตัวเลข1-10ของนายคอปครับ")

number = random.randint(1 , 10)
guess = int(input("ทายตัวเลข1-10: "))

if  guess ==  number :
     print("ปิ๊งป่อง คุณทายถูกต้อง goodboy/gril")
else :
     print("หว่า เสียใจด้วยคุณทายผิด  เลขทีถูกต้องคือ ", number )
