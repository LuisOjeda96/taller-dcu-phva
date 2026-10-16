# -*- coding: utf-8 -*-
"""
Simulador de iteración DCU-PHVA

Taller académico: El Desafío del Diseño Centrado en el Usuario
Unidad 3 — La interfaz web y sus principios de diseño
Interacción Humano-Computador · UNEMI

El programa recorre las cuatro actividades del Diseño Centrado en el Usuario
mapeadas sobre el ciclo de mejora continua PHVA:

    Planear   -> Comprensión del contexto de uso (CECU)
                 Especificación de requisitos de usuario (ERU)
    Hacer     -> Producción de soluciones de diseño (PSD)
    Verificar -> Evaluación del diseño contra los requisitos (EDR)
    Actuar    -> Cierra el ciclo si satisface; itera si no lo hace

El bucle solo termina cuando la evaluación resulta satisfactoria, de modo que
el control sobre el cierre lo tiene la verificación y no el desarrollo.
"""


def simulador_dcu():
    """Ejecuta el ciclo DCU-PHVA hasta que la evaluación sea satisfactoria.

    Devuelve el número de iteraciones que hicieron falta para cerrarlo.
    """
    print("Iniciando Proceso DCU (PHVA)...")
    satisfactorio = False
    iteracion = 0

    while not satisfactorio:
        iteracion += 1
        print("\n--- Iteración %d ---" % iteracion)
        print("Planear: Analizando usuario y requisitos.")
        print("Hacer: Produciendo soluciones de diseño.")

        evaluacion = input("Verificar: ¿Satisface el sistema los requerimientos? (s/n): ")

        if evaluacion.lower() == "s":
            print("Actuar: Desarrollo Exitoso.")
            satisfactorio = True
        else:
            print("Actuar: Iterando el ciclo de diseño.")

    print("\nProceso cerrado tras %d iteración(es)." % iteracion)
    return iteracion


if __name__ == "__main__":
    simulador_dcu()
