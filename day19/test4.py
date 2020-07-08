# class A():pass
# class B(A):pass
# class C(A):pass
# class D(A):pass
# class E(B,C,D):pass
# class F(C,D,B):pass
# class G(D,B,C):pass
# class H(E,F,G):pass
#
# print(H.__mro__)

class O:pass
class A(O):pass
class B(O):pass
class C(O):pass
class E(A,B):pass
class F(B,C):pass
class G(E,F):pass

print(G.__mro__)