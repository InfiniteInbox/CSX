import math
import matplotlib.pyplot as plt
class polynomial:
    def __init__(self,polynomarray):
        self.coefficients = polynomarray
    def create_polynomial(self):
        terms = []
        for i, coeff in enumerate(self.coefficients):
            if coeff == 0:
                continue
            if i == 0:
                terms.append(str(coeff))
            elif i == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{i}")
        return " + ".join(terms)
    def eval(self, x):
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (x ** i)
        return result
    def right_riemann_sum(self, a, b, n):
        dx = (b - a)/n
        result = 0
        for i in range(1, n + 1):
            x = a + i * dx 
            result += dx * self.eval(x)
        return result
    def left_riemann_sum(self, a, b, n):
        dx = (b - a)/n
        result = 0
        for i in range(n):
            x = a + i * dx
            result += dx * self.eval(x)
        return result
    def mid_riemann_sum(self, a, b, n):
        dx = (b - a)/n
        result = 0
        for i in range(n):
            x = a + (i + 0.5) * dx 
            result += self.eval(x) * dx
        return result
    def trapezoidal_sum(self, a, b, n):
        dx = (b - a)/n
        result = 0.5 * (self.eval(a) + self.eval(b))
        for i in range(1,n):
            x = a + i * dx
            result += self.eval(x)
            result *= dx
        return result
    def simpsons_rule(self, a, b, n):
        if n % 2 == 1:
            raise(ValueError)
        dx = (b - a)/n
        result = self.eval(a) + self.eval(b)
        for i in range(1,n):
            x = a + 1 * dx
            if i % 2 == 0:
                result += 2 * self.eval(x)
            else:
                result += 4 * self.eval(x)
        result *= dx / 3
        return result
class Experession:
    def __init__(self, tokens):
        self.root = self.build_tree(tokens)
    def build_tree(self, tokens):
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/', '^']:
                right = stack.pop()
                left = stack.pop()
                stack.append((token, left, right))
            elif token in ['ln', 'sin', 'cos','tan','asin','acos','atan','sqrt']:
                operand = stack.pop()
                stack.append((token, operand))
            else:
                stack.append(token)
        return stack[0]
    def str_tree(self, node):
        if isinstance(node, tuple):
            op = node[0]
            if op in ['+', '-', '*', '/', '^']:
                left = node[1]
                right = node[2]
                if op in ['+', '-']:
                    return f"({self.str_tree(left)} {op} {self.str_tree(right)})"
                else:
                    return f"{self.str_tree(left)} {op} {self.str_tree(right)}"
            elif op in ['ln', 'sin', 'cos', 'tan','asin','acos','atan','sqrt']:
                operand = node[1]
                return f"{op}({self.str_tree(operand)})"
        
        elif node == 'x':
            return "x"
        else:
            return str(node)

    def evaluate(self, x):
        return self.eval_tree(self.root, x)

    def eval_tree(self, node, x):
        if isinstance(node, tuple):
            op = node[0]
            if op in ['+', '-', '*', '/', '^','sqrt']:
                left = node[1]
                right = node[2]
                if op == '+':
                    return self.eval_tree(left, x) + self.eval_tree(right, x)
                elif op == '-':
                    return self.eval_tree(left, x) - self.eval_tree(right, x)
                elif op == '*':
                    return self.eval_tree(left, x) * self.eval_tree(right, x)
                elif op == '/':
                    return self.eval_tree(left, x) / self.eval_tree(right, x)
                elif op == '^':
                    return self.eval_tree(left, x) ** self.eval_tree(right, x)
                elif op == 'sqrt':
                    return math.sqrt(self.eval_tree(right, x))
            elif op in ['ln', 'sin', 'cos', 'tan','asin','atan','acos']:
                operand = node[1]
                if op == 'ln':
                    return math.log(self.eval_tree(operand, x))
                elif op == 'sin':
                    return math.sin(self.eval_tree(operand, x))
                elif op == 'cos':
                    return math.cos(self.eval_tree(operand, x))
                elif op == 'tan':
                    return math.tan(self.eval_tree(operand, x))
                elif op == 'asin':
                    return math.asin(self.eval_tree(operand, x))
                elif op == 'acos':
                    return math.acos(self.eval_tree(operand, x))
                elif op == 'atan':
                    return math.atan(self.eval_tree(operand, x))
                
        elif node == 'x':
            return x
        else:
            return node
    def right_riemann_sum(self, a, b, n):
        dx = (b - a)/n
        result = 0
        for i in range(1, n + 1):
            x = a + i * dx 
            result += dx * self.evaluate(x)
        return result
    def left_riemann_sum(self, a, b, n):
        dx = (b - a)/n
        result = 0
        for i in range(n):
            x = a + i * dx
            result += dx * self.evaluate(x)
        return result
    def mid_riemann_sum(self, a, b, n):
        dx = (b - a)/n
        result = 0
        for i in range(n):
            x = a + (i + 0.5) * dx 
            result += self.evaluate(x) * dx
        return result
    def trapezoidal_sum(self, a, b, n):
        dx = (b - a)/n
        result = 0.5 * (self.evaluate(a) + self.evaluate(b))
        for i in range(1,n):
            x = a + i * dx
            result += self.evaluate(x)
            result *= dx
        return result
    def simpsons_rule(self, a, b, n):
        if n % 2 == 1:
            raise(ValueError)
        dx = (b - a)/n
        result = self.evaluate(a) + self.evaluate(b)
        for i in range(1,n):
            x = a + 1 * dx
            if i % 2 == 0:
                result += 2 * self.evaluate(x)
            else:
                result += 4 * self.evaluate(x)
        result *= dx / 3
        return result

