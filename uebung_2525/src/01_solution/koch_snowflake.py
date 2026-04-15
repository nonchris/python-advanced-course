import turtle as t

# Go faast
t.speed(0)


def snowflake(cur_length: int):
    # end condition
    if cur_length < 5:
        t.fd(cur_length)
        return

    # We split the Line into 4 Segments each one is again a Koch Curve
    snowflake(cur_length//3)
    t.left(60)
    snowflake(cur_length//3)
    t.right(120)
    snowflake(cur_length//3)
    t.left(60)
    snowflake(cur_length//3)


length = 300  # Length of whole Segment

# Reposition
t.penup()
t.bk(length/2)
t.pendown()

# Draw Triangle out of koch curves
snowflake(length)
t.right(120)
snowflake(length)
t.right(120)
snowflake(length)

t.mainloop()
