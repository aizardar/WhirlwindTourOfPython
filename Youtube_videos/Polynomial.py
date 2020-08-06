# Following code is taken from a Youtube video "What does it 
# takes to be an expert in python?" 

# ================Start======================#


# some behaviour that I want to implement --> write some __ function__
# x + y -> __add__
# inti x -> __init__




class Polynomial():

    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))


    def __len__(self):

        return len(self.coeffs)


p1 = Polynomial(1,2,3) # x² + 2x +3 
p2 = Polynomial(3,4,3) # 3x² + 4x + 3

