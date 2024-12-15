

def introspection_info(obj):
    # Создаем словарь для хранения информации об объекте
    info = {}

    # Получаем тип объекта
    info['type'] = str(type(obj)).split("'")[1]

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods

    # Получаем модуль, к которому принадлежит объект
    info['module'] = obj.__class__.__module__

    # Другие интересные свойства (по желанию)
    info['doc'] = obj.__doc__  # Докстринг объекта (если есть)

    return info

# Пример использования функции
class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value * 2

# Создаем объект
my_object = MyClass(10)

# Проводим интроспекцию
object_info = introspection_info(my_object)
print(object_info)

# Пример работы с числом
number_info = introspection_info(20)
print(number_info)