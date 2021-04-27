#Daniel Adi Putranto
#71200574
'''
Disini kita disuruh membauat program tentang seorang baru saja on
dalam game hingga kita disuruh membuat program tersebut, seperti baru
saja masuk ke game dan langsung masuk ke online tersebut yang online
'''
player_1 = {'nama':'johan', 'level':4, 'score':128}
player_2 = {'nama':'paul', 'level':3, 'score':88}
player_3 = {'nama':'angel', 'level':7, 'score':215}
players = [player_1, player_2, player_3]
for player in players:
    print(player)

print("Player 4 is online.......")
player_4 = {'nama':'rocky', 'level':20, 'score':956}
players.append(player_4)
for player in players:
    print(player)
