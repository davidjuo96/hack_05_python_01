### David Urdaneta - Social Oplesk - Programa Fullstack - Grupo 9
---

# Solución de Hacks - 1era parte

## Tecnologías utilizadas
[![My Skills](https://skillicons.dev/icons?i=py)](https://skillicons.dev)


## Tabla de contenidos
- [Instrucciones de Instalación](#instrucciones-de-instalación)
- [Descripción de los Hacks](#descripción-de-los-hacks)
- [Pruebas](#pruebas)


## Instrucciones de Instalación

1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/davidjuo96/hack_06_python_02
   ```

2. **Instalar Requerimientos**  
   ```bash
   pip install -r requirements.txt
   ```
   
## Descripción de los Hacks

| Hack  | Descripción                            |  
|-------|----------------------------------------|
| H-1   | Cambiar `"fooziman"` a `"FOOZIMAN"` |
| H-2   | Cambiar `"FOOZIMAN"` a `"fooziman"` |
| H-3   | Cambiar `"fooziman"` a `"Fooziman"` |
| H-4   | Cambiar `"fooziman"` a `"foozimaN"` |
| H-5   | Cambiar `"fooziman"` a `"f00z1m@n"` |
| H-6   | Generar la lista `[0,1,2,3,4,5]` usando `for` |
| H-7   | Generar la lista `[5,4,3,2,1,0]` usando `while` |
| H-8   | Filtrar `[1,3,5,7,9]` para obtener `[3,5,7]` |
| H-9   | Transformar `[1,2,3]` en `[1,'@',2,'@',3,'@']` usando `while` |
| H-10  | Convertir `"fooziman"` en `["F","0","0","Z","1","M","@","N"]` |

## Pruebas

Para verificar cada hack, se utilizan pruebas con `pytest`:

- Ejecutar todas las pruebas:

  ```bash
  python -m pytest test_hack.py -v
  ```

- Ejecutar una prueba específica:  
  ```bash
  python -m pytest test_hack.py::test_hack_1 -v
  ```
