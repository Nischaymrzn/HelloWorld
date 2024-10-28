def second_largest(lst):
    return sorted(set(lst))[-2] if len(set(lst)) > 1 else None
