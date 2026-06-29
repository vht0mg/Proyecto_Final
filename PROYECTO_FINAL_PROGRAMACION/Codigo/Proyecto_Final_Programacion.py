"""
==================================================================
 PROYECTO  : ADIVINA EL NÚMERO (Búsqueda Binaria)
 MATERIA   : Lógica de Programación
 DOCENTE   : MCS. Lilian Aman
 ESTUDIANTE: Mery Elizabeth Guzmán Ontaneda
 AVANCE    : Paso 1 + Paso 2 + Paso 3 — Versión con Estructuras de Datos
==================================================================
Descripción:
  La computadora adivina en ≤ 7 intentos el número secreto del usuario
  (entre 1 y 100) usando búsqueda binaria. Cada intento descarta el
  50 % del rango activo. La lógica del algoritmo NO ha sido modificada.

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

Por qué tupla y no lista para RANGO y RESPUESTAS_VALIDAS:
  Las tuplas son INMUTABLES. Los límites del juego y las respuestas
  válidas son constantes del dominio que nunca deben modificarse en
  ejecución. Usar tupla comunica esa intención de forma explícita.
==================================================================
"""

# ================================================================
# CONSTANTES DE MÓDULO
# ================================================================

# ── TUPLA: Límites inmutables del espacio de búsqueda.
#    El desempaquetado directo (bajo, alto = RANGO) permite
#    inicializar ambas variables en una sola expresión, asegurando
#    que el mensaje de bienvenida y el algoritmo usen siempre
#    los mismos valores fuente.
RANGO: tuple = (1, 100)

# ── TUPLA: Conjunto fijo de respuestas que el sistema acepta.
#    Se usa en dos lugares:
#      1. join() genera dinámicamente el mensaje de error.
#      2. El índice -1 ["correcto"] es la condición de victoria.
#    Al ser tupla, nadie puede ampliar o eliminar opciones por error.
RESPUESTAS_VALIDAS: tuple = ("mayor", "menor", "correcto")

# ── Cota máxima de intentos garantizada por ⌈log₂(100)⌉ = 7.
#    Declarada a nivel de módulo para que tanto jugar() como el
#    bloque __main__ puedan acceder sin pasarla como argumento.
MAX_INTENTOS: int = 7


