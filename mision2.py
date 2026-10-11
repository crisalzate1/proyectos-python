def ingresar_usuarios():
    usuarios = []
    print("--- REGISTRO DE USUARIOS ---")
    
    while True:
        nombre = input("Ingresa el nombre (o escribe 'salir' para terminar): ").strip()
        if nombre.lower() == "salir":
            break
            
        ciudad = input("Ingresa la ciudad: ").strip()
        
        while True:
            try:
                edad = int(input("Ingresa la edad: "))
                if 0 <= edad <= 120:
                    break
                else:
                    print("Error: La edad debe estar entre 0 y 120.")
            except ValueError:
                print("Error: Ingresa un número entero válido.")
                
        # Guardamos los datos como un diccionario dentro de la lista
        usuario = {
            "nombre": nombre,
            "ciudad": ciudad,
            "edad": edad
        }
        usuarios.append(usuario)
        print(f"-> ¡Usuario {nombre} registrado con éxito!\n")
        
    return usuarios


def analizar_datos(usuarios):
    if not usuarios:
        print("\nNo se registraron usuarios para analizar.")
        return

    total_usuarios = len(usuarios)
    suma_edades = sum(u["edad"] for u in usuarios)
    promedio_edad = suma_edades / total_usuarios
    mayores_edad = [u["nombre"] for u in usuarios if u["edad"] >= 18]

    print("\n" + "="*30)
    print("--- REPORTE DE DATOS ---")
    print("="*30)
    print(f"Total de usuarios registrados: {total_usuarios}")
    print(f"Promedio de edad: {promedio_edad:.1f} años")
    print(f"Usuarios mayores de edad: {', '.join(mayores_edad) if mayores_edad else 'Ninguno'}")


def main():
    lista_usuarios = ingresar_usuarios()
    analizar_datos(lista_usuarios)


if __name__ == "__main__":
    main()