class BA:
    def __init__(s,n,h):
        s.n=n
        s.h=h
        s.b=0.0
    def d(s,a):
        s.b+=a
        print("Deposit of $% 2f successful" %a)
        s.pb()
    def w(s,a):
        if s.b>=a:
            s.b-=a
            print("withdrawal of $% 2f successful"%a)
        else:
            print("insufficient funds")
        s.pb()
    def g(s):
        return s.b
    def pb(s):
        print("current balance: $% 2f" %s.b)
class SA(BA):
    def __init__(s,n,h,r):
        super().__init__(n,h)
        s.r=r
    def al(s):
        l=s.b*s.r
        s.d(l)
    def pb(s):
        super().pb()
        print("interest rate: %2f%%"%(s.r*100))
ba=BA("123456789","jane Doe")
ba.d(1000)
ba.w(500)
sa=SA("987654321","jane Smith",0.05)
sa.d(1000)
sa.al()
sa.pb()        