from logging import getLogger, DEBUG, StreamHandler, Formatter


# “Requests" package uses "urllib3" package to make HTTP calls
# That's why, we need to configure logging for the "urllib3"
urllib3_logger = getLogger("urllib3")
urllib3_logger.setLevel(DEBUG)

# prepare handler
handler = StreamHandler()
# prepare formatter
formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add handler
urllib3_logger.addHandler(handler)


# "requests" package uses "urllib3" package to make HTTP calls.
# That's why we need to configure logging for the "urllib3".
logger = getLogger("DriverLogger")
logger.setLevel(DEBUG)

# prepare handler
handler = StreamHandler()
# prepare formatter
formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add handler
logger.addHandler(handler)
