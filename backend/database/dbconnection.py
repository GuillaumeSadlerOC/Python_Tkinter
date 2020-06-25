""" DATABASE CONNECTION
This class get an server connection with SQLAlchemy.
(!) An internet connection must be active. """

# -*- coding: utf-8 -*-
# From Python 3
import json
# From mysql connector
import mysql.connector
# From SQLAlchemy
from sqlalchemy import create_engine, exc
# From Program


class DbConnection():
    def __init__(
        self
    ):
        """ 'server_logs'     (Dict): extracts data of JSON file 'logs.json'.
            'server_statuts'  (Dict): extracts data of JSON file 'logs.json'.
            'server_user'     (str ): name of user for server access.
            'server_pass'     (str ): password of user for server access.
            'server_host'     (str ): host name.
            'server_db_name'  (str ): name of database.
            'server_conn'     (int ):
                                0 for no connection,
                                1 for server connection only,
                                2 for database connection. """

        # JSON FILE ATTRIBUTES
        self.server_logs = None
        self.server_status = None
        self.server_user = None
        self.server_pass = None
        self.server_host = None
        self.server_db_name = None
        self.server_conn = 0

        self.engine_default = None

        self.json_file(action="load")

    def json_file(self, action=None):
        """ Extracts the configurations from the JSON file 'logs.json'
        Or Save configuration from the JSON file 'logs.json' """

        if action == "load":

            with open('backend/serverconfigs.json') as json_data:
                json_dict = json.load(json_data)

            self.server_logs = json_dict.get("server_logs")
            self.server_status = json_dict.get("server_status")

        elif action == "write":

            # Write in JSON File
            write_json = {}
            write_json["server_logs"] = {}
            write_json["server_logs"]["server_user"] = self.server_user
            write_json["server_logs"]["server_pass"] = self.server_pass
            write_json["server_logs"]["server_host"] = self.server_host

            write_json["server_status"] = {}
            write_json["server_status"]["server_conn"] = self.server_conn
            write_json["server_status"]["server_db_name"] = self.server_db_name

            with open(
                "backend/serverconfigs.json", "w", encoding="utf-8"
            ) as json_file:

                json.dump(write_json, json_file, indent=4)

    def connection(
        self,
        server_user=None,
        server_pass=None,
        server_host=None,
        server_db_name=None
    ):
        """ Return a connection to the server """

        self.json_file(action="load")

        s_user = None
        s_pass = None
        s_host = None
        s_db_name = None
        s_err = 0

        # We check server user status
        if server_user is not None:
            s_user = server_user
        elif self.server_logs["server_user"] is not None:
            s_user = self.server_logs["server_user"]
        else:
            s_err += 1

        # We check server pass status
        if server_pass is not None:
            s_pass = server_pass
        elif self.server_logs["server_pass"] is not None:
            s_pass = self.server_logs["server_pass"]
        else:
            s_err += 1

        # We check server host status
        if server_host is not None:
            s_host = server_host
        elif self.server_logs["server_host"] is not None:
            s_host = self.server_logs["server_host"]
        else:
            s_err += 1

        # We start connection
        if s_err == 0:

            if server_db_name is not None or server_db_name != "":
                s_db_name = server_db_name
            elif self.server_status["server_db_name"] is not None:
                s_db_name = self.server_status["server_db_name"]

            if s_db_name is not None or s_db_name == "":
                try:
                    self.engine = create_engine(
                        'mysql+mysqlconnector://{}:{}@{}/{}?charset=utf8mb4'
                        .format(s_user, s_pass, s_host, s_db_name)
                    )
                    self.engine.connect()
                    self.server_conn = 2
                except exc.SQLAlchemyError:
                    self.server_conn = 0
            else:

                try:
                    self.engine = create_engine(
                            'mysql+mysqlconnector://{}:{}@{}'.format(
                                s_user, s_pass, s_host
                            )
                        )
                    self.engine_default = self.engine
                    self.engine.connect()
                    self.engine.execute(
                        "CREATE DATABASE IF NOT EXISTS purbeurre"
                    )
                    s_db_name = "purbeurre"
                    self.engine = create_engine(
                        'mysql+mysqlconnector://{}:{}@{}/{}?charset=utf8mb4'
                        .format(s_user, s_pass, s_host, s_db_name)
                    )
                    self.engine.connect()
                    self.server_conn = 2

                    # Save and write in JSON file
                    self.server_user = s_user
                    self.server_pass = s_pass
                    self.server_host = s_host
                    self.server_db_name = s_db_name
                    self.json_file(action="write")

                except Exception as e:
                    self.server_conn = 0

        return self.server_conn
