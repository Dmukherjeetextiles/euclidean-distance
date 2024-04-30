def euclid(a1, b1, a2, b2):
    d = ((a1-a2)**2 + (b1-b2)**2)**0.5
    return d

def main():
    x1 = 2.5
    y1 = -7
    x2 = 4
    y2 = 9.5
    print(euclid(x1,y1, x2, y2))

if __name__=='__main__':
    main()