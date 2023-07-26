# se puede crear un logging personalizado con otro nombre para no llamar siempre logging
import logging

logger = logging.getLogger(__name__)
print(logger)

logger.warning("Log de advertencia")