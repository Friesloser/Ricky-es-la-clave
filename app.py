import streamlit as st

st.set_page_config(page_title="Justicia Digital", layout="wide")

# -----------------------------
# CONTROL DE SECCIÓN ACTUAL
# -----------------------------
if "step" not in st.session_state:
    st.session_state.step = 0

def siguiente():
    if st.session_state.step < 7:
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

    st.markdown('<div class="bloque">', unsafe_allow_html=True)

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
Los algoritmos aprenden a partir de datos del pasado. Este fenómeno puede
generar lo que los investigadores llaman **sesgo algorítmico**.

Sandra Mayson (2019) explica que cualquier sistema que predice el futuro
utilizando datos históricos puede terminar reproduciendo las desigualdades
del pasado.
""")


# 4 DILEMA
elif st.session_state.step == 4:

    st.header("¿Precisión o justicia?")

    st.write("""
Un sistema puede ser matemáticamente preciso, pero socialmente injusto.

Miron et al. (2021) encontraron que algunos modelos pueden superar a expertos
humanos en predicción, pero al mismo tiempo fallar en métricas de equidad para
grupos protegidos como mujeres o personas extranjeras.
""")


# 5 EJEMPLOS
elif st.session_state.step == 5:

    st.header("Errores con consecuencias reales")

    st.write("""
En sistemas de evaluación de riesgo de violencia de género se han documentado
casos donde clasificaciones de riesgo bajo terminaron en tragedias.

También se han identificado diferencias en falsos positivos entre grupos
raciales, lo que significa que algunos grupos reciben más alertas injustificadas.
""")


# 6 FUTURO
elif st.session_state.step == 6:

    st.header("¿Hacia dónde vamos?")

    st.write("""
La tecnología puede ser una aliada poderosa, pero no es neutral.

Para evitar injusticias es necesario que los sistemas de IA sean transparentes
y que incluyan perspectivas sociales y de género desde su diseño.
""")


# 7 REFERENCIAS
elif st.session_state.step == 7:

    st.header("Referencias")

    refs = {
        "Chaverra Mena (2023)": "Analiza el sesgo algorítmico en sistemas judiciales y su impacto en víctimas de violencia de género.",
        "Fernández-Prados et al. (2025)": "Revisión sistemática sobre sesgos raciales y étnicos en sistemas de inteligencia artificial.",
        "Mayson (2019)": "Explica cómo los sistemas predictivos reproducen desigualdades históricas.",
        "Miron et al. (2021)": "Estudia las causas del sesgo en modelos de predicción criminal.",
        "Montesinos García (2023)": "Propone integrar perspectiva de género en algoritmos judiciales.",
        "Neil & Zanger-Tishler (2025)": "Analiza el sesgo en herramientas de evaluación de riesgo criminal.",
        "Roa Avella et al. (2023)": "Estudio sobre herramientas de predicción de violencia de género basadas en IA.",
        "Skeem & Lowenkamp (2020)": "Discute los dilemas entre precisión y justicia en predicción de reincidencia."
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
