import logging
from logging.handlers import SMTPHandler
import os

# def get_SMTPlogger(module_name, type):
#     logger = logging.getLogger(module_name + '_' + type)
#     config = utils.config_parser()
#     enable_alert_email = config.get('alert_email', 'enable_email_alert_for_feedback')
#     if enable_alert_email.lower() == "true":
#         email_server = config.get('alert_email', 'email_server')
#         sender_addr = config.get('alert_email', 'sender_addr')
#         receiver_addrs = config.get('alert_email', 'receiver_addrs')
#         email_subject = config.get('alert_email', 'email_subject_for_subjective_feedback')
#         email_handler = SMTPHandler(mailhost=email_server, fromaddr=sender_addr, toaddrs=receiver_addrs, subject=email_subject)
#         log_formatter = logging.Formatter('''%(message)s''')
#         email_handler.setFormatter(log_formatter)
#         email_handler.setLevel(logging.INFO)
#         logger.addHandler(email_handler)
#     return logger

def get_SMTPlogger(module_name, type):
    logger = logging.getLogger(module_name + '_' + type)

    email_handler = SMTPHandler(mailhost="emailmum.xoriant.com", fromaddr="nirav.kothari@xoriant.com", toaddrs="ashwini.kudure@xoriant.com,ramesh.rangarajan@xoriant.com", subject="test mail 2")
    log_formatter = logging.Formatter('''%(message)s''')
    email_handler.setFormatter(log_formatter)
    email_handler.setLevel(logging.INFO)
    logger.addHandler(email_handler)

    return logger