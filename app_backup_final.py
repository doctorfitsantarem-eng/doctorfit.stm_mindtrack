<<<<<<< Updated upstream
# DoctorFit MindTrack — SISTEMA COMPLETO COM RELATÓRIOS PREMIUM
=======
# DoctorFit MindTrack — VERSÃO COMPLETA COM ÍCONE PERSONALIZADO
>>>>>>> Stashed changes
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image
from io import BytesIO
import base64, os
from datetime import datetime, timedelta

# ================= CONFIG COM ÍCONE PERSONALIZADO =================
st.set_page_config(
    page_title="DoctorFit MindTrack", 
<<<<<<< Updated upstream
    page_icon="🧠",
=======
    page_icon="assets/doctorfit_icon.png",  # SEU ÍCONE PERSONALIZADO
>>>>>>> Stashed changes
    layout="centered",
    initial_sidebar_state="collapsed"
)

<<<<<<< Updated upstream
# ================= CSS =================
st.markdown("""
<style>
    .main { background: #000000; color: #ffffff; }
    .stApp { background: #000000; }
    .stButton>button { background: #A6CE39; color: #000000; width: 100%; }
    h1, h2, h3 { color: #ffffff !important; }
    .metric-card { 
        background: #1a1a1a; 
        padding: 15px; 
        border-radius: 10px; 
        text-align: center;
        border: 1px solid #333;
        margin: 5px 0;
    }
    .metric-value { 
        font-size: 1.8rem; 
        font-weight: 700; 
        color: #A6CE39; 
    }
    .metric-label { 
        font-size: 0.8rem; 
        color: #888888; 
        margin-top: 4px;
    }
    .feedback-card {
        background: #1a1a1a;
        border: 1px solid #333;
        border-radius: 12px;
        padding: 15px;
        margin: 8px 0;
        border-left: 4px solid #A6CE39;
    }
    .report-header {
        background: linear-gradient(135deg, #A6CE39 0%, #8BC34A 100%);
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
    }
    .logo-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .logo-img {
        max-width: 200px;
        height: auto;
    }
</style>
""", unsafe_allow_html=True)

# ================= FUNÇÃO PARA CARREGAR LOGO =================
def carregar_logo():
    """Carrega a logo da DoctorFit"""
    try:
        # Tenta carregar a logo se existir
        logo = Image.open("logo.png")
        return logo
    except:
        try:
            logo = Image.open("logo.jpg")
            return logo
        except:
            # Se não encontrar logo, retorna None
            return None

# ================= FUNÇÃO PARA LOGO BASE64 (PDF) =================
def get_logo_base64():
    """Converte a logo para base64 para uso no PDF"""
    try:
        logo = carregar_logo()
        if logo:
            buffered = BytesIO()
            logo.save(buffered, format="PNG")
            return base64.b64encode(buffered.getvalue()).decode()
        return None
    except:
        return None

# ================= SISTEMA DE ESTADO =================
=======
LOGO_PATH = "assets/logo_doctorfit.jpg"
ICON_PATH = "assets/doctorfit_icon.png"

# ================= CORES DOCTORFIT =================
DOCTORFIT_GREEN = "#A6CE39"
DOCTORFIT_DARK = "#000000"
DOCTORFIT_LIGHT = "#1A1A1A"
DOCTORFIT_WHITE = "#FFFFFF"

