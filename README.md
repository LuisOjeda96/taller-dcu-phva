# Taller: El Desafío del Diseño Centrado en el Usuario

Trabajo del Grupo 2 para la asignatura **Interacción Humano-Computador**, 4.º nivel,
paralelo C2 — Universidad Estatal de Milagro.

Unidad 3: La interfaz web y sus principios de diseño
Tema 1: Diseño centrado en el usuario (DCU) y sus métodos

---

## Contenido

| Archivo | Qué es |
|---|---|
| `simulador_dcu.py` | Simulador del ciclo DCU-PHVA pedido en el apartado 4 del taller |
| `mesa_seleccion_unemi.html` | Prototipo de la interfaz, fase «Hacer» del ciclo |
| `capturas/` | Tres capturas del prototipo usadas como evidencia en el informe |

---

## El simulador

Reproduce las cuatro actividades del DCU mapeadas sobre el ciclo de mejora
continua PHVA. El bucle repite Planear y Hacer mientras la verificación no sea
satisfactoria, de modo que la condición de cierre no es «el desarrollo terminó»
sino «la evaluación fue satisfactoria».

```
Planear   ->  Comprensión del contexto de uso (CECU)
              Especificación de requisitos de usuario (ERU)
Hacer     ->  Producción de soluciones de diseño (PSD)
Verificar ->  Evaluación del diseño contra los requisitos (EDR)
Actuar    ->  Cierra el ciclo si satisface; itera si no lo hace
```

### Cómo ejecutarlo

Requiere Python 3. No usa librerías externas.

```bash
python simulador_dcu.py
```

El programa pide en cada vuelta si el sistema satisface los requerimientos.
Responder `n` devuelve el control al inicio; responder `s` cierra el ciclo e
informa cuántas iteraciones hicieron falta.

### Pruebas realizadas

| Entrada | Resultado esperado | Resultado obtenido |
|---|---|---|
| `n`, `n`, `s` | Itera dos veces y cierra en la tercera | Correcto |
| `s` | Cierra en la primera vuelta | Correcto |
| Entrada no reconocida | Se trata como no satisfactoria y vuelve a iterar | Correcto |

---

## El prototipo

`mesa_seleccion_unemi.html` es la mesa de selección de postulantes del caso de
estudio: la universidad debe cubrir cuatro cupos —analista de usuario, arquitecto
de requisitos, diseñador de interacción y evaluador de calidad— a partir de una
lista de postulantes evaluados con una rúbrica.

Es un único archivo, sin dependencias ni conexión a internet. Se abre con doble
clic en cualquier navegador.

Tres decisiones de la interfaz responden a requisitos levantados en la fase ERU:

- **Los cupos encabezan la pantalla.** El coordinador sabe qué falta por cubrir
  sin tener que abrir nada.
- **La rúbrica se despliega antes de decidir**, con el puntaje de cada criterio y
  su peso, no después de la asignación.
- **Toda asignación es reversible.** Al ocupar un cupo aparece la opción de
  deshacer, y el cupo se puede liberar desde la ficha o desde la cabecera.

Cuando un postulante declara menos de 15 horas semanales, la ficha lo advierte y
el cupo queda marcado como pendiente de visto bueno del coordinador. La
restricción se comunica en el momento de decidir y no en una validación posterior.

### Comprobaciones

- Sin desplazamiento horizontal entre 320 y 1440 px de ancho.
- Navegable con teclado, con foco visible en todos los controles.
- Contraste de texto por encima de 4,5:1.
- Respeta `prefers-reduced-motion`.

Los datos de los postulantes son inventados y los pesos de la rúbrica son una
propuesta del grupo.
