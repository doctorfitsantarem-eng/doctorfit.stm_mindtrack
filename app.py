# DoctorFit MindTrack — VERSÃO DEPLOY
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image
from io import BytesIO
import base64, os
from datetime import datetime, timedelta
import hashlib
import json

# ================= IMPORTAÇÕES PARA PDF =================
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

# ================= CONFIG =================
st.set_page_config(page_title="DoctorFit MindTrack", page_icon="🧠", layout="centered")
LOGO_PATH = "assets/logo_doctorfit.jpg"
# ================= PWA CONFIG =================
st.markdown("""
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#A6CE39">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="apple-mobile-web-app-title" content="DoctorFit">
<link rel="apple-touch-icon" href="assets/logo_doctorfit.jpg">
""", unsafe_allow_html=True)
# ================= CSS SIMPLIFICADO =================
st.markdown("""
<style>
html, body, .stApp { 
    background: #000000 !important; 
    color: #ffffff !important;
    font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif !important;
}
.block-container { 
    padding-top: 1rem; 
    max-width: 1200px;
}
.app-title { 
    text-align: center; 
    font-size: 2.8rem; 
    font-weight: 700 !important;
    color: #A6CE39 !important;
    margin-bottom: 0.2rem;
    letter-spacing: -0.5px;
    text-transform: uppercase;
}
.app-subtitle {
    text-align: center;
    font-size: 1rem;
    color: #888888 !important;
    font-weight: 400;
    margin-bottom: 2rem;
    letter-spacing: 0.5px;
}
.gradient-divider {
    width: 180px;
    height: 3px;
    background: linear-gradient(90deg, #A6CE39, #8BC34A);
    margin: 0 auto 2rem;
    border-radius: 2px;
}
.stButton > button {
    width: 100%;
    background: #A6CE39;
    color: #000000 !important;
    border: none;
    border-radius: 8px;
    padding: 12px 1rem;
    font-weight: 600;
    font-size: 0.95rem;
    transition: all 0.3s ease;
}
.stButton > button:hover {
    background: #8BC34A;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(166, 206, 57, 0.3);
}
.metric-corporate {
    background: #1a1a1a;
    border-radius: 10px;
    padding: 18px;
    text-align: center;
    border: 1px solid #333;
    margin: 8px 0;
    transition: all 0.3s ease;
}
.metric-corporate:hover {
    border-color: #A6CE39;
    transform: translateY(-2px);
}
.metric-value-corporate {
    font-size: 2.2rem;
    font-weight: 700;
    color: #A6CE39;
}
.metric-label-corporate {
    font-size: 0.85rem;
    color: #888888;
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
h1, h2, h3 {
    color: #ffffff !important;
    font-weight: 600 !important;
}
h1 {
    font-size: 2rem !important;
    margin-bottom: 1.5rem !important;
    border-left: 4px solid #A6CE39;
    padding-left: 1rem;
}
.stSlider {
    margin: 1.2rem 0;
}
.stSlider > div > div {
    background: #A6CE39 !important;
}
.feedback-card {
    background: linear-gradient(135deg, #1a1a1a, #2d2d2d);
    border: 1px solid #333;
    border-radius: 12px;
    padding: 20px;
    margin: 10px 0;
    transition: all 0.3s ease;
}
.feedback-card:hover {
    border-color: #A6CE39;
    transform: translateY(-2px);
}
.history-card {
    background: linear-gradient(135deg, #1a1a1a, #2d2d2d);
    border: 1px solid #3498DB;
    border-radius: 12px;
    padding: 20px;
    margin: 10px 0;
    border-left: 4px solid #3498DB;
}
/* === RESPONSIVIDADE MOBILE & TABLET === */
@media (max-width: 768px) {
    .block-container {
        padding: 0.5rem !important;
        max-width: 100% !important;
    }
    
    .app-title {
        font-size: 2rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    .app-subtitle {
        font-size: 0.9rem !important;
        margin-bottom: 1rem !important;
    }
    
    .metric-corporate {
        padding: 12px !important;
        margin: 5px 0 !important;
    }
    
    .metric-value-corporate {
        font-size: 1.8rem !important;
    }
    
    .stButton > button {
        min-height: 48px !important;
        font-size: 1rem !important;
        padding: 14px 1rem !important;
    }
    
    h1 {
        font-size: 1.6rem !important;
        padding-left: 0.5rem !important;
    }
    
    h2 {
        font-size: 1.3rem !important;
    }
    
    h3 {
        font-size: 1.1rem !important;
    }
}

/* === TABLET OPTIMIZATION === */
@media (min-width: 769px) and (max-width: 1024px) {
    .block-container {
        padding: 1rem !important;
        max-width: 95% !important;
    }
    
    .app-title {
        font-size: 2.4rem !important;
    }
    
    .metric-corporate {
        padding: 15px !important;
    }
}

/* === TOUCH FRIENDLY === */
.stButton > button {
    min-height: 44px;
}

.stSlider {
    margin: 1rem 0;
}

.stSlider > div {
    padding: 8px 0 !important;
}

/* === ORIENTATION SUPPORT === */
@media (max-height: 500px) and (orientation: landscape) {
    .block-container {
        padding-top: 0.5rem !important;
    }
    
    .app-title {
        font-size: 1.8rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ================= SISTEMA DE ESTADO ROBUSTO =================
def ensure_state():
    """Sistema robusto de estado que persiste entre recarregamentos"""
    # Estado básico
    if "page" not in st.session_state:
        st.session_state.page = "cadastro"
    if "aluno" not in st.session_state:
        st.session_state.aluno = ""
    if "turma" not in st.session_state:
        st.session_state.turma = ""
    
    # Sistema de scores com verificação
    default_scores = {
        "Geral - Autorregulação": None,
        "Geral - Autoeficácia": None,
        "Geral - Estabilidade": None,
        "Treino - Autorregulação": None,
        "Treino - Autoeficácia": None,
        "Treino - Estabilidade": None,
    }
    
    if "scores" not in st.session_state:
        st.session_state.scores = default_scores.copy()
    else:
        # Garante que todos os scores existam
        for key in default_scores:
            if key not in st.session_state.scores:
                st.session_state.scores[key] = None
    
    # Sistema de histórico temporal
    if "historico" not in st.session_state:
        st.session_state.historico = {}
    
    # Flag para mostrar feedback
    if "show_feedback" not in st.session_state:
        st.session_state.show_feedback = False

def save_score(label: str, value: float):
    """Salva score e marca para mostrar feedback"""
    st.session_state.scores[label] = float(value)
    st.session_state.show_feedback = True

def salvar_avaliacao_historico():
    """Salva a avaliação atual no histórico temporal"""
    if not st.session_state.aluno or not all(v is not None for v in st.session_state.scores.values()):
        return
    
    aluno_key = f"{st.session_state.aluno}_{st.session_state.turma}"
    
    # Inicializa histórico do aluno se não existir
    if aluno_key not in st.session_state.historico:
        st.session_state.historico[aluno_key] = []
    
    # Cria registro da avaliação atual
    avaliacao_atual = {
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "timestamp": datetime.now().isoformat(),
        "scores": st.session_state.scores.copy(),
        "media_geral": group_averages()[0],
        "media_treino": group_averages()[1],
        "aluno": st.session_state.aluno,
        "turma": st.session_state.turma
    }
    
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
    fig.patch.set_facecolor('#000000')
    ax.set_facecolor('#000000')
    
    # Plot das linhas
    linha_geral, = ax.plot(datas, medias_geral, marker='o', linewidth=3, 
                          color='#A6CE39', markersize=8, label='Média Geral')
    linha_treino, = ax.plot(datas, medias_treino, marker='s', linewidth=3, 
                           color='#3498DB', markersize=8, label='Média Treino')
    
    # Preenchimento sob as curvas
    ax.fill_between(datas, medias_geral, alpha=0.2, color='#A6CE39')
    ax.fill_between(datas, medias_treino, alpha=0.2, color='#3498DB')
    
    # Configurações do gráfico
    ax.set_ylabel('Pontuação Média', color='#cccccc', fontsize=12, fontweight=600)
    ax.set_xlabel('Data da Avaliação', color='#cccccc', fontsize=12, fontweight=600)
    ax.set_title('EVOLUÇÃO TEMPORAL - DESEMPENHO PSICOSSOCIAL', 
                color='#ffffff', fontsize=14, fontweight=700, pad=20)
    
    # Limites e grades
    ax.set_ylim(0, 10)
    ax.set_yticks(range(0, 11, 2))
    ax.grid(True, alpha=0.2, color='#cccccc')
    ax.set_axisbelow(True)
    
    # Legendas
    ax.legend(facecolor='#1a1a1a', edgecolor='#333333', fontsize=11,
             loc='upper left', bbox_to_anchor=(0, 1))
    
    # Estilo dos eixos
    ax.tick_params(colors='#cccccc', labelsize=10)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Salva o gráfico
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"evolucao_{ts}.png"
    plt.savefig(path, dpi=300, transparent=True, bbox_inches='tight',
                facecolor='#000000', edgecolor='none')
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
    
    # Análise de Autorregulação - VERSÃO SIMPLIFICADA
    autorregulacao_geral = scores.get("Geral - Autorregulacao")
    autorregulacao_treino = scores.get("Treino - Autorregulacao")
    
    if autorregulacao_geral and autorregulacao_geral <= 5:
        insights.append("Desafio na Organizacao: Sua autorregulacao geral esta abaixo do ideal")
        recomendacoes.append("Estabeleca rotinas diarias com horarios fixos")
    
    if autorregulacao_treino and autorregulacao_treino <= 5:
        insights.append("Consistencia no Treino: Dificuldade em manter regularidade")
        recomendacoes.append("Agende os treinos como compromissos inadiaveis")
    
    return insights, recomendacoes
    
    # Análise de Autoeficácia
    autoeficacia_geral = scores.get("Geral - Autoeficácia")
    autoeficacia_treino = scores.get("Treino - Autoeficácia")
    
    if autoeficacia_geral and autoeficacia_geral <= 5:
        insights.append("🎯 **Confiança em Desenvolvimento**: Crença nas capacidades pessoais precisa ser fortalecida")
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
        st.markdown("""
        <div class='feedback-card' style='border-left: 4px solid #A6CE39;'>
            <h4 style='color: #A6CE39; margin-bottom: 15px;'>🔍 INSIGHTS IDENTIFICADOS</h4>
        """, unsafe_allow_html=True)
        
        if insights:
            for insight in insights:
                st.markdown(f"""
                <div style='background: #2d2d2d; padding: 12px; border-radius: 8px; margin: 8px 0; 
                            border-left: 3px solid #A6CE39;'>
                    <p style='margin: 0; color: #ffffff; font-size: 0.95rem;'>{insight}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
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
                    <p style='margin: 0; color: #ffffff; font-size: 0.95rem;'>
                    <strong>#{i}</strong> {recomendacao}</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

# ================= SISTEMA DE GRÁFICOS =================
def score_color(v: float) -> str:
    if v is None: return "#555555"
    if v <= 4: return "#E74C3C"
    if v <= 7: return "#F1C40F"
    return "#A6CE39"

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
    
    fig.patch.set_facecolor('#000000')
    ax.set_facecolor('#000000')
    
    bars = ax.barh(labels, valores, color=colors, edgecolor="#111", linewidth=1, height=0.6)
    
    ax.set_xlim(0, 10)
    ax.set_xlabel("Pontuação (0–10)", color="#cccccc", fontsize=11, fontweight=500)
    ax.set_title(title, color="#ffffff", fontsize=13, fontweight=600, pad=15)
    
    ax.grid(True, axis='x', alpha=0.1, color="#cccccc")
    ax.set_axisbelow(True)
    
    ax.tick_params(colors="#cccccc", labelsize=10)
    for i, (bar, v) in enumerate(zip(bars, valores)):
        ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, 
                f"{v:.1f}", va='center', ha='left', color="#ffffff", 
                fontsize=10, fontweight=500)
    
    plt.tight_layout()
    plt.savefig(path, dpi=300, transparent=True, bbox_inches='tight',
                facecolor='#000000', edgecolor='none')
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
            textColor=colors.HexColor('#A6CE39'),
            spaceAfter=12,
            alignment=1
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=12,
            textColor=colors.HexColor('#A6CE39'),
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
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#A6CE39')),
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

