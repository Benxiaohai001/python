import const


const.name  = "Megvii"

print(const.name)

try:
    const.name = "Megvii.com"
except TypeError as Err:
    print(Err)



try:
    const.name = "Megvii"
except TypeError as Err:
    print(Err)
