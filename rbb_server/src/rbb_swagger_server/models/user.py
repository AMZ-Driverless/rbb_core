# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rbb_swagger_server.models.base_model_ import Model
from rbb_swagger_server.models.permission import Permission  # noqa: F401,E501
from rbb_swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, alias: str=None, full_name: str=None, email: str=None, permissions: List[Permission]=None, password: str=None):  # noqa: E501
        """User - a model defined in Swagger

        :param alias: The alias of this User.  # noqa: E501
        :type alias: str
        :param full_name: The full_name of this User.  # noqa: E501
        :type full_name: str
        :param email: The email of this User.  # noqa: E501
        :type email: str
        :param permissions: The permissions of this User.  # noqa: E501
        :type permissions: List[Permission]
        :param password: The password of this User.  # noqa: E501
        :type password: str
        """
        self.swagger_types = {
            'alias': str,
            'full_name': str,
            'email': str,
            'permissions': List[Permission],
            'password': str
        }

        self.attribute_map = {
            'alias': 'alias',
            'full_name': 'full_name',
            'email': 'email',
            'permissions': 'permissions',
            'password': 'password'
        }

        self._alias = alias
        self._full_name = full_name
        self._email = email
        self._permissions = permissions
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def alias(self) -> str:
        """Gets the alias of this User.


        :return: The alias of this User.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias: str):
        """Sets the alias of this User.


        :param alias: The alias of this User.
        :type alias: str
        """

        self._alias = alias

    @property
    def full_name(self) -> str:
        """Gets the full_name of this User.


        :return: The full_name of this User.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name: str):
        """Sets the full_name of this User.


        :param full_name: The full_name of this User.
        :type full_name: str
        """

        self._full_name = full_name

    @property
    def email(self) -> str:
        """Gets the email of this User.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this User.


        :param email: The email of this User.
        :type email: str
        """

        self._email = email

    @property
    def permissions(self) -> List[Permission]:
        """Gets the permissions of this User.


        :return: The permissions of this User.
        :rtype: List[Permission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions: List[Permission]):
        """Sets the permissions of this User.


        :param permissions: The permissions of this User.
        :type permissions: List[Permission]
        """

        self._permissions = permissions

    @property
    def password(self) -> str:
        """Gets the password of this User.

        Only set for changing password, otherwise empty.  # noqa: E501

        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this User.

        Only set for changing password, otherwise empty.  # noqa: E501

        :param password: The password of this User.
        :type password: str
        """

        self._password = password
