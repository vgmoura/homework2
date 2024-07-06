def test_function():
    print('тестируем')
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()