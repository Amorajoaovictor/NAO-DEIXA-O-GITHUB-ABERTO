#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Versão rápida da pegadinha para testes
"""

import random
from datetime import datetime

def main():
    """Versão rápida da pegadinha"""
    mensagens = [
        "🚨 ATENÇÃO: GITHUB ABANDONADO DETECTADO! 🚨",
        "Ei, ei, ei! Quem deixou o GitHub aberto aqui? KKKKKKKK",
        "🎭 PEGADINHA DO MALANDRO: Nunca deixe o GitHub aberto na faculdade!",
        "🔒 REGRA Nº 1 DA INFORMÁTICA: SEMPRE FAZER LOGOUT!",
        "👀 Os colegas estão vendo seu código... EMBARRASSING! KKKKKK"
    ]
    
    print("🎪" * 20)
    print("🎭 BEM-VINDO À PEGADINHA DO GITHUB ABERTO! 🎭")
    print("🎪" * 20)
    print()
    
    mensagem = random.choice(mensagens)
    print(f"📣 {mensagem}")
    print()
    
    agora = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
    print(f"⏰ Momento da vergonha: {agora}")
    print()
    
    print("🎊 PARABÉNS! VOCÊ FOI OFICIALMENTE ZOADO! 🎊")
    print()
    print("📜 LIÇÕES APRENDIDAS:")
    print("   1. 🔒 Sempre fazer logout quando usar computador público")
    print("   2. 🧠 Nunca deixar contas pessoais abertas na faculdade") 
    print("   3. 😅 Aceitar que foi zoado com bom humor KKKKKKKK")
    print()
    print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")

if __name__ == "__main__":
    main()