# ================= MOBILE CONFIG =================
def setup_mobile_config():
    """Configurações específicas para mobile"""
    st.markdown("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <meta name="theme-color" content="#A6CE39">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <style>
    @viewport {
        width: device-width;
        zoom: 1.0;
    }
    </style>
    """, unsafe_allow_html=True)

setup_mobile_config()

# ================= CSS DOCTORFIT PERSONALIZADO =================
st.markdown(f"""
<style>
/* FUNDO E CORES DOCTORFIT */
html, body, [class*="css"]  {{ 
    background: {DOCTORFIT_DARK} !important; 
    color: {DOCTORFIT_WHITE} !important;
    font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif !important;
}}

.stApp {{
    background: {DOCTORFIT_DARK} !important;
    background-color: {DOCTORFIT_DARK} !important;
}}

/* Container principal */
.main .block-container {{
    padding-top: 1rem;
    padding-bottom: 1rem;
    max-width: 1200px;
    background: {DOCTORFIT_DARK} !important;
}}

/* HEADER DOCTORFIT */
.app-title {{ 
    text-align: center; 
    font-size: 2.5rem; 
    font-weight: 800 !important;
    color: {DOCTORFIT_GREEN} !important;
    margin-bottom: 0.5rem;
    letter-spacing: -1px;
    text-transform: uppercase;
    font-family: 'Inter', sans-serif;
}}

.app-subtitle {{
    text-align: center;
    font-size: 1.1rem;
    color: #CCCCCC !important;
    font-weight: 400;
    margin-bottom: 2rem;
    letter-spacing: 1px;
}}

.gradient-divider {{
    width: 200px;
    height: 4px;
    background: linear-gradient(90deg, {DOCTORFIT_GREEN}, #8BC34A);
    margin: 0 auto 2rem;
    border-radius: 2px;
}}

/* BOTÕES DOCTORFIT */
.stButton > button {{
    width: 100%;
    background: {DOCTORFIT_GREEN};
    color: {DOCTORFIT_DARK} !important;
    border: none;
    border-radius: 12px;
    padding: 16px 1rem;
    font-weight: 700;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    min-height: 56px;
    margin: 8px 0;
    font-family: 'Inter', sans-serif;
}}

.stButton > button:hover {{
    background: #8BC34A;
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(166, 206, 57, 0.4);
}}

/* MÉTRICAS DOCTORFIT */
.metric-corporate {{
    background: {DOCTORFIT_LIGHT};
    border-radius: 12px;
    padding: 18px;
    text-align: center;
    border: 1px solid #333;
    margin: 8px 0;
    transition: all 0.3s ease;
}}
.metric-corporate:hover {{
    border-color: {DOCTORFIT_GREEN};
    transform: translateY(-2px);
}}
.metric-value-corporate {{
    font-size: 2rem;
    font-weight: 800;
    color: {DOCTORFIT_GREEN};
}}
.metric-label-corporate {{
    font-size: 0.8rem;
    color: #888888;
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

/* TÍTULOS */
h1, h2, h3 {{
    color: {DOCTORFIT_WHITE} !important;
    font-weight: 700 !important;
}}
h1 {{
    font-size: 1.8rem !important;
    margin-bottom: 1.5rem !important;
    border-left: 4px solid {DOCTORFIT_GREEN};
    padding-left: 1rem;
}}

/* SLIDERS */
.stSlider {{
    margin: 1.2rem 0;
}}
.stSlider > div > div {{
    background: {DOCTORFIT_GREEN} !important;
}}

/* CARDS */
.feedback-card {{
    background: linear-gradient(135deg, {DOCTORFIT_LIGHT}, #2d2d2d);
    border: 1px solid #333;
    border-radius: 12px;
    padding: 18px;
    margin: 10px 0;
    transition: all 0.3s ease;
}}
.feedback-card:hover {{
    border-color: {DOCTORFIT_GREEN};
    transform: translateY(-2px);
}}

.history-card {{
    background: linear-gradient(135deg, {DOCTORFIT_LIGHT}, #2d2d2d);
    border: 1px solid #3498DB;
    border-radius: 12px;
    padding: 18px;
    margin: 10px 0;
    border-left: 4px solid #3498DB;
}}

/* ========== MOBILE CRITICAL FIXES ========== */
@media (max-width: 768px) {{
    .main .block-container {{
        padding-left: 10px !important;
        padding-right: 10px !important;
        padding-top: 0.5rem !important;
        max-width: 100% !important;
        background: {DOCTORFIT_DARK} !important;
    }}
    
    .app-title {{
        font-size: 2rem !important;
        margin-bottom: 0.3rem !important;
    }}
    
    .app-subtitle {{
        font-size: 0.9rem !important;
        margin-bottom: 1rem !important;
    }}
    
    .gradient-divider {{
        width: 120px;
        margin-bottom: 1.5rem;
    }}
    
    .metric-corporate {{
        padding: 12px !important;
        margin: 5px 0 !important;
    }}
    
    .metric-value-corporate {{
        font-size: 1.6rem !important;
    }}
    
    .metric-label-corporate {{
        font-size: 0.7rem !important;
    }}
    
    .stButton > button {{
        min-height: 52px !important;
        font-size: 1rem !important;
        padding: 14px 1rem !important;
    }}
    
    h1 {{
        font-size: 1.5rem !important;
        padding-left: 0.5rem !important;
        margin-bottom: 1rem !important;
    }}
    
    h2 {{
        font-size: 1.3rem !important;
    }}
    
    h3 {{
        font-size: 1.1rem !important;
    }}
    
    .feedback-card {{
        padding: 15px !important;
    }}
    
    /* Ajuste para colunas em mobile */
    .row-widget.stColumns {{
        gap: 8px;
    }}
}}

/* ========== TABLET OPTIMIZATION ========== */
@media (min-width: 769px) and (max-width: 1024px) {{
    .block-container {{
        padding: 1rem !important;
        max-width: 95% !important;
        background: {DOCTORFIT_DARK} !important;
    }}
    
    .app-title {{
        font-size: 2.2rem !important;
    }}
    
    .metric-corporate {{
        padding: 15px !important;
    }}
}}

/* ========== ORIENTATION SUPPORT ========== */
@media (max-height: 500px) and (orientation: landscape) {{
    .block-container {{
        padding-top: 0.5rem !important;
        background: {DOCTORFIT_DARK} !important;
    }}
    
    .app-title {{
        font-size: 1.8rem !important;
    }}
    
    .app-subtitle {{
        margin-bottom: 0.5rem !important;
    }}
}}

/* Hide Streamlit elements */
#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
header {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

# ================= SISTEMA DE ESTADO ROBUSTO =================
>>>>>>> Stashed changes
def ensure_state():
    if "page" not in st.session_state:
        st.session_state.page = "cadastro"
    if "aluno" not in st.session_state:
        st.session_state.aluno = ""
    if "turma" not in st.session_state:
        st.session_state.turma = ""
    
    # Scores separados
    if "scores_geral" not in st.session_state:
        st.session_state.scores_geral = {
            "Autorregulação": None,
            "Autoeficácia": None, 
            "Estabilidade": None
        }
    
    if "scores_treino" not in st.session_state:
        st.session_state.scores_treino = {
            "Autorregulação": None,
            "Autoeficácia": None,
            "Estabilidade": None  
        }
    
    if "historico" not in st.session_state:
        st.session_state.historico = {}

ensure_state()

# ================= FUNÇÕES AUXILIARES =================
def calcular_media(scores_dict):
    valores = [v for v in scores_dict.values() if v is not None]
    return round(sum(valores) / len(valores), 1) if valores else None

def salvar_no_historico(tipo_avaliacao):
    if not st.session_state.aluno:
        return
    
    aluno_key = f"{st.session_state.aluno}_{st.session_state.turma}"
    
    if aluno_key not in st.session_state.historico:
        st.session_state.historico[aluno_key] = []
    
    if tipo_avaliacao == "geral":
        scores = st.session_state.scores_geral
    else:
        scores = st.session_state.scores_treino
    
    registro = {
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tipo": tipo_avaliacao,
        "scores": scores.copy(),
        "media": calcular_media(scores),
        "aluno": st.session_state.aluno,
        "turma": st.session_state.turma
    }
    
<<<<<<< Updated upstream
    st.session_state.historico[aluno_key].append(registro)
    return True
=======
    # Verifica se já existe avaliação no mesmo dia (evita duplicatas)
    data_hoje = datetime.now().strftime("%Y-%m-%d")
    avaliacoes_hoje = [av for av in st.session_state.historico[aluno_key] 
                      if av['data'].startswith(data_hoje)]
    
    if not avaliacoes_hoje:
        st.session_state.historico[aluno_key].append(avaliacao_atual)
        return True
    return False

def carregar_historico_aluno():
    """Carrega o histórico do aluno atual"""
    if not st.session_state.aluno:
        return []
    
    aluno_key = f"{st.session_state.aluno}_{st.session_state.turma}"
    return st.session_state.historico.get(aluno_key, [])

# ================= SISTEMA DE HISTÓRICO TEMPORAL =================
def gerar_grafico_evolucao():
    """Gera gráfico de evolução temporal das médias"""
    historico = carregar_historico_aluno()
    
    if len(historico) < 2:
        return None  # Precisa de pelo menos 2 avaliações
    
    # Ordena por data
    historico_ordenado = sorted(historico, key=lambda x: x['timestamp'])
    
    # Prepara dados
    datas = [datetime.fromisoformat(av['timestamp']).strftime('%d/%m') for av in historico_ordenado]
    medias_geral = [av['media_geral'] for av in historico_ordenado]
    medias_treino = [av['media_treino'] for av in historico_ordenado]
    
    # Cria gráfico
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Configurações de estilo
    fig.patch.set_facecolor(DOCTORFIT_DARK)
    ax.set_facecolor(DOCTORFIT_DARK)
    
    # Plot das linhas
    linha_geral, = ax.plot(datas, medias_geral, marker='o', linewidth=3, 
                          color=DOCTORFIT_GREEN, markersize=8, label='Média Geral')
    linha_treino, = ax.plot(datas, medias_treino, marker='s', linewidth=3, 
                           color='#3498DB', markersize=8, label='Média Treino')
    
    # Preenchimento sob as curvas
    ax.fill_between(datas, medias_geral, alpha=0.2, color=DOCTORFIT_GREEN)
    ax.fill_between(datas, medias_treino, alpha=0.2, color='#3498DB')
    
    # Configurações do gráfico
    ax.set_ylabel('Pontuação Média', color='#cccccc', fontsize=12, fontweight=600)
    ax.set_xlabel('Data da Avaliação', color='#cccccc', fontsize=12, fontweight=600)
    ax.set_title('EVOLUÇÃO TEMPORAL - DESEMPENHO PSICOSSOCIAL', 
                color=DOCTORFIT_WHITE, fontsize=14, fontweight=700, pad=20)
    
    # Limites e grades
    ax.set_ylim(0, 10)
    ax.set_yticks(range(0, 11, 2))
    ax.grid(True, alpha=0.2, color='#cccccc')
    ax.set_axisbelow(True)
    
    # Legendas
    ax.legend(facecolor=DOCTORFIT_LIGHT, edgecolor='#333333', fontsize=11,
             loc='upper left', bbox_to_anchor=(0, 1))
    
    # Estilo dos eixos
    ax.tick_params(colors='#cccccc', labelsize=10)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Salva o gráfico
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"evolucao_{ts}.png"
    plt.savefig(path, dpi=300, transparent=True, bbox_inches='tight',
                facecolor=DOCTORFIT_DARK, edgecolor='none')
    plt.close(fig)
    
    return path

def calcular_estatisticas_evolucao():
    """Calcula estatísticas de evolução do aluno"""
    historico = carregar_historico_aluno()
    
    if len(historico) < 2:
        return None
    
    historico_ordenado = sorted(historico, key=lambda x: x['timestamp'])
    
    # Primeira e última avaliação
    primeira = historico_ordenado[0]
    ultima = historico_ordenado[-1]
    
    # Progresso
    progresso_geral = ultima['media_geral'] - primeira['media_geral']
    progresso_treino = ultima['media_treino'] - primeira['media_treino']
    
    # Tendência
    tendencia_geral = "📈 Melhoria" if progresso_geral > 0 else "📉 Queda" if progresso_geral < 0 else "➡️ Estável"
    tendencia_treino = "📈 Melhoria" if progresso_treino > 0 else "📉 Queda" if progresso_treino < 0 else "➡️ Estável"
    
    # Consistência (desvio padrão das médias)
    medias_geral = [av['media_geral'] for av in historico_ordenado]
    medias_treino = [av['media_treino'] for av in historico_ordenado]
    
    consistencia_geral = np.std(medias_geral)
    consistencia_treino = np.std(medias_treino)
    
    return {
        'total_avaliacoes': len(historico),
        'periodo_dias': (datetime.fromisoformat(ultima['timestamp']) - 
                        datetime.fromisoformat(primeira['timestamp'])).days,
        'progresso_geral': progresso_geral,
        'progresso_treino': progresso_treino,
        'tendencia_geral': tendencia_geral,
        'tendencia_treino': tendencia_treino,
        'consistencia_geral': consistencia_geral,
        'consistencia_treino': consistencia_treino,
        'primeira_avaliacao': primeira['data'][:10],
        'ultima_avaliacao': ultima['data'][:10]
    }

def exibir_painel_historico():
    """Exibe o painel de histórico temporal"""
    historico = carregar_historico_aluno()
    
    if len(historico) < 2:
        return
    
    st.markdown("---")
    st.subheader("📈 Histórico Temporal & Evolução")
    
    # Estatísticas
    stats = calcular_estatisticas_evolucao()
    
    if stats:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="Total de Avaliações",
                value=stats['total_avaliacoes'],
                help=f"Período: {stats['periodo_dias']} dias"
            )
        
        with col2:
            st.metric(
                label="Progresso Geral",
                value=f"{stats['progresso_geral']:+.1f}",
                delta=stats['tendencia_geral']
            )
        
        with col3:
            st.metric(
                label="Progresso Treino", 
                value=f"{stats['progresso_treino']:+.1f}",
                delta=stats['tendencia_treino']
            )
        
        with col4:
            consistencia = "Alta" if stats['consistencia_geral'] < 1.5 else "Média" if stats['consistencia_geral'] < 2.5 else "Baixa"
            st.metric(
                label="Consistência",
                value=consistencia
            )
    
    # Gráfico de evolução
    p_evolucao = gerar_grafico_evolucao()
    if p_evolucao:
        st.image(p_evolucao, use_column_width=True)
    
    # Tabela de histórico detalhado
    with st.expander("📋 Histórico Detalhado de Avaliações"):
        dados_tabela = []
        for av in sorted(historico, key=lambda x: x['timestamp'], reverse=True):
            dados_tabela.append({
                'Data': av['data'][:16],
                'Média Geral': f"{av['media_geral']}/10",
                'Média Treino': f"{av['media_treino']}/10",
                'Status': '🟢 Atual' if av == historico[-1] else '⚪ Anterior'
            })
        
        df_historico = pd.DataFrame(dados_tabela)
        st.dataframe(df_historico, use_container_width=True, hide_index=True)
        
        # Botão para limpar histórico
        if st.button("🗑️ Limpar Histórico", type="secondary", use_container_width=True):
            aluno_key = f"{st.session_state.aluno}_{st.session_state.turma}"
            if aluno_key in st.session_state.historico:
                st.session_state.historico[aluno_key] = [st.session_state.historico[aluno_key][-1]]  # Mantém apenas o último
                st.rerun()

# ================= FUNÇÕES AUXILIARES =================
def group_averages():
    g_keys = ["Geral - Autorregulação","Geral - Autoeficácia","Geral - Estabilidade"]
    t_keys = ["Treino - Autorregulação","Treino - Autoeficácia","Treino - Estabilidade"]
    g_vals = [st.session_state.scores[k] for k in g_keys if st.session_state.scores[k] is not None]
    t_vals = [st.session_state.scores[k] for k in t_keys if st.session_state.scores[k] is not None]
    avg_g  = round(sum(g_vals)/len(g_vals),1) if g_vals else None
    avg_t  = round(sum(t_vals)/len(t_vals),1) if t_vals else None
    return avg_g, avg_t

def image_to_base64(path:str):
    try:
        img = Image.open(path)
        buf = BytesIO()
        img.save(buf, format="JPEG")
        return base64.b64encode(buf.getvalue()).decode()
    except Exception:
        return None

# ================= SISTEMA DE FEEDBACK AUTOMÁTICO =================
def gerar_insights_automaticos(scores):
    """Gera insights automáticos baseados nos scores do aluno"""
    insights = []
    recomendacoes = []
    
    # Análise de Autorregulação
    autorregulacao_geral = scores.get("Geral - Autorregulação")
    autorregulacao_treino = scores.get("Treino - Autorregulação")
    
    if autorregulacao_geral and autorregulacao_geral <= 5:
        insights.append("🎯 **Desafio na Organização**: Sua autorregulação geral está abaixo do ideal")
        recomendacoes.append("Estabeleça rotinas diárias com horários fixos para atividades importantes")
    
    if autorregulacao_treino and autorregulacao_treino <= 5:
        insights.append("💪 **Consistência no Treino**: Dificuldade em manter regularidade nos exercícios")
        recomendacoes.append("Agende os treinos como compromissos inadiáveis na sua agenda")
    
    # Análise de Autoeficácia
    autoeficacia_geral = scores.get("Geral - Autoeficácia")
    autoeficacia_treino = scores.get("Treino - Autoeficácia")
    
    if autoeficacia_geral and autoeficacia_geral <= 5:
        insights.append("🌟 **Confiança em Desenvolvimento**: Crença nas capacidades pessoais precisa ser fortalecida")
        recomendacoes.append("Celebre pequenas vitórias diárias para construir confiança progressiva")
    
    if autoeficacia_treino and autoeficacia_treino >= 8:
        insights.append("🚀 **Excelente Autoconfiança**: Grande confiança na capacidade de treinar")
        recomendacoes.append("Use essa confiança para explorar novos desafios e variedade de exercícios")
    
    # Análise de Estabilidade Emocional
    estabilidade_geral = scores.get("Geral - Estabilidade")
    estabilidade_treino = scores.get("Treino - Estabilidade")
    
    if estabilidade_geral and estabilidade_geral <= 5:
        insights.append("🌊 **Sensibilidade Emocional**: Emoções afetam significativamente o dia a dia")
        recomendacoes.append("Pratique técnicas de respiração e mindfulness por 5 minutos ao dia")
    
    if estabilidade_treino and estabilidade_treino >= 7:
        insights.append("⚖️ **Equilíbrio Sólido**: Boa capacidade de manter foco mesmo sob pressão")
    
    # Análise Comparativa
    if autorregulacao_treino and autoeficacia_treino:
        if autorregulacao_treino > autoeficacia_treino + 2:
            insights.append("🔍 **Disparidade Interessante**: Tem disciplina, mas precisa trabalhar a confiança")
            recomendacoes.append("Relembre conquistas passadas no treino para fortalecer a autoeficácia")
    
    # Insight de Perfil Completo
    scores_preenchidos = [v for v in scores.values() if v is not None]
    if scores_preenchidos:
        media_geral = sum(scores_preenchidos) / len(scores_preenchidos)
        if media_geral >= 8:
            insights.append("🏆 **Perfil de Excelência**: Desempenho consistente em todas as dimensões")
            recomendacoes.append("Mantenha os hábitos atuais e considere mentorar outros alunos")
        elif media_geral <= 4:
            insights.append("🌱 **Fase de Fundamentos**: Foque no desenvolvimento das bases")
            recomendacoes.append("Trabalhe uma dimensão de cada vez, começando pela mais crítica")
    
    return insights, recomendacoes

def exibir_painel_feedback():
    """Exibe o painel de feedback automático - SEMPRE VISÍVEL quando há dados"""
    if not any(v is not None for v in st.session_state.scores.values()):
        return
        
    st.markdown("---")
    st.subheader("🧠 Análise Inteligente & Recomendações")
    
    insights, recomendacoes = gerar_insights_automaticos(st.session_state.scores)
    
    # Card de Insights - SEMPRE tenta mostrar, mesmo se vazio
    with st.container():
        st.markdown(f"""
        <div class='feedback-card' style='border-left: 4px solid {DOCTORFIT_GREEN};'>
            <h4 style='color: {DOCTORFIT_GREEN}; margin-bottom: 15px;'>🔍 INSIGHTS IDENTIFICADOS</h4>
        """, unsafe_allow_html=True)
        
        if insights:
            for insight in insights:
                st.markdown(f"""
                <div style='background: #2d2d2d; padding: 12px; border-radius: 8px; margin: 8px 0; 
                            border-left: 3px solid {DOCTORFIT_GREEN};'>
                    <p style='margin: 0; color: {DOCTORFIT_WHITE}; font-size: 0.95rem;'>{insight}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style='background: #2d2d2d; padding: 12px; border-radius: 8px; margin: 8px 0;'>
                <p style='margin: 0; color: #888888; font-size: 0.95rem; text-align: center;'>
                    Complete mais avaliações para gerar insights personalizados
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Card de Recomendações
    if recomendacoes:
        with st.container():
            st.markdown("""
            <div class='feedback-card' style='border-left: 4px solid #3498DB;'>
                <h4 style='color: #3498DB; margin-bottom: 15px;'>💡 RECOMENDAÇÕES ESTRATÉGICAS</h4>
            """, unsafe_allow_html=True)
            
            for i, recomendacao in enumerate(recomendacoes, 1):
                st.markdown(f"""
                <div style='background: #2d2d2d; padding: 12px; border-radius: 8px; margin: 8px 0; 
                            border-left: 3px solid #3498DB;'>
                    <p style='margin: 0; color: {DOCTORFIT_WHITE}; font-size: 0.95rem;'>
                    <strong>#{i}</strong> {recomendacao}</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

# ================= SISTEMA DE GRÁFICOS =================
def score_color(v: float) -> str:
    if v is None: return "#555555"
    if v <= 4: return "#E74C3C"
    if v <= 7: return "#F1C40F"
    return DOCTORFIT_GREEN

def subset(prefix: str):
    return {k:v for k,v in st.session_state.scores.items() if k.startswith(prefix) and v is not None}

def gerar_bar_chart(resultados: dict, path="chart.png", title="Resultados", media=None, media_label="Média"):
    if not resultados: return None
    
    labels = [l.replace(" - ", "\n") for l in resultados.keys()]
    valores = list(resultados.values())
    colors = [score_color(v) for v in valores]

    if media is not None:
        labels.append(media_label)
        valores.append(media)
        colors.append("#3498DB")

    fig, ax = plt.subplots(figsize=(9, 4.5 + 0.25*len(labels)))
    
    fig.patch.set_facecolor(DOCTORFIT_DARK)
    ax.set_facecolor(DOCTORFIT_DARK)
    
    bars = ax.barh(labels, valores, color=colors, edgecolor="#111", linewidth=1, height=0.6)
    
    ax.set_xlim(0, 10)
    ax.set_xlabel("Pontuação (0–10)", color="#cccccc", fontsize=11, fontweight=500)
    ax.set_title(title, color=DOCTORFIT_WHITE, fontsize=13, fontweight=600, pad=15)
    
    ax.grid(True, axis='x', alpha=0.1, color="#cccccc")
    ax.set_axisbelow(True)
    
    ax.tick_params(colors="#cccccc", labelsize=10)
    for i, (bar, v) in enumerate(zip(bars, valores)):
        ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, 
                f"{v:.1f}", va='center', ha='left', color=DOCTORFIT_WHITE, 
                fontsize=10, fontweight=500)
    
    plt.tight_layout()
    plt.savefig(path, dpi=300, transparent=True, bbox_inches='tight',
                facecolor=DOCTORFIT_DARK, edgecolor='none')
    plt.close(fig)
    return path

def gerar_tres_graficos():
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    avg_g, avg_t = group_averages()
    
    filled = {k:v for k,v in st.session_state.scores.items() if v is not None}
    p_all = gerar_bar_chart(filled, f"chart_all_{ts}.png", "RESULTADOS CONSOLIDADOS") if filled else None
    
    g = subset("Geral")
    p_g = gerar_bar_chart(g, f"chart_geral_{ts}.png", "AVALIAÇÃO GERAL", 
                         media=avg_g, media_label="Média Geral") if g else None
    
    t = subset("Treino")
    p_t = gerar_bar_chart(t, f"chart_treino_{ts}.png", "AVALIAÇÃO NO TREINO", 
                         media=avg_t, media_label="Média Treino") if t else None
    
    return p_all, p_g, p_t, avg_g, avg_t

# ================= SISTEMA DE PDF PREMIUM =================
def gerar_relatorio_pdf():
    """Gera relatório PDF premium com design profissional"""
    if not PDF_AVAILABLE:
        st.error("Funcionalidade PDF não disponível. Instale: pip install reportlab")
        return None
        
    try:
        # Dados básicos
        nome = st.session_state.aluno
        turma = st.session_state.turma
        avg_g, avg_t = group_averages()
        
        # Nome do arquivo
        filename = f"Relatorio_DoctorFit_{nome.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
        
        # Criar documento
        doc = SimpleDocTemplate(filename, pagesize=letter,
                              topMargin=0.5*inch, bottomMargin=0.5*inch)
        story = []
        styles = getSampleStyleSheet()
        
        # ===== ESTILOS PERSONALIZADOS =====
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=16,
            textColor=colors.HexColor(DOCTORFIT_GREEN),
            spaceAfter=12,
            alignment=1
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=12,
            textColor=colors.HexColor(DOCTORFIT_GREEN),
            spaceAfter=6
        )
        
        normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=10,
            textColor=colors.black,
            spaceAfter=6
        )
        
        # ===== CABEÇALHO =====
        # Logo (se existir)
        if os.path.exists(LOGO_PATH):
            from reportlab.platypus import Image
            logo = Image(LOGO_PATH, width=2*inch, height=0.7*inch)
            story.append(logo)
            story.append(Spacer(1, 0.1*inch))
        
        # Título
        title = Paragraph("RELATÓRIO DE DESEMPENHO PSICOSSOCIAL", title_style)
        story.append(title)
        story.append(Spacer(1, 0.2*inch))
        
        # ===== INFORMAÇÕES DO ALUNO =====
        info_text = f"""
        <b>Aluno:</b> {nome.upper()}<br/>
        <b>Turma:</b> {turma}<br/>
        <b>Data:</b> {datetime.now().strftime('%d/%m/%Y %H:%M')}<br/>
        """
        story.append(Paragraph(info_text, normal_style))
        story.append(Spacer(1, 0.2*inch))
        
        # ===== MÉTRICAS PRINCIPAIS =====
        if avg_g or avg_t:
            metrics_text = "<b>MÉTRICAS PRINCIPAIS:</b><br/>"
            if avg_g:
                metrics_text += f"Média Geral: <b>{avg_g}/10</b><br/>"
            if avg_t:
                metrics_text += f"Média Treino: <b>{avg_t}/10</b><br/>"
            story.append(Paragraph(metrics_text, heading_style))
            story.append(Spacer(1, 0.1*inch))
        
        # ===== INSIGHTS E RECOMENDAÇÕES =====
        insights, recomendacoes = gerar_insights_automaticos(st.session_state.scores)
        
        if insights:
            story.append(Paragraph("<b>INSIGHTS IDENTIFICADOS:</b>", heading_style))
            for insight in insights:
                insight_clean = insight.split(' ', 1)[1] if ' ' in insight else insight
                story.append(Paragraph(f"• {insight_clean}", normal_style))
            story.append(Spacer(1, 0.1*inch))
        
        if recomendacoes:
            story.append(Paragraph("<b>RECOMENDAÇÕES ESTRATÉGICAS:</b>", heading_style))
            for recomendacao in recomendacoes:
                story.append(Paragraph(f"• {recomendacao}", normal_style))
            story.append(Spacer(1, 0.2*inch))
        
        # ===== GRÁFICOS =====
        story.append(Paragraph("<b>VISUALIZAÇÃO DOS RESULTADOS:</b>", heading_style))
        
        # Gerar gráficos para o PDF
        p_all, p_g, p_t, avg_g, avg_t = gerar_tres_graficos()
        
        charts = [
            (p_all, "Resultados Consolidados"),
            (p_g, "Desempenho Geral"), 
            (p_t, "Desempenho no Treino")
        ]
        
        for p, title in charts:
            if p and os.path.exists(p):
                story.append(Paragraph(f"<b>{title}:</b>", normal_style))
                try:
                    from reportlab.platypus import Image
                    chart_img = Image(p, width=6*inch, height=2.5*inch)
                    story.append(chart_img)
                    story.append(Spacer(1, 0.1*inch))
                except Exception as e:
                    story.append(Paragraph(f"[Gráfico {title} não disponível]", normal_style))
        
        # ===== TABELA DE SCORES DETALHADOS =====
        story.append(Spacer(1, 0.1*inch))
        story.append(Paragraph("<b>DETALHAMENTO DOS SCORES:</b>", heading_style))
        
        data = [['Dimensão', 'Score', 'Classificação']]
        for teste, score in st.session_state.scores.items():
            if score is not None:
                tipo = "autorregulacao" if "Autorregulação" in teste else "autoeficacia" if "Autoeficácia" in teste else "estabilidade"
                classificacao = classificar_score(score, tipo)
                data.append([teste, f"{score}/10", classificacao["categoria"]])
        
        if len(data) > 1:
            table = Table(data, colWidths=[3.2*inch, 1*inch, 1.8*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(DOCTORFIT_GREEN)),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 9),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ]))
            story.append(table)
        
        # ===== RODAPÉ =====
        story.append(Spacer(1, 0.3*inch))
        footer_text = f"Relatório gerado automaticamente pelo Sistema DoctorFit MindTrack • {datetime.now().strftime('%d/%m/%Y')}"
        footer_style = ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, textColor=colors.grey, alignment=1)
        story.append(Paragraph(footer_text, footer_style))
        
        # ===== GERAR PDF =====
        doc.build(story)
        return filename
        
    except Exception as e:
        st.error(f"Erro ao gerar PDF: {str(e)}")
        return None
