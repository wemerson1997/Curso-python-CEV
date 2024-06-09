from time import sleep
import emoji
print("-=-" * 20)
print("Os fogos de artifício estão prestes a começar!!!")
print("-=-" * 20)
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.2)
for e in range(0, 20):
    print(emoji.emojize(":fireworks:"), end="")
print('BOOOOM')