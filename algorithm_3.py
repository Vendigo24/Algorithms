import remove_unreachable_symbols


def remove_useless_symbols(old_grammar):
    not_empty, grammar = old_grammar.is_empty()
    return remove_unreachable_symbols.algorithm(grammar) if not_empty else None
