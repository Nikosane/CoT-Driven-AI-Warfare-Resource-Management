import logging

# Configure logging
logging.basicConfig(
    filename="logs/simulation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_message(level, message):
    """Logs a message with the specified logging level."""
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    elif level == "debug":
        logging.debug(message)
    else:
        logging.info(message)

def log_ai_thought_process(agent, thought):
    """Logs the AI agent's thought process."""
    log_message("info", f"{agent}: {thought}")
