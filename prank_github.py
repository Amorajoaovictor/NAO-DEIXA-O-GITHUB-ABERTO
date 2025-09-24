#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para zoar quem deixa o GitHub aberto no PC da faculdade
KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
"""

import time
import random
import os
import webbrowser
from datetime import datetime

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mensagens_engracadas():
    """Retorna uma lista de mensagens engraçadas"""
    return [
        "🚨 ATENÇÃO: GITHUB ABANDONADO DETECTADO! 🚨",
        "Ei, ei, ei! Quem deixou o GitHub aberto aqui? KKKKKKKK",
        "🎭 PEGADINHA DO MALANDRO: Nunca deixe o GitHub aberto na faculdade!",
        "🔒 REGRA Nº 1 DA INFORMÁTICA: SEMPRE FAZER LOGOUT!",
        "👀 Os colegas estão vendo seu código... EMBARRASSING! KKKKKK",
        "🎪 CIRCO PEGOU FOGO: Alguém esqueceu de fechar o GitHub!",
        "⚠️  SISTEMA COMPROMETIDO: Detected unauthorized laughter access KKKKKK",
        "🤡 Palhaço detectado: Quem não faz logout merece ser zoado!",
        "🎵 🎶 Closed GitHub, closed problems, open GitHub, open troubles! 🎶 🎵",
        "💻 DICA PRO: Ctrl+Shift+T não vai te salvar dessa vez! KKKKKK"
    ]

def efeito_matrix():
    """Simula o efeito Matrix por alguns segundos"""
    caracteres = "01"
    for i in range(50):
        linha = ""
        for j in range(80):
            linha += random.choice(caracteres) + " "
        print(linha)
        time.sleep(0.1)

def contador_vergonha():
    """Contador de vergonha"""
    print("\n" + "="*60)
    print("🔥 CONTADOR DE VERGONHA ATIVADO 🔥")
    print("="*60)
    
    for i in range(10, 0, -1):
        print(f"⏰ Tempo para você perceber que foi zoado: {i} segundos...")
        print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
        time.sleep(1)
        limpar_tela()
    
    print("💥 TEMPO ESGOTADO! VOCÊ FOI OFICIAMENTE ZOADO! 💥")

def mostrar_avisos():
    """Mostra uma série de avisos engraçados"""
    avisos = [
        "⚠️  AVISO: Este computador agora pertence aos memes",
        "📢 COMUNICADO: Sua reputação como programador foi comprometida",
        "🚨 ALERTA: Colegas da sala já tiraram print da tela",
        "📱 INFO: WhatsApp da turma já sabe que você esqueceu o GitHub aberto",
        "🎯 META: Aprender a fazer logout = DESBLOQUEADA",
        "🏆 CONQUISTA: 'Esquecimento Level Master' - DESBLOQUEADA"
    ]
    
    for aviso in avisos:
        print(aviso)
        time.sleep(2)

def abrir_videos_engracados():
    """Abre alguns vídeos/links engraçados (opcional)"""
    links_engracados = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # Rick Roll clássico
        "https://github.com/"  # Volta pro GitHub com uma lição aprendida
    ]
    
    print("🎬 Abrindo vídeo educativo sobre segurança...")
    time.sleep(2)
    # Descomentiar a linha abaixo se quiser que abra o browser (pode ser muito invasivo)
    # webbrowser.open(random.choice(links_engracados))

def main():
    """Função principal da pegadinha"""
    try:
        limpar_tela()
        
        # Header da pegadinha
        print("🎪" * 20)
        print("🎭 BEM-VINDO À PEGADINHA DO GITHUB ABERTO! 🎭")
        print("🎪" * 20)
        print()
        
        # Mostra mensagem aleatória
        mensagem = random.choice(mensagens_engracadas())
        print(f"📣 {mensagem}")
        print()
        
        # Timestamp da vergonha
        agora = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        print(f"⏰ Momento da vergonha: {agora}")
        print()
        
        # Efeito especial
        print("🌟 Preparando efeitos especiais...")
        time.sleep(2)
        
        # Simula carregamento
        for i in range(1, 6):
            print(f"⚡ Carregando pegadinha... {i*20}%")
            time.sleep(0.5)
        
        limpar_tela()
        
        # Efeito Matrix
        print("🔴 INICIANDO SEQUÊNCIA MATRIX...")
        time.sleep(1)
        limpar_tela()
        efeito_matrix()
        
        limpar_tela()
        
        # Mensagem final
        print("🎊 PARABÉNS! VOCÊ FOI OFICIALMENTE ZOADO! 🎊")
        print()
        print("📜 LIÇÕES APRENDIDAS:")
        print("   1. 🔒 Sempre fazer logout quando usar computador público")
        print("   2. 🧠 Nunca deixar contas pessoais abertas na faculdade") 
        print("   3. 😅 Aceitar que foi zoado com bom humor KKKKKKKK")
        print()
        
        mostrar_avisos()
        print()
        
        # Contador final
        contador_vergonha()
        
        print()
        print("🎪 Obrigado por participar da nossa pegadinha!")
        print("🎭 Lembre-se: NUNCA MAIS deixe o GitHub aberto!")
        print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
        print()
        
        # Opcional: abrir links engraçados
        resposta = input("🎬 Quer assistir um vídeo educativo sobre segurança? (s/n): ")
        if resposta.lower() in ['s', 'sim', 'y', 'yes']:
            abrir_videos_engracados()
        
        print("\n🚪 Tchau! E não esqueça: Ctrl+Shift+Q para fechar tudo! 😉")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Tentando escapar da pegadinha? NICE TRY! KKKKKK")
        print("🏃‍♂️ Correndo não vai te salvar da vergonha!")
        time.sleep(2)
    
    except Exception as e:
        print(f"💥 Erro inesperado na pegadinha: {e}")
        print("🤷‍♂️ Mas a zoação foi entregue mesmo assim! KKKKKK")

if __name__ == "__main__":
    print("🎪 Iniciando pegadinha do GitHub aberto...")
    time.sleep(1)
    main()