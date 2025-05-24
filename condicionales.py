print("ejemplos de condicionales")

usuario_activo = True
rol = "admin"

if usuario_activo and rol in ["admin", "supervisor"]:
    print("Acceso completo")
else:
    print("Acceso limitado")