# ================= SISTEMA DE CLASSIFICAÇÃO =================
def classificar_score(score: float, tipo: str) -> dict:
    if score is None:
        return {"categoria": "Não avaliado", "cor": "#555555", "feedback": "Avaliação pendente"}
    
    if tipo == "autorregulacao":
        if score <= 4:
            return {"categoria": "EM DESENVOLVIMENTO", "cor": "#E74C3C", "feedback": "Habilidade em fase de construção. Foque em estabelecer rotinas básicas."}
        elif score <= 7:
            return {"categoria": "INTERMEDIÁRIA", "cor": "#F1C40F", "feedback": "Habilidade presente com espaço para otimização. Trabalhe na consistência."}
        else:
            return {"categoria": "CONSOLIDADA", "cor": "#A6CE39", "feedback": "Excelente capacidade de autogestão. Mantenha a consistência."}
    
    elif tipo == "autoeficacia":
        if score <= 4:
            return {"categoria": "EM FORMAÇÃO", "cor": "#E74C3C", "feedback": "Confiança em desenvolvimento. Foque em pequenas vitórias."}
        elif score <= 7:
            return {"categoria": "ESTABILIZADA", "cor": "#F1C40F", "feedback": "Confiança adequada. Continue construindo sobre bases sólidas."}
        else:
            return {"categoria": "EXCELENTE", "cor": "#A6CE39", "feedback": "Alta confiança nas capacidades. Ideal para desafios complexos."}
    
    elif tipo == "estabilidade":
        if score <= 4:
            return {"categoria": "SENSÍVEL", "cor": "#E74C3C", "feedback": "Sensibilidade emocional elevada. Pratique técnicas de regulação."}
        elif score <= 7:
            return {"categoria": "EQUILIBRADA", "cor": "#F1C40F", "feedback": "Bom equilíbrio emocional. Desenvolva resiliência para pressão."}
        else:
            return {"categoria": "ROBUSTA", "cor": "#A6CE39", "feedback": "Excelente estabilidade emocional. Mantenha práticas de autocuidado."}

