# 配置文件
# import os
# basedir = os.path.abspath(os.path.dirname(__file__))


# 获取随机
# a = os.urandom(24)
# print(a)

mysqlconfig = {
    "USER": "root",
    "PASSWORD": "root",
    "HOST": "139.9.172.8",
    "PORT": 3306,
    "CHARSET": "utf8",
    "DATABASE": "mitu",
}

# 通用配置
class Config:
    SCRECT_KEY = "b'\xdc\x8eS\x14\x94\x99\x95\xdf\xaaP\xba\xabY\x11\xd86\xa3\x07#)\xcb\x86\xb4\xc7'"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 开发人员使用配置
class DevelopmentConfig(Config):
    DEBUG = True
    # 'mysql+pymysql://用户名称:密码@localhost:端口/数据库名称'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(mysqlconfig.get("USER"),
                                                                        mysqlconfig.get("PASSWORD"),
                                                                        mysqlconfig.get("HOST"),
                                                                        mysqlconfig.get("PORT"),
                                                                        mysqlconfig.get("DATABASE"))



# 测试人员使用配置
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(mysqlconfig.get("USER"),
                                                                      mysqlconfig.get("PASSWORD"),
                                                                      mysqlconfig.get("HOST"),
                                                                      mysqlconfig.get("CHARSET"),
                                                                      mysqlconfig.get("DATABASE"))



# 项目演示配置
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(mysqlconfig.get("USER"),
                                                                      mysqlconfig.get("PASSWORD"),
                                                                      mysqlconfig.get("HOST"),
                                                                      mysqlconfig.get("CHARSET"),
                                                                      mysqlconfig.get("DATABASE"))


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig,
}