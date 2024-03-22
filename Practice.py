def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()

#Попробовав вызвать inner_function вне test_function, получаем ошибку,
# так как inner_function доступна только внутри test_function.
inner_function()




