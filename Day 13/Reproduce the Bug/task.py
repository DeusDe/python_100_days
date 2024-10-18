from random import randint
dice_images = {1:"❶", 'a':"❷", 3:"❸", 4:"❹", 5:"❺", 6:"❻"}
dice_num = randint(0, len(dice_images)-1)
print(dice_images[dice_num])

dice_images.pop('a')
print(dice_images)
