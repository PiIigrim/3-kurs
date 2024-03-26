import random

class Component:
    def __init__(self, name, characteristics):
        self.name = name
        self.characteristics = characteristics

    def __str__(self):
        return f"{self.name}: {', '.join([f'{key}: {value}' for key, value in self.characteristics.items()])}"


class PC:
    def __init__(self, cpu=None, gpu=None, psu=None):
        self.cpu = cpu
        self.gpu = gpu
        self.psu = psu

    def __str__(self):
        return f"CPU: {self.cpu}\nGPU: {self.gpu}\nPSU: {self.psu}"


class Inventory:
    def __init__(self):
        self.components = []
        self.pcs = {}

    def add_component(self, component):
        self.components.append(component)
    index = 0
    def add_pc(self, pc):
        self.index += 1
        self.pcs[self.index] = pc

    def remove_used_components(self, pc):
        self.components.remove(pc.cpu)
        self.components.remove(pc.gpu)
        self.components.remove(pc.psu)

    def remove_item(self, inventory_type):
        if inventory_type == 'компоненты' or inventory_type == '1':
            if not self.components:
                print("Нет компонентов.")
                return
            item_name = input("Введите название компонента для удаления: ")
            for component in self.components:
                if component.name == item_name:
                    self.components.remove(component)
                    print(f"{item_name} удален.")
                    break
            else:
                print(f"{item_name} не найден.")
        elif inventory_type == 'пк' or inventory_type == '2':
            if not self.pcs:
                print("Нет собранных пк.")
                return
            pc_index = int(input("Введите индекс пк для удаления: "))
            if pc_index in self.pcs:
                del self.pcs[pc_index]
                print(f"PC {pc_index} удален.")
            else:
                print("Неверный индекс пк.")
        else:
            print("Неверный тип.")

    def show_inventory(self, choice):
        if choice == 'компоненты' or choice == '1':
            print("Компоненты:")
            for component in self.components:
                print(component)
        elif choice == 'пк' or choice == '2':
            print("ПК:")
            for index, pc in self.pcs.items():
                print(f"Индекс: {index}")
                print(pc)
        else:
            print("Неверный выбор.")
    
    def find_pc_with_highest_cpu_frequency(self):
        highest_frequency_pc = None
        highest_frequency = 0
        for pc in self.pcs.values():
            if pc.cpu and "частота" in pc.cpu.characteristics:
                frequency = float(pc.cpu.characteristics["частота"].split()[0])
                if frequency > highest_frequency:
                    highest_frequency = frequency
                    highest_frequency_pc = pc
        return highest_frequency_pc

def create_cpu():
    return Component(
        name=f"CPU_{random.randint(1, 100)}",
        characteristics={
            "частота": f"{random.uniform(2, 5):.2f} GHz",
            "ядра": random.randint(2, 16),
        }
    )

def create_gpu():
    return Component(
        name=f"GPU_{random.randint(1, 100)}",
        characteristics={
            "память": f"{random.randint(4, 12)} GB",
            "частота": f"{random.randint(1000, 2000)} MHz",
        }
    )

def create_psu():
    return Component(
        name=f"PSU_{random.randint(1, 100)}",
        characteristics={
            "мощность": f"{random.randint(400, 1000)} W",
            "эффективность": f"{random.randint(80, 95)}%",
        }
    )

def create_pc(components):
    cpu_options = [component for component in components if "CPU" in component.name]
    gpu_options = [component for component in components if "GPU" in component.name]
    psu_options = [component for component in components if "PSU" in component.name]

    if cpu_options and gpu_options and psu_options:
        cpu = random.choice(cpu_options)
        gpu = random.choice(gpu_options)
        psu = random.choice(psu_options)
        pc = PC(cpu, gpu, psu)
        components.remove(cpu)
        components.remove(gpu)
        components.remove(psu)
        return pc
    else:
        print("Недостаточно компонентов для сборки ПК.")
        return None

def main():
    inventory = Inventory()

    for _ in range(3):
        inventory.add_component(create_cpu())
        inventory.add_component(create_gpu())
        inventory.add_component(create_psu())

    while True:
        print("\n1. Показать инвентарь\n2. Создать ПК\n3. Создать компонент\n4. Удалить предмет\n5. Найти ПК с самым высокочастотным процессором\n6. Выход")
        choice = input("Что делаем?: ")

        if choice == '1':
            inventory_type = input("Введите тип предмета (компоненты/пк): ")
            inventory.show_inventory(inventory_type)

        elif choice == '2':
            pc = create_pc(inventory.components)
            if pc:
                inventory.add_pc(pc)
                print("ПК создан.")

        elif choice == '3':
            component_type = input("Введите тип компонента (CPU/GPU/PSU): ")
            if component_type.upper() == "CPU" or component_type == '1':
                new_component = create_cpu()
            elif component_type.upper() == "GPU" or component_type == '2':
                new_component = create_gpu()
            elif component_type.upper() == "PSU" or component_type == '3':
                new_component = create_psu()
            else:
                print("Неверный тип компонента.")
                continue
            inventory.add_component(new_component)
            print(f"Новый компонент создан: {new_component}")

        elif choice == '4':
            inventory_type = input("Введите тип предмета (компоненты/пк): ")
            inventory.remove_item(inventory_type)

        elif choice == '5':
            pc_with_highest_frequency = inventory.find_pc_with_highest_cpu_frequency()
            if pc_with_highest_frequency:
                print(f"ПК с самым высокочастотным процессором:\n{pc_with_highest_frequency}")
            else:
                print("ПК не найденны.")

        elif choice == '6':
            print("Выход...")
            break

        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()