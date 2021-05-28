#     REPRESENTATION OF LOGIC OPERATIONS

# return result of implication (A -> B)

def impl(a, b):
    return int(not a) or b

# equivalence can be represented as (A == B)

# xor can be represented as (A != B)


#     LIST OF COMBINATION

# generates a list of binary numbers of a length given as an argument

def generate_solutions(num_logic_vars):
    solutions = []
    for i in range(2 ** num_logic_vars):
        solution = bin(i)[2:].zfill(num_logic_vars)
        solutions.append(solution)
    return solutions

# solves logic equation
#        left_expr = right_expr
# NB! expressions must be strings
#     where logic operation are represented as described above 
# NB! logic variables must be CAPITAL letters 

def solve_logic_equation(left_expr, right_expr, *logic_vars):
    num_logic_vars = len(logic_vars)
    solutions = generate_solutions(num_logic_vars) 
    counter_solutions = 0
    for solution in solutions:
        logic_vars_values = dict()
        i = 0
        subst_left_expr = str(left_expr)
        subst_right_expr = str(right_expr)
        for logic_var in logic_vars:
            subst_left_expr = subst_left_expr.replace(logic_var, solution[i])
            subst_right_expr = subst_right_expr.replace(logic_var, solution[i])
            logic_vars_values[logic_var] = solution[i]
            i += 1
        if eval(subst_left_expr) == eval(subst_right_expr):
            counter_solutions += 1
            print(solution)
    print('Количество решений: {}'.format(counter_solutions))
