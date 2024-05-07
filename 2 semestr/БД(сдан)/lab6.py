import time

class LightingControlSystem:
    def __init__(self):
        self.motion_sensor = False
        self.twilight_switch = False
        self.time_switch = False
        self.main_switch = False
        self.neon_sign = False

    def check_lamps(self):
        if not self.main_switch:
            print("Главный выключатель выключен. Включите главный выключатель перед проверкой ламп.")
            return
        print("Проверка ламп...")
        self.turn_on_neon_sign()
        self.turn_on_first_group_lights()
        self.turn_on_second_group_lights()
        self.turn_on_third_group_lights()

    def turn_on_neon_sign(self):
        if self.neon_sign:
            print("Неоновая подсветка уже включена")
        else:
            print("Неоновая подсветка включена")
            self.neon_sign = True

    def turn_off_neon_sign(self):
        if not self.neon_sign:
            print("Неоновая подсветка уже выключена")
        else:
            print("Неоновая подсветка выключена")
            self.neon_sign = False

    def turn_on_first_group_lights(self):
        if self.time_switch:
            print("Первая группа освещения включена по времени")
        else:
            print("Первая группа освещения выключена")

    def turn_on_second_group_lights(self):
        if self.twilight_switch:
            print("Вторая группа освещения включена по датчикам света")
        else:
            print("Вторая группа освещения выключена")

    def turn_on_third_group_lights(self):
        if self.motion_sensor and not self.time_switch:
            print("Третья группа освещения включена по датчику движения")
        else:
            print("Третья группа освещения выключена")

    def toggle_motion_sensor(self):
        if not self.main_switch:
            print("Главный выключатель выключен. Включите главный выключатель перед активацией датчика движения.")
            return
        self.motion_sensor = not self.motion_sensor
        if self.motion_sensor:
            print("Датчик движения активирован")
        else:
            print("Датчик движения деактивирован")

    def switch_twilight(self):
        if not self.main_switch:
            print("Главный выключатель выключен. Включите главный выключатель перед переключением режима ночного света.")
            return
        print("Ночный режим переключен")
        self.twilight_switch = not self.twilight_switch

    def switch_time(self):
        if not self.main_switch:
            print("Главный выключатель выключен. Включите главный выключатель перед переключением режима времени.")
            return
        print("Режим времени переключен")
        self.time_switch = not self.time_switch

    def switch_main(self):
        print("Главный выключатель переключен")
        self.main_switch = not self.main_switch
        if not self.main_switch:
            self.turn_off_neon_sign()

    def turn_on_all_lights_for_x_seconds(self, seconds):
        if not self.main_switch:
            print("Главный выключатель выключен. Включите главный выключатель перед включением всех ламп.")
            return
        print(f"Все лампы включены на {seconds} секунд")
        print("Неоновая подсветка включена")
        print("Первая группа освещения включена")
        print("Вторая группа освещения включена")
        print("Третья группа освещения включена")
        time.sleep(seconds)

def user_input(control_system):
    while True:
        print("\n-----------------------------------------")
        print("Выберите действие:")
        print("1. Проверить лампы")
        print("2. Переключить основной выключатель")
        print("3. Переключить режим времени")
        print("4. Переключить режим ночного света")
        print("5. Включить/выключить датчик движения")
        print("6. Включить все лампы на X секунд")
        print("7. Выход")

        choice = input("Введите ваш выбор: ")
        print("-----------------------------------------")
        print("")

        if choice == "1":
            control_system.check_lamps()
        elif choice == "2":
            control_system.switch_main()
        elif choice == "3":
            control_system.switch_time()
        elif choice == "4":
            control_system.switch_twilight()
        elif choice == "5":
            control_system.toggle_motion_sensor()
        elif choice == "6":
            seconds = int(input("Введите количество секунд для включения всех ламп: "))
            control_system.turn_on_all_lights_for_x_seconds(seconds)
        elif choice == "7":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите верное значение.")

if __name__ == "__main__":
    control_system = LightingControlSystem()
    user_input(control_system)