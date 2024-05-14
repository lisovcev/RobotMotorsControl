import time
def set_motor_speed(speed):
    print(f"Установка скорости мотора на {speed}%")


def smooth_set_speed(target_speed):
    current_speed = 0
    step = 1 if target_speed > current_speed else -1
    for speed in range(current_speed, target_speed, step):
        set_motor_speed(speed)
        time.sleep(0.1)
    set_motor_speed(target_speed)


def main():
    while True:
        speed = int(input("Введите скорость мотора (0-100%): "))
        smooth_set_speed(speed)


if __name__ == "__main__":
    main()