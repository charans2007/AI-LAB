Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# ==========================================================
# AI Lab - Week 8: First-Order Logic (FOL) Forward Reasoning
# Name : CHARAN S
# USN  : 1WN24CS070
# ==========================================================

def is_variable(x):
    return isinstance(x, str) and x.islower()

def unify(x, y, subst=None):
    if subst is None:
        subst = {}
    if x == y:
        return subst
    elif is_variable(x):
        return unify_var(x, y, subst)
    elif is_variable(y):
        return unify_var(y, x, subst)
    elif isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        if x != y:  # Predicate names must match
            return None
        for a, b in zip(x[1:], y[1:]):
            subst = unify(a, b, subst)
            if subst is None:
                return None
        return subst
    else:
        return None

def unify_var(var, x, subst):
    if var in subst:
        return unify(subst[var], x, subst)
    elif x in subst:
        return unify(var, subst[x], subst)
    else:
        new_subst = subst.copy()
        new_subst[var] = x
        return new_subst

def substitute(atom, subst):
    pred = atom
    args = tuple(subst.get(arg, arg) for arg in atom[1:])
    return (pred,) + args

def match_premises(premises, kb, subst=None):
    if subst is None:
        subst = {}
    if not premises:
        return [subst]
    
    first, rest = premises, premises[1:]
    results = []
    for fact in kb:
        new_subst = unify(first, fact, subst)
        if new_subst is not None:
            results.extend(match_premises(rest, kb, new_subst))
    return results

def fol_forward_chaining(kb, rules, query):
    print("==========================================")
    print("Name : CHARAN S")
    print("USN  : 1WN24CS070")
    print("==========================================\n")
    
    print("--- Initial Knowledge Base ---")
    for fact in sorted(kb):
        print(f"  {fact}({', '.join(fact[1:])})")
    print("\n--- Starting Forward Chaining ---")
    
    iteration = 1
    while True:
        new_facts = set()
        for premises, conclusion in rules:
            substitutions = match_premises(premises, kb)
            for subst in substitutions:
                inferred = substitute(conclusion, subst)
                if inferred not in kb and inferred not in new_facts:
...                     new_facts.add(inferred)
...                     print(f"[Iter {iteration}] Inferred: {inferred}({', '.join(inferred[1:])}) using {subst}")
...                     if inferred == query:
...                         print(f"\nSUCCESS: Query {query}({', '.join(query[1:])}) has been proven!")
...                         return True
...         if not new_facts:
...             print(f"\nFAILURE: Query {query}({', '.join(query[1:])}) cannot be proven.")
...             return False
...         kb.update(new_facts)
...         iteration += 1
... 
... # --- Knowledge Base Setup ---
... # Representation: ('Predicate', 'arg1', 'arg2', ...)
... # Variables start with lowercase; Constants start with uppercase.
... 
... initial_facts = {
...     ('American', 'Robert'),
...     ('Enemy', 'CountryA', 'America'),
...     ('Owns', 'CountryA', 'T1'),
...     ('Missile', 'T1')
... }
... 
... # Rules: ( [list_of_premises], conclusion )
... rules = [
...     ([('American', 'x'), ('Weapon', 'y'), ('Sells', 'x', 'y', 'z'), ('Hostile', 'z')], ('Criminal', 'x')),
...     ([('Missile', 'x'), ('Owns', 'CountryA', 'x')], ('Sells', 'Robert', 'x', 'CountryA')),
...     ([('Missile', 'x')], ('Weapon', 'x')),
...     ([('Enemy', 'x', 'America')], ('Hostile', 'x'))
... ]
... 
... query = ('Criminal', 'Robert')
... 
... # Run Forward Reasoning
... if __name__ == "__main__":
