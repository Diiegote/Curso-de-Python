# En JS se usa camelCase como por ejemplo nombreCompleto
# En Python se recomienda usar snake_case en vez de camelCase, como por ejemplo:
nombre_completo = "diego martinotti"
edad = 45

booleanos= True ,False

# Para concatenar string se usa la F adelante del dato

bienvenida= f"hola {nombre_completo} como estas?"
# de esta manera es como usar los bastick de js `${nombre}`
print(bienvenida)


# para decir que una variable no este mas declarada se usa el operador del
del booleanos

# operadores de pertenencia( in,not in)(para encontrar algun dato en alguna variable)
print("hola" in bienvenida) # esto me da true porque hola esta adentro de la variable bienvenida

# not in se usa para decir que algo no esta en esa variable
print("pedro" not in bienvenida) # esto me da true porque pedro no se encuentra en la variable bienvenida pero si le pongo "hola" me va a dar false porque hola si se encuentra en bienvenida 