import inspect


def introspection_info(obj):
    # Собираем информацию об объекте
    info = {}

    # Тип объекта
    info['type'] = str(type(obj).__name__)  # Получаем только имя типа

    # Атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes

    # Методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods

    # Модуль, к которому принадлежит объект
    if hasattr(obj, '__module__'):
        info['module'] = obj.__module__
    else:
        info['module'] = None  # Для встроенных типов

    # Другие интересные свойства (например, size объекта для коллекций)
    if isinstance(obj, (list, dict, set, tuple)):
        info['length'] = len(obj)

    return info


# Пример использования
class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value * 2


# Создаем объект
my_object = MyClass(10)

# Интроспекция объекта
object_info = introspection_info(my_object)
print(object_info)

# Интроспекция примитивного типа
number_info = introspection_info(42)
print(number_info)