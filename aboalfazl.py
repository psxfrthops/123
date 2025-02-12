import random

def simulate_game(change_choice):
    # انتخاب تصادفی درها
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    
    # انتخاب اولیه بازیکن
    player_choice = random.randint(0, 2)
    
    # مجری یک در را باز می‌کند که پشتش بز است
    # مجری نمی‌تواند در انتخابی که بازیکن انتخاب کرده باشد، و درهایی که پشتشان ماشین است باز کند
    remaining_doors = [i for i in range(3) if i != player_choice and doors[i] != 'car']
    host_choice = random.choice(remaining_doors)
    
    # اگر بازیکن تصمیم به تغییر انتخاب بگیرد
    if change_choice:
        player_choice = 3 - player_choice - host_choice  # تغییر به در باقی‌مانده

    # آیا بازیکن برنده شده؟
    return doors[player_choice] == 'car'

def monte_hall_simulation(num_trials, change_choice):
    wins = 0
    for _ in range(num_trials):
        if simulate_game(change_choice):
            wins += 1
    return wins / num_trials

# شبیه‌سازی برای استراتژی‌ها
num_trials = 10000
win_rate_change = monte_hall_simulation(num_trials, True)
win_rate_stay = monte_hall_simulation(num_trials, False)

print(f"نرخ برنده شدن با تغییر انتخاب: {win_rate_change * 100:.2f}%")
print(f"نرخ برنده شدن با نگه داشتن انتخاب اولیه: {win_rate_stay * 100:.2f}%")
