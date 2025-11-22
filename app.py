import streamlit as st
import backend
import os

# --- Page Config ---
st.set_page_config(
    page_title="Atlantia Excel Processor",
    page_icon="📊",
    layout="wide"
)

# --- Load Custom CSS ---
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css("styles.css")

# --- Header ---
st.markdown('<h1 style="text-align: center; margin-bottom: 2rem;">📊 <span class="gradient-text">Atlantia Excel Processor</span></h1>', unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("assets/logo.png", use_container_width=True)
    st.markdown("### ⚙️ Configuración")
    
    mode = st.radio(
        "Modo de Procesamiento",
        ["Full Processing", "DS Only"],
        help="Elige el nivel de detalle del reporte."
    )

    sheet_name = st.text_input(
        "Nombre de la Hoja", 
        value="T2", 
        help="La hoja del Excel que contiene los datos principales."
    )

    segment_pdp = False
        
    st.markdown("---")
    st.info("ℹ️ **Tip:** Asegúrate de que tu archivo Excel tenga la estructura correcta.")

# --- Main Content ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Card Container
    with st.container(border=True):
        st.markdown("### 📤 Cargar Archivo")
        st.markdown("Sube tu archivo `.xlsx` para comenzar el análisis.")
        
        uploaded_file = st.file_uploader("", type=["xlsx"])
        
        if uploaded_file:
            st.success(f"✅ Archivo cargado: **{uploaded_file.name}**")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("🚀 Procesar Archivo", type="primary", use_container_width=True):
                with st.spinner("🔄 Procesando datos... por favor espera."):
                    try:
                        output_path = None
                        
                        if mode == "Full Processing":
                            output_path = backend.process_workbook_by_pdp(
                                uploaded_file,
                                segment_with_pdp=segment_pdp,
                                general_sheet=sheet_name
                            )
                        else: # DS Only
                            output_path = backend.process_workbook_ds_only(
                                uploaded_file,
                                sheet_name=sheet_name
                            )
                        
                        if output_path and os.path.exists(output_path):
                            st.balloons()
                            st.markdown("### 🎉 ¡Procesamiento Completado!")
                            st.markdown("Tu archivo está listo para descargar.")
                            
                            # Read file for download
                            with open(output_path, "rb") as f:
                                file_data = f.read()
                            
                            out_name = f"PROCESSED_{uploaded_file.name}"
                            
                            st.download_button(
                                label="📥 Descargar Resultado",
                                data=file_data,
                                file_name=out_name,
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                use_container_width=True
                            )
                            
                            # Cleanup temp file
                            os.remove(output_path)
                            
                    except Exception as e:
                        st.error(f"❌ Ocurrió un error: {e}")
                        st.exception(e)

        else:
            st.info("Esperando archivo...")
