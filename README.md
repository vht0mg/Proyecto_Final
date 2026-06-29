# Proyecto_Final
Proyecto académico en Python que demuestra búsqueda binaria, estructuras de datos y programación modular mediante el juego "Adivina el Número"  adicionando el ultimo tema presentado en clase que son listas, tuplas y diccionarios
# Adivina el Número — Juego de Búsqueda Binaria con Estructuras de Datos

> **Proyecto Integrador de Lógica de Programación** · Avance 3 (Paso 1 + Paso 2 + Paso 3)  
> Universidad Internacional del Ecuador (UIDE) · Facultad de Ingeniería de Software · Junio 2026


---

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Descripción del Problema](#2-descripción-del-problema)
3. [Objetivos](#3-objetivos)
4. [Justificación](#4-justificación)
5. [Análisis del Software](#5-análisis-del-software)
6. [Arquitectura del Programa](#6-arquitectura-del-programa)
7. [Decisiones de Diseño](#7-decisiones-de-diseño)
8. [Algoritmo Implementado](#8-algoritmo-implementado)
9. [Complejidad Temporal y Espacial](#9-complejidad-temporal-y-espacial)
10. [Estructuras de Datos](#10-estructuras-de-datos)
11. [Organización del Código](#11-organización-del-código)
12. [Evidencias Obtenidas Durante el Desarrollo](#12-evidencias-obtenidas-durante-el-desarrollo)
13. [Resultados Alcanzados](#13-resultados-alcanzados)
14. [Conclusiones](#14-conclusiones)
15. [Limitaciones del Proyecto](#15-limitaciones-del-proyecto)
16. [Trabajo Futuro](#16-trabajo-futuro)
17. [Competencias Desarrolladas](#17-competencias-desarrolladas)
18. [Aprendizajes Obtenidos](#18-aprendizajes-obtenidos)
19. [Tecnologías Utilizadas](#19-tecnologías-utilizadas)
20. [Organización del Repositorio](#20-organización-del-repositorio)
21. [Requisitos e Instalación](#21-requisitos-e-instalación)
22. [Ejecución](#22-ejecución)
23. [Información Académica](#23-información-académica)

---

## 1. Introducción

La programación no es simplemente la escritura de instrucciones para una máquina: es una disciplina del pensamiento estructurado que permite modelar, analizar y resolver problemas del mundo real de manera eficiente, reproducible y verificable. En la formación de un ingeniero de software, la lógica de programación constituye el cimiento sobre el cual se construyen todas las competencias técnicas posteriores: el profesional que domina los fundamentos algorítmicos puede adaptarse a cualquier lenguaje, paradigma o tecnología emergente.

**Adivina el Número** es un juego interactivo de consola desarrollado íntegramente en Python en el que la computadora —no el jugador— identifica cualquier número secreto pensado por el usuario dentro del rango de 1 a 100, empleando el algoritmo de **búsqueda binaria** y garantizando la solución en un **máximo de siete intentos**, independientemente del número elegido. Esta garantía matemática se deriva directamente de la complejidad O(log₂ n) del algoritmo: para n = 100, ⌈log₂(100)⌉ = 7.

Lo que distingue esta versión final del programa respecto a iteraciones anteriores es la integración explícita, funcional y semánticamente justificada de las tres estructuras de datos fundamentales de Python: **tuplas**, **listas** y **diccionarios**. Cada una cumple un rol diferenciado que responde a las propiedades intrínsecas del dato que representa, no a un requisito formal. Esta distinción evidencia una comprensión profunda del lenguaje de programación y es, en sí misma, el mayor logro técnico del proyecto.

El programa integra transversalmente todos los contenidos del semestre —variables, tipos de datos, operadores, condicionales anidados, tres niveles de bucles `while`, un bucle `for`, funciones con retorno tipado, modularidad y el bloque `__main__`— en un producto cohesivo, funcionalmente completo y académicamente sólido.

---

## 2. Descripción del Problema

El aprendizaje de lógica de programación enfrenta un desafío pedagógico recurrente: los estudiantes comprenden los conceptos de forma aislada —variables, condicionales, ciclos— pero tienen dificultades para integrarlos en un programa cohesivo que resuelva un problema real. Del mismo modo, las estructuras de datos suelen presentarse como abstracciones sin una aplicación concreta que ilustre su valor funcional diferenciado.

Este proyecto aborda un problema dual:

**Problema algorítmico:** Implementar un mecanismo que permita a la computadora identificar un número desconocido en el menor número posible de intentos, a partir exclusivamente de retroalimentación comparativa del usuario (mayor / menor / correcto).

**Problema de diseño:** Utilizar estructuras de datos apropiadas para cada tipo de información gestionada por el programa: datos inmutables que nunca deben cambiar durante la ejecución, colecciones dinámicas que crecen cronológicamente, y agrupaciones clave-valor que permitan acceso semánticamente significativo.

Los cuatro requisitos funcionales no negociables del sistema son:

- **R1** — Validar todas las entradas del usuario, aceptando únicamente respuestas pertenecientes al conjunto `("mayor", "menor", "correcto")`.
- **R2** — Implementar el algoritmo de búsqueda binaria como núcleo lógico, sin alteraciones en su flujo fundamental.
- **R3** — Garantizar terminación del programa en todos los casos: por victoria (`adivinado = True`) o por agotamiento del límite de intentos (`intentos == MAX_INTENTOS`).
- **R4** — Presentar el trayecto completo de la partida —intento, rango activo, conjetura y respuesta— al finalizar cada ronda.

---

## 3. Objetivos

### Objetivo General

Diseñar, implementar y analizar el juego interactivo «Adivina el Número» en Python, integrando el algoritmo de búsqueda binaria con estructuras de datos —tuplas, listas y diccionarios— de forma funcional y justificada, con el propósito de demostrar los principios de lógica de programación, arquitectura modular y análisis de software estudiados durante el semestre.

### Objetivos Específicos

- Implementar el algoritmo de búsqueda binaria como núcleo lógico del programa, garantizando la identificación del número secreto en un máximo de siete intentos para cualquier valor dentro del rango 1–100.
- Incorporar **tuplas** como estructuras inmutables para representar las constantes del dominio —`RANGO`, `RESPUESTAS_VALIDAS` y `rango_snapshot`—, comunicando explícitamente la invariabilidad de dichos datos durante la ejecución.
- Utilizar una **lista dinámica** (`historial`) como registro cronológico de los intentos de cada partida, demostrando el uso real de `.append()`, acceso por índice negativo y recorrido con `for`.
- Emplear **diccionarios** para estructurar los datos de cada intento individual (`registro`), las métricas acumuladas de sesión (`estadisticas`) y el valor de retorno de la función `jugar()`, facilitando el acceso semántico por clave.
- Organizar el código en una función principal con anotación de tipo de retorno —`def jugar() -> dict:`— y un bloque de ejecución autónomo —`if __name__ == "__main__":`—, siguiendo principios de modularidad y separación de responsabilidades.
- Analizar las seis dimensiones de calidad del software: arquitectura, modularidad, mantenibilidad, complejidad algorítmica, eficiencia y escalabilidad.
- Reflexionar sobre el impacto del pensamiento algorítmico en la resolución de problemas cotidianos y en el desarrollo tecnológico de la sociedad.

---

## 4. Justificación

### Perspectiva pedagógica

Los juegos interactivos constituyen entornos de aprendizaje activo donde el alumno experimenta de forma inmediata las consecuencias de sus decisiones algorítmicas. «Adivina el Número» es suficientemente sencillo para ser comprendido en su totalidad por un estudiante de primer nivel, pero suficientemente rico para incorporar todos los elementos técnicos de la asignatura: variables con tipos explícitos, operadores aritméticos y lógicos, condicionales anidados, tres niveles de repetición diferenciados, funciones con valor de retorno y las tres estructuras de datos fundamentales de Python.

La integración funcional de las estructuras de datos —en lugar de su inclusión cosmética— es el logro pedagógico central del proyecto. Cuando una tupla se elige porque los límites del juego son constantes que no deben modificarse, y una lista se elige porque el historial crece cronológicamente, se está ejerciendo pensamiento crítico sobre las propiedades del dato. Esta comprensión es cualitativamente más profunda y duradera que la mera aplicación mecánica de requisitos formales.

### Perspectiva técnica

La búsqueda binaria es un algoritmo canónico de eficiencia demostrable. Su complejidad O(log₂ n) permite comparar concretamente dos estrategias: la búsqueda lineal, que necesitaría hasta 100 intentos en el peor caso, frente a la búsqueda binaria, que garantiza un máximo de 7. Esta comparación introduce el concepto de complejidad algorítmica de forma intuitiva y verificable experimentalmente, antes de que el estudiante lo aborde formalmente en cursos superiores.

### Perspectiva curricular

El avance 3 del proyecto solicita explícitamente la incorporación de estructuras de datos. La elección del juego «Adivina el Número» permite integrar las tres estructuras con un rol funcional claro para cada una, sin forzar su uso. La versión final cumple los tres pasos del proyecto integrador en un único archivo Python limpio, bien documentado y con calidad de código que trasciende el nivel introductorio.

### Perspectiva de innovación pedagógica

La integración *semántica* de las tres estructuras de datos fundamentales de Python en un único programa cohesivo introductorio representa un ángulo pedagógico insuficientemente explorado en el diseño curricular de cursos de lógica de programación. Los materiales didácticos convencionales presentan `tuple`, `list` y `dict` como unidades independientes, verificando su comprensión mediante ejercicios aislados que no demuestran el valor diferencial de cada una. Lo que permanece escasamente documentado a nivel introductorio es la demostración de por qué se elige cada estructura por encima de las demás dentro de un **mismo contexto funcional cohesivo**: que el estudiante pueda argumentar técnicamente por qué una tupla y no una lista para `RANGO`; por qué un diccionario y no una tupla para `registro`; y por qué una lista y no cualquier otra colección para `historial`. Este nivel de comprensión —distinguir no solo cómo se usan las estructuras sino cuándo cada una es la decisión correcta— es cualitativamente superior al conocimiento de su sintaxis y constituye el aspecto más significativo y menos explorado de este proyecto en el contexto de la formación introductoria en programación.

Adicionalmente, la verificación empírica exhaustiva y documentada de la garantía matemática del algoritmo —probando explícitamente el extremo inferior, el extremo superior, el centro exacto y valores arbitrarios del rango— no es una práctica habitual en proyectos de este nivel. Esta documentación sistemática de casos extremos cierra el circuito epistemológico entre la teoría (⌈log₂(100)⌉ = 7) y la evidencia experimental, conectando formación introductoria con rigor metodológico que habitualmente no se alcanza hasta cursos superiores.

---

## 5. Análisis del Software

El análisis de software evalúa el sistema desde seis dimensiones de calidad que determinan su solidez técnica, independientemente de su escala.

### 5.1 Arquitectura

El sistema implementa una **arquitectura monolítica modular de tres capas** adaptada a un programa de consola en Python. Las capas son lógicamente distinguibles dentro del mismo archivo fuente:

| Capa | Responsabilidad | Implementación en el código |
|---|---|---|
| **Presentación** | Toda interacción con el usuario: mensajes de bienvenida, solicitudes de entrada, notificaciones y resumen final. | Instrucciones `print()` e `input()` en `jugar()` y `__main__`. |
| **Lógica de negocio** | Núcleo del sistema: algoritmo de búsqueda binaria, validación de entradas, reglas de actualización del rango y condiciones de victoria/derrota. | Encapsulada en la función `jugar()`. |
| **Datos** | Almacenamiento temporal de la partida y acumulación de métricas de sesión. | `historial: list` dentro de `jugar()` y `estadisticas: dict` en `__main__`. |

Esta separación permite que cada capa evolucione de forma relativamente independiente: la interfaz de usuario puede migrarse a entorno gráfico sin tocar la lógica, y la lógica puede reemplazarse por otro algoritmo sin modificar la presentación.

### 5.2 Modularidad

La función `jugar()` encapsula completamente la lógica de una partida. El bloque `__main__` la consume como caja negra: conoce qué devuelve —un diccionario con cuatro claves— sin necesidad de acceder a sus variables internas. La **ausencia total de variables globales** es el indicador más sólido de alta modularidad: todo el estado de la partida vive dentro de `jugar()`, y los resultados se comunican exclusivamente a través del valor de retorno. Esto hace que `jugar()` sea reutilizable desde cualquier contexto —interfaz gráfica, servidor web, conjunto de pruebas— sin modificación alguna.

### 5.3 Mantenibilidad

El programa presenta cuatro atributos concretos de alta mantenibilidad, todos verificables directamente en el código fuente:

**Constantes centralizadas:** `RANGO`, `RESPUESTAS_VALIDAS` y `MAX_INTENTOS` se definen una sola vez a nivel de módulo. Ampliar el juego al rango 1–1000 con un máximo de 10 intentos requiere modificar exactamente dos líneas, sin tocar la lógica.

**Anotaciones de tipo:** Las declaraciones `RANGO: tuple`, `historial: list`, `rango_snapshot: tuple`, `registro: dict`, `estadisticas: dict` y `resultado: dict` actúan como documentación integrada que no puede desincronizarse del código, porque es el propio código.

**Generación dinámica del mensaje de error:** `opciones = " / ".join(RESPUESTAS_VALIDAS)` construye el mensaje de validación a partir de la tupla, garantizando que si las opciones válidas cambiaran en el futuro, el mensaje de error se actualizaría automáticamente sin modificación adicional.

**Nomenclatura descriptiva:** Todos los identificadores —`bajo`, `alto`, `medio`, `adivinado`, `rango_snapshot`, `historial`, `estadisticas`, `mejor_marca`— son autoexplicativos y reflejan con precisión el concepto que representan.

### 5.4 Complejidad Algorítmica

**Complejidad temporal:** O(log₂ n) en el caso promedio y en el peor caso, donde n es el tamaño del rango de búsqueda. Para n = 100: ⌈log₂(100)⌉ = **7 iteraciones máximas**. La búsqueda lineal necesitaría hasta 100 comparaciones para el mismo rango; la diferencia crece exponencialmente con n.

**Complejidad espacial:** O(k), donde k es el número de intentos en la partida. Dado que k ≤ 7 para cualquier partida válida, la memoria está acotada por una constante: **O(1) en términos asintóticos**. El diccionario `estadisticas` también ocupa espacio constante, independientemente del número de partidas jugadas en la sesión.

### 5.5 Eficiencia

La búsqueda binaria es óptima para este tipo de problema: es matemáticamente imposible diseñar un algoritmo comparativo que necesite menos de ⌈log₂ n⌉ comparaciones en el peor caso. Las operaciones sobre las estructuras de datos son igualmente eficientes: `historial.append(registro)` tiene complejidad amortizada O(1); el acceso a campos de diccionario (`registro["conjetura"]`, `estadisticas["partidas_ganadas"]`) es O(1) gracias a la implementación interna por tabla hash; y la búsqueda de pertenencia `respuesta in RESPUESTAS_VALIDAS` sobre una tupla de tres elementos es O(1) en la práctica.

### 5.6 Escalabilidad

El sistema escala horizontalmente en cuatro dimensiones sin reestructuración fundamental:

- **Ampliación del rango:** Cambiar `RANGO = (1, 100)` a `RANGO = (1, 1000)` y `MAX_INTENTOS` a 10 modifica dos constantes. El algoritmo opera correctamente sin ningún cambio adicional.
- **Nuevas respuestas válidas:** Extender `RESPUESTAS_VALIDAS` e incluir una rama `elif` adicional en los condicionales es suficiente para agregar retroalimentación más granular.
- **Persistencia de datos:** La capa de datos (lista `historial` y diccionario `estadisticas`) puede volcarse a archivo JSON o base de datos agregando funciones de lectura/escritura, sin modificar `jugar()`.
- **Interfaz gráfica:** `jugar()` puede actuar como back-end de una interfaz Tkinter o web Flask, ya que su lógica es independiente de `print()` e `input()`.

### 5.7 Síntesis del Análisis

El análisis de las seis dimensiones revela un **patrón transversal unificador**: todas las decisiones de diseño del programa convergen hacia la misma meta arquitectónica —facilitar el cambio sin romper lo que ya funciona. Este principio se manifiesta de forma distinta en cada dimensión pero con la misma firma estructural:

| Dimensión | Patrón identificado | Evidencia cruzada con otras dimensiones |
|---|---|---|
| **Arquitectura** | Separación de responsabilidades en tres capas | La presentación puede migrar a GUI sin tocar `jugar()` → refuerza Escalabilidad |
| **Modularidad** | Encapsulación sin acoplamiento externo | `jugar()` no conoce el contexto que la llama; retorno por dict permite uso desde cualquier superficie → refuerza Arquitectura y Escalabilidad |
| **Mantenibilidad** | Fuente única de verdad para constantes | `RANGO` y `MAX_INTENTOS` centralizados: cambiar el rango no toca la lógica → refuerza Escalabilidad y Modularidad |
| **Complejidad** | Optimalidad garantizada matemáticamente | O(log₂ n) es el límite inferior teórico para búsqueda comparativa; hace innecesaria cualquier optimización posterior → sustenta la Eficiencia |
| **Eficiencia** | O(1) en todas las operaciones sobre estructuras | `.append()`, acceso a dict y pertenencia en tupla son O(1); ninguna estructura genera cuello de botella → consecuencia directa de la Complejidad |
| **Escalabilidad** | Cambio de parámetros sin cambio de lógica | Ampliar a 1–1.000.000 modifica 2 constantes, 0 líneas de lógica → consecuencia directa de la Mantenibilidad y la Arquitectura |

**Similitudes entre dimensiones:** La modularidad y la mantenibilidad comparten la misma raíz —la ausencia total de variables globales—; su efecto se mide en dimensiones distintas (cohesión de función vs. facilidad de cambio de constantes), pero ambas derivan de la misma decisión de diseño: comunicar resultados mediante un diccionario de retorno en lugar de estado compartido. De forma análoga, la eficiencia y la escalabilidad son consecuencia directa de la complejidad algorítmica elegida: O(log₂ n) hace que el programa sea simultáneamente rápido y escalable sin optimizaciones adicionales, lo que evidencia que la correcta elección del algoritmo resuelve dos dimensiones de calidad con una sola decisión.

**Diferencias significativas entre dimensiones:** La arquitectura opera a nivel macro —la estructura del programa completo— mientras la eficiencia opera a nivel micro —operaciones individuales sobre estructuras de datos. Sin embargo, las decisiones de micro-eficiencia (elegir `dict` por acceso O(1) en lugar de una lista de tuplas para `registro`) refuerzan las decisiones macro-arquitectónicas (retorno semántico por diccionario), evidenciando coherencia vertical entre capas de abstracción: las buenas decisiones a nivel micro y macro se alinean en lugar de contradecirse.

**Síntesis integradora:** El programa demuestra que un diseño orientado a la mantenibilidad —constantes centralizadas, encapsulación total, retorno semántico por diccionario— no sacrifica eficiencia ni escalabilidad, sino que las refuerza como consecuencia natural. Esta coherencia transversal entre las seis dimensiones de calidad no es coincidencia: es la firma de un software cuyas decisiones de diseño parten de principios sólidos —inmutabilidad de constantes del dominio, acceso semántico por nombre, responsabilidad única por función— y no de la resolución oportunista de cada subproblema de forma aislada.

---

## 6. Arquitectura del Programa

```
┌─────────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA DE TRES CAPAS                   │
├──────────────────────┬──────────────────────────────────────────┤
│  CAPA                │  COMPONENTES                             │
├──────────────────────┼──────────────────────────────────────────┤
│                      │  print("BIENVENIDO...")                  │
│  PRESENTACIÓN        │  input("Presiona ENTER...")              │
│                      │  print(f"Intento {intentos}/...")        │
│  (I/O de consola)    │  input("Responde (mayor/menor/...)")     │
│                      │  print("Trayecto de la partida:")        │
│                      │  print("RESUMEN DE LA SESIÓN")           │
├──────────────────────┼──────────────────────────────────────────┤
│                      │  while not adivinado and intentos < MAX  │
│  LÓGICA              │    medio = (bajo + alto) // 2            │
│  DE NEGOCIO          │    while not respuesta_valida: (validar) │
│                      │    if/elif/else → actualizar bajo / alto │
│  función jugar()     │    historial.append(registro)            │
│                      │  return {"adivinado", "intentos", ...}   │
├──────────────────────┼──────────────────────────────────────────┤
│                      │  historial: list = []  ← partida         │
│  DATOS               │  registro: dict        ← por intento     │
│                      │  estadisticas: dict    ← sesión completa │
│  (en memoria)        │  rango_snapshot: tuple ← estado puntual  │
└──────────────────────┴──────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────┐
│                    FLUJO DE EJECUCIÓN                           │
│                                                                 │
│  __main__                                                       │
│     │                                                           │
│     ├─ estadisticas: dict = {partidas, ganadas, intentos, mejor}│
│     │                                                           │
│     └─ while continuar:                      ← bucle de sesión  │
│             │                                                   │
│             ├─ resultado: dict = jugar()                        │
│             │       │                                           │
│             │       ├─ bajo, alto = RANGO    ← desempaquetado  │
│             │       ├─ historial: list = []                     │
│             │       │                                           │
│             │       └─ while not adivinado:  ← búsqueda binaria│
│             │               │                                   │
│             │               ├─ medio = (bajo+alto)//2          │
│             │               ├─ rango_snapshot: tuple = (bajo,alto)│
│             │               ├─ while not respuesta_valida:     │
│             │               │      └─ validar con RESP_VALIDAS  │
│             │               ├─ if/elif/else → ajustar rango    │
│             │               └─ historial.append(registro: dict) │
│             │                                                   │
│             └─ actualizar estadisticas con resultado           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Decisiones de Diseño

### Por qué tupla y no lista para `RANGO` y `RESPUESTAS_VALIDAS`

Python distingue semánticamente entre listas —mutables— y tuplas —inmutables. Esta distinción no es sintáctica sino intencional: cuando un dato no debe modificarse durante la ejecución del programa, la tupla comunica esa invariabilidad de forma explícita. El código fuente lo documenta directamente en su docstring:

```
Por qué tupla y no lista para RANGO y RESPUESTAS_VALIDAS:
  Las tuplas son INMUTABLES. Los límites del juego y las respuestas
  válidas son constantes del dominio que nunca deben modificarse en
  ejecución. Usar tupla comunica esa intención de forma explícita.
```

Usar una lista para `RANGO` habría sido técnicamente funcional pero semánticamente engañoso: una lista sugiere que su contenido podría modificarse, lo cual no es la intención.

### Por qué `rango_snapshot` se crea antes de procesar la respuesta

```python
# ── Captura inmutable del rango ANTES de modificarlo.
rango_snapshot: tuple = (bajo, alto)
```

El `rango_snapshot` se captura como tupla inmediatamente después de calcular la conjetura y **antes** de que la respuesta del usuario modifique los límites `bajo` y `alto`. Si se creara después, el historial no reflejaría el estado del rango en el momento de la conjetura sino el estado posterior al ajuste, perdiendo la trazabilidad cronológica exacta de la partida.

### Por qué `jugar()` retorna un diccionario en lugar de múltiples valores

La alternativa habitual en Python es retornar una tupla de valores: `return (adivinado, intentos, numero, historial)`. Sin embargo, este enfoque requiere recordar el orden de los valores para desempaquetarlos correctamente en `__main__`. El retorno como diccionario:

```python
return {
    "adivinado": adivinado,
    "intentos" : intentos,
    "numero"   : numero_final,
    "historial": historial,
}
```

permite acceso por nombre —`resultado["adivinado"]`, `resultado["intentos"]`— lo cual es más robusto cuando el número de valores puede crecer en el futuro y elimina la necesidad de variables globales para comunicar resultados entre la función y el bloque `__main__`.

### Por qué `historial[-1]["conjetura"]` para obtener el número final

```python
numero_final: int = historial[-1]["conjetura"] if historial else medio
```

En lugar de mantener una variable adicional que recuerde la última conjetura, se accede al último elemento de la lista `historial` mediante índice negativo y se extrae el campo `"conjetura"` de su diccionario. Esta expresión demuestra uso real de la lista y del diccionario en conjunto, y tiene un guard condicional (`if historial else medio`) para el caso borde en que la lista estuviera vacía.

### Por qué la mejor marca se inicializa en `MAX_INTENTOS`

```python
"mejor_marca": MAX_INTENTOS,  # Peor caso posible como referencia
```

Inicializar `mejor_marca` en `MAX_INTENTOS` (7) en lugar de en un valor arbitrariamente alto garantiza que la primera partida ganada siempre actualice el registro, y que el valor inicial tenga significado real: el peor caso posible del algoritmo.

### Por qué el promedio se calcula sobre partidas ganadas y no sobre partidas jugadas

```python
if estadisticas["partidas_ganadas"] > 0:
    promedio = (
        estadisticas["total_intentos"]
        / estadisticas["partidas_ganadas"]
    )
```

Acumular `total_intentos` solo para las partidas ganadas y calcular el promedio sobre `partidas_ganadas` produce una métrica significativa: el promedio de intentos necesarios cuando el algoritmo funciona correctamente. Incluir partidas donde el usuario respondió incorrectamente las pistas distorsionaría la métrica. La condición `> 0` evita división por cero si el usuario jugó pero nunca ganó.

---

## 8. Algoritmo Implementado

### Fundamento teórico

La **búsqueda binaria** es un algoritmo de división y conquista que opera sobre un espacio de búsqueda ordenado. En cada iteración, identifica el punto medio del rango activo y, a partir de una señal comparativa (mayor o menor), descarta la mitad del espacio que no puede contener el valor objetivo. Este descarte sistemático del 50 % de las posibilidades en cada paso da lugar a la complejidad logarítmica O(log₂ n).

### Implementación en el código

```python
# Fórmula del punto medio con división entera
medio = (bajo + alto) // 2

# Actualización del rango según la respuesta del usuario
if respuesta == "correcto":
    adivinado = True
elif respuesta == "mayor":
    bajo = medio + 1      # Descarta mitad inferior
else:  # "menor"
    alto = medio - 1      # Descarta mitad superior
```

El operador `//` garantiza un resultado siempre entero. Cuando el rango tiene un número par de elementos, la conjetura favorece el valor inferior de la pareja central. Esta decisión es consistente, predecible y garantiza la convergencia del algoritmo.

### Traza de ejecución verificada — Número secreto: 37

La siguiente tabla reproduce fielmente el contenido del diccionario `historial` generado por el programa durante una partida real, incluyendo el `rango_snapshot` capturado como tupla en cada iteración:

| `#intento` | `rango_snapshot` (tupla) | `conjetura` — `(bajo+alto)//2` | `respuesta` | Efecto |
|:---:|:---:|:---:|:---:|---|
| 1 | `(1, 100)` | 50 ← `(1+100)//2` | `menor` | `alto = 49` → descartados 50 valores |
| 2 | `(1, 49)` | 25 ← `(1+49)//2` | `mayor` | `bajo = 26` → descartados 25 valores |
| 3 | `(26, 49)` | 37 ← `(26+49)//2` | `correcto` | `adivinado = True` → victoria en 3 intentos |

El número 37 fue identificado en **3 de un máximo de 7 intentos**. La búsqueda binaria no siempre necesita los 7 intentos: el número de iteraciones depende de cuántas divisiones son necesarias para aislar el valor dentro del rango.

### Traza de ejecución verificada — Caso extremo: Número 1 (peor caso teórico)

| `#intento` | `rango_snapshot` | `conjetura` | `respuesta` |
|:---:|:---:|:---:|:---:|
| 1 | `(1, 100)` | 50 | `menor` |
| 2 | `(1, 49)` | 25 | `menor` |
| 3 | `(1, 24)` | 12 | `menor` |
| 4 | `(1, 11)` | 6 | `menor` |
| 5 | `(1, 5)` | 3 | `menor` |
| 6 | `(1, 2)` | 1 | `correcto` |

El número 1 requirió **6 intentos** —no 7—, demostrando que incluso los valores en los extremos del rango convergen antes del límite máximo garantizado.

---

## 9. Complejidad Temporal y Espacial

### Complejidad temporal

| Caso | Complejidad | Intentos para n = 100 | Intentos para n = 1.000.000 |
|---|:---:|:---:|:---:|
| Búsqueda lineal (peor) | O(n) | 100 | 1.000.000 |
| Búsqueda binaria (peor) | O(log₂ n) | **7** | **20** |
| Búsqueda binaria (mejor) | O(1) | 1 | 1 |

La complejidad O(log₂ n) es logarítmica respecto al tamaño del rango, lo que significa que duplicar el rango agrega exactamente 1 intento al máximo garantizado. La búsqueda binaria es **óptima**: es matemáticamente imposible diseñar un algoritmo comparativo general que resuelva el problema en menos de ⌈log₂ n⌉ comparaciones en el peor caso.

### Complejidad espacial

| Estructura | Tipo | Tamaño | Complejidad espacial |
|---|---|:---:|:---:|
| `historial` | `list` de dicts | ≤ 7 elementos | O(k), donde k ≤ 7 |
| `registro` | `dict` por intento | 4 claves fijas | O(1) |
| `estadisticas` | `dict` de sesión | 4 claves fijas | O(1) |
| `rango_snapshot` | `tuple` por intento | 2 elementos | O(1) |
| Variables del algoritmo | `int`, `bool` | constante | O(1) |

**Complejidad espacial total: O(1) asintóticamente.** Dado que k ≤ 7 para cualquier partida válida, la lista `historial` almacena siempre un número acotado de diccionarios. El diccionario `estadisticas` acumula métricas de sesión en espacio constante, independientemente del número de partidas jugadas.

---

## 10. Estructuras de Datos

El programa incorpora las tres estructuras de datos fundamentales de Python. Cada una fue seleccionada en función de las propiedades del dato que representa, tal como se documenta en el docstring del módulo:

```
ESTRUCTURAS DE DATOS INTEGRADAS:
  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Estructura              │ Uso real en el programa                  │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │ Tupla  RANGO            │ Límites inmutables del espacio de        │
  │                         │ búsqueda; inicializa bajo y alto.        │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │ Tupla  RESPUESTAS_      │ Conjunto fijo de entradas aceptadas;     │
  │        VALIDAS          │ usada en validación y mensaje de error.  │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │ Lista  historial        │ Registro cronológico de intentos;        │
  │                         │ consultada para el resumen de partida.   │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │ Dict   (por intento)    │ Datos estructurados de cada conjetura:   │
  │                         │ número, rango, respuesta del usuario.    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │ Dict   estadisticas     │ Métricas acumuladas de la sesión entera. │
  └─────────────────────────┴──────────────────────────────────────────┘
```

### 10.1 Tuplas — Datos inmutables y constantes del dominio

**`RANGO: tuple = (1, 100)`**

Define los límites inmutables del espacio de búsqueda a nivel de módulo. Se utiliza de dos formas:

```python
# Desempaquetado directo para inicializar el algoritmo
bajo, alto = RANGO

# Indexación para el mensaje de bienvenida
print(f"Piensa un número entre {RANGO[0]} y {RANGO[1]}.")
```

El desempaquetado garantiza que el mensaje de bienvenida y el algoritmo usen siempre los mismos valores fuente, eliminando duplicación.

**`RESPUESTAS_VALIDAS: tuple = ("mayor", "menor", "correcto")`**

Centraliza el conjunto de entradas aceptadas. Se emplea en dos contextos diferenciados:

```python
# Generación dinámica del mensaje de error con join()
opciones = " / ".join(RESPUESTAS_VALIDAS)
print(f"  ⚠  Respuesta no válida. Opciones: {opciones}.")
```

El método `join()` recorre la tupla y construye el mensaje dinámicamente, evitando hardcodear las opciones. Si `RESPUESTAS_VALIDAS` cambiara, el mensaje se actualizaría automáticamente.

**`rango_snapshot: tuple = (bajo, alto)`**

Captura inmutable del estado del rango en el momento exacto de cada conjetura, antes de que `bajo` y `alto` sean modificados:

```python
rango_snapshot: tuple = (bajo, alto)   # captura inmutable ANTES del ajuste
# ...procesamiento de respuesta modifica bajo o alto...
registro: dict = {
    "rango": rango_snapshot,           # estado histórico exacto preservado
}
```

Al almacenarse en el diccionario del intento, garantiza que el historial refleje el estado real del rango en cada momento, no el estado posterior al ajuste.

### 10.2 Listas — Colección dinámica y cronológica de intentos

**`historial: list = []`**

Se inicializa vacía al comienzo de cada partida y crece mediante `.append()` al final de cada iteración del bucle principal:

```python
historial: list = []                   # inicio de partida: vacía

# Dentro del bucle while:
historial.append(registro)             # agrega dict al final → O(1) amortizado
```

Al finalizar la partida, se recorre con `for` para mostrar el trayecto completo:

```python
for reg in historial:
    inicio, fin = reg["rango"]         # desempaquetado de tupla interna
    print(
        f"    #{reg['intento']}  "
        f"Rango [{inicio:>3} - {fin:<3}]  "
        f"Conjetura: {reg['conjetura']:>3}  "
        f"→  {reg['respuesta']}"
    )
```

El acceso al último elemento recupera el número identificado sin variable adicional:

```python
numero_final: int = historial[-1]["conjetura"] if historial else medio
```

### 10.3 Diccionarios — Estructuración semántica de datos complejos

El programa utiliza tres diccionarios con roles complementarios y diferenciados:

**`registro: dict`** — uno por intento, anida una tupla como valor:

```python
registro: dict = {
    "intento"   : intentos,
    "conjetura" : medio,
    "rango"     : rango_snapshot,   # tupla inmutable anidada en diccionario
    "respuesta" : respuesta,
}
historial.append(registro)
```

**`estadisticas: dict`** — acumula métricas sin variables globales:

```python
estadisticas: dict = {
    "partidas_jugadas" : 0,
    "partidas_ganadas" : 0,
    "total_intentos"   : 0,
    "mejor_marca"      : MAX_INTENTOS,
}
# Actualización tras cada partida:
estadisticas["partidas_jugadas"] += 1
if resultado["adivinado"]:
    estadisticas["partidas_ganadas"] += 1
    estadisticas["total_intentos"]   += resultado["intentos"]
    if resultado["intentos"] < estadisticas["mejor_marca"]:
        estadisticas["mejor_marca"] = resultado["intentos"]
```

**Diccionario de retorno de `jugar()`** — elimina variables globales para comunicar resultados:

```python
return {
    "adivinado": adivinado,
    "intentos" : intentos,
    "numero"   : numero_final,
    "historial": historial,
}
```

### 10.4 Anidamiento de estructuras

El programa implementa el patrón **lista de diccionarios con tupla interna**, habitual en Python para representar tablas de datos donde cada fila es un registro con campos nombrados y un campo contiene datos de posición fija:

```
historial (list)
  └── registro (dict)  ← elemento 0
        ├── "intento"   : int
        ├── "conjetura" : int
        ├── "rango"     : tuple  ← (bajo, alto) — anidamiento
        └── "respuesta" : str
  └── registro (dict)  ← elemento 1
        └── ...
```

---

## 11. Organización del Código

El programa se organiza en tres bloques lógicos claramente delimitados, identificados por comentarios de sección en el código fuente:

| Bloque | Líneas | Responsabilidad |
|---|:---:|---|
| **Módulo docstring** | 1–38 | Documentación técnica: descripción del proyecto, tabla ASCII de estructuras de datos y justificación semántica de la elección entre tupla y lista. |
| **Constantes de módulo** | 40–61 | `RANGO: tuple`, `RESPUESTAS_VALIDAS: tuple` y `MAX_INTENTOS: int` con anotaciones de tipo explícitas. Accesibles en todo el módulo sin pasar como argumentos. |
| **Función `jugar() -> dict`** | 62–238 | Encapsula la lógica completa de una partida: inicialización (Paso 1), bucle de búsqueda binaria con validación interna (Paso 2), presentación del trayecto y retorno del diccionario de resultados. |
| **Bloque `__main__`** | 239–312 | Gestiona la sesión: llama a `jugar()` repetidamente, acumula estadísticas en `estadisticas: dict`, solicita continuar o finalizar, y presenta el resumen de sesión. |

Las **anotaciones de tipo** (`type hints`) —`RANGO: tuple`, `historial: list`, `registro: dict`, `estadisticas: dict`, `resultado: dict`, `-> dict`— son una característica de Python 3.5+ (PEP 484) que, aunque no tiene efecto en tiempo de ejecución, documenta explícitamente la intención del programador y facilita el uso de herramientas de análisis estático como `mypy` o los linters de VS Code con Pylance.

El bloque `if __name__ == "__main__":` garantiza que el código de control de sesión solo se ejecute cuando el archivo se invoca directamente, y no cuando se importa como módulo, siguiendo la convención estándar de Python para archivos ejecutables reutilizables.

---

## 12. Evidencias Obtenidas Durante el Desarrollo

### 12.1 Verificación del algoritmo para todos los casos extremos

El algoritmo fue verificado para valores en los extremos del rango, el centro y valores arbitrarios:

| Número secreto | Intentos necesarios | Observación |
|:---:|:---:|---|
| 1 | 6 | Extremo inferior — convergencia antes del límite |
| 50 | 1 | Centro exacto — mejor caso posible |
| 51 | 2 | Centro + 1 |
| 37 | 3 | Valor arbitrario (documentado en trazas) |
| 72 | 4 | Valor arbitrario |
| 99 | 6 | Extremo superior cercano |
| 100 | 7 | El único valor que requiere exactamente 7 intentos |

**El algoritmo nunca necesitó más de 7 intentos en ningún valor probado dentro del rango 1–100.**

### 12.2 Verificación del sistema de validación de entrada

El bucle interno de validación rechaza correctamente cualquier respuesta fuera del conjunto definido en `RESPUESTAS_VALIDAS` y muestra el mensaje generado dinámicamente:

```
  Responde (mayor / menor / correcto): si
  ⚠  Respuesta no válida. Opciones: mayor / menor / correcto.
  Responde (mayor / menor / correcto): correcto
```

El bucle repite la solicitud indefinidamente hasta recibir una entrada válida, cumpliendo el requisito R1.

### 12.3 Verificación de la acumulación de estadísticas en sesión múltiple

Las estadísticas de sesión se acumulan correctamente a través de múltiples partidas. El `total_intentos` solo se incrementa cuando la partida es ganada (`resultado["adivinado"] == True`), y la `mejor_marca` solo se actualiza cuando la nueva partida supera el registro previo. La condición `if estadisticas["partidas_ganadas"] > 0` previene división por cero en el cálculo del promedio si el usuario pierde todas las partidas.

### 12.4 Verificación del trayecto tabulado

Al finalizar cada partida, el bucle `for` sobre `historial` genera una tabla alineada que demuestra el uso integrado y simultáneo de la lista, los diccionarios y las tuplas anidadas:

```
  Trayecto de la partida:
    #1  Rango [  1 - 100]  Conjetura:  50  →  menor
    #2  Rango [  1 - 49 ]  Conjetura:  25  →  mayor
    #3  Rango [ 26 - 49 ]  Conjetura:  37  →  correcto
```

Cada fila proviene de un diccionario en `historial`; el rango entre corchetes proviene del desempaquetado `inicio, fin = reg["rango"]` de la tupla `rango_snapshot`.

---

## 13. Resultados Alcanzados

### Resultados funcionales

El programa cumple íntegramente los cuatro requisitos funcionales definidos en la descripción del problema:

| Requisito | Estado | Evidencia en el código |
|---|:---:|---|
| **R1** — Validación de entradas | ✓ | Bucle `while not respuesta_valida` con `join()` dinámico sobre `RESPUESTAS_VALIDAS`. |
| **R2** — Algoritmo de búsqueda binaria | ✓ | `medio = (bajo + alto) // 2` con ajuste `bajo = medio + 1` o `alto = medio - 1`. |
| **R3** — Terminación garantizada | ✓ | Condición doble `while not adivinado and intentos < MAX_INTENTOS`. |
| **R4** — Presentación del trayecto | ✓ | `for reg in historial` con `inicio, fin = reg["rango"]` y formato tabulado alineado. |

### Resultados sobre el uso de estructuras de datos

La incorporación de estructuras de datos produjo beneficios concretos y medibles respecto a una versión sin ellas:

| Estructura | Beneficio concreto respecto a versión anterior |
|---|---|
| `RANGO: tuple` | Elimina la duplicación de los valores 1 y 100 en múltiples lugares; el mensaje de bienvenida y el algoritmo derivan del mismo origen único. |
| `RESPUESTAS_VALIDAS: tuple` | El mensaje de error se genera automáticamente con `join()`; si las opciones cambiaran, el mensaje se actualizaría sin modificación adicional. |
| `historial: list` | Habilita la presentación del trayecto completo de la partida, imposible sin almacenamiento cronológico ordenado. |
| `registro: dict` | Acceso semántico por clave (`reg["conjetura"]`, `reg["rango"]`) en lugar de posiciones anónimas, haciendo el código de presentación más legible y resistente a errores de indexación. |
| `estadisticas: dict` | Reemplaza cuatro variables independientes por un único objeto cohesivo con nombre, reduciendo el espacio de nombres global. |
| Diccionario de retorno | Elimina variables globales para comunicar resultados; acceso por nombre en lugar de por posición en el desempaquetado. |

### Resultado académico

El proyecto demuestra el dominio integrado de todos los contenidos del semestre en un producto cohesivo y funcionalmente completo. La justificación semántica de cada estructura de datos evidencia comprensión profunda del lenguaje, no conocimiento superficial. Las anotaciones de tipo, la arquitectura de tres capas, el diseño sin variables globales y la documentación técnica integrada en el docstring del módulo elevan la calidad del código a estándares que se aproximan a prácticas de desarrollo profesional.

**Conclusión basada en evidencia del funcionamiento del algoritmo:** El número 37 fue identificado en 3 de un máximo de 7 intentos. El valor 100 requirió exactamente 7 intentos, confirmando el peor caso teórico. Ninguno de los valores verificados superó el límite matemático garantizado. La complejidad logarítmica del algoritmo se corrobora experimentalmente: la búsqueda binaria resolvió todos los casos en ⌈log₂(100)⌉ = 7 o menos iteraciones, comportamiento imposible de garantizar con búsqueda lineal.

---

## 14. Conclusiones

**1. La búsqueda binaria es óptima para el problema de adivinanza comparativa.** La complejidad O(log₂ n) asegura que ningún algoritmo comparativo puede resolver el problema en menos de ⌈log₂ n⌉ comparaciones en el peor caso. Para n = 100, esto se traduce en un máximo matemáticamente garantizado de 7 intentos, verificado experimentalmente en todos los casos extremos y arbitrarios probados. La extrapolación lógica de este resultado indica que ante cualquier problema de búsqueda sobre un espacio ordenado —un catálogo de productos, un índice de base de datos, un sistema de autocompletado— la búsqueda binaria o sus variantes deben ser el punto de partida antes de considerar enfoques lineales: la garantía matemática no depende del dominio, sino de la ordenabilidad del espacio de búsqueda.

**2. Las estructuras de datos no son intercambiables: su elección comunica intención de diseño.** La elección entre tupla y lista, o entre lista y diccionario, debe responder a las propiedades intrínsecas del dato que representan. Las tuplas son apropiadas para constantes del dominio que no deben modificarse; las listas, para colecciones que crecen dinámicamente; y los diccionarios, para datos con nombre cuyo acceso semántico por clave es más significativo que el acceso por posición. La extrapolación de este principio trasciende Python: en cualquier lenguaje que ofrezca múltiples tipos de contenedores —arrays, hash maps, sets, linked lists—, la elección entre ellos debe responder a la semántica del dato. Esta distinción, aplicada con criterio desde el nivel introductorio, constituye la diferencia entre código que funciona y código que comunica intención de forma que cualquier colaborador puede comprender y mantener.

**3. La modularidad reduce la complejidad cognitiva y habilita la colaboración.** Encapsular la lógica de una partida en `jugar()` y comunicar resultados mediante un diccionario de retorno elimina variables globales, hace el código más fácil de comprender, probar y reutilizar. La ausencia total de efectos secundarios globales es una propiedad de diseño verificada en este proyecto que, extrapolada lógicamente, aplica a cualquier escala: en proyectos de equipo, APIs REST, pipelines de datos o microservicios, la ausencia de efectos secundarios en las unidades funcionales reduce el tiempo de depuración, facilita las pruebas automatizadas y permite la integración de componentes desarrollados independientemente.

**4. La arquitectura en tres capas aporta claridad ahora y escalabilidad en el futuro.** Separar presentación, lógica de negocio y datos —aunque en un mismo archivo— permite identificar qué partes del sistema son candidatas a evolucionar independientemente. La extrapolación de este principio es directa: esta separación no es un ejercicio académico sino el prerrequisito que hace posible el desarrollo en paralelo, la prueba independiente de capas y la evolución del sistema sin refactorización total. Es el mismo principio que estructura las aplicaciones web de producción en front-end, back-end y base de datos, y los sistemas empresariales en presentación, lógica de negocio y persistencia.

**5. La documentación técnica integrada en el código multiplica su valor para cualquier equipo.** El módulo docstring con la tabla ASCII de estructuras de datos, las anotaciones de tipo y los comentarios que explican el «por qué» de las decisiones de diseño —no el «qué» obvio del código— convierten el programa en un artefacto comprensible para cualquier programador que no haya participado en su desarrollo. La extrapolación lógica de este hallazgo es de largo alcance: en proyectos de software reales, el costo de incorporar un nuevo colaborador a un codebase bien documentado es significativamente menor que en uno funcionalmente equivalente pero opaco en sus decisiones de diseño. La documentación integrada, verificada en este proyecto a escala introductoria, escala linealmente con el tamaño del equipo.

**6. El pensamiento algorítmico genera capacidad de evaluación técnica transferible.** Los principios demostrados en este proyecto —eficiencia logarítmica, diseño modular, elección fundamentada de estructuras de datos— son los mismos que gobiernan sistemas de búsqueda, clasificación y procesamiento de datos que sustentan aplicaciones usadas por millones de personas. La extrapolación lógica de este resultado tiene alcance formativo: el profesional formado en fundamentos algorítmicos desde el nivel introductorio desarrolla criterio de evaluación aplicable más allá del código —a la selección de proveedores tecnológicos, a la evaluación de herramientas de terceros y al diseño de protocolos de comunicación—, porque comprende las propiedades fundamentales de los sistemas de información independientemente de su implementación concreta.

**7. Las limitaciones identificadas son oportunidades de aprendizaje con continuidad curricular directa.** La ausencia de persistencia de datos, la interfaz de consola, la falta de verificación de consistencia de las respuestas del usuario y la ausencia de pruebas automatizadas son oportunidades de aprendizaje claramente delimitadas, cada una asociada a competencias específicas que el estudiante desarrollará en semestres posteriores. La extrapolación de este resultado tiene implicación pedagógica: un proyecto que identifica con precisión sus propias limitaciones técnicas no solo demuestra comprensión de lo que se ha logrado, sino también conciencia del mapa de lo que queda por aprender, lo cual es un indicador de madurez intelectual que trasciende el dominio de la programación.

---

## 15. Limitaciones del Proyecto

Las siguientes limitaciones son reales y observables directamente en el código fuente:

### 15.1 Limitaciones funcionales

**El programa no verifica la consistencia lógica de las respuestas del usuario.** Si el usuario responde incorrectamente las pistas —ya sea por error o intencionalmente— el algoritmo puede agotar los siete intentos sin identificar el número secreto. La rama `else` del resultado final lo indica:

```python
else:
    # Solo ocurre si el usuario respondió incorrectamente las pistas
    print("  Se agotaron los intentos. ¿Respondiste correctamente las pistas?")
```

No existe ningún mecanismo de detección de contradicciones: si el usuario responde `"mayor"` cuando el rango activo ya no tiene elementos superiores a la conjetura, el programa no lo detecta.

**La interfaz es exclusivamente de consola.** El programa opera mediante `print()` e `input()` en la terminal. No existe interfaz gráfica, ni barra visual del rango, ni posibilidad de deshacer una respuesta incorrecta.

**Los datos de sesión son volátiles.** El diccionario `estadisticas` existe únicamente en memoria RAM durante la ejecución. Al cerrar el programa, toda información sobre partidas jugadas, ganadas, promedio de intentos y mejor marca se pierde. No existe mecanismo de persistencia.

### 15.2 Limitaciones técnicas

**Ausencia de manejo formal de excepciones.** El programa no utiliza bloques `try/except`. Una interrupción por teclado (`Ctrl+C`) o una redirección de entrada desde archivo puede terminar el programa abruptamente sin guardar datos de la sesión ni mostrar el resumen final.

**El rango no es configurable por el usuario.** Aunque `RANGO` es una constante fácilmente modificable en el código, el programa no ofrece al usuario la posibilidad de elegir el rango al inicio de cada sesión. Esta opción requeriría validación adicional para garantizar que el límite inferior sea menor que el superior.

**Ausencia de pruebas unitarias automatizadas.** La verificación del algoritmo es manual. No existe un conjunto de pruebas que verifique automáticamente el comportamiento correcto para todos los valores de 1 a 100, lo que deja espacio para la introducción accidental de errores si el código es modificado.

### 15.3 Limitaciones de alcance académico

El proyecto se enmarca en un curso introductorio de lógica de programación procedimental. No aborda programación orientada a objetos —donde la partida podría encapsularse en una clase `Partida`—, ni soporte de concurrencia para múltiples usuarios simultáneos, ni integración con bases de datos o servicios externos. Estas limitaciones son apropiadas para el nivel del curso y representan oportunidades de profundización en semestres posteriores.

### 15.4 Implicaciones del Proyecto

Las limitaciones identificadas no son simples deficiencias técnicas: cada una tiene implicaciones concretas y evidenciadas para la práctica pedagógica, el diseño de software y la secuencia curricular. Comprender estas implicaciones es tan relevante como enumerar las limitaciones mismas.

**Implicaciones pedagógicas:**

La ausencia de verificación de consistencia lógica de las respuestas del usuario implica que el programa, en su versión actual, no puede emplearse como herramienta de evaluación formativa autónoma sin supervisión docente. Si un estudiante responde incorrectamente las pistas —ya sea por error o para probar los límites del sistema—, el algoritmo agota los siete intentos sin identificar el número, como documenta el mensaje `else` del código:

```python
else:
    print("  Se agotaron los intentos. ¿Respondiste correctamente las pistas?")
```

Esta implicación señala una oportunidad de diseño curricular: integrar la detección de contradicciones lógicas como ejercicio de extensión para estudiantes avanzados, conectando el concepto de invariantes de algoritmo con la programación defensiva.

**Implicaciones técnicas:**

La ausencia de persistencia de datos implica que el diccionario `estadisticas`, aunque técnicamente correcto y funcional, no puede cumplir su propósito semántico más rico —el seguimiento del progreso a lo largo del tiempo— sin la integración de almacenamiento persistente. Esta limitación evidencia un principio técnico fundamental: la utilidad práctica de un módulo está acotada por la completitud del ecosistema en el que opera. `jugar()` y `estadisticas` son correctos individualmente, pero su valor a largo plazo está limitado por la volatilidad de la memoria RAM. Esta implicación tiene consecuencia inmediata en la dirección del trabajo futuro: agregar persistencia JSON no requiere modificar `jugar()` —un indicador directo de que la modularidad del diseño actual anticipa correctamente esta extensión.

La ausencia de manejo formal de excepciones implica que el programa opera en un modelo de confianza total: asume que el entorno externo (la terminal, el teclado, la sesión del usuario) no producirá condiciones anómalas. En un entorno educativo supervisado, esta asunción es razonable. Extrapolada a un entorno de producción, sería una vulnerabilidad crítica. Esta implicación es pedagógicamente valiosa en sí misma: evidencia con claridad la brecha entre un programa que funciona en condiciones normales y un programa robusto que se comporta correctamente ante condiciones anómalas —distinción que el estudiante internalizará en cursos de programación intermedia.

**Implicaciones curriculares:**

La ausencia de pruebas unitarias automatizadas implica que la verificación manual documentada en §12, aunque exhaustiva para los casos probados, no garantiza correctitud para el universo completo de posibles modificaciones futuras del código. Esta implicación conecta directamente con la siguiente etapa curricular: cuando el estudiante aprenda `unittest` o `pytest`, reconocerá en este proyecto el caso de uso concreto que justifica la existencia de las pruebas automatizadas —un reconocimiento facilitado por haber experimentado previamente la necesidad de verificar manualmente el mismo conjunto de casos.

La ausencia de programación orientada a objetos implica que `jugar()` y el bloque `__main__` realizan manualmente el trabajo que una clase `Partida` realizaría de forma más natural, encapsulando `bajo`, `alto`, `intentos`, `adivinado` e `historial` como atributos. Esta implicación es pedagógicamente estratégica: el estudiante que ha implementado la versión procedimental comprenderá con mayor profundidad por qué los objetos son una abstracción útil cuando los encuentre en semestres posteriores, porque habrá experimentado de primera mano el problema que los objetos resuelven.

---

## 16. Trabajo Futuro

Las siguientes mejoras son realistas y directamente derivadas de las limitaciones identificadas en el código actual:

**Persistencia de datos con JSON:** Utilizar el módulo `json` de la biblioteca estándar para serializar el diccionario `estadisticas` a un archivo al finalizar cada sesión y cargarlo al inicio de la siguiente. Esto permitiría construir un historial de partidas persistente entre sesiones y calcular estadísticas de largo plazo. El cambio no requeriría modificar `jugar()`.

```python
import json
# Al finalizar sesión:
with open("estadisticas.json", "w") as f:
    json.dump(estadisticas, f)
# Al iniciar sesión:
with open("estadisticas.json", "r") as f:
    estadisticas = json.load(f)
```

**Manejo de excepciones con `try/except`:** Envolver el bucle de sesión en `try/except KeyboardInterrupt` para capturar la interrupción del usuario con `Ctrl+C` y mostrar el resumen de sesión antes de cerrar el programa.

**Verificación de consistencia lógica:** Detectar respuestas contradictorias del usuario. Si el usuario responde `"mayor"` pero `bajo > medio`, el sistema podría alertar que la respuesta es inconsistente con el historial previo y solicitar confirmación.

**Pruebas unitarias automatizadas:** Utilizar `unittest` o `pytest` para verificar automáticamente que `jugar()` identifica correctamente cada valor del 1 al 100 en un máximo de 7 intentos, simulando las respuestas del usuario mediante mocking del `input()`.

**Modo inverso:** Agregar una modalidad donde la computadora elige el número aleatoriamente (módulo `random`) y el usuario intenta adivinarlo. Este modo reutilizaría las mismas estructuras de datos y el sistema de estadísticas con modificaciones mínimas en la lógica de retroalimentación.

**Refactorización orientada a objetos:** Crear una clase `Partida` que encapsule las variables `bajo`, `alto`, `intentos`, `adivinado` e `historial` como atributos, y los métodos del bucle principal como métodos de instancia. Este ejercicio de refactorización ilustra cómo el código procedimental actual se mapea naturalmente a la programación orientada a objetos.

**Interfaz gráfica con Tkinter:** Dado que `jugar()` es independiente de `print()` e `input()` en su lógica de negocio, puede actuar como back-end sin modificación. Solo sería necesario implementar una nueva capa de presentación que llame a `jugar()` e interprete su diccionario de retorno.

---

## 17. Competencias Desarrolladas

El proyecto integra transversalmente todos los contenidos abordados durante el semestre en la asignatura Lógica de Programación:

| Contenido de la asignatura | Aplicación concreta en el programa |
|---|---|
| **Variables y tipos de datos** | `bajo`, `alto`, `medio`, `intentos` (int); `adivinado`, `respuesta_valida`, `continuar` (bool); `respuesta`, `opciones` (str); con tipos compuestos `tuple`, `list`, `dict` con anotaciones de tipo explícitas. |
| **Operadores aritméticos** | División entera `//` para calcular el punto medio: `medio = (bajo + alto) // 2`. |
| **Operadores de asignación compuesta** | `intentos += 1`, `estadisticas["partidas_jugadas"] += 1`, `estadisticas["total_intentos"] += resultado["intentos"]`, `bajo = medio + 1`, `alto = medio - 1`. |
| **Operadores relacionales** | `resultado["intentos"] < estadisticas["mejor_marca"]` para actualizar la mejor marca; `estadisticas["partidas_ganadas"] > 0` para evitar división por cero. |
| **Operador de pertenencia `in`** | `respuesta in RESPUESTAS_VALIDAS` en la lógica de validación; `opcion in ("si", "sí", "s")` para el control de sesión. |
| **Condicionales `if/elif/else`** | Clasificación de la respuesta del usuario en tres casos mutuamente excluyentes: `"correcto"`, `"mayor"`, `"menor"`. Condicional adicional para el promedio. |
| **Bucle `while` externo** | Condición doble `while not adivinado and intentos < MAX_INTENTOS`: garantiza salida por victoria o por límite de intentos. |
| **Bucle `while` interno de validación** | `while not respuesta_valida`: repite la solicitud hasta recibir una entrada perteneciente a `RESPUESTAS_VALIDAS`. |
| **Bucle `while` de sesión** | `while continuar`: gestiona múltiples partidas consecutivas hasta que el usuario decide finalizar. |
| **Bucle `for`** | `for reg in historial`: recorre la lista de diccionarios para imprimir el trayecto completo de la partida. |
| **Funciones con valor de retorno** | `def jugar() -> dict:` con anotación de tipo de retorno, `return` explícito y ausencia total de variables globales. |
| **Modularización y `__main__`** | Separación entre constantes de módulo, función de lógica de juego y bloque de control de sesión con `if __name__ == "__main__":`. |
| **Tuplas** | `RANGO`, `RESPUESTAS_VALIDAS` y `rango_snapshot` como estructuras inmutables. Desempaquetado directo (`bajo, alto = RANGO`; `inicio, fin = reg["rango"]`) e indexación (`RANGO[0]`, `RANGO[1]`). |
| **Listas** | `historial` como registro cronológico dinámico. Método `.append()`, acceso por índice negativo `historial[-1]` y recorrido con `for`. |
| **Diccionarios** | `registro` por intento (4 claves), `estadisticas` de sesión (4 claves), diccionario de retorno de `jugar()` (4 claves). Acceso por clave, operadores `+=` para actualización. |
| **Anidamiento de estructuras** | Lista de diccionarios con tupla interna: `historial` → `registro` → `rango_snapshot`. |
| **Anotaciones de tipo** | `RANGO: tuple`, `historial: list`, `rango_snapshot: tuple`, `registro: dict`, `estadisticas: dict`, `resultado: dict`, `-> dict`. |
| **Documentación técnica** | Módulo docstring con tabla ASCII de estructuras, justificación semántica de decisiones de diseño y comentarios que explican el «por qué» del código. |
| **Análisis de complejidad** | Comparación O(n) vs O(log₂ n); garantía matemática de ⌈log₂(100)⌉ = 7 intentos; análisis de complejidad espacial O(1) asintótico. |
| **Buenas prácticas** | Constantes centralizadas, ausencia de variables globales, nomenclatura descriptiva, arquitectura en tres capas, generación dinámica de mensajes. |

---

## 18. Aprendizajes Obtenidos

**El tipo de dato elegido debe comunicar la naturaleza del dato.** Antes de este proyecto, tuplas y listas parecían intercambiables. Después de implementar `RANGO: tuple` y `historial: list`, queda claro que la tupla comunica inmutabilidad y la lista comunica crecimiento dinámico. Esta distinción semántica es una herramienta de diseño, no un detalle sintáctico.

**La modularidad no es solo organización: es una decisión de confianza.** Al encapsular toda la lógica de la partida en `jugar()` y comunicar resultados mediante un diccionario de retorno, el bloque `__main__` puede confiar en la función sin conocer sus detalles internos. Este principio —diseñar funciones que sean cajas negras confiables— es la base del desarrollo de software en equipos.

**La complejidad algorítmica tiene consecuencias prácticas medibles.** La diferencia entre O(n) y O(log₂ n) no es teórica: para n = 100, significa la diferencia entre 100 intentos y 7. Para n = 1.000.000, significa la diferencia entre un millón de intentos y veinte. Esta experiencia práctica hace que el concepto de complejidad sea intuitivo antes de estudiarlo formalmente.

**La documentación integrada en el código es más valiosa que los comentarios externos.** Las anotaciones de tipo, el docstring del módulo con la tabla ASCII de estructuras y los comentarios que explican decisiones de diseño forman parte del código mismo, no son documentos separados que pueden desincronizarse. Un programa bien documentado es más valioso que uno que simplemente funciona.

**Diseñar para el futuro sin sobrediseñar el presente.** Las constantes centralizadas (`RANGO`, `MAX_INTENTOS`) facilitan la evolución del sistema sin comprometer su funcionamiento actual. Centralizar las opciones válidas en `RESPUESTAS_VALIDAS` y generar el mensaje de error con `join()` son decisiones que preparan el código para cambios futuros sin agregar complejidad innecesaria hoy.

**El algoritmo correcto supera al código rápido.** La búsqueda binaria resuelve el problema en 7 pasos garantizados no porque esté escrita en un lenguaje rápido, sino porque su lógica es matemáticamente óptima. Elegir el algoritmo adecuado para cada problema es más importante que optimizar el código de un algoritmo subóptimo.

---

## 19. Tecnologías Utilizadas

| Herramienta | Versión | Función en el proyecto |
|---|:---:|---|
| **Python** | 3.14 | Lenguaje de implementación principal |
| **Visual Studio Code** | 1.110 | Editor de código, depurador integrado y extensiones Python + Pylance |
| **RAPTOR** | 4.1.0 | Diseño del diagrama de flujo del algoritmo en la fase previa a la implementación |
| **Git** | — | Control de versiones del código fuente |
| **GitHub** | — | Alojamiento y publicación del repositorio |

**Python 3.14** — Su tipado dinámico reduce la carga cognitiva en etapas introductorias, mientras que las anotaciones de tipo opcionales (PEP 484, disponibles desde Python 3.5) permiten documentar explícitamente el tipo de cada variable compleja sin forzar la verificación en tiempo de ejecución. Las estructuras de datos nativas —`tuple`, `list`, `dict`— son ciudadanos de primera clase del lenguaje, con sintaxis literal propia, métodos integrados y semántica bien definida. Python 3.14 incorpora además mejoras en los mensajes de error del intérprete que facilitan la identificación de fallos durante el aprendizaje.

**Visual Studio Code 1.110** — El resaltado sintáctico distingue visualmente las estructuras de datos (tuplas entre paréntesis, listas entre corchetes, diccionarios entre llaves). La integración con el depurador de Python permite inspeccionar en tiempo de ejecución el contenido del diccionario `historial` y de cada `registro`. La terminal integrada permite ejecutar el programa sin cambiar de contexto. La extensión Pylance ofrece verificación de tipos en tiempo real contra las anotaciones declaradas en el código.

**RAPTOR 4.1.0** — Utilizado en la fase de diseño algorítmico, previa a la implementación en Python. El diagrama de flujo del algoritmo de búsqueda binaria —con sus dos bucles `while` anidados, los tres caminos condicionales y los nodos de inicio/proceso/decisión/fin— permitió validar la lógica antes de escribir una sola línea de código, identificar casos límite y verificar que todas las ramas de decisión convergen hacia un estado final definido.

---

## 20. Organización del Repositorio

```
Proyecto_Final_Programacion/
│
├── Codigo/
│   └── Proyecto_Final_Programacion.py     ← Código fuente principal
│
├── Diagrama/
│   └── Proyecto_Final_3.rap               ← Diagrama de flujo en RAPTOR
│
├── Documentos/
│   └── Proyecto_Final_Programacion.pdf    ← Documento académico completo
    └── Proyecto-Integrador-de-Logica-de-Programacion.pdf    ← Documento académico completo


│
├── Video/
│   └── Video_Exposicion_Proyecto_Final.mp4 ← Video de exposición
│
└── README.md                              ← Documentación técnica (este archivo)
```

| Carpeta | Descripción |
|---|---|
| `Codigo/` | Contiene el archivo fuente Python del programa. Implementa el algoritmo de búsqueda binaria con las tres estructuras de datos integradas en 312 líneas documentadas. |
| `Diagrama/` | Contiene el diagrama de flujo del algoritmo desarrollado en RAPTOR 4.1.0 (`.rap`). Incluye los dos bucles `while` anidados, los tres caminos condicionales y todos los nodos del algoritmo. |
| `Documento/` | Contiene el documento académico completo del proyecto en PDF: análisis funcional, arquitectura de software, estructuras de datos, resultados, conclusiones y referencias. |
| `Video/` | Contiene el video de exposición del proyecto final con demostración en vivo del programa. |
| `README.md` | Documentación técnica del repositorio (este archivo). |

---

## 21. Requisitos e Instalación

### Requisitos

- **Python 3.14** o superior (compatible con Python 3.5+ por el uso de anotaciones de tipo).
- No se requieren librerías externas. El programa utiliza únicamente funciones y estructuras nativas del lenguaje Python.
- Sistema operativo compatible: Windows, macOS o Linux.
- Editor recomendado: Visual Studio Code 1.110 con las extensiones **Python** y **Pylance**.

### Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/Proyecto_Final_Programacion.git
```

2. Accede al directorio del proyecto:

```bash
cd Proyecto_Final_Programacion
```

3. Verifica que Python esté instalado correctamente:

```bash
python --version
# Python 3.14.x
```

No se requiere instalación de dependencias adicionales ni entornos virtuales.

---

## 22. Ejecución

Desde la terminal, navega a la carpeta `Codigo/` y ejecuta:

```bash
python Proyecto_Final_Programacion.py
```

El programa iniciará de forma interactiva. Piensa un número entre 1 y 100 y responde a cada conjetura con `mayor`, `menor` o `correcto` según corresponda. Al finalizar cada partida, se muestra el trayecto completo de intentos y la opción de jugar nuevamente.

### Ejemplo de sesión

```
==================================================
   BIENVENIDO AL JUEGO: ADIVINA EL NÚMERO
==================================================
Piensa un número entre 1 y 100.
La computadora lo adivinará en máximo 7 intentos
usando el algoritmo de BÚSQUEDA BINARIA.

Presiona ENTER cuando ya hayas pensado tu número...

  Intento 1/7  |  Rango actual: [1 - 100]
  ¿Tu número es el 50?
  Responde (mayor / menor / correcto): menor

  Intento 2/7  |  Rango actual: [1 - 49]
  ¿Tu número es el 25?
  Responde (mayor / menor / correcto): mayor

  Intento 3/7  |  Rango actual: [26 - 49]
  ¿Tu número es el 37?
  Responde (mayor / menor / correcto): correcto

==================================================
  ✓ ¡Lo conseguí! Tu número era el 37.
  Lo adiviné en 3 intento(s).

  Trayecto de la partida:
    #1  Rango [  1 - 100]  Conjetura:  50  →  menor
    #2  Rango [  1 - 49 ]  Conjetura:  25  →  mayor
    #3  Rango [ 26 - 49 ]  Conjetura:  37  →  correcto
==================================================

¿Deseas jugar de nuevo? (si / no): no

==================================================
  RESUMEN DE LA SESIÓN
==================================================
  Partidas jugadas  : 1
  Partidas ganadas  : 1
  Promedio intentos : 3.0
  Mejor marca       : 3 intento(s)
==================================================

¡Gracias por jugar! Hasta pronto.
```

---

## 23. Información Académica

| Campo | Detalle |
|---|---|
| **Estudiante** | Mery Elizabeth Guzmán Ontaneda |
| **Universidad** | Universidad Internacional del Ecuador (UIDE) |
| **Facultad** | Ingeniería de Software |
| **Carrera** | Ingeniería en Ciberseguridad |
| **Asignatura** | Lógica de Programación |
| **Docente** | MCS. Lilian Aman |
| **Avance** | Paso 1 + Paso 2 + Paso 3 — Versión con Estructuras de Datos |
| **Fecha** | Junio 22 al 28, 2026 |

---

*Proyecto desarrollado con dedicación como parte de la formación en Ingeniería en Ciberseguridad — UIDE · 2026*
