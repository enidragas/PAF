def jedPravca(P,Q):
    a= Q[1]- P[1]
    b= P[0]-Q[0]
    c= a*(P[0]) + b*(P[1])

    if (b < 0 ):
        print("jednadzba pravca:", a, "x -", b, "y =", c, "\n")
    else:
        print("jednadzba pravca:", a, "x +", b, "y =", c, "\n")

if __name__ == '__main__':
    P= [1,2]
    Q= [-2,3]
    jedPravca(P,Q)