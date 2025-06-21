import logging
from typing import Optional

def executar_tarefa(descricao: str) -> str:
    """Executa a tarefa descrita. Placeholder simples."""
    logging.info("Executando tarefa: %s", descricao)
    # Simulacao: se a descricao contem a palavra 'erro', retorna 'erro'
    if "erro" in descricao.lower():
        return "erro"
    return "sucesso"

def analisar_resultado(saida: str) -> Optional[str]:
    """Analisa o resultado retornado pela tarefa."""
    logging.info("Analisando resultado: %s", saida)
    if saida == "erro":
        return "Resultado indica falha."
    return None

def corrigir_tarefa(descricao: str, erro: str, saida: str) -> str:
    """Tenta corrigir a descricao da tarefa baseada no erro."""
    logging.info("Corrigindo tarefa. Erro: %s", erro)
    # Exemplo simples: remove a palavra 'erro' da descricao
    return descricao.replace("erro", "corrigido")

def salvar_resultado(tarefa: str, saida: str) -> None:
    logging.info("Salvando resultado final da tarefa '%s': %s", tarefa, saida)

def registrar_falha(tarefa: str, ultima_saida: str, ultimo_erro: str) -> None:
    logging.error(
        "Falha na tarefa '%s'. Saida: %s | Erro: %s",
        tarefa,
        ultima_saida,
        ultimo_erro,
    )

def loop_de_execucao() -> str:
    tentativa = 1
    limite_tentativas = 9
    sucesso = False
    tarefa = input("Descreva a tarefa a ser executada: ")

    resultado: Optional[str] = None
    erro: Optional[str] = None

    while tentativa <= limite_tentativas and not sucesso:
        logging.info("Tentativa numero: %d", tentativa)
        resultado = executar_tarefa(tarefa)
        logging.info("Resultado da execucao: %s", resultado)

        erro = analisar_resultado(resultado)
        logging.info("Analise: %s", erro)

        if not erro:
            sucesso = True
            logging.info("Execucao bem-sucedida! Resultado: %s", resultado)
            salvar_resultado(tarefa, resultado)
        else:
            logging.info("Erro detectado: %s", erro)
            tarefa = corrigir_tarefa(tarefa, erro, resultado)
            logging.info("Nova versao corrigida da tarefa: %s", tarefa)
            tentativa += 1

    if not sucesso:
        logging.error("Limite de tentativas atingido. Tarefa nao concluida com sucesso.")
        registrar_falha(tarefa, resultado or "", erro or "")

    return "Processo concluido."


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    print(loop_de_execucao())
