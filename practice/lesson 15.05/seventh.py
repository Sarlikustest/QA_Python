def test_calc(operation, num_1, num_2):
    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        try:
            if operation == '+':
                result = num_1 + num_2
                    #return result
            elif operation == '-':
                result = num_1 - num_2
                    #return result
            elif operation == '*':
                result = num_1*num_2
                    #return result
            elif operation == '/':
                try:
                    result = num_1/num_2
                        #return result
                except ZeroDivisionError:
                    result = 'Ошибка'

        except ValueError:
            print('Ошибка')
            
    else:
            result = 'Ошибка'
    print(f'Ответ = {result}')

            

test_calc('+', 10, 2)
test_calc('-', 'tyu', 2)
test_calc('*', 10, 2)
test_calc('/', 10, 2)
test_calc('/', 10, 0)
test_calc('?', 10, 2)