>>>>>>> Stashed changes

# ================= SISTEMA DE CLASSIFICAÇÃO =================
def classificar_score(score: float, tipo: str) -> dict:
    if score is None:
        return {"categoria": "Não avaliado", "cor": "#555555", "feedback": "Avaliação pendente"}
    
    if tipo == "Autorregulação":
        if score <= 4:
            return {"categoria": "EM DESENVOLVIMENTO", "cor": "#E74C3C", "feedback": "Habilidade em fase de construção. Foque em estabelecer rotinas básicas."}
        elif score <= 7:
            return {"categoria": "INTERMEDIÁRIA", "cor": "#F1C40F", "feedback": "Habilidade presente com espaço para otimização. Trabalhe na consistência."}
        else:
            return {"categoria": "CONSOLIDADA", "cor": DOCTORFIT_GREEN, "feedback": "Excelente capacidade de autogestão. Mantenha a consistência."}
    
    elif tipo == "Autoeficácia":
        if score <= 4:
            return {"categoria": "EM FORMAÇÃO", "cor": "#E74C3C", "feedback": "Confiança em desenvolvimento. Foque em pequenas vitórias."}
        elif score <= 7:
            return {"categoria": "ESTABILIZADA", "cor": "#F1C40F", "feedback": "Confiança adequada. Continue construindo sobre bases sólidas."}
        else:
            return {"categoria": "EXCELENTE", "cor": DOCTORFIT_GREEN, "feedback": "Alta confiança nas capacidades. Ideal para desafios complexos."}
    
    elif tipo == "Estabilidade":
        if score <= 4:
            return {"categoria": "SENSÍVEL", "cor": "#E74C3C", "feedback": "Sensibilidade emocional elevada. Pratique técnicas de regulação."}
        elif score <= 7:
            return {"categoria": "EQUILIBRADA", "cor": "#F1C40F", "feedback": "Bom equilíbrio emocional. Desenvolva resiliência para pressão."}
        else:
            return {"categoria": "ROBUSTA", "cor": DOCTORFIT_GREEN, "feedback": "Excelente estabilidade emocional. Mantenha práticas de autocuidado."}

