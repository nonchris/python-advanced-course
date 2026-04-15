import turtle as t

# Schpeeed
t.speed(0)


def fractal(l: float):
    # end condition
    if l < 5:
        return
    
    # Move forward 
    t.forward(l)

    # Draw tree to the left
    t.left(45)
    fractal(l * 0.8)

    # Draw tree to the right
    t.right(90)
    fractal(l * 0.8)

    # return
    t.left(45)
    t.backward(l)


t.left(90)
fractal(30)

t.mainloop()
