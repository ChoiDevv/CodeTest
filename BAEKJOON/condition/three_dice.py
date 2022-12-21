# 주사위 세개

dice_list = list(map(int, input().split()))
prize_money = 0

if dice_list[0] == dice_list[1] == dice_list[2]:
    prize_money = (dice_list[0] * 1000) + 10000
elif dice_list[0] == dice_list[1]:
    prize_money = (dice_list[0]) * 100 + 1000
elif dice_list[1] == dice_list[2]:
    prize_money = (dice_list[1]) * 100 + 1000
elif dice_list[0] == dice_list[2]:
    prize_money = (dice_list[0]) * 100 + 1000
else:
    prize_money = max(dice_list) * 100

print(prize_money)