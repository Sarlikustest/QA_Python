def taxi_cost(path, cost, start_price):
   
    return path*cost + start_price

a = int(input())
b = int(input())
c = int(input())

taxi = taxi_cost(a, b, c)
print(f'Стоимость поездки {taxi}')