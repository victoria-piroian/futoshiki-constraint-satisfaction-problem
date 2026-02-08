# Look for #IMPLEMENT tags in this file.
'''
All models need to return a CSP object, and a list of lists of Variable objects
representing the board. The returned list of lists is used to access the
solution.

For example, after these three lines of code

    csp, var_array = futoshiki_csp_model_1(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array[0][0].get_assigned_value() should be the correct value in the top left
cell of the Futoshiki puzzle.

1. futoshiki_csp_model_1 (worth 20/100 marks)
    - A model of a Futoshiki grid built using only
      binary not-equal constraints for both the row and column constraints.

2. futoshiki_csp_model_2 (worth 20/100 marks)
    - A model of a Futoshiki grid built using only n-ary
      all-different constraints for both the row and column constraints.
    
    The input board is specified as a list of n lists. Each of the n lists
    represents a row of the board. If a 0 is in the list it represents an empty
    cell. Otherwise if a number between 1--n is in the list then this
    represents a pre-set board position.

    Each list is of length 2n-1, with each space on the board being separated
    by the potential inequality constraints. '>' denotes that the previous
    space must be bigger than the next space; '<' denotes that the previous
    space must be smaller than the next; '.' denotes that there is no
    inequality constraint.

    E.g., the board

    -------
    | > |2|
    | | | |
    | | < |
    -------
    would be represented by the list of lists

    [[0,>,0,.,2],
     [0,.,0,.,0],
     [0,.,0,<,0]]

'''
import cspbase
import itertools

def futoshiki_csp_model_1(futo_grid):
    n = len(futo_grid)
    csp = cspbase.CSP("Futoshiki_Model_1")
    
    var_array = []
    for i in range(n):
        row_vars = []
        for j in range(0, 2 * n - 1, 2):
            if futo_grid[i][j] == 0:
                domain = list(range(1, n + 1))
            else:
                domain = [futo_grid[i][j]]
            var = cspbase.Variable(f"V{i}{j//2}", domain)
            row_vars.append(var)
            csp.add_var(var)
        var_array.append(row_vars)
    
    for i in range(n):
        for j in range(n):
            for k in range(j + 1, n):
                con = cspbase.Constraint(f"C_Row_{i}_{j}_{k}", [var_array[i][j], var_array[i][k]])
                satisfying_tuples = [(a, b) for a in var_array[i][j].cur_domain() for b in var_array[i][k].cur_domain() if a != b]
                con.add_satisfying_tuples(satisfying_tuples)
                csp.add_constraint(con)
    
    for j in range(n):
        for i in range(n):
            for k in range(i + 1, n):
                con = cspbase.Constraint(f"C_Col_{i}_{k}_{j}", [var_array[i][j], var_array[k][j]])
                satisfying_tuples = [(a, b) for a in var_array[i][j].cur_domain() for b in var_array[k][j].cur_domain() if a != b]
                con.add_satisfying_tuples(satisfying_tuples)
                csp.add_constraint(con)
    
    for i in range(n):
        for j in range(1, 2 * n - 1, 2):
            if futo_grid[i][j] in ['<', '>']:
                left_var = var_array[i][j // 2]
                right_var = var_array[i][j // 2 + 1]
                con = cspbase.Constraint(f"C_Ineq_{i}_{j//2}_{j//2 + 1}", [left_var, right_var])
                if futo_grid[i][j] == '<':
                    satisfying_tuples = [(a, b) for a in left_var.cur_domain() for b in right_var.cur_domain() if a < b]
                else:
                    satisfying_tuples = [(a, b) for a in left_var.cur_domain() for b in right_var.cur_domain() if a > b]
                con.add_satisfying_tuples(satisfying_tuples)
                csp.add_constraint(con)
    
    return csp, var_array


def futoshiki_csp_model_2(futo_grid):
    n = len(futo_grid)
    csp = cspbase.CSP("Futoshiki_Model_2")
    
    var_array = []
    for i in range(n):
        row_vars = []
        for j in range(0, 2 * n - 1, 2):
            if futo_grid[i][j] == 0:
                domain = list(range(1, n + 1))
            else:
                domain = [futo_grid[i][j]]
            var = cspbase.Variable(f"V{i}{j//2}", domain)
            row_vars.append(var)
            csp.add_var(var)
        var_array.append(row_vars)
    
    for i in range(n):
        con = cspbase.Constraint(f"C_Row_{i}", var_array[i])
        satisfying_tuples = [tup for tup in itertools.permutations(range(1, n + 1), n)]
        con.add_satisfying_tuples(satisfying_tuples)
        csp.add_constraint(con)
    
    for j in range(n):
        col_vars = [var_array[i][j] for i in range(n)]
        con = cspbase.Constraint(f"C_Col_{j}", col_vars)
        satisfying_tuples = [tup for tup in itertools.permutations(range(1, n + 1), n)]
        con.add_satisfying_tuples(satisfying_tuples)
        csp.add_constraint(con)
    
    for i in range(n):
        for j in range(1, 2 * n - 1, 2):
            if futo_grid[i][j] in ['<', '>']:
                left_var = var_array[i][j // 2]
                right_var = var_array[i][j // 2 + 1]
                con = cspbase.Constraint(f"C_Ineq_{i}_{j//2}_{j//2 + 1}", [left_var, right_var])
                if futo_grid[i][j] == '<':
                    satisfying_tuples = [(a, b) for a in left_var.cur_domain() for b in right_var.cur_domain() if a < b]
                else:
                    satisfying_tuples = [(a, b) for a in left_var.cur_domain() for b in right_var.cur_domain() if a > b]
                con.add_satisfying_tuples(satisfying_tuples)
                csp.add_constraint(con)
    
    return csp, var_array
