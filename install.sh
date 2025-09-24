#!/bin/bash
# Script de instalação da pegadinha do GitHub

echo "🎪 Instalando pegadinha do GitHub... 🎪"
echo ""

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Por favor instale Python3 primeiro."
    exit 1
fi

echo "✅ Python3 encontrado!"
echo "✅ Scripts de pegadinha prontos para uso!"
echo ""
echo "📁 Arquivos disponíveis:"
echo "   • prank_github.py - Versão completa com efeitos"
echo "   • quick_prank.py - Versão rápida"
echo ""
echo "🚀 Como usar:"
echo "   python3 prank_github.py   # Versão completa"
echo "   python3 quick_prank.py    # Versão rápida"
echo ""
echo "🎭 Lembre-se: Use com responsabilidade e sempre para educar!"
echo "KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"