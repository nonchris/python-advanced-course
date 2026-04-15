import inspect
from dataclasses import dataclass
from typing import Literal
import typing


@dataclass
class CSMember:
    first_name: str
    last_name: str
    # warning: this argument can only be set as positional argument
    # as it's kwarg name is mangled before function is called
    # see: https://www.geeksforgeeks.org/name-mangling-in-python/
    __status: Literal["SHK", "Student", "Employee"]

    @property
    def is_student(self) -> bool:  # new dynamic state variable
        return self.__status == "Student" or self.__status == "SHK"

    @property
    def gsg_account_name(self):  # information that can be generated on demand
        return f"{self.last_name}{self.first_name[0]}{0 if self.is_student else 1}".lower()

    @property
    def status(self):  # read only interface for status
        return self.__status

    @status.setter  # note: the defined function must have the same name!
    def status(self, new_status):
        # get the allowed values out of the literal, totally no black magic involved
        types = typing.get_args(self.__annotations__["_CSMember__status"])
        if new_status not in types:
            raise ValueError(f"Invalid status '{new_status}'!")

        self.__status = new_status


if __name__ == '__main__':
    chris = CSMember("Chris", "Geron", "Student")

    print(chris.gsg_account_name)
    chris.status = "SHK"

    print(chris.status)