# ================= SISTEMA DE ANÁLISE =================
def gerar_insights_geral(scores):
    """Gera insights específicos para avaliação GERAL"""
    insights = []
    recomendacoes = []
    
    autorregulacao = scores.get("Autorregulação")
    autoeficacia = scores.get("Autoeficácia")
    estabilidade = scores.get("Estabilidade")
    
<<<<<<< Updated upstream
    # Análise de Autorregulação
    if autorregulacao is not None:
        if autorregulacao <= 4:
            insights.append("🎯 **Organização Pessoal**: Desafio significativo em manter rotinas e foco")
            recomendacoes.append("Estabeleça horários fixos para atividades importantes usando agenda digital")
            recomendacoes.append("Divida tarefas grandes em etapas menores com prazos específicos")
            recomendacoes.append("Use técnicas Pomodoro (25min trabalho + 5min descanso) para melhorar o foco")
        elif autorregulacao <= 6:
            insights.append("📊 **Autogestão Intermediária**: Capacidade organizacional em desenvolvimento")
            recomendacoes.append("Revise semanalmente suas metas e ajuste conforme necessário")
            recomendacoes.append("Experimente diferentes métodos de planejamento (matriz Eisenhower, listas)")
        else:
            insights.append("✅ **Excelente Autogestão**: Habilidades organizacionais bem desenvolvidas")
            recomendacoes.append("Mantenha a consistência e compartilhe suas estratégias com colegas")
            recomendacoes.append("Considere mentorar outros em técnicas de organização pessoal")
    
    # Análise de Autoeficácia
    if autoeficacia is not None:
        if autoeficacia <= 4:
            insights.append("🌟 **Confiança em Desenvolvimento**: Crença nas capacidades precisa ser fortalecida")
            recomendacoes.append("Liste 3 pequenas conquistas diárias para construir autoconfiança")
            recomendacoes.append("Enfrente um pequeno desafio por dia para expandir zona de conforto")
            recomendacoes.append("Pratique afirmações positivas sobre suas capacidades")
        elif autoeficacia <= 6:
            insights.append("💪 **Confiança Estável**: Autoeficácia adequada com espaço para crescimento")
            recomendacoes.append("Registre seus sucessos em um diário de conquistas")
            recomendacoes.append("Busque feedback construtivo para validar suas capacidades")
        else:
            insights.append("🚀 **Alta Autoeficácia**: Grande confiança nas capacidades pessoais")
            recomendacoes.append("Use essa confiança para assumir projetos desafiadores")
            recomendacoes.append("Mentore colegas que possam se beneficiar da sua experiência")
    
    # Análise de Estabilidade
    if estabilidade is not None:
        if estabilidade <= 4:
            insights.append("🌊 **Sensibilidade Emocional**: Emoções afetam significativamente o desempenho")
            recomendacoes.append("Pratique respiração profunda por 2 minutos ao sentir estresse")
            recomendacoes.append("Mantenha um diário emocional para identificar padrões de reação")
            recomendacoes.append("Desenvolva uma rotina de autocuidado (exercícios, meditação, hobbies)")
        elif estabilidade <= 6:
            insights.append("⚖️ **Equilíbrio Emocional**: Boa capacidade de lidar com pressões")
            recomendacoes.append("Continue praticando técnicas de regulação emocional")
            recomendacoes.append("Identifique gatilhos emocionais e desenvolva estratégias de coping")
        else:
            insights.append("🛡️ **Estabilidade Robusta**: Excelente resiliência emocional")
            recomendacoes.append("Mantenha práticas de autocuidado para preservar o equilíbrio")
            recomendacoes.append("Compartilhe suas estratégias de resiliência com outras pessoas")
    
    # Análises comparativas
    if autorregulacao and autoeficacia:
        if autorregulacao > autoeficacia + 2:
            insights.append("🔍 **Disciplina > Confiança**: Tem organização, mas precisa trabalhar autoconfiança")
            recomendacoes.append("Relembre conquistas passadas para fortalecer a autoeficácia")
        elif autoeficacia > autorregulacao + 2:
            insights.append("🎭 **Confiança > Disciplina**: Alta autoconfiança, mas organização precisa de atenção")
            recomendacoes.append("Desenvolva sistemas e rotinas para apoiar sua confiança")
    
    return insights, recomendacoes

