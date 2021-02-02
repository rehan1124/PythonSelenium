import logging


class LogGen:
    # @staticmethod
    # def log_gen():
    #     logging.basicConfig(
    #         filename="./Logs/Automation.log",
    #         format="%(asctime)s:%(levelname)s:%(message)s",
    #         datefmt="%d-%m-%Y %I:%M:%S %p",
    #     )
    #     logger = logging.getLogger()
    #     logger.setLevel(logging.INFO)
    #     return logger

    @staticmethod
    def log_gen():
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler = logging.FileHandler(filename="./Logs/automation.log")
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger
