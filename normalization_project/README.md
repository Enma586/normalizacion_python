# Guía de Uso de la Interfaz Interactiva

Al iniciar la aplicación, se desplegará un menú principal interactivo en la terminal con las siguientes opciones:

1. Procesar y Normalizar Archivo JSON
   - Lee el conjunto de datos crudos.
   - Separa los registros inválidos en invalidas.json.
   - Almacena los registros homogéneos en memoria interna listos para su exploración.

2. Listar Transacciones Normalizadas
   - Muestra una vista limpia en formato de tabla de todos los registros normalizados vigentes.

3. Aplicar Filtros Avanzados
   - Permite segmentar dinámicamente los registros por:
     - Fuente de Origen: visualizar solo transacciones importadas de la Fuente B.
     - Estado Uniforme: visualizar únicamente transacciones con estado SUCCESS.
     - Tipo de Moneda: filtrar exclusivamente movimientos en USD.

4. Visualizar Tablero de Métricas
   - Despliega un resumen estadístico global con:
     - volúmenes procesados,
     - tasas de error,
     - sumatoria acumulada neta por cada divisa individual.

5. Salir
   - Finaliza la sesión de forma segura.

# Nota Técnica: Decisiones de Diseño y Uso Consciente de IA

## 1. Decisiones de Diseño Técnico

- Aislamiento de Errores (Resiliencia): en lugar de interrumpir de forma abrupta la ejecución mediante excepciones no controladas, se optó por un patrón de diseño defensivo. El módulo validator.py captura la incongruencia, registra el índice, añade un campo descriptivo explicando la falla (error_reason) y desvía la transacción corrupta a un repositorio de depuración externo.
- Estrategia de Parsing de Montos: la diversidad en la representación de los montos representaba el mayor riesgo de desbordamiento o error de tipo. Se diseñó un formateador basado en expresiones regulares que elimina caracteres tipográficos, como el símbolo €, convierte comas en puntos decimales y, en el caso específico de la Fuente B, aplica una división matemática por factores de potencia de 10 para normalizar centavos a flotantes reales.

## 2. Uso Consciente de la Inteligencia Artificial como Apoyo al Desarrollo

- Límites de Autonomía de la IA: siguiendo rigurosamente las pautas metodológicas de la actividad, la Inteligencia Artificial se utilizó estrictamente como un acelerador de productividad y estructura arquitectónica. La IA no tomó decisiones conceptuales ni de negocio sobre las reglas del sistema. El esquema de salida, los criterios que determinan si una transacción es descartada, el mapeo semántico de los estados y la estructuración del flujo de control fueron definidos enteramente por el criterio del estudiante, codificándose explícitamente en el archivo centralizado config.py.
- Refinamiento y Ajustes sobre las Sugerencias: durante las iteraciones de desarrollo, el modelo de IA sugirió inicialmente el uso de bibliotecas de terceros de gran peso, como pandas o pydantic, para agilizar el proceso de data-parsing y validación de tipos. Analizando las restricciones del entorno, se descartó esta propuesta con el fin de priorizar una solución liviana, portable y con cero dependencias externas, optimizando rutinas nativas con el uso estructurado de módulos nativos como datetime y re.
