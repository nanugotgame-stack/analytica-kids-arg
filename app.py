import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Analytica Kids - Argentina", page_icon="🧒")

# Título Principal
st.title("🧒 Analytica Kids")
st.subheader("Nutrición Invisible para el Hogar")

# Banner del PDF Premium (Estrategia de Venta)
st.info("🚀 **¡Llevá la nutrición al siguiente nivel!** Desbloqueá las 20 recetas exclusivas y la guía de marcas en nuestro PDF Premium por solo $10.000.")
if st.button("Descargar PDF Completo"):
    st.write("🔗 Redirigiendo a Mercado Pago...")

st.divider()

# Diccionario de Datos: Los 20 Platos Base (Versión Gratuita)
platos_base = {
    "Fideos Blancos": {
        "hack": "Disolver 5g de albúmina en polvo en la manteca o aceite de servido[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span).",
        "aporte": "Proteína de alta calidad para el desarrollo muscular[span_4](start_span)[span_4](end_span).",
        "tip": "Asegurate de mezclar bien para que no queden rastros blancos visibles[span_5](start_span)[span_5](end_span)."
    },
    "Puré de Papas": {
        "hack": "Mezclar con un 10% de puré de coliflor blanca ultra procesada[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span).",
        "aporte": "Fibra y vitaminas esenciales sin cambiar el color del puré[span_8](start_span)[span_8](end_span)[span_9](start_span)[span_9](end_span).",
        "tip": "La coliflor debe estar al vapor y procesada a punto crema para evitar grumos[span_10](start_span)[span_10](end_span)."
    },
    "Arroz Blanco": {
        "hack": "Cocinar el arroz usando caldo de huesos casero filtrado (transparente) en lugar de agua[span_11](start_span)[span_11](end_span)[span_12](start_span)[span_12](end_span).",
        "aporte": "Aminoácidos y minerales clave para la salud intestinal[span_13](start_span)[span_13](end_span)[span_14](start_span)[span_14](end_span).",
        "tip": "Filtrar el caldo con tela para que parezca agua pura antes de cocinar[span_15](start_span)[span_15](end_span)."
    },
    "Milanesas": {
        "hack": "Mezclar el pan rallado con harina de girasol molida extra fina (proporción 80/20)[span_16](start_span)[span_16](end_span)[span_17](start_span)[span_17](end_span).",
        "aporte": "Zinc y Magnesio, fundamentales para el crecimiento[span_18](start_span)[span_18](end_span)[span_19](start_span)[span_19](end_span).",
        "tip": "La harina de girasol debe estar bien tamizada para que pase desapercibida[span_20](start_span)[span_20](end_span)."
    },
    "Nuggets": {
        "hack": "Pincelar con aceite de coco neutro o inyectar gel de chía transparente[span_21](start_span)[span_21](end_span)[span_22](start_span)[span_22](end_span).",
        "aporte": "Grasas saludables y Omega 3[span_23](start_span)[span_23](end_span)[span_24](start_span)[span_24](end_span).",
        "tip": "Usar aceite de coco neutro para que no huela a coco al cocinarse[span_25](start_span)[span_25](end_span)."
    },
    "Yogur de Vainilla": {
        "hack": "Añadir inulina o psyllium en polvo de forma gradual[span_26](start_span)[span_26](end_span)[span_27](start_span)[span_27](end_span).",
        "aporte": "Fibra prebiótica para mejorar el tránsito y la microbiota[span_28](start_span)[span_28](end_span)[span_29](start_span)[span_29](end_span).",
        "tip": "Mezclar vigorosamente; el psyllium tiende a espesar el yogur si reposa mucho[span_30](start_span)[span_30](end_span)."
    }
}

# Renderizado de la App
st.header("🍴 Platos Sugeridos")
st.write("Seleccioná un plato para ver cómo enriquecerlo de forma invisible:")

for plato, info in platos_base.items():
    with st.expander(f"📍 {plato}"):
        st.markdown(f"**¿Cómo enriquecerlo?**\n\n{info['hack']}")
        st.success(f"**¿Qué aporta?**\n\n{info['aporte']}")
        st.caption(f"💡 **Tip del Lic. Viberti:** {info['tip']}")

# Footer con Contacto
st.divider()
st.markdown("""
**Lic. Emanuel Viberti**  
Nutricionista - Especialista en Musculación y Selectividad  
[WhatsApp](https://wa.me/5491136768018) | [Instagram](https://instagram.com/viberti.nutricion)[span_31](start_span)[span_31](end_span)[span_32](start_span)[span_32](end_span)
""")
