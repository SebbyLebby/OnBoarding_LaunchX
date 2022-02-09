from datetime import *
from dateutil.relativedelta import *
import numpy as np

now = datetime.now()
print(now)

now = now + relativedelta(months = 1, weeks = 1, hour = 10) # Se pueden sumar ya que son el mismo tipo de dato.
# relativedelta puede hacer una estimación sobre la fecha que cae en cierto tiempo 'x'.
# puesto que puede presentarse cálculos complejos al haber año bisiesto, o meses con 30 ó 31 días.
print(now)

a = np.array([1,2,3,4,5,6])
print('a = ',a)

b = np.array([[3, 5, 1],
             [9, 4, 11],
             [23, 7, 2]])

print('b = ',b)