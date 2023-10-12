import datetime

from pydantic import BaseModel, constr


class Student(BaseModel):
    first_name: constr(min_length=1, max_length=50)
    last_name: constr(min_length=1, max_length=50)
    date_of_birth: datetime.datetime
    email: constr(min_length=1, max_length=100)
