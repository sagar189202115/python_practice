ar = [2, 3, 4, 3, 2]
count = 0
bot_energy = ar[0]
while bot_energy < max(ar):
    for i in ar:
        @a
        @f
        if bot_energy < i:
            bot_energy = bot_energy - (i - bot_energy)
            count += 1
        else:
            bot_energy = bot_energy + (bot_energy - i)
            count += 1
        if bot_energy < 1:
            break
    bot_energy += 1
    if count == len(ar):
        break
print(bot_energy)