def gerar_insights_treino(scores):
    """Gera insights específicos para avaliação de TREINO"""
    insights = []
    recomendacoes = []
    
    autorregulacao = scores.get("Autorregulação")
    autoeficacia = scores.get("Autoeficácia") 
    estabilidade = scores.get("Estabilidade")
    
    # Análise de Autorregulação no Treino
    if autorregulacao is not None:
        if autorregulacao <= 4:
            insights.append("💪 **Consistência no Treino**: Dificuldade significativa em manter regularidade")
            recomendacoes.append("Agende os treinos como compromissos fixos na semana")
            recomendacoes.append("Prepare a roupa de treino na noite anterior para reduzir barreiras")
            recomendacoes.append("Estabeleça metas semanais realistas de frequência")
        elif autorregulacao <= 6:
            insights.append("📈 **Disciplina em Desenvolvimento**: Regularidade adequada com espaço para melhoria")
            recomendacoes.append("Monitore sua consistência com um aplicativo de treino")
            recomendacoes.append("Crie recompensas para manter a motivação nos treinos")
        else:
            insights.append("✅ **Excelente Disciplina no Treino**: Adesão exemplar à rotina de exercícios")
            recomendacoes.append("Mantenha a consistência e explore novas modalidades para variar")
            recomendacoes.append("Compartilhe suas estratégias de aderência com outros atletas")
    
    # Análise de Autoeficácia no Treino
    if autoeficacia is not None:
        if autoeficacia <= 4:
            insights.append("🎯 **Confiança no Treino**: Dúvidas significativas sobre capacidade de evolução")
            recomendacoes.append("Registre pequenas melhorias (ex: mais repetições, menos cansaço)")
            recomendacoes.append("Foque no processo de evolução, não apenas nos resultados finais")
            recomendacoes.append("Trabalhe com um profissional para estabelecer metas realistas")
        elif autoeficacia <= 6:
            insights.append("💫 **Confiança Estável**: Crença adequada nas capacidades atléticas")
            recomendacoes.append("Documente seus progressos com fotos e medidas")
            recomendacoes.append("Celebre marcos importantes no seu desenvolvimento")
        else:
            insights.append("🚀 **Alta Confiança no Treino**: Grande crença na capacidade de evolução")
            recomendacoes.append("Use essa mentalidade para superar platôs de desempenho")
            recomendacoes.append("Estabeleça metas desafiadoras que aproveitem sua confiança")
    
    # Análise de Estabilidade no Treino
    if estabilidade is not None:
        if estabilidade <= 4:
            insights.append("⚡ **Sensibilidade no Treino**: Fatores externos afetam muito a motivação")
            recomendacoes.append("Crie um ritual pré-treino para entrar no estado mental adequado")
            recomendacoes.append("Tenha um plano B para dias com imprevistos ou baixa motivação")
            recomendacoes.append("Pratique visualização positiva antes dos treinos")
        elif estabilidade <= 6:
            insights.append("🔄 **Resiliência em Desenvolvimento**: Capacidade adequada de lidar com adversidades")
            recomendacoes.append("Desenvolva estratégias específicas para lidar com dias difíceis")
            recomendacoes.append("Mantenha uma rotina de recuperação pós-treino")
        else:
            insights.append("🛡️ **Resiliência Robusta**: Excelente capacidade de manter foco sob pressão")
            recomendacoes.append("Continue desenvolvendo estratégias de coping para desafios específicos")
            recomendacoes.append("Aproveite sua resiliência para experimentar novos desafios esportivos")
    
    return insights, recomendacoes

# ================= SISTEMA DE GRÁFICOS =================
def gerar_grafico_avaliacao(scores, titulo, tipo):
    if not any(v is not None for v in scores.values()):
        return None
    
    labels = list(scores.keys())
    valores = [scores[k] if scores[k] is not None else 0 for k in labels]
    
    # Classifica cada score para definir cores
    colors = []
    for label, valor in zip(labels, valores):
        if valor > 0:
            classificacao = classificar_score(valor, label)
            colors.append(classificacao["cor"])
        else:
            colors.append("#555555")
    
    dados_grafico = [(l, v, c) for l, v, c in zip(labels, valores, colors) if v > 0]
    if not dados_grafico:
        return None
        
    labels_filtrado = [d[0] for d in dados_grafico]
    valores_filtrado = [d[1] for d in dados_grafico]
    colors_filtrado = [d[2] for d in dados_grafico]
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # FUNDO PRETO NO GRÁFICO
    fig.patch.set_facecolor('#000000')
    ax.set_facecolor('#000000')
    
    bars = ax.barh(labels_filtrado, valores_filtrado, color=colors_filtrado, 
                   edgecolor="#111", linewidth=1, height=0.6)
    
    ax.set_xlim(0, 10)
    ax.set_xlabel("Pontuação (0–10)", color="#cccccc", fontsize=12, fontweight=600)
    ax.set_title(titulo, color="#ffffff", fontsize=16, fontweight=700, pad=20)
    
    ax.grid(True, axis='x', alpha=0.2, color="#cccccc")
    ax.set_axisbelow(True)
    ax.tick_params(colors="#cccccc", labelsize=11)
    
    # Adiciona valores e classificações nas barras
    for bar, v, label in zip(bars, valores_filtrado, labels_filtrado):
        classificacao = classificar_score(v, label)
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, 
                f"{v:.1f}/10 - {classificacao['categoria']}", 
                va='center', ha='left', color="#ffffff", 
                fontsize=10, fontweight=500)
    
    plt.tight_layout()
    
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"grafico_{tipo}_{ts}.png"
    plt.savefig(path, dpi=300, transparent=True, bbox_inches='tight',
                facecolor='#000000', edgecolor='none')
    plt.close(fig)
    
    return path

# ================= SISTEMA DE RELATÓRIOS PREMIUM =================
def gerar_relatorio_pdf(scores, insights, recomendacoes, tipo_avaliacao):
    """Gera relatório PDF premium com design profissional"""
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.lib.utils import ImageReader
        from reportlab.lib.units import inch
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.lib.colors import HexColor, black, white
        
        nome = st.session_state.aluno
        turma = st.session_state.turma
        media = calcular_media(scores)
        
        filename = f"Relatorio_{tipo_avaliacao}_{nome.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
        
        # Criar PDF
        c = canvas.Canvas(filename, pagesize=A4)
        width, height = A4
        
        # CORES
        COR_PRIMARIA = HexColor("#A6CE39")  # Verde DoctorFit
        COR_SECUNDARIA = HexColor("#2C3E50")  # Azul escuro
        COR_TEXTO = black
        COR_FUNDO = white
        
        # Configurar fonte
        try:
            c.setFont("Helvetica-Bold", 16)
        except:
            c.setFont("Helvetica-Bold", 16)
        
        # ===== CABEÇALHO COM LOGO =====
        # Fundo do cabeçalho
        c.setFillColor(COR_PRIMARIA)
        c.rect(0, height-1.5*inch, width, 1.5*inch, fill=1)
        
        # Tenta adicionar a logo
        logo_base64 = get_logo_base64()
        if logo_base64:
            try:
                logo_img = ImageReader(BytesIO(base64.b64decode(logo_base64)))
                c.drawImage(logo_img, 0.5*inch, height-1.3*inch, width=1*inch, height=1*inch, preserveAspectRatio=True)
