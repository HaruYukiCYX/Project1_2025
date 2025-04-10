from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('Left player name: ')
right_name = input('Right player name: ')

left_score = 0
right_score = 0
rounds = 5 

def pressed(button):
    global left_score, right_score
    if button.pin.number == 14:
        print(f"{left_name} won this round!")
        left_score += 1
    else:
        print(f"{right_name} won this round!")
        right_score += 1

    right_button.when_pressed = None
    left_button.when_pressed = None

for round_num in range(1, rounds + 1):
    print(f"\n--- Round {round_num} ---")
    print(f"Scores: {left_name}: {left_score} | {right_name}: {right_score}")
    print("Get ready...")
    
    led.off()
    sleep(2) 
    
    led.on()
    start_time = sleep(uniform(5, 10))  
    led.off()
    
    right_button.when_pressed = pressed
    left_button.when_pressed = pressed
    
    while right_button.when_pressed is not None:
        sleep(0.1)

print("\n--- Game Over ---")
print(f"Final Scores: {left_name}: {left_score} | {right_name}: {right_score}")
if left_score > right_score:
    print(f"{left_name} wins the game!")
elif right_score > left_score:
    print(f"{right_name} wins the game!")
else:
    print("It's a tie!")
