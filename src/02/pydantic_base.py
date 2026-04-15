import datetime as dt
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str = 'Undisclosed'

class Pet(BaseModel):
    type: str
    name: str | None

class UserAndPet(BaseModel):
    user: User
    pet: Pet
    # we wanna store the creation of the object but dont't wanna serialize it
    date_of_creation: dt.datetime = Field(default_factory=dt.datetime.now, exclude=True)

pi = User(name="Das Pi", id=31415)
dongo = Pet(name="Dongo", type="Labrador")
print(f"{pi=}")
print(f"{dongo=}")

pair = UserAndPet(user=pi, pet=dongo)
print(f"{pair = }")

dump = pair.model_dump()
print(dump)

recreation = UserAndPet.validate(dump)
print(f"{recreation = }")
