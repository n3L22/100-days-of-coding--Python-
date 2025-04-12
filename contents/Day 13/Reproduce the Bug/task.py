from random import randint

#reproduce the bug what is wrong if you click run too many times?
"""dice_images = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣", "6️⃣"]
dice_num = randint(1,6)
print(dice_images[dice_num])"""


#solution
dice_images = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣", "6️⃣"]
dice_num = randint(0,5) # takes from 1 to 6 but list is 0 to 5 
print(dice_images[dice_num])