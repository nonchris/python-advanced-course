from dataclasses import dataclass, field


@dataclass(order=True)
class Comment:
    id: int
    text: str = ""
    items: list[str] = field(default_factory=list, repr=False, compare=False)

    # TODO: start your functionality here


c1 = Comment(1, "hello")
c2 = Comment(2, "hello")

c1.id = 42

print(c1 < c2)