# ================================================================
# FUNCIÓN PRINCIPAL DEL JUEGO
# ================================================================
def jugar() -> dict:
    """
    Ejecuta una partida completa del juego Adivina el Número.

    La lógica del algoritmo de búsqueda binaria es exactamente
    la misma que en la versión anterior. Las estructuras de datos
    (lista + diccionarios) se incorporan para registrar y presentar
    el trayecto de cada partida sin alterar el flujo de decisiones.

    Retorna
    -------
    dict
        Resultados de la partida con las claves:
          "adivinado" (bool) — True si la computadora acertó.
          "intentos"  (int)  — Número de intentos empleados.
          "numero"    (int)  — Número secreto identificado.
          "historial" (list) — Lista de dicts, uno por intento.
    """

    # ------------------------------------------------------------------
    # PASO 1 — INICIALIZACIÓN DE VARIABLES
    # ------------------------------------------------------------------

    # ── Desempaquetado de la TUPLA RANGO.
    #    bajo y alto se derivan de la constante de módulo, garantizando
    #    coherencia entre el mensaje de bienvenida y el algoritmo.
    bajo, alto = RANGO

    intentos  = 0      # Contador de intentos (int); arranca en 0
    adivinado = False  # Bandera de control del bucle principal (bool)

    # ── LISTA: Registro cronológico de todos los intentos de la partida.
    #    Comienza vacía. En cada iteración del bucle principal se agrega
    #    un DICCIONARIO con los datos de ese intento mediante .append().
    #    Al terminar la partida se recorre con un for para imprimir el
    #    trayecto completo, demostrando utilidad real de la estructura.
    historial: list = []

    # ------------------------------------------------------------------
    # PASO 1 — MENSAJE DE BIENVENIDA  (OUTPUT)
    # Los índices RANGO[0] y RANGO[1] acceden a la TUPLA directamente,
    # asegurando que el mensaje refleje siempre los límites reales.
    # ------------------------------------------------------------------
    print("=" * 50)
    print("   BIENVENIDO AL JUEGO: ADIVINA EL NÚMERO")
    print("=" * 50)
    print(f"Piensa un número entre {RANGO[0]} y {RANGO[1]}.")
    print(f"La computadora lo adivinará en máximo {MAX_INTENTOS} intentos")
    print("usando el algoritmo de BÚSQUEDA BINARIA.\n")

    # ------------------------------------------------------------------
    # PASO 1 — CONFIRMACIÓN DEL USUARIO  (INPUT)
    # ------------------------------------------------------------------
    input("Presiona ENTER cuando ya hayas pensado tu número... ")
    print()

    # ------------------------------------------------------------------
    # PASO 2 — BUCLE PRINCIPAL (while)
    # Condición doble: garantiza salida por VICTORIA (adivinado = True)
    # o por LÍMITE DE INTENTOS (intentos == MAX_INTENTOS).
    # ------------------------------------------------------------------
    while not adivinado and intentos < MAX_INTENTOS:

        # ── Calcular conjetura: punto medio del rango activo.
        #    División entera (//) garantiza resultado entero.
        medio     = (bajo + alto) // 2
        intentos += 1   # Operador de asignación compuesta

        # ── Captura inmutable del rango ANTES de modificarlo.
        #    Se almacena como TUPLA para preservar en el historial
        #    el estado exacto al momento de la conjetura, aunque
        #    bajo/alto cambien después.
        rango_snapshot: tuple = (bajo, alto)

        # ── OUTPUT: Estado del intento actual
        print(f"  Intento {intentos}/{MAX_INTENTOS}  |  Rango actual: [{bajo} - {alto}]")
        print(f"  ¿Tu número es el {medio}?")

        # ── PASO 2 — Bucle interno de validación de entrada.
        #    Repite la solicitud hasta recibir una respuesta que
        #    pertenezca a la TUPLA RESPUESTAS_VALIDAS.
        respuesta_valida = False

        while not respuesta_valida:
            respuesta = input("  Responde (mayor / menor / correcto): ").strip().lower()

            # ── CONDICIONALES: clasificación exhaustiva de la respuesta.
            #    El orden es intencional: el caso de victoria se evalúa
            #    primero como práctica de diseño limpio.
            if respuesta == "correcto":
                # Computadora acertó → activar bandera y salir del bucle
                adivinado        = True
                respuesta_valida = True

            elif respuesta == "mayor":
                # Número secreto > conjetura → descartar mitad inferior
                bajo             = medio + 1
                respuesta_valida = True
                print()

            elif respuesta == "menor":
                # Número secreto < conjetura → descartar mitad superior
                alto             = medio - 1
                respuesta_valida = True
                print()

            else:
                # Respuesta fuera de RESPUESTAS_VALIDAS → rechazar entrada.
                # join() recorre la TUPLA y construye el mensaje dinámicamente,
                # evitando hardcodear las opciones en el string.
                opciones = " / ".join(RESPUESTAS_VALIDAS)
                print(f"  ⚠  Respuesta no válida. Opciones: {opciones}.")

        # ── Construir el DICCIONARIO del intento y añadirlo a la LISTA.
        #    Este registro se crea DESPUÉS de procesar la respuesta, cuando
        #    todos los campos ya tienen su valor definitivo.
        #    Claves del diccionario:
        #      "intento"   → posición ordinal del intento en la partida (int)
        #      "conjetura" → número propuesto por la computadora (int)
        #      "rango"     → estado del rango al momento de la conjetura (tupla)
        #      "respuesta" → pista proporcionada por el usuario (str)
        registro: dict = {
            "intento"   : intentos,
            "conjetura" : medio,
            "rango"     : rango_snapshot,   # tupla inmutable (bajo, alto)
            "respuesta" : respuesta,
        }
        historial.append(registro)   # Agrega el dict al final de la LISTA

    # ------------------------------------------------------------------
    # PASO 2 — RESULTADO FINAL
    # El número identificado se extrae del ÚLTIMO elemento de la LISTA
    # historial accediendo a la clave "conjetura" de su DICCIONARIO.
    # Esto demuestra lectura real de la estructura: historial[-1]["conjetura"]
    # ------------------------------------------------------------------
    numero_final: int = historial[-1]["conjetura"] if historial else medio

    print()
    print("=" * 50)

    if adivinado:
        print(f"  ✓ ¡Lo conseguí! Tu número era el {numero_final}.")
        print(f"  Lo adiviné en {intentos} intento(s).")
    else:
        # Solo ocurre si el usuario respondió incorrectamente las pistas
        print("  Se agotaron los intentos. ¿Respondiste correctamente las pistas?")

    # ── Resumen de la partida recorriendo la LISTA historial con un for.
    #    Por cada DICCIONARIO se desempaqueta su TUPLA "rango" y se
    #    muestran todos los campos de forma tabulada y alineada.
    print()
    print("  Trayecto de la partida:")
    for reg in historial:
        inicio, fin = reg["rango"]          # desempaquetado de la tupla interna
        print(
            f"    #{reg['intento']}  "
            f"Rango [{inicio:>3} - {fin:<3}]  "
            f"Conjetura: {reg['conjetura']:>3}  "
            f"→  {reg['respuesta']}"
        )

    print("=" * 50)

    # ── Retornar DICCIONARIO con los resultados de esta partida.
    #    El bloque __main__ lo usa para actualizar las estadísticas
    #    de sesión sin necesidad de variables globales.
    return {
        "adivinado": adivinado,
        "intentos" : intentos,
        "numero"   : numero_final,
        "historial": historial,
    }


