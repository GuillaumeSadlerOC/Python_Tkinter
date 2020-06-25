""" DATABASE USER
- In charge of the database CRUD user :
Create - Read - Update - Delete
- Need an instance of Connection.
- The database connection must be active.
- (!) An internet connection must be active. """

# -*- coding: utf-8 -*-
# From Python 3
# From Requests
from requests import get
# From SQLAlchemy
from sqlalchemy import update
# From Program
from backend.lib.user import User


class DbUser():
    def __init__(
        self,
        db_manager=None
    ):
        """ 'db_manager'            (obj ): an instance of DbManager.
            'err'                   (int ): error counter.
            'err_posts'             (list): errors posts.
            'result'                (    ): result of SQLAlchemy request.
            'user_name_lenght_max'  (int ): maximum number of characters. """

        self.db_manager = db_manager
        self.current_connection = self.db_manager.db_connection
        self.Session = self.db_manager.Session
        self.new_session = self.db_manager.new_session

        self.err = 0
        self.err_posts = []
        self.result = None

        self.user_name_lenght_max = 10

    def create(
        self,
        user_name="",
        avatar_name=""
    ):
        """ Add a new user to the database.
            'user_name'     (str): name of user.
            'avatar_name'   (str): name of avatar. """

        # err initialisation
        self.err = 0
        self.err_posts = []

        # Empty test
        if user_name == "":
            self.err += 1
            self.err_posts.append("Nom d'utilisateur manquant")
        elif avatar_name == "":
            self.err += 1
            self.err_posts.append("Nom de l'avatar manquant")
        # Lenght test
        elif len(user_name) > self.user_name_lenght_max:
            self.err += 1
            self.err_posts.append(
                "Le nom d'utilisateur contient {} caractères contre {} maximum"
                .format(
                    len(user_name), self.user_name_lenght_max
                )
            )

        # Query
        if self.err == 0:
            new_user = User(
                user_name=str(user_name),
                avatar_name=str(avatar_name)
            )
            self.new_session.add(new_user)
            self.new_session.commit()

        return self.err

    def read(
        self,
        action=None,
        user_id=None,
        user_name=None
    ):
        """ 'action'            (str): name of action to execute.
            'user_id'           (int): unique id of user.
            'user_name'         (str): name of user.
            'result'            ()   : result of SQLAlchemy request. """

        # err initialisation
        self.err = 0
        self.err_posts = []
        self.result = None

        # User id
        if action == "id":
            """ SQLAlchemy query to retrieve a user
            whose identifier we know. """

            try:
                user_id = int(user_id)
                req_results = self.new_session.query(User).\
                    filter(
                        User.userID == user_id
                    ).all()

                for req_result in req_results:

                    user = {}

                    user["user_id"] = req_result.userID
                    user["user_name"] = req_result.userName
                    user["user_avatar_name"] = req_result.userAvatarName

                result = user

            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # User name
        elif action == "name":
            """ SQLAlchemy query to retrieve an user
            whose name we know. """

            try:
                user_name = str(user_name)
                result = self.new_session.query(User).\
                    filter(
                        User.userName == user_name
                    ).all()
            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # All users
        elif action == "*":
            """ SQLAlchemy query to retrieve \
            all users. """

            try:
                req_results = self.new_session.query(User).all()

                result = []

                for req_result in req_results:

                    user = {}

                    user["user_id"] = req_result.userID
                    user["user_name"] = req_result.userName
                    user["user_avatar_name"] = req_result.userAvatarName

                    result.append(user)

            except Exception as e:
                self.err += 1
                self.err_posts.append("{}".format(e))

        # Error
        else:
            self.err += 1
            self.err_posts.append("Action non reconnue.")

        return result

    def update(
        self,
        user_id=None,
        user_name=None,
        user_avatar_name=None
    ):
        """ Update user to the database.
            'user_name'     (str): id of user.
            'user_name'     (str): (optional) name of user.
            'avatar_name'   (str): (optional) name of avatar. """

        # err initialisation
        self.err = 0
        self.err_posts = []

        # Id test
        if user_id is None:
            self.err += 1
            self.err_posts.append("Identifiant de l'utilisateur inconnu")
        else:
            user_to_up = self.new_session.query(User).\
                filter(User.userID == user_id).one()

        # Query
        if self.err == 0:

            if user_name is not None:
                user_to_up.userName = user_name
            if user_avatar_name is not None:
                user_to_up.userAvatarName = user_avatar_name

            self.new_session.commit()

        return self.err

    def delete(
        self,
        user_id=None
    ):
        """ Delete user to the database.
            'user_id'    (str): id of user to delete. """

        # err initialisation
        self.err = 0
        self.err_posts = []

        # Id test
        if user_id is None:
            self.err += 1
            self.err_posts.append("Identifiant de l'utilisateur inconnu")
        else:
            user_to_del = self.new_session.query(User).\
                filter(User.userID == user_id).one()

        # Query
        if self.err == 0:

            self.new_session.delete(user_to_del)
            self.new_session.commit()

        return self.err