=======
    for teste, score in st.session_state.scores.items():
        if score is not None:
            tipo = tipos_teste[teste]
            classificacao = classificar_score(score, tipo)
            
            st.markdown(f"""
            <div class='feedback-card' style='border-left: 4px solid {classificacao["cor"]}'>
                <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;'>
                    <div style='font-weight:600; font-size:0.95rem; color:{DOCTORFIT_WHITE};'>{teste}</div>
                    <div style='padding:4px 10px; border-radius:12px; font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.5px; background:{classificacao["cor"]}; color:#000000;'>
                        {classificacao["categoria"]}
                    </div>
                </div>
                <div style='color: {DOCTORFIT_GREEN}; font-weight: 600; font-size: 0.9rem; margin: 5px 0;'>
                    Score: {score}/10
                </div>
                <div style='font-size:0.85rem; color:#cccccc; line-height:1.4;'>
                    {classificacao["feedback"]}
                </div>
            </div>
            """, unsafe_allow_html=True)

# ================= PÁGINA CADASTRO =================
def pagina_cadastro():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        # Logo DoctorFit
        if os.path.exists(LOGO_PATH):
            try:
                img = Image.open(LOGO_PATH)
                st.image(img, width=180)
>>>>>>> Stashed changes
            except:
                # Fallback para ícone personalizado
                st.markdown(f"""
                <div style='text-align:center; margin-bottom:2rem;'>
                    <div style='font-size:3rem; color:{DOCTORFIT_GREEN};'>🧠</div>
                    <div style='font-size:0.9rem; color:#888;'>DOCTORFIT</div>
                </div>
                """, unsafe_allow_html=True)
        
        # Título
        c.setFillColor(black)
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(width/2, height-0.8*inch, f"RELATÓRIO {tipo_avaliacao.upper()}")
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(width/2, height-1.1*inch, "DOCTORFIT MINDTRACK")
        
<<<<<<< Updated upstream
        # ===== INFORMAÇÕES DO ALUNO =====
        y_position = height - 2.0*inch
=======
        with st.form("cadastro_corporate"):
            st.session_state.aluno = st.text_input("👤 Nome completo do aluno", 
                                                 st.session_state.aluno,
                                                 placeholder="Digite o nome completo do aluno")
            
            turmas = ["06:00","06:45","07:30","08:15","09:00","09:45","10:30","11:15",
                     "12:00","13:00","13:45","14:30","15:15","16:00","16:45","17:30",
                     "18:15","19:00","19:45","20:30"]
            
            st.session_state.turma = st.selectbox("🕐 Selecione a turma", 
                                                turmas,
                                                index=turmas.index(st.session_state.turma) if st.session_state.turma in turmas else 0)
            
            ok = st.form_submit_button("🚀 Iniciar Avaliação", use_container_width=True)
            
        if ok and st.session_state.aluno.strip():
            st.session_state.page = "menu"
            st.session_state.show_feedback = False
            st.rerun()

