# HORION

HORION é um framework inteligente de automação e paralelismo Python, projetado para processar dados de forma eficiente, robusta e escalável. Conta com estratégias automáticas para tarefas I/O bound, CPU bound, e tratamento de exceções inteligentes para garantir resiliência.

## Principais Features
- Paralelismo híbrido: threads, processos e fallback automático.
- Estratégias inteligentes baseadas no tamanho e tipo dos dados.
- Fácil de adaptar e integrar em outros projetos.
- Testes automáticos de robustez incluídos.
- Exemplo de loop de correção em `cot_hmp.py`.
- Script de teste `github_test.py` demonstra uso básico da API do GitHub.
- Defina a variável de ambiente `GITHUB_TOKEN` para autenticar as chamadas do script.
- Opcionalmente defina `USUARIO_GITHUB` para consultar as informações de um usuário específico.

---

## Exemplo de Loop de Correção (COT.HMP)

O arquivo `cot_hmp.py` demonstra um ciclo de execução que tenta uma tarefa várias vezes,
analisando o resultado e aplicando correções sempre que há erro. A lógica geral pode
ser representada no pseudocódigo abaixo:

```pseudo
# COT.HMP — LOOP DE CORREÇÃO E ANÁLISE (HMP PURO)

# 1. INICIALIZAÇÃO DE VARIÁVEIS E CONTEXTO
SET tentativa       TO 1
SET limite_tentativas TO 9
SET sucesso         TO False

# 2. RECEBE TAREFA DO USUÁRIO
SET tarefa          TO INPUT("Descreva a tarefa a ser executada:")

# 3. LOOP DE EXECUÇÃO E CORREÇÃO
WHILE tentativa <= limite_tentativas AND sucesso == False DO
    LOG "Tentativa número: " + tentativa

    # 3.1 EXECUTA A TAREFA
    CALL executar_tarefa WITH descricao = tarefa
    SET resultado      TO OUTPUT
    LOG "Resultado da execução: " + resultado

    # 3.2 ANALISA O RESULTADO
    CALL analisar_resultado WITH saida = resultado
    SET erro           TO OUTPUT
    LOG "Análise: " + erro

    # 3.3 DECISÃO: ERRO OU SUCESSO
    IF erro == "" OR erro == None THEN
        SET sucesso   TO True
        LOG "Execução bem-sucedida! Resultado: " + resultado
        CALL salvar_resultado WITH tarefa = tarefa, saida = resultado
    ELSE
        LOG "Erro detectado: " + erro
        # 3.4 TENTA CORRIGIR O ERRO
        CALL corrigir_tarefa WITH descricao = tarefa, erro = erro, saida = resultado
        SET tarefa   TO OUTPUT
        LOG "Nova versão corrigida da tarefa: " + tarefa
        # Incrementa tentativa
        SET tentativa TO tentativa + 1
    ENDIF
ENDWHILE

# 4. FINALIZAÇÃO
IF sucesso == False THEN
    LOG "Limite de tentativas atingido. Tarefa não concluída com sucesso."
    CALL registrar_falha WITH tarefa = tarefa, ultima_saida = resultado, ultimo_erro = erro
ENDIF

RETURN "Processo concluído."
```

---

> Desenvolvido com 💡 e aquele toque de malícia Python.
