import streamlit as st

st.set_page_config(page_title="Justicia Digital", layout="wide")

# -----------------------------
# CONTROL DE SECCIÓN ACTUAL
# -----------------------------
if "step" not in st.session_state:
    st.session_state.step = 0

def siguiente():
    if st.session_state.step < 5:
        st.session_state.step += 1

def anterior():
    if st.session_state.step > 0:
        st.session_state.step -= 1


# -----------------------------
# ESTILOS
# -----------------------------
st.markdown("""
<style>

body {
    font-family: serif;
}

h1,h2,h3 {
    font-family: sans-serif;
}

.bloque {
    height: 80vh;
    display:flex;
    flex-direction:column;
    justify-content:center;
}

.frase {
    text-align:right;
    font-style:italic;
    font-size:20px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# SECCIONES
# -----------------------------

# 0 PORTADA
if st.session_state.step == 0:

    st.title("¿Pueden los algoritmos heredar nuestros prejuicios?")
    st.subheader("El desafío de la justicia digital")

    st.write("Por: Mex Felipe y Gemini")

    st.markdown("""
    <div class="frase">
    "La verdadera inteligencia de un algoritmo no reside en su capacidad
    de predecir el futuro, sino en nuestra voluntad humana de programarlo
    para que no repita las injusticias del pasado."<br>
    ~Gemini
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# 1 INTRODUCCIÓN
elif st.session_state.step == 1:

    st.header("Introducción")

    st.write("""
Imagina que un juez debe decidir si una persona puede esperar su juicio en casa
o debe permanecer en prisión. Hoy en día, en muchos países, los jueces cuentan
con algoritmos que intentan predecir si alguien volverá a cometer un delito.

A primera vista parece una solución perfecta para lograr decisiones más rápidas
y objetivas. Sin embargo, la ciencia advierte que estos sistemas podrían estar
aprendiendo los prejuicios históricos de la sociedad.
""")


# 2 SECCIÓN IA EN LA CORTE
elif st.session_state.step == 2:

    st.header("La Inteligencia Artificial entra a la corte")

    st.write("""
La Inteligencia Artificial ha llegado al mundo legal para intentar predecir el
comportamiento humano. Según Roa Avella, Sanabria-Moyano y Dinas-Hurtado (2023),
estas herramientas pueden ayudar a predecir niveles de riesgo en situaciones
delicadas como la violencia de género.

Sin embargo, si no se diseñan cuidadosamente, pueden afectar derechos
fundamentales como la igualdad.
""")


# 3 SESGO ALGORÍTMICO
elif st.session_state.step == 3:

    st.header("El espejo del pasado: ¿por qué fallan los algoritmos?")

    st.write("""
Un algoritmo no piensa por sí mismo; aprende analizando miles de datos del pasado. Aquí es donde surge el problema que los científicos llaman "sesgo algorítmico". Sandra Mayson (2019), una experta en el tema, lo explica de forma muy clara: 
“El problema profundo es la naturaleza de la predicción misma. Toda predicción mira al pasado para hacer conjeturas sobre eventos futuros. En un mundo racialmente estratificado, cualquier método de predicción proyectará las desigualdades del pasado hacia el futuro”. 
Es como si intentáramos usar un mapa antiguo para navegar por una ciudad que ha cambiado: seguiremos chocando con los mismos muros. Si en el pasado ciertos grupos sufrieron más arrestos por prejuicios sociales, el algoritmo asumirá que esas personas son "más peligrosas" por naturaleza. Neil y Zanger-Tishler (2025) explican que los registros de arrestos no son medidas neutrales, ya que personas negras con pocos delitos enfrentan un riesgo de arresto mucho mayor que personas blancas en la misma situación.
""")


# 4 DILEMA
elif st.session_state.step == 4:

    st.header("¿Precisión o justicia? El dilema de la balanza")

    st.write("""
A veces, un programa puede ser muy "preciso" matemáticamente, pero muy injusto socialmente. Miron et al. (2021) observaron que estos modelos pueden ser más potentes que los expertos humanos, pero "a expensas de no satisfacer métricas de justicia para grupos protegidos como extranjeros y mujeres". 
Esto se traduce en errores con nombre y apellido: 
• En el género: En sistemas como VioGén en España, Chaverra Mena (2023) describe casos donde clasificar a alguien como "riesgo bajo" falló en proteger a mujeres que luego fueron asesinadas. 
• En la raza: Fernández-Prados et al. (2025) indican que existen "disparidades en métricas de equidad, tales como diferencias en sensibilidades y falsos positivos entre grupos raciales". Esto significa que el algoritmo suele dar "falsas alarmas" mucho más seguido cuando analiza a personas de ciertas etnias.
""")


# 5 FUTURO
elif st.session_state.step == 5:

    st.header("¿Hacia dónde vamos?")

    st.write("""
La tecnología puede ser una gran aliada, pero no es mágica. Para que la justicia sea realmente justa, necesitamos que estos sistemas sean transparentes y que incluyan una "perspectiva de género" desde el momento en que se escriben sus códigos (Montesinos García, 2023). 
Como advierte Skeem y Lowenkamp (2020), el costo de no corregir estos errores lo pagan las comunidades que ya son vulnerables. La ciencia nos dice que la IA solo será justa si nosotros, los humanos, nos esforzamos por enseñarle a serlo.
""")


# 6 REFERENCIAS
elif st.session_state.step == 6:

    st.header("Referencias")

    refs = {
        "Chaverra Mena, Y. E. (2023). El Sesgo Algorítmico en Sistemas Judiciales y su Impacto en Víctimas de Género. Universidad Católica de Colombia.": "El presente artículo explora el fenómeno del sesgo algorítmico en sistemas judiciales, con énfasis en su impacto sobre las víctimas de género. Se describe cómo el uso creciente de algoritmos e inteligencia artificial en la administración de justicia puede reproducir o amplificar prejuicios existentes, afectando negativamente a mujeres y grupos vulnerables. A través del análisis de casos internacionales (como COMPAS en Estados Unidos y VioGén en España) y la revisión del marco normativo colombiano, se evidencian riesgos de discriminación y limitaciones en la protección judicial. Se proponen estrategias para prevenir y mitigar estos sesgos, incluyendo la necesidad de transparencia, auditorías independientes, inclusión de perspectiva de género en el diseño algorítmico y formación especializada para operadores judiciales. Se concluye que la tecnología puede ser una aliada de la justicia solo si se implementa bajo principios de equidad y respeto por los derechos humanos. Palabras clave: Sesgo algorítmico, sistemas judiciales, violencia de género, tecnología legal, equidad, ética de la IA.",
        "Fernández-Prados, J. S., Cara-Fernández, Y., & Torres-Haro, M. J. (2025). Racial/Ethnic Bias in AI Systems: A PRISMA Systematic Review. International Journal of Migration Studies.": "Objetivo. Examinar la magnitud, dirección y ámbitos en los que aparece el sesgo étnico/racial en los sistemas de IA/ML, así como qué estrategias de mitigación muestran evidencia de efectividad. Métodos: Realizamos una búsqueda en Scopus (2014–presente) utilizando las cadenas de búsqueda bias AND “artificial intelligence” AND (racial OR ethni)*, siguiendo las directrices PRISMA 2020. Tras eliminar duplicados, se examinaron 526 registros mediante revisión doble (concordancia y resolución de discrepancias). Para asegurar una síntesis sólida, centramos el análisis en 10 revisiones sistemáticas recientes que abordan disparidades raciales/étnicas en salud, seguridad/justicia, crédito/finanzas, empleo/selección, educación y plataformas digitales. Extraímos resultados por subgrupos (por ejemplo, diferencias de precisión/errores entre grupos), métricas de equidad reportadas (como comparación de sensibilidades y falsos positivos entre grupos, diferencias globales de desempeño e “impacto dispar”), y medidas de mitigación (antes, durante y después del modelado, así como medidas de gobernanza). Resultados: Las 10 revisiones coinciden en que muchos sistemas de inteligencia artificial (IA) reproducen o amplifican desigualdades raciales/étnicas en diversos ámbitos. En salud, es común observar menor precisión o más errores para personas negras, latinas e indígenas; en seguridad/justicia, se documentan más falsos positivos para minorías. Entre las estrategias con evidencia de respaldo se encuentran mejoras en los datos (representatividad y calidad), reponderación/reescala de pérdidas, ajuste de umbrales para subgrupos y auditorías externas con resultados transparentes; sin embargo, la heterogeneidad y la medición de raza/etnicidad mediante inferencias o proxies limitan la certeza. Conclusiones: La evidencia apunta de manera consistente a la existencia de sesgos raciales/étnicos en la IA. Las medidas de mitigación pueden reducir las disparidades, pero su efecto es parcial y depende del contexto. Se recomienda reportar resultados por subgrupos, realizar validación externa, usar código y datos reproducibles, y fortalecer la gobernanza (auditorías y rendición de cuentas). Limitación: fuente única (Scopus). Palabras clave: justicia algorítmica; sesgo racial; inteligencia artificial; revisiones sistemáticas; PRISMA. Traducido al español.",
        "Mayson, S. G. (2019). Bias In, Bias Out. The Yale Law Journal, 128, 2218-2300.": "La policía, los fiscales, los jueces y otros actores del sistema de justicia penal utilizan cada vez más la evaluación algorítmica del riesgo para estimar la probabilidad de que una persona cometa un delito en el futuro. Como muchos académicos han señalado, estos algoritmos tienden a tener impactos raciales desiguales. En respuesta, los críticos proponen tres estrategias de resistencia: (1) la exclusión de factores de entrada que se correlacionan estrechamente con la raza; (2) ajustes en el diseño algorítmico para igualar las predicciones entre grupos raciales; y (3) el rechazo total de los métodos algorítmicos. La afirmación central de este artículo es que estas estrategias son, en el mejor de los casos, superficiales y, en el peor, contraproducentes, porque la fuente de la desigualdad racial en la evaluación del riesgo no reside ni en los datos de entrada, ni en un algoritmo específico, ni en la metodología algorítmica en sí. El problema profundo es la naturaleza misma de la predicción. Toda predicción recurre al pasado para hacer estimaciones sobre eventos futuros. En un mundo racialmente estratificado, cualquier método de predicción proyectará las desigualdades del pasado hacia el futuro. Esto es tan cierto para la predicción subjetiva que durante mucho tiempo ha predominado en la justicia penal como para las herramientas algorítmicas que ahora la están reemplazando. La evaluación algorítmica del riesgo ha revelado la desigualdad inherente a toda predicción, obligándonos a enfrentar un problema mucho mayor que los desafíos de una nueva tecnología. En resumen, los algoritmos arrojan nueva luz sobre un problema antiguo. En última instancia, sostiene el artículo, corregir la disparidad racial en la predicción requerirá cambios más fundamentales en la forma en que el sistema de justicia penal concibe y responde al riesgo. El artículo argumenta que el derecho penal y las políticas públicas deberían, en primer lugar, delimitar con mayor claridad los riesgos que realmente importan y, en segundo lugar, reconocer que algunos tipos de riesgo pueden estar más allá de nuestra capacidad de medición sin distorsión racial—en cuyo caso no deberían justificar la coerción estatal. Además, en la medida en que podamos evaluar el riesgo de manera confiable, los actores del sistema penal deberían procurar, siempre que sea posible, responder al riesgo con apoyo en lugar de restricción. De manera contraintuitiva, la evaluación algorítmica del riesgo podría ser una herramienta valiosa en un sistema que apoye a quienes están en situación de riesgo. Traducido al español.",
        "Miron, M., Tolan, S., Gómez, E., & Castillo, C. (2021). Evaluating causes of algorithmic bias in juvenile criminal recidivism. Artificial Intelligence and Law.": "En este artículo investigamos la predicción del riesgo de reincidencia delictiva entre acusados juveniles utilizando algoritmos de aprendizaje automático (ML) de propósito general. Mostramos que, en nuestro conjunto de datos, que contiene cientos de casos, los modelos de ML logran un mayor poder predictivo que una herramienta estructurada de evaluación profesional del riesgo, el Structured Assessment of Violence Risk in Youth (SAVRY), a costa de no cumplir con métricas relevantes de equidad entre grupos que SAVRY sí satisface. Exploramos con mayor detalle dos posibles causas de este sesgo algorítmico que están relacionadas con sesgos en los datos con respecto a dos grupos protegidos: extranjeros y mujeres. En particular, analizamos (1) las diferencias en la prevalencia de reincidencia entre los grupos protegidos y (2) la influencia del grupo protegido o de características correlacionadas en la predicción. Nuestros experimentos muestran que ambos factores pueden generar disparidades entre grupos en las métricas de equidad consideradas. Observamos que los métodos para mitigar la influencia de cualquiera de estas causas no garantizan resultados justos. Un análisis de la importancia de las variables utilizando LIME, un método de interpretabilidad en aprendizaje automático, muestra que algunos métodos de mitigación pueden desplazar el conjunto de características en las que se basan las técnicas de ML, alejándolas de variables demográficas y del historial delictivo, que están altamente correlacionadas con características sensibles. Palabras clave: Reincidencia delictiva · Aprendizaje automático · Equidad algorítmica · Evaluación de riesgo · Justicia penal · Toma de decisiones automatizada. Traducido al español.",
        "Montesinos García, A. (2023). Algoritmos predictivos y perspectiva de género en el proceso penal. IDP. Revista de Internet, Derecho y Política.": "La introducción en el proceso judicial de herramientas algorítmicas de evaluación del riesgo para auxiliar al juez debe necesariamente venir precedida de un análisis exhaustivo con perspectiva de género acerca de su impacto sobre los derechos fundamentales de las partes que pueden verse seriamente afectados, principalmente el de igualdad. Se reflexiona en este trabajo acerca de la posible incorporación de herramientas predictivas en diferentes etapas de un proceso penal para pasar a continuación a examinar el problema de los sesgos de género que pueden contener estas y sus consecuencias en el marco de un proceso. Palabras clave: algoritmos, inteligencia artificial, proceso penal, perspectiva de género, sesgos.",
        "Neil, R., & Zanger-Tishler, M. (2025). Algorithmic Bias in Criminal Risk Assessment. Annual Review of Criminology.": "Existe una gran preocupación por el sesgo racial algorítmico en los instrumentos de evaluación de riesgo (RAIs) utilizados en el sistema de justicia penal. Al evaluar el sesgo algorítmico, la mayoría de las investigaciones utiliza los datos de arrestos como una medida no sesgada de la conducta delictiva, lo cual entra en conflicto con preocupaciones de larga data de que el arresto es un indicador sesgado del delito. Dado el papel central de los datos de arresto en los RAIs, las diferencias raciales en la manera en que los arrestos representan la conducta delictiva pueden ser una vía clave a través de la cual estos instrumentos se vuelven sesgados. En esta revisión, evaluamos el amplio cuerpo de investigación sobre las diferencias raciales en el uso del arresto como medida del delito. Además, detallamos varias formas en que el sesgo racial en los registros de arresto podría generar sesgo algorítmico, aunque poca investigación ha intentado medir el grado de sesgo algorítmico producido por el uso de registros de arresto racialmente sesgados. Proporcionamos una guía para apoyar futuras investigaciones en la comprensión del impacto de los registros de arresto sesgados en los RAIs. Palabras clave: algoritmos, sesgo racial, conducta delictiva, arresto, evaluación de riesgo, predicción. Traducido al español",
        "Roa Avella, M. P., Sanabria-Moyano, J. E., & Dinas-Hurtado, K. (2023). Herramientas de predicción de violencia basada en género mediante la IA. Revista Jurídica Mario Alario D'Filippo.": "La Violencia basada en género, ha sido definida por la Organización de las Naciones Unidas como cualquier acto dañino basado en las diferencias de género atribuidas socialmente. Dentro de sus muchas manifestaciones, aquella violencia en su máxima expresión llega hasta el feminicidio; fenómeno que lejos de disminuir, se ha extendido alrededor del mundo. Por otra parte, la inteligencia artificial ha aparecido en la escena de diversos sectores, sin que el ámbito jurídico haya sido la excepción. La conexión entre la violencia basada en género y la Inteligencia artificial se da de la mano de las necesidades crecientes de prevención de la primera, a través por ejemplo de la predicción de niveles de riesgo en la que la segunda ofrece importantes ventajas. Utilizando una metodología cualitativa deductiva con alcance descriptivo exploratorio, en la que se aplican métodos propios del derecho y las ciencias computacionales para analizar fuentes primarias, secundarias y estudio de casos de algoritmos y herramientas de evaluación de riesgo, (sin dejar de lado la referencia a herramientas de predicción tradicionales que no utilizan Inteligencia artificial), se arriba a resultados que apuntan a que los algoritmos y herramientas mencionadas evalúan y ponderan factores situacionales y disparadores, relacionados con el perpetrador, la víctima, y la relación familiar; variando en el valor asignado a cada uno de estos; en cuanto a las críticas se encuentran estandarizadas en la precisión y confiabilidad de la predicción. Palabras clave: inteligencia artificial; violencia de género; feminicidio; predicción; niveles de riesgo.",
        "Skeem, J. & Lowenkamp, C. (2020). Using Algorithms to Address Trade-Offs Inherent in Predicting Recidivism. Behavioral Science and the Law.": "Aunque la evaluación del riesgo se ha utilizado cada vez más como una herramienta para ayudar a reformar el sistema de justicia penal, algunos actores se oponen firmemente al uso de algoritmos. La principal preocupación es que cualquier beneficio logrado al reducir de forma segura las tasas de encarcelamiento se vea compensado por costos para la justicia racial, que se consideran inherentes a los propios algoritmos. Sin embargo, los compromisos en términos de equidad son inherentes a la tarea de predecir la reincidencia, ya sea que la predicción la realice un algoritmo o un ser humano. Con base en una muestra emparejada de 67,784 personas negras y blancas bajo supervisión federal, evaluadas con el Post Conviction Risk Assessment (PCRA), comparamos cómo tres estrategias alternativas para “eliminar sesgos” en algoritmos afectan estos compromisos, utilizando el arresto por un delito violento como criterio. Estos algoritmos candidatos predicen fuertemente la reincidencia violenta (AUCs = .71–.72), pero varían en su asociación con la raza (r = .00–.21) y modifican los equilibrios entre el valor predictivo positivo y las tasas de falsos positivos. Proporcionar a los algoritmos acceso a la variable de raza (en lugar de omitirla o “cegar” sus efectos) puede maximizar la calibración y minimizar tasas de error desbalanceadas. Se discuten las implicaciones para los responsables de políticas públicas con preferencias de valor entre eficiencia y equidad. Palabras clave: evaluación de riesgo, algoritmo, raza, equidad, sesgo. Traducido al español."
    }

    for ref, resumen in refs.items():
        with st.expander(ref):
            st.write(resumen)


# -----------------------------
# BOTONES NAVEGACIÓN
# -----------------------------

col1, col2, col3 = st.columns([1,2,1])

with col1:
    st.button("⬅ Anterior", on_click=anterior)

with col3:
    st.button("Siguiente ➡", on_click=siguiente)
