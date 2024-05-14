def set_motor_power(power):
    print(f"Установка мощности мотора на {power}%")


def main():
    while True:
        power = input("Введите мощность мотора (0-100%): ")
        set_motor_power(power)


if __name__ == "__main__":
    main()