def main():
    user = input('do you want a function other than a polynomial?:')
    if user == 'Y':
        func = input('enter your function in in postfix:')
        lower_bound = float(input('enter your lower bound:'))
        upper_bound = float(input('enter your upper bound:'))
        intervals = int(input('enter the amount of intervals:'))
        func = [i for i in func.split(' ')]
        for i,k in enumerate(func):
            if k in ['1','2','3','4','5','6','7','8','9','0']:
                try:
                    func[i] = float(k)
                except ValueError:
                    pass

        func = Experession(func)
        step = (upper_bound - lower_bound) / intervals
        
        x = [lower_bound + i * step for i in range(intervals + 1)]
        y = [func.evaluate(i) for i in x]
        plt.plot(x,y)
        plt.show()
        
        print(func.str_tree(func.root))
        print(func.right_riemann_sum(lower_bound,upper_bound,intervals))
        print(func.left_riemann_sum(lower_bound,upper_bound,intervals))
        print(func.mid_riemann_sum(lower_bound,upper_bound,intervals))
        print(func.trapezoidal_sum(lower_bound,upper_bound,intervals))
        print(func.simpsons_rule(lower_bound,upper_bound,intervals))
        
    elif user == 'N':
        func2 = input('enter your polynomials coefficients (eg. [1,2,3] = 1 + 2x + 3x^2):')
        func2 = [int(j) for j in func2.split(' ')]
        func2 = polynomial(func2)
        lower_bound1 = float(input('enter your lower bound:'))
        upper_bound1 = float(input('enter your upper bound:'))
        intervals1 = int(input('enter the amount of intervals:'))
        print(func2.create_polynomial())
        print(func2.right_riemann_sum(lower_bound1,upper_bound1,intervals1))
        print(func2.left_riemann_sum(lower_bound1,upper_bound1,intervals1))
        print(func2.mid_riemann_sum(lower_bound1,upper_bound1,intervals1))
        print(func2.trapezoidal_sum(lower_bound1,upper_bound1,intervals1))
        print(func2.simpsons_rule(lower_bound1,upper_bound1,intervals1))



if __name__ == '__main__':
    main()

#g = polynomial([0,2,0])
#t = Experession(['x','cos','ln'])
#print(t.str_tree(t.root))
#print(Experession.right_riemann_sum(t,1,3,2))

#print(polynomial.create_polynomial(g))
#print(polynomial.eval(g,2))
#print(polynomial.right_riemann_sum(g,1,3,2))
#print(polynomial.left_riemann_sum(g,1,3,2))
#print(polynomial.mid_riemann_sum(g,1,3,2))
#print(polynomial.trapezoidal_sum(g,1,3,2))

    








        