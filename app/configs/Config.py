import yaml

with open("app/resources/config.yml", '+r') as config:
    cfg = yaml.load(config, Loader=yaml.FullLoader)


class ProjectConfig:
    PRJ_ALIAS = cfg['project']['alias']



class MailConfig:
    MAIL_USERNAME = cfg['mail']['mail_username']
    MAIL_PASSWORD = cfg['mail']['mail_password']
    MAIL_FROM = cfg['mail']['mail_from']
    MAIL_PORT = cfg['mail']['mail_port']
    MAIL_SERVER = cfg['mail']['mail_server']
    MAIL_TLS = cfg['mail']['mail_tls']
    MAIL_SSL = cfg['mail']['mail_ssl']
    USE_CREDENTIALS = cfg['mail']['use_credentials']
    VALIDATE_CERTS = cfg['mail']['validate_certs']



