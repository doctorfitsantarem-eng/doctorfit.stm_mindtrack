# DoctorFit MindTrack — SISTEMA COMPLETO COM RELATÓRIOS PREMIUM
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image
from io import BytesIO
import base64, os
from datetime import datetime, timedelta

# ================= CONFIG =================
st.set_page_config(
    page_title="DoctorFit MindTrack", 
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

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
</style>
""", unsafe_allow_html=True)

# ================= SISTEMA DE ESTADO =================
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
    
    st.session_state.historico[aluno_key].append(registro)
    return True

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
            return {"categoria": "CONSOLIDADA", "cor": "#A6CE39", "feedback": "Excelente capacidade de autogestão. Mantenha a consistência."}
    
    elif tipo == "Autoeficácia":
        if score <= 4:
            return {"categoria": "EM FORMAÇÃO", "cor": "#E74C3C", "feedback": "Confiança em desenvolvimento. Foque em pequenas vitórias."}
        elif score <= 7:
            return {"categoria": "ESTABILIZADA", "cor": "#F1C40F", "feedback": "Confiança adequada. Continue construindo sobre bases sólidas."}
        else:
            return {"categoria": "EXCELENTE", "cor": "#A6CE39", "feedback": "Alta confiança nas capacidades. Ideal para desafios complexos."}
    
    elif tipo == "Estabilidade":
        if score <= 4:
            return {"categoria": "SENSÍVEL", "cor": "#E74C3C", "feedback": "Sensibilidade emocional elevada. Pratique técnicas de regulação."}
        elif score <= 7:
            return {"categoria": "EQUILIBRADA", "cor": "#F1C40F", "feedback": "Bom equilíbrio emocional. Desenvolva resiliência para pressão."}
        else:
            return {"categoria": "ROBUSTA", "cor": "#A6CE39", "feedback": "Excelente estabilidade emocional. Mantenha práticas de autocuidado."}

# ================= SISTEMA DE ANÁLISE =================
def gerar_insights_geral(scores):
    """Gera insights específicos para avaliação GERAL"""
    insights = []
    recomendacoes = []
    
    autorregulacao = scores.get("Autorregulação")
    autoeficacia = scores.get("Autoeficácia")
    estabilidade = scores.get("Estabilidade")
    
    if autorregulacao and autorregulacao <= 5:
        insights.append("🎯 **Organização Pessoal**: Desafio em manter rotinas e foco no dia a dia")
        recomendacoes.append("Estabeleça horários fixos para atividades importantes usando agenda")
        recomendacoes.append("Divida tarefas grandes em etapas menores e com prazos definidos")
    
    if autorregulacao and autorregulacao >= 8:
        insights.append("✅ **Excelente Autogestão**: Boa capacidade de organização pessoal")
        recomendacoes.append("Mantenha a consistência e compartilhe suas estratégias com outros")
    
    if autoeficacia and autoeficacia <= 5:
        insights.append("🌟 **Confiança em Desenvolvimento**: Crença nas capacidades precisa ser fortalecida")
        recomendacoes.append("Liste 3 pequenas conquistas diárias para construir autoconfiança")
        recomendacoes.append("Enfrente um pequeno desafio por dia para expandir zona de conforto")
    
    if autoeficacia and autoeficacia >= 8:
        insights.append("🚀 **Alta Autoeficácia**: Grande confiança nas capacidades pessoais")
        recomendacoes.append("Use essa confiança para mentorar ou ajudar outros colegas")
    
    if estabilidade and estabilidade <= 5:
        insights.append("🌊 **Sensibilidade Emocional**: Emoções afetam significativamente o desempenho")
        recomendacoes.append("Pratique respiração profunda por 2 minutos ao sentir estresse")
        recomendacoes.append("Mantenha um diário emocional para identificar padrões de reação")
    
    if estabilidade and estabilidade >= 7:
        insights.append("⚖️ **Equilíbrio Emocional**: Boa capacidade de lidar com pressões")
        recomendacoes.append("Continue praticando autocuidado para manter o equilíbrio emocional")
    
    # Análise comparativa
    if autorregulacao and autoeficacia:
        if autorregulacao > autoeficacia + 2:
            insights.append("🔍 **Disciplina > Confiança**: Tem organização, mas precisa trabalhar autoconfiança")
            recomendacoes.append("Relembre conquistas passadas para fortalecer a autoeficácia")
    
    return insights, recomendacoes

def gerar_insights_treino(scores):
    """Gera insights específicos para avaliação de TREINO"""
    insights = []
    recomendacoes = []
    
    autorregulacao = scores.get("Autorregulação")
    autoeficacia = scores.get("Autoeficácia") 
    estabilidade = scores.get("Estabilidade")
    
    if autorregulacao and autorregulacao <= 5:
        insights.append("💪 **Consistência no Treino**: Dificuldade em manter regularidade nos exercícios")
        recomendacoes.append("Agende os treinos como compromissos fixos na semana")
        recomendacoes.append("Prepare a roupa de treino na noite anterior para reduzir barreiras")
    
    if autorregulacao and autorregulacao >= 8:
        insights.append("✅ **Excelente Disciplina no Treino**: Boa aderência à rotina de exercícios")
        recomendacoes.append("Mantenha a consistência e explore novas modalidades para variar")
    
    if autoeficacia and autoeficacia <= 5:
        insights.append("🎯 **Confiança no Treino**: Dúvidas sobre capacidade de evolução física")
        recomendacoes.append("Registre pequenas melhorias (ex: mais repetições, menos cansaço)")
        recomendacoes.append("Foque no processo de evolução, não apenas nos resultados finais")
    
    if autoeficacia and autoeficacia >= 8:
        insights.append("🚀 **Alta Confiança no Treino**: Grande crença na capacidade de evolução")
        recomendacoes.append("Use essa mentalidade para superar platôs de desempenho")
    
    if estabilidade and estabilidade <= 5:
        insights.append("⚡ **Sensibilidade no Treino**: Fatores externos afetam muito a motivação")
        recomendacoes.append("Crie um ritual pré-treino para entrar no estado mental adequado")
        recomendacoes.append("Tenha um plano B para dias com imprevistos ou baixa motivação")
    
    if estabilidade and estabilidade >= 7:
        insights.append("🛡️ **Resiliência no Treino**: Boa capacidade de manter foco mesmo sob pressão")
        recomendacoes.append("Continue desenvolvendo estratégias de coping para desafios específicos")
    
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
        COR_TEXTO = black
        COR_FUNDO = white
        
        # Configurar fonte
        try:
            # Tentar usar fontes mais profissionais
            c.setFont("Helvetica-Bold", 16)
        except:
            c.setFont("Helvetica-Bold", 16)
        
        # ===== CABEÇALHO =====
        # Fundo do cabeçalho
        c.setFillColor(COR_PRIMARIA)
        c.rect(0, height-1.2*inch, width, 1.2*inch, fill=1)
        
        # Título
        c.setFillColor(black)
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(width/2, height-0.7*inch, f"RELATÓRIO {tipo_avaliacao.upper()}")
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(width/2, height-1.0*inch, "DOCTORFIT MINDTRACK")
        
        # ===== INFORMAÇÕES DO ALUNO =====
        y_position = height - 1.8*inch
        
        c.setFillColor(COR_TEXTO)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(1*inch, y_position, "INFORMAÇÕES DO ALUNO:")
        y_position -= 0.25*inch
        
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
            y_position -= 0.4*inch
        
        # ===== SCORES DETALHADOS COM CLASSIFICAÇÃO =====
        c.setFont("Helvetica-Bold", 12)
        c.drawString(1*inch, y_position, "RESULTADOS DETALHADOS:")
        y_position -= 0.3*inch
        
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
        
        # ===== INSIGHTS =====
        if insights:
            if y_position < 2*inch:
                c.showPage()
                c.setFillColor(COR_TEXTO)
                y_position = height - 1*inch
            
            c.setFillColor(COR_PRIMARIA)
            c.setFont("Helvetica-Bold", 12)
            c.drawString(1*inch, y_position, "INSIGHTS IDENTIFICADOS:")
            y_position -= 0.3*inch
            
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
        
        # ===== RECOMENDAÇÕES =====
        if recomendacoes:
            if y_position < 2*inch:
                c.showPage()
                c.setFillColor(COR_TEXTO)
                y_position = height - 1*inch
            
            c.setFillColor(HexColor("#3498db"))
            c.setFont("Helvetica-Bold", 12)
            c.drawString(1*inch, y_position, "RECOMENDAÇÕES ESTRATÉGICAS:")
            y_position -= 0.3*inch
            
            c.setFillColor(COR_TEXTO)
            c.setFont("Helvetica", 9)
            for i, recomendacao in enumerate(recomendacoes, 1):
                if y_position < 1*inch:
                    c.showPage()
                    c.setFillColor(COR_TEXTO)
                    y_position = height - 1*inch
                
                c.drawString(1.2*inch, y_position, f"{i}. {recomendacao}")
                y_position -= 0.18*inch
        
        # ===== RODAPÉ =====
        c.setFillColor(HexColor("#666666"))
        c.setFont("Helvetica", 8)
        c.drawString(1*inch, 0.5*inch, f"Relatório gerado automaticamente pelo Sistema DoctorFit MindTrack • {datetime.now().strftime('%d/%m/%Y')}")
        
        c.save()
        return filename
        
    except Exception as e:
        st.error(f"Erro ao gerar PDF: {str(e)}")
        return None

# ================= PÁGINA CADASTRO =================
def pagina_cadastro():
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
        st.subheader("💪 Avaliação de Treino")
        st.write("Avalie suas habilidades psicossociais no contexto do treino esportivo")
        if st.button("🏋️ Fazer Avaliação de Treino", use_container_width=True):
            st.session_state.page = "avaliacao_treino"
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
            st.image(grafico_path, use_column_width=True)
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
            st.image(grafico_path, use_column_width=True)
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