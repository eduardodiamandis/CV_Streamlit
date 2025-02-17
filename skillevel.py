import streamlit as st


# Configuração da página
st.set_page_config(
    page_title="Eduardo Diamandis da Cruz - Currículo",
    page_icon="📄",
    layout="wide"
)

# CSS personalizado
st.markdown("""
<style>
    .header { color: #2e86c1; }
    .skill-bar { background-color: #e8f8f5; border-radius: 5px; padding: 3px; }
    .skill-progress { background-color: #2e86c1; border-radius: 5px; color: white; padding-left: 5px; }
</style>
""", unsafe_allow_html=True)

# Sidebar com informações de contato
with st.sidebar:
    st.header("📬 Contatos")
    st.write("**Telefone:** 11 947154475")
    st.write("**Email:** eduardodiamandis080@gmail.com")
    st.write("**GitHub:** [https://github.com/eduardodiamandis)")  # Adicione seu link real
    st.write("**LinkedIn:** [www.linkedin.com/in/eduardo-diamandis-080pp)")  # Adicione seu link real
    
    # Botão para download do PDF
    with open("Eduardo_curriculo_2024.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(
        label="📄 Download PDF",
        data=PDFbyte,
        file_name="Eduardo_Diamandis_CV.pdf",
        mime="application/octet-stream"
    )

# Seção principal
col1, col2 = st.columns([3,1])
with col1:
    st.title("EDUARDO DIAMANDIS DA CRUZ")
    st.header("Gestor de Tecnologia & Desenvolvedor", divider="blue")

    # Experiência Profissional
    with st.expander("## 🧑💻 Experiência Profissional", expanded=True):
        st.subheader("FCF - Gestor de Projetos (2022 – Atual)")
        st.markdown("""
        - Gestão de projetos de infraestrutura e redes
        - Desenvolvimento de automações em Python
        - Planejamento e acompanhamento de cronogramas
        - Redução de 40% no tempo de execução de processos
        """)

    # Formação Acadêmica
    with st.expander("## 🎓 Educação", expanded=True):
        st.subheader("Ciência da Computação - FIAP (2022–2026)")
        st.markdown("""
        - Automações em Python, Java e C++
        - GitFlow e EDA (Event-Driven Architecture)
        - Sistemas Cloud e APIs REST
        - Clean Architecture
        """)
        
        st.subheader("FulCycle 3.0 (2024–Atualmente)")
        st.markdown("- Arquitetura de Software e DevOps")

with col2:
    # Habilidades Técnicas
    st.header("🛠️ Habilidades", divider="blue")
    skills = {
        "Python": 100,
        "Java": 50,
        "Git": 75,
        "Inglês": 100,
        "C++": 50,
        "APIs REST": 80,
        "Cloud": 70
    }
    
    for skill, level in skills.items():
        st.markdown(f"""
        <div class="skill-bar">
            <div class="skill-progress" style="width: {level}%">{skill} - {level}%
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.write("")

    # Passatempos
    st.header("🎵 Passatempos", divider="blue")
    st.markdown("""
    - Leitura
    - Tocar Música
    - Corrida
    - Musculação
    """)

# Seção de Perfil
st.header("👤 Perfil Profissional", divider="blue")
st.markdown("""
Profissional da área de tecnologia com experiência em:
- Automação de processos com Python
- Gestão de projetos ágeis
- Desenvolvimento de arquiteturas escaláveis
- Otimização de fluxos de trabalho
- Implementação de soluções cloud
""")

# Rodapé
st.divider()
st.caption("Atualizado em Julho/2024 | Desenvolvido com Streamlit 🎈")
