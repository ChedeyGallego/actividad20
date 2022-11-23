from bs4 import BeautifulSoup

print("hola desde python")
with open('Clientes.xml', 'r') as f:
    data = f.read()
#print(data)
Bs_data = BeautifulSoup(data,"xml")
#print(Bs_data)
telefonos = Bs_data.find_all('telefono')
print(telefonos)
cliente = Bs_data.find('cliente', {'ID':'C001'})
print(cliente)

#escribir etiqueta, atributo en archivo
for precio in Bs_data.find_all('cliente', {'ID':'C001'}):
    precio['oferta'] = "promoción 2x1"

print(Bs_data.prettify)