# 4. Escribe un programa en Python que muestre la hora actual con una suma de dos horas adicionales

import datetime

hora_actual = datetime.datetime.now()
print('Hora actual:', hora_actual)

resultado = hora_actual + datetime.timedelta(hours=2)

print('Hora más 2 horas:', resultado)