# ================= PÁGINA MENU COMPLETA =================
def pagina_menu():
    st.markdown(f"""
    <div style='text-align:center; margin-bottom:2rem;'>
        <h2>Bem-vindo, {st.session_state.aluno}</h2>
        <p style='color:#888888;'>Turma: {st.session_state.turma}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Métricas rápidas - SEMPRE VISÍVEIS
    avg_g, avg_t = group_averages()
    completed = sum(1 for v in st.session_state.scores.values() if v is not None)
    historico = carregar_historico_aluno()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class='metric-corporate'>
            <div class='metric-value-corporate'>{completed}/6</div>
            <div class='metric-label-corporate'>Avaliações Concluídas</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        mg = avg_g if avg_g else "-"
        st.markdown(f"""
        <div class='metric-corporate'>
            <div class='metric-value-corporate'>{mg}</div>
            <div class='metric-label-corporate'>Média Geral</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        mt = avg_t if avg_t else "-"
        st.markdown(f"""
        <div class='metric-corporate'>
            <div class='metric-value-corporate'>{mt}</div>
            <div class='metric-label-corporate'>Média Treino</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        total_avaliacoes = len(historico)
        st.markdown(f"""
        <div class='metric-corporate'>
            <div class='metric-value-corporate'>{total_avaliacoes}</div>
            <div class='metric-label-corporate'>Avaliações Totais</div>
        </div>
        """, unsafe_allow_html=True)
    
    # EXIBIR FEEDBACK E CLASSIFICAÇÃO - SEMPRE que houver dados
    exibir_painel_feedback()
    exibir_classificacao_instantanea()
    
    # EXIBIR HISTÓRICO TEMPORAL se houver múltiplas avaliações
    exibir_painel_historico()
    
    # EXIBIR GRÁFICOS E BOTÃO PDF se todos completos
    if all(v is not None for v in st.session_state.scores.values()):
        st.markdown("---")
        st.subheader("📊 Visualização Gráfica")
>>>>>>> Stashed changes
        
        c.setFillColor(COR_SECUNDARIA)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(1*inch, y_position, "INFORMAÇÕES DO ALUNO:")
        y_position -= 0.25*inch
        
        c.setFillColor(COR_TEXTO)
        c.setFont("Helvetica", 10)
        c.drawString(1*inch, y_position, f"Nome: {nome.upper()}")
        y_position -= 0.2*inch
        c.drawString(1*inch, y_position, f"Turma: {turma}")
        y_position -= 0.2*inch
        c.drawString(1*inch, y_position, f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        y_position -= 0.3*inch
        
        # ===== MÉTRICA PRINCIPAL =====
        if media:
            c.setFillColor(COR_PRIMARIA)
            c.setFont("Helvetica-Bold", 14)
            c.drawString(1*inch, y_position, f"MÉDIA {tipo_avaliacao.upper()}: {media}/10")
            c.setFillColor(COR_TEXTO)
            
            # Classificação da média
            classificacao_media = classificar_score(media, "Autoeficácia")
            c.setFont("Helvetica", 10)
            c.drawString(1*inch, y_position - 0.2*inch, f"Classificação Geral: {classificacao_media['categoria']}")
            y_position -= 0.4*inch
        
        # ===== SCORES DETALHADOS COM CLASSIFICAÇÃO =====
        c.setFillColor(COR_SECUNDARIA)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(1*inch, y_position, "RESULTADOS DETALHADOS:")
        y_position -= 0.3*inch
        
        c.setFillColor(COR_TEXTO)
        c.setFont("Helvetica", 9)
        for dimensao, score in scores.items():
            if score is not None:
                classificacao = classificar_score(score, dimensao)
                
                # Dimensão e Score
                c.drawString(1.2*inch, y_position, f"{dimensao}: {score}/10")
                
                # Classificação com cor
                c.setFillColor(HexColor(classificacao["cor"]))
                c.drawString(4*inch, y_position, f"{classificacao['categoria']}")
                c.setFillColor(COR_TEXTO)
                
                # Feedback
                y_position -= 0.15*inch
                feedback_lines = []
                words = classificacao['feedback'].split()
                current_line = ""
                
                for word in words:
                    if len(current_line + " " + word) <= 50:
                        current_line += " " + word if current_line else word
                    else:
                        feedback_lines.append(current_line)
                        current_line = word
                if current_line:
                    feedback_lines.append(current_line)
                
                for line in feedback_lines:
                    if y_position < 1.5*inch:
                        c.showPage()
                        c.setFillColor(COR_TEXTO)
                        y_position = height - 1*inch
                    
                    c.setFont("Helvetica-Oblique", 8)
                    c.drawString(1.4*inch, y_position, f"  {line}")
                    y_position -= 0.13*inch
                
                c.setFont("Helvetica", 9)
                y_position -= 0.1*inch
        
        y_position -= 0.2*inch
        
        # ===== GRÁFICO =====
        grafico_path = gerar_grafico_avaliacao(scores, f"Resultados {tipo_avaliacao}", tipo_avaliacao)
        if grafico_path and os.path.exists(grafico_path):
            if y_position < 3.5*inch:
                c.showPage()
                c.setFillColor(COR_TEXTO)
                y_position = height - 1*inch
            
            c.setFillColor(COR_SECUNDARIA)
            c.setFont("Helvetica-Bold", 12)
            c.drawString(1*inch, y_position, "VISUALIZAÇÃO GRÁFICA:")
            y_position -= 0.3*inch
            
            try:
                img = ImageReader(grafico_path)
                # Centralizar o gráfico
                img_width = 6*inch
                img_height = 3*inch
                x_pos = (width - img_width) / 2
                c.drawImage(img, x_pos, y_position - img_height, width=img_width, height=img_height)
                y_position -= img_height + 0.3*inch
            except Exception as e:
                c.drawString(1.2*inch, y_position, "[Gráfico não disponível]")
                y_position -= 0.3*inch
        
        # ===== INSIGHTS ESTRATÉGICOS =====
        if insights:
            if y_position < 2*inch:
                c.showPage()
                c.setFillColor(COR_TEXTO)
                y_position = height - 1*inch
            
            c.setFillColor(COR_PRIMARIA)
            c.setFont("Helvetica-Bold", 12)
            c.drawString(1*inch, y_position, "ANÁLISE ESTRATÉGICA:")
            y_position -= 0.3*inch
            
            c.setFillColor(COR_SECUNDARIA)
            c.setFont("Helvetica-Bold", 11)
            c.drawString(1*inch, y_position, "PRINCIPAIS INSIGHTS:")
            y_position -= 0.25*inch
            
            c.setFillColor(COR_TEXTO)
            c.setFont("Helvetica", 9)
            for i, insight in enumerate(insights, 1):
                # Remove emojis para o PDF
                insight_text = ''.join(char for char in insight if char.isprintable() and ord(char) < 128)
                
                if y_position < 1*inch:
                    c.showPage()
                    c.setFillColor(COR_TEXTO)
                    y_position = height - 1*inch
                
                c.drawString(1.2*inch, y_position, f"{i}. {insight_text}")
                y_position -= 0.2*inch
            
            y_position -= 0.1*inch
        
        # ===== PLANO DE AÇÃO =====
        if recomendacoes:
            if y_position < 2*inch:
                c.showPage()
                c.setFillColor(COR_TEXTO)
                y_position = height - 1*inch
            
            c.setFillColor(HexColor("#3498db"))
            c.setFont("Helvetica-Bold", 11)
            c.drawString(1*inch, y_position, "PLANO DE AÇÃO RECOMENDADO:")
            y_position -= 0.25*inch
            
            c.setFillColor(COR_TEXTO)
            c.setFont("Helvetica", 9)
            for i, recomendacao in enumerate(recomendacoes, 1):
                if y_position < 1*inch:
                    c.showPage()
                    c.setFillColor(COR_TEXTO)
                    y_position = height - 1*inch
                
                c.drawString(1.2*inch, y_position, f"{i}. {recomendacao}")
                y_position -= 0.18*inch
        
        # ===== RESUMO EXECUTIVO =====
        if y_position < 2*inch:
            c.showPage()
            c.setFillColor(COR_TEXTO)
            y_position = height - 1*inch
        
        c.setFillColor(COR_SECUNDARIA)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(1*inch, y_position, "RESUMO EXECUTIVO:")
        y_position -= 0.25*inch
        
        c.setFillColor(COR_TEXTO)
        c.setFont("Helvetica", 9)
        
        # Resumo baseado na média
        if media:
            if media <= 5:
                resumo = f"O perfil atual indica oportunidades significativas de desenvolvimento nas competências psicossociais. Com uma média de {media}/10, recomenda-se foco prioritário no fortalecimento das habilidades avaliadas."
            elif media <= 7:
                resumo = f"Perfil em desenvolvimento com bases sólidas (média {media}/10). As competências demonstram boa estruturação com espaço para otimização estratégica."
            else:
                resumo = f"Excelente desempenho psicossocial (média {media}/10). O perfil demonstra competências bem consolidadas, indicando alta capacidade de adaptação e resiliência."
            
            # Quebra de texto para o resumo
            resumo_lines = []
            words = resumo.split()
            current_line = ""
            
            for word in words:
                if len(current_line + " " + word) <= 70:
                    current_line += " " + word if current_line else word
                else:
                    resumo_lines.append(current_line)
                    current_line = word
            if current_line:
                resumo_lines.append(current_line)
            
            for line in resumo_lines:
                if y_position < 1*inch:
                    c.showPage()
                    c.setFillColor(COR_TEXTO)
                    y_position = height - 1*inch
                
                c.drawString(1.2*inch, y_position, line)
                y_position -= 0.18*inch
        
        # ===== RODAPÉ =====
        c.setFillColor(HexColor("#666666"))
        c.setFont("Helvetica", 8)
        c.drawString(1*inch, 0.5*inch, f"Relatório gerado automaticamente pelo Sistema DoctorFit MindTrack • {datetime.now().strftime('%d/%m/%Y')}")
        c.drawString(1*inch, 0.3*inch, "Confidencial - Uso exclusivo do aluno e equipe técnica")
        
        c.save()
        return filename
        
    except Exception as e:
        st.error(f"Erro ao gerar PDF: {str(e)}")
        return None

# ================= PÁGINA CADASTRO =================
def pagina_cadastro():
    # Mostra a logo se existir
    logo = carregar_logo()
    if logo:
        st.image(logo, use_container_width=True)
    
    st.title("DoctorFit MindTrack 🧠")
    st.subheader("Sistema de Avaliação Psicossocial")
    
    with st.form("cadastro"):
        st.session_state.aluno = st.text_input(
            "👤 Nome completo do aluno", 
            placeholder="Digite o nome completo do aluno"
        )
        
        turmas = ["06:00","06:45","07:30","08:15","09:00","09:45","10:30","11:15",
                 "12:00","13:00","13:45","14:30","15:15","16:00","16:45","17:30",
                 "18:15","19:00","19:45","20:30"]
        
        st.session_state.turma = st.selectbox("🕐 Selecione a turma", turmas)
        
        if st.form_submit_button("🚀 Iniciar Avaliações", use_container_width=True):
            if st.session_state.aluno.strip():
                st.session_state.page = "menu_principal"
                st.rerun()

# ================= MENU PRINCIPAL =================
def pagina_menu_principal():
    # Mostra a logo se existir
    logo = carregar_logo()
    if logo:
        st.image(logo, use_container_width=True)
    
    st.title(f"Bem-vindo, {st.session_state.aluno}!")
    st.write(f"Turma: {st.session_state.turma}")
    
    # Métricas rápidas
    col1, col2 = st.columns(2)
    
    with col1:
        completas_geral = sum(1 for v in st.session_state.scores_geral.values() if v is not None)
        media_geral = calcular_media(st.session_state.scores_geral)
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-value'>{completas_geral}/3</div>
            <div class='metric-label'>Avaliações Gerais</div>
            <div class='metric-label'>Média: {media_geral if media_geral else '-'}/10</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
<<<<<<< Updated upstream
        completas_treino = sum(1 for v in st.session_state.scores_treino.values() if v is not None)
        media_treino = calcular_media(st.session_state.scores_treino)
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-value'>{completas_treino}/3</div>
            <div class='metric-label'>Avaliações de Treino</div>
            <div class='metric-label'>Média: {media_treino if media_treino else '-'}/10</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Botões de navegação
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌍 Avaliação Geral")
        st.write("Avalie suas habilidades psicossociais no contexto geral da vida")
        if st.button("📊 Fazer Avaliação Geral", use_container_width=True):
            st.session_state.page = "avaliacao_geral"
=======
        st.markdown("#### 💪 Avaliações no Treino")
        if st.button("🎯 Autorregulação no Treino", use_container_width=True, key="btn_t_autor"):
            st.session_state.page = "t_autor"; st.rerun()
        if st.button("🚀 Autoeficácia no Treino", use_container_width=True, key="btn_t_autoef"):
            st.session_state.page = "t_autoef"; st.rerun()
        if st.button("⚡ Estabilidade no Treino", use_container_width=True, key="btn_t_emoc"):
            st.session_state.page = "t_emoc"; st.rerun()

# ================= TELAS DE AVALIAÇÃO =================
def tela_avaliacao(titulo, itens, label):
    st.markdown(f"<h1>{titulo}</h1>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style='background:{DOCTORFIT_LIGHT}; padding:18px; border-radius:10px; border-left:4px solid {DOCTORFIT_GREEN}; margin:20px 0;'>
    <p style='color:#cccccc; font-size:1rem; margin:0;'>
    <strong>Instruções:</strong> Avalie cada afirmação de 0 a 10, onde:<br>
    0 = Discordo totalmente | 10 = Concordo totalmente
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    vals = []
    for i, txt in enumerate(itens):
        st.markdown(f"**{i+1}. {txt}**")
        val = st.slider("", 0, 10, 5, key=f"{label}_{i}", label_visibility="collapsed")
        
        # Indicador visual
        cor = "#E74C3C" if val <= 4 else "#F1C40F" if val <= 7 else DOCTORFIT_GREEN
        st.markdown(f"""
        <div style='background:#333333; border-radius:5px; height:6px; margin:5px 0 15px 0;'>
            <div style='background:{cor}; border-radius:5px; height:6px; width:{val*10}%'></div>
        </div>
        <div style='text-align:center; color:#888888; font-size:0.85rem; margin-top:-5px;'>
            Pontuação: {val}/10
        </div>
        """, unsafe_allow_html=True)
        vals.append(val)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Salvar Avaliação", use_container_width=True, type="primary"):
            save_score(label, round(sum(vals)/len(vals), 1))
            
            # Salva no histórico se for a última avaliação
            if all(v is not None for v in st.session_state.scores.values()):
                salvar_avaliacao_historico()
            
            st.success("✅ Avaliação salva com sucesso!")
            st.session_state.page = "menu"
>>>>>>> Stashed changes
            st.rerun()
        
        # Mostrar análise geral se existir
        if any(v is not None for v in st.session_state.scores_geral.values()):
            insights, recomendacoes = gerar_insights_geral(st.session_state.scores_geral)
            if insights or recomendacoes:
                with st.expander("🔍 Ver Análise Geral"):
                    if insights:
                        st.write("**Insights:**")
                        for insight in insights:
                            st.write(f"• {insight}")
                    
                    if recomendacoes:
                        st.write("**Recomendações:**")
                        for rec in recomendacoes:
                            st.write(f"• {rec}")
    
    with col2:
<<<<<<< Updated upstream
        st.subheader("💪 Avaliação de Treino")
        st.write("Avalie suas habilidades psicossociais no contexto do treino esportivo")
        if st.button("🏋️ Fazer Avaliação de Treino", use_container_width=True):
            st.session_state.page = "avaliacao_treino"
=======
        if st.button("↩️ Voltar ao Menu", use_container_width=True):
            st.session_state.page = "menu"
>>>>>>> Stashed changes
            st.rerun()
        
        # Mostrar análise treino se existir
        if any(v is not None for v in st.session_state.scores_treino.values()):
            insights, recomendacoes = gerar_insights_treino(st.session_state.scores_treino)
            if insights or recomendacoes:
                with st.expander("🔍 Ver Análise de Treino"):
                    if insights:
                        st.write("**Insights:**")
                        for insight in insights:
                            st.write(f"• {insight}")
                    
                    if recomendacoes:
                        st.write("**Recomendações:**")
                        for rec in recomendacoes:
                            st.write(f"• {rec}")

# ================= AVALIAÇÃO GERAL =================
def pagina_avaliacao_geral():
    # Mostra a logo se existir
    logo = carregar_logo()
    if logo:
        st.image(logo, use_container_width=True)
    
    st.title("🌍 Avaliação Geral")
    st.write("Avalie suas habilidades no contexto geral da vida")
    
    dimensoes = {
        "Autorregulação": [
            "Tenho facilidade em manter o foco nas tarefas do dia a dia.",
            "Consigo manter disciplina em compromissos e rotinas pessoais.", 
            "Tenho bom controle dos meus impulsos (ex.: evitar distrações)."
        ],
        "Autoeficácia": [
            "Acredito na minha capacidade de superar desafios do dia a dia.",
            "Quando decido algo importante, confio que conseguirei realizar.",
            "Mesmo em situações difíceis, encontro soluções para seguir em frente."
        ],
        "Estabilidade": [
            "Consigo manter a calma diante de situações de estresse.",
            "Se algo dá errado, não deixo que isso afete todo o meu dia.",
            "Sou capaz de me recuperar emocionalmente após frustrações."
        ]
    }
    
    scores = {}
    
    for dimensao, perguntas in dimensoes.items():
        st.subheader(f"{dimensao}")
        
        vals = []
        for i, pergunta in enumerate(perguntas):
            st.write(f"**{i+1}. {pergunta}**")
            val = st.slider("", 0, 10, 5, key=f"geral_{dimensao}_{i}", label_visibility="collapsed")
            vals.append(val)
        
        if vals:
            scores[dimensao] = round(sum(vals) / len(vals), 1)
            classificacao = classificar_score(scores[dimensao], dimensao)
            st.write(f"**Pontuação {dimensao}: {scores[dimensao]}/10**")
            st.info(f"**Classificação:** {classificacao['categoria']} - {classificacao['feedback']}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("💾 Salvar Avaliação Geral", use_container_width=True):
            for dimensao, score in scores.items():
                st.session_state.scores_geral[dimensao] = score
            
            salvar_no_historico("geral")
            st.success("✅ Avaliação geral salva com sucesso!")
            st.session_state.page = "menu_principal"
            st.rerun()
    
    with col2:
        if st.button("↩️ Voltar ao Menu", use_container_width=True):
            st.session_state.page = "menu_principal"
            st.rerun()
    
    # Análise em tempo real
    if any(scores.values()):
        st.markdown("---")
        st.subheader("🔍 Análise Preliminar")
        
        insights, recomendacoes = gerar_insights_geral(scores)
        
        if insights:
            st.write("**Insights Identificados:**")
            for insight in insights:
                st.info(insight)
        
        if recomendacoes:
            st.write("**Recomendações:**")
            for rec in recomendacoes:
                st.success(rec)
        
        # Gráfico em tempo real
        grafico_path = gerar_grafico_avaliacao(scores, "Resultados Avaliação Geral", "geral_preview")
        if grafico_path:
            st.image(grafico_path, use_container_width=True)  # CORREÇÃO: use_container_width
            try:
                os.remove(grafico_path)
            except:
                pass
        
        # Botão para gerar relatório
        if st.button("📄 Gerar Relatório Geral em PDF", use_container_width=True):
            with st.spinner("🔄 Gerando relatório premium..."):
                pdf_path = gerar_relatorio_pdf(
                    st.session_state.scores_geral, 
                    insights, 
                    recomendacoes, 
                    "Geral"
                )
                
                if pdf_path and os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f:
                        pdf_bytes = f.read()
                    
                    st.download_button(
                        label="⬇️ Baixar Relatório Geral Premium",
                        data=pdf_bytes,
                        file_name=os.path.basename(pdf_path),
                        mime="application/pdf",
                        use_container_width=True
                    )
                    
                    # Limpar arquivos temporários
                    try:
                        for file in os.listdir("."):
                            if file.startswith("grafico_geral_") and file.endswith(".png"):
                                os.remove(file)
                        if os.path.exists(pdf_path):
                            os.remove(pdf_path)
                    except:
                        pass

# ================= AVALIAÇÃO DE TREINO =================
def pagina_avaliacao_treino():
    # Mostra a logo se existir
    logo = carregar_logo()
    if logo:
        st.image(logo, use_container_width=True)
    
    st.title("💪 Avaliação de Treino")
    st.write("Avalie suas habilidades no contexto do treino esportivo")
    
    dimensoes = {
        "Autorregulação": [
            "Mantenho meu compromisso com os treinos mesmo quando estou cansado(a) ou desanimado(a).",
            "Costumo refletir sobre o que posso melhorar nos meus hábitos de treino e alimentação.",
            "Faço o possível para não faltar no treino, mesmo quando há imprevistos."
        ],
        "Autoeficácia": [
            "Tenho confiança em minha capacidade de seguir meu programa de treino.",
            "Mesmo em dias difíceis, sei que sou capaz de executar satisfatoriamente meu programa de treino.",
            "Confio que vou me dedicar para melhorar meu condicionamento físico e conquistar resultados."
        ],
        "Estabilidade": [
            "Mesmo em dias de mau humor ou estresse, consigo ir treinar.",
            "Consigo lidar com frustrações do dia a dia e me manter psicologicamente estável.",
            "Quando algo me frustra no treino, não deixo que isso afete minha alimentação ou frequência."
        ]
    }
    
    scores = {}
    
    for dimensao, perguntas in dimensoes.items():
        st.subheader(f"{dimensao}")
        
        vals = []
        for i, pergunta in enumerate(perguntas):
            st.write(f"**{i+1}. {pergunta}**")
            val = st.slider("", 0, 10, 5, key=f"treino_{dimensao}_{i}", label_visibility="collapsed")
            vals.append(val)
        
        if vals:
            scores[dimensao] = round(sum(vals) / len(vals), 1)
            classificacao = classificar_score(scores[dimensao], dimensao)
            st.write(f"**Pontuação {dimensao}: {scores[dimensao]}/10**")
            st.info(f"**Classificação:** {classificacao['categoria']} - {classificacao['feedback']}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("💾 Salvar Avaliação de Treino", use_container_width=True):
            for dimensao, score in scores.items():
                st.session_state.scores_treino[dimensao] = score
            
            salvar_no_historico("treino")
            st.success("✅ Avaliação de treino salva com sucesso!")
            st.session_state.page = "menu_principal"
            st.rerun()
    
    with col2:
        if st.button("↩️ Voltar ao Menu", use_container_width=True):
            st.session_state.page = "menu_principal"
            st.rerun()
    
    # Análise em tempo real
    if any(scores.values()):
        st.markdown("---")
        st.subheader("🔍 Análise Preliminar")
        
        insights, recomendacoes = gerar_insights_treino(scores)
        
        if insights:
            st.write("**Insights Identificados:**")
            for insight in insights:
                st.info(insight)
        
        if recomendacoes:
            st.write("**Recomendações:**")
            for rec in recomendacoes:
                st.success(rec)
        
        # Gráfico em tempo real
        grafico_path = gerar_grafico_avaliacao(scores, "Resultados Avaliação de Treino", "treino_preview")
        if grafico_path:
            st.image(grafico_path, use_container_width=True)  # CORREÇÃO: use_container_width
            try:
                os.remove(grafico_path)
            except:
                pass
        
        # Botão para gerar relatório
        if st.button("📄 Gerar Relatório de Treino em PDF", use_container_width=True):
            with st.spinner("🔄 Gerando relatório premium..."):
                pdf_path = gerar_relatorio_pdf(
                    st.session_state.scores_treino, 
                    insights, 
                    recomendacoes, 
                    "Treino"
                )
                
                if pdf_path and os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f:
                        pdf_bytes = f.read()
                    
                    st.download_button(
                        label="⬇️ Baixar Relatório de Treino Premium",
                        data=pdf_bytes,
                        file_name=os.path.basename(pdf_path),
                        mime="application/pdf",
                        use_container_width=True
                    )
                    
                    # Limpar arquivos temporários
                    try:
                        for file in os.listdir("."):
                            if file.startswith("grafico_treino_") and file.endswith(".png"):
                                os.remove(file)
                        if os.path.exists(pdf_path):
                            os.remove(pdf_path)
                    except:
                        pass

# ================= ROTEADOR PRINCIPAL =================
if st.session_state.page == "cadastro":
    pagina_cadastro()

elif st.session_state.page == "menu_principal":
    pagina_menu_principal()

elif st.session_state.page == "avaliacao_geral":
    pagina_avaliacao_geral()

elif st.session_state.page == "avaliacao_treino":
    pagina_avaliacao_treino()