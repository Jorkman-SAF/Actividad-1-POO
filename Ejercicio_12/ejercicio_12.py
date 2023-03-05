hrs = 48
pg_h = 5000
bruto = hrs * pg_h
retencion = bruto*0.125
neto = bruto - retencion

print(f'Salario bruto: {bruto}')
print(f'Retención en la fuente: {retencion}')
print(f'Salarion Neto: {neto}')