# ================================================================
# BLOQUE DE EJECUCIÓN Y ESTADÍSTICAS DE SESIÓN
# ================================================================
if __name__ == "__main__":

    # ── DICCIONARIO: Métricas acumuladas de toda la sesión de juego.
    #    Se actualiza tras cada partida con los datos del DICCIONARIO
    #    retornado por jugar(), sin necesidad de variables globales.
    #    Claves:
    #      "partidas_jugadas" → total de rondas completadas en la sesión
    #      "partidas_ganadas" → rondas donde la computadora acertó
    #      "total_intentos"   → suma de intentos en partidas ganadas
    #      "mejor_marca"      → menor número de intentos para acertar
    estadisticas: dict = {
        "partidas_jugadas" : 0,
        "partidas_ganadas" : 0,
        "total_intentos"   : 0,
        "mejor_marca"      : MAX_INTENTOS,  # Peor caso posible como referencia
    }

    continuar = True

    while continuar:

        # ── Ejecutar una partida y capturar su DICCIONARIO de resultados
        resultado: dict = jugar()

        # ── Actualizar el DICCIONARIO de estadísticas con los datos
        #    de la partida recién finalizada
        estadisticas["partidas_jugadas"] += 1

        if resultado["adivinado"]:
            estadisticas["partidas_ganadas"] += 1
            estadisticas["total_intentos"]   += resultado["intentos"]

            # Actualizar mejor marca si esta partida fue más eficiente
            if resultado["intentos"] < estadisticas["mejor_marca"]:
                estadisticas["mejor_marca"] = resultado["intentos"]

        # ── INPUT: Preguntar si el usuario desea continuar
        print()
        opcion = input("¿Deseas jugar de nuevo? (si / no): ").strip().lower()

        # Condicional para decidir si se lanza otra partida
        if opcion in ("si", "sí", "s"):
            print("\n" + "─" * 50 + "\n")
            continuar = True
        else:
            continuar = False

            # ── Mostrar resumen de sesión recorriendo el DICCIONARIO estadisticas.
            #    Cada clave se accede individualmente para imprimir las métricas
            #    finales de la sesión completa.
            print("\n" + "=" * 50)
            print("  RESUMEN DE LA SESIÓN")
            print("=" * 50)
            print(f"  Partidas jugadas  : {estadisticas['partidas_jugadas']}")
            print(f"  Partidas ganadas  : {estadisticas['partidas_ganadas']}")

            # Calcular e imprimir promedio solo si hubo al menos una victoria,
            # evitando una división por cero
            if estadisticas["partidas_ganadas"] > 0:
                promedio = (
                    estadisticas["total_intentos"]
                    / estadisticas["partidas_ganadas"]
                )
                print(f"  Promedio intentos : {promedio:.1f}")
                print(f"  Mejor marca       : {estadisticas['mejor_marca']} intento(s)")

            print("=" * 50)
            print("\n¡Gracias por jugar! Hasta pronto.\n")