def exibir_classificacao_instantanea():
    """Exibe classificação - SEMPRE VISÍVEL quando há dados"""
    if not any(v is not None for v in st.session_state.scores.values()):
        return
        
    st.markdown("---")
    st.subheader("📋 Classificação dos Resultados")
    
    tipos_teste = {
        "Geral - Autorregulação": "autorregulacao",
        "Geral - Autoeficácia": "autoeficacia", 
        "Geral - Estabilidade": "estabilidade",
        "Treino - Autorregulação": "autorregulacao",
        "Treino - Autoeficácia": "autoeficacia",
        "Treino - Estabilidade": "estabilidade"
    }
    
    for teste, score in st.session_state.scores.items():
        if score is not None:
            tipo = tipos_teste[teste]
            classificacao = classificar_score(score, tipo)
            
            st.markdown(f"""
            <div class='feedback-card' style='border-left: 4px solid {classificacao["cor"]}'>
                <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;'>
                    <div style='font-weight:600; font-size:0.95rem; color:#ffffff;'>{teste}</div>
                    <div style='padding:4px 10px; border-radius:12px; font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.5px; background:{classificacao["cor"]}; color:#000000;'>
                        {classificacao["categoria"]}
                    </div>
                </div>
                <div style='color: #A6CE39; font-weight: 600; font-size: 0.9rem; margin: 5px 0;'>
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
        if os.path.exists(LOGO_PATH):
            b64 = image_to_base64(LOGO_PATH)
            if b64:
                st.markdown(f"""
                <div style='text-align:center; margin-bottom:1.5rem;'>
                    <img src='data:image/jpeg;base64,{b64}' width='200' style='border-radius:8px;'>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('<div class="app-title">DoctorFit MindTrack</div>', unsafe_allow_html=True)
        st.markdown('<div class="app-subtitle">Sistema de Avaliação Psicossocial</div>', unsafe_allow_html=True)
        st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
        
        with st.form("cadastro_corporate"):
            st.session_state.aluno = st.text_input("Nome completo do aluno", 
                                                 st.session_state.aluno,
                                                 placeholder="Digite o nome completo do aluno")
            
            turmas = ["06:00","06:45","07:30","08:15","09:00","09:45","10:30","11:15",
                     "12:00","13:00","13:45","14:30","15:15","16:00","16:45","17:30",
                     "18:15","19:00","19:45","20:30"]
            
            st.session_state.turma = st.selectbox("Selecione a turma", 
                                                turmas,
                                                index=turmas.index(st.session_state.turma) if st.session_state.turma in turmas else 0)
            
            ok = st.form_submit_button("Iniciar Avaliação", use_container_width=True)
            
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
        
        try:
            p_all, p_g, p_t, avg_g, avg_t = gerar_tres_graficos()
            
            if p_all: 
                st.image(p_all, use_column_width=True)
            
            col1, col2 = st.columns(2)
            if p_g and col1: 
                col1.image(p_g, use_column_width=True)
            if p_t and col2: 
                col2.image(p_t, use_column_width=True)
            
            # BOTÃO PDF SEMPRE VISÍVEL quando completo
            st.markdown("---")
            st.subheader("📄 Relatório Premium")
            
            col1, col2 = st.columns([2,1])
            with col1:
                st.info("""
                **Recursos do Relatório PDF:**
                - 🎨 Design profissional com logo DoctorFit
                - 📊 Gráficos em alta resolução  
                - 📋 Análise detalhada dos scores
                - 💡 Recomendações personalizadas
                - 🏢 Formatação corporativa
                - 📈 Insights automáticos
                - 📈 Histórico temporal (se disponível)
                """)

            with col2:
                if st.button("📄 Gerar Relatório PDF", use_container_width=True, type="primary", key="btn_pdf"):
                    with st.spinner("🔄 Gerando relatório premium..."):
                        # Salva no histórico antes de gerar PDF
                        salvar_avaliacao_historico()
                        
                        pdf_path = gerar_relatorio_pdf()
                        
                        if pdf_path and os.path.exists(pdf_path):
                            # Ler arquivo PDF
                            with open(pdf_path, "rb") as pdf_file:
                                pdf_bytes = pdf_file.read()
                            
                            # Botão de download
                            st.download_button(
                                label="⬇️ Baixar Relatório PDF",
                                data=pdf_bytes,
                                file_name=os.path.basename(pdf_path),
                                mime="application/pdf",
                                use_container_width=True,
                                key="download_pdf"
                            )
                            
                            st.success("✅ Relatório PDF gerado com sucesso!")
                            
                            # Limpar arquivos temporários
                            try:
                                # Limpar gráficos temporários
                                for file in os.listdir("."):
                                    if file.startswith("chart_") and file.endswith(".png"):
                                        os.remove(file)
                                if os.path.exists(pdf_path):
                                    os.remove(pdf_path)
                            except:
                                pass
                        else:
                            st.error("❌ Erro ao gerar o PDF. Tente novamente.")
                    
        except Exception as e:
            st.error(f"Erro ao gerar gráficos: {str(e)}")
    
    st.markdown("---")
    
    # Grid de avaliações
    st.subheader("Avaliações Disponíveis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🌍 Avaliações Gerais")
        if st.button("🧠 Autorregulação Geral", use_container_width=True, key="btn_g_autor"):
            st.session_state.page = "g_autor"; st.rerun()
        if st.button("💫 Autoeficácia Geral", use_container_width=True, key="btn_g_autoef"):
            st.session_state.page = "g_autoef"; st.rerun()
        if st.button("🌈 Estabilidade Geral", use_container_width=True, key="btn_g_emoc"):
            st.session_state.page = "g_emoc"; st.rerun()
    
    with col2:
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
    
    st.markdown("""
    <div style='background:#1a1a1a; padding:18px; border-radius:10px; border-left:4px solid #A6CE39; margin:20px 0;'>
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
        cor = "#E74C3C" if val <= 4 else "#F1C40F" if val <= 7 else "#A6CE39"
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
            st.rerun()
    with col2:
        if st.button("↩️ Voltar ao Menu", use_container_width=True):
            st.session_state.page = "menu"
            st.rerun()

# ================= ROTEADOR PRINCIPAL =================
ensure_state()

if st.session_state.page == "cadastro":
    pagina_cadastro()

elif st.session_state.page == "menu":
    pagina_menu()

# Telas de avaliação
elif st.session_state.page == "g_autor":
    tela_avaliacao(
        "Autorregulação Geral",
        [
            "Tenho facilidade em manter o foco nas tarefas do dia a dia.",
            "Consigo manter disciplina em compromissos e rotinas pessoais.", 
            "Tenho bom controle dos meus impulsos (ex.: evitar distrações)."
        ],
        "Geral - Autorregulação"
    )

elif st.session_state.page == "g_autoef":
    tela_avaliacao(
        "Autoeficácia Geral", 
        [
            "Acredito na minha capacidade de superar desafios do dia a dia.",
            "Quando decido algo importante, confio que conseguirei realizar.",
            "Mesmo em situações difíceis, encontro soluções para seguir em frente."
        ],
        "Geral - Autoeficácia"
    )

elif st.session_state.page == "g_emoc":
    tela_avaliacao(
        "Estabilidade Emocional Geral",
        [
            "Consigo manter a calma diante de situações de estresse.",
            "Se algo dá errado, não deixo que isso afete todo o meu dia.",
            "Sou capaz de me recuperar emocionalmente após frustrações."
        ],
        "Geral - Estabilidade"
    )

elif st.session_state.page == "t_autor":
    tela_avaliacao(
        "Autorregulação no Treino",
        [
            "Mantenho meu compromisso com os treinos mesmo quando estou cansado(a) ou desanimado(a).",
            "Costumo refletir sobre o que posso melhorar nos meus hábitos de treino e alimentação.",
            "Faço o possível para não faltar no treino, mesmo quando há imprevistos."
        ],
        "Treino - Autorregulação"
    )

elif st.session_state.page == "t_autoef":
    tela_avaliacao(
        "Autoeficácia no Treino", 
        [
            "Tenho confiança em minha capacidade de seguir meu programa de treino.",
            "Mesmo em dias difíceis, sei que sou capaz de executar satisfatoriamente meu programa de treino.",
            "Confio que vou me dedicar para melhorar meu condicionamento físico e conquistar resultados."
        ],
        "Treino - Autoeficácia"
    )

elif st.session_state.page == "t_emoc":
    tela_avaliacao(
        "Estabilidade no Treino",
        [
            "Mesmo em dias de mau humor ou estresse, consigo ir treinar.",
            "Consigo lidar com frustrações do dia a dia e me manter psicologicamente estável.",
            "Quando algo me frustra no treino, não deixo que isso afete minha alimentação ou frequência."
        ],
        "Treino - Estabilidade"

    )

