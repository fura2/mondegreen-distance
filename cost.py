import math
from typing import List, Optional

import numpy as np

from japanese import (MORAS, VOWELS, hiragana_to_mora, is_affiricate,
                      is_consonant, is_fricative, is_lateral, is_nasal,
                      is_obstruent, is_plosive, is_semivowel,
                      is_special_mora, is_voiced, is_vowel)

VOWEL_COST_MATRIX = {c1: {c2: 0.0 for c2 in VOWELS} for c1 in VOWELS}
VOWEL_COST_MATRIX['a']['i'] = VOWEL_COST_MATRIX['i']['a'] = 71 / (2 * 73)
VOWEL_COST_MATRIX['a']['u'] = VOWEL_COST_MATRIX['u']['a'] = 51 / (2 * 73)
VOWEL_COST_MATRIX['a']['e'] = VOWEL_COST_MATRIX['e']['a'] = 39 / (2 * 73)
VOWEL_COST_MATRIX['a']['o'] = VOWEL_COST_MATRIX['o']['a'] = 37 / (2 * 73)
VOWEL_COST_MATRIX['i']['u'] = VOWEL_COST_MATRIX['u']['i'] = 55 / (2 * 73)
VOWEL_COST_MATRIX['i']['e'] = VOWEL_COST_MATRIX['e']['i'] = 32 / (2 * 73)
VOWEL_COST_MATRIX['i']['o'] = VOWEL_COST_MATRIX['o']['i'] = 73 / (2 * 73)
VOWEL_COST_MATRIX['u']['e'] = VOWEL_COST_MATRIX['e']['u'] = 44 / (2 * 73)
VOWEL_COST_MATRIX['u']['o'] = VOWEL_COST_MATRIX['o']['u'] = 26 / (2 * 73)
VOWEL_COST_MATRIX['e']['o'] = VOWEL_COST_MATRIX['o']['e'] = 51 / (2 * 73)
# check symmetricity
assert all(VOWEL_COST_MATRIX[c1][c2] == VOWEL_COST_MATRIX[c2][c1]
           for c1 in VOWELS for c2 in VOWELS)


def compute_consonant_cost(cons1: str, cons2: str) -> float:
    '''
    Compute replacing cost between two consonants
    Assume that both cons1 and cons2 are consonants
    0.0 <= cost <= 0.4
    '''
    if cons1 == cons2:
        return 0.0

    cost = 0.2
    if is_voiced(cons1) != is_voiced(cons2):
        cost += 0.2
    if is_nasal(cons1) != is_nasal(cons2):
        cost += 0.2
    if is_lateral(cons1) != is_lateral(cons2):
        cost += 0.2

    ob1 = is_obstruent(cons1)
    ob2 = is_obstruent(cons2)
    if ob1 != ob2:
        cost += 0.2
    elif ob1 and ob2:
        def get_index(cons: str) -> int:
            if is_plosive(cons):
                return 0
            if is_affiricate(cons):
                return 1
            if is_fricative(cons):
                return 2
            raise RuntimeError(f'Unexpected consonant: {cons}')

        cost += [
            [0.0, 0.1, 0.2],
            [0.1, 0.0, 0.1],
            [0.2, 0.1, 0.0],
        ][get_index(cons1)][get_index(cons2)]

    return 0.4 * cost


def compute_mora_cost(mora1: str, mora2: str) -> float:
    '''
    Compute replacing cost between two moras
    Assume that both mora1 and mora2 are moras
    0.0 <= cost <= 1.0
    '''
    sp1 = is_special_mora(mora1)
    sp2 = is_special_mora(mora2)
    if sp1 != sp2:
        return 1.0  # TODO: decrease replacing cost between 'N' and (voiced or nasal)
    if sp1 and sp2:
        return 0.0 if mora1 == mora2 else 1.0

    # both mora1 and mora2 are not special moras
    def get_vowel(mora: str) -> str:
        return mora[-1]

    def get_semivowel(mora: str) -> Optional[str]:
        if len(mora) == 1:
            return None
        return mora[-2] if is_semivowel(mora[-2]) else None

    def get_consonant(mora: str) -> Optional[str]:
        return mora[0] if is_consonant(mora[0]) else None

    cost = 0.0
    # 0 <= vowel cost <= 0.5
    vowel1 = get_vowel(mora1)
    vowel2 = get_vowel(mora2)
    cost += VOWEL_COST_MATRIX[vowel1][vowel2]
    # 0 <= semivowel cost <= 0.1
    semivowel1 = get_semivowel(mora1)
    semivowel2 = get_semivowel(mora2)
    cost += 0.0 if semivowel1 == semivowel2 else 0.1
    # 0 <= consonant cost <= 0.4
    consonant1 = get_consonant(mora1)
    consonant2 = get_consonant(mora2)
    if consonant1 is None or consonant2 is None:
        if consonant1 != consonant2:
            cost += 0.4
    else:
        cost += compute_consonant_cost(consonant1, consonant2)
    return cost


# precompute replacing cost matrix to improve performance
COST_MATRIX = {
    mora1: {
        mora2: compute_mora_cost(mora1, mora2)
        for mora2 in MORAS
    }
    for mora1 in MORAS
}
# check symmetricity
assert all(COST_MATRIX[mora1][mora2] == COST_MATRIX[mora2][mora1]
           for mora1 in MORAS for mora2 in MORAS)

# 字余りのコスト
COST_DELETE = dict.fromkeys(MORAS, 5.0)
COST_DELETE['N'] = 0.5
COST_DELETE['Q'] = 0.3

# 字足らずのコスト
COST_INSERT = 20.0


def replace_Hs(moras: List[str]) -> List[str]:
    '''
    Replace every 'H' (長音) with previous vowel

    Examples
    ['zye', 'i', 'su'] -> ['e', 'i', 'u']
    ['ka', 'H', 'N'] -> ['a', 'a', 'N']
    '''
    result = []
    for mora in moras:
        if mora == 'H':
            assert is_vowel(result[-1][-1])
            result.append(result[-1][-1])
        else:
            result.append(mora)
    return result


def extract_vowels(moras: List[str]) -> List[str]:
    '''
    Convert moras to vowels
    - leave special moras as they are

    Examples
    ['zye', 'i', 'su'] -> ['e', 'i', 'u']
    ['ni', 'Q', 'sa'] -> ['i', 'Q', 'a']
    ['ka', 'H', 'N'] -> ['a', 'H', 'N']
    '''
    vowels = []
    for mora in moras:
        if is_vowel(mora[-1]):
            vowels.append(mora[-1])
        elif is_special_mora(mora):
            vowels.append(mora)
        else:
            raise RuntimeError(f'Unexpected input: {mora} of {moras}')
    return vowels


def distance(
    s1: str,
    s2: str,
    *,
    same_first_n_vowels: int = 0,
    same_last_n_vowels: int = 0,
    same_first_n_moras: int = 0,
    same_last_n_moras: int = 0,
    # deficient_moras: int = 0,
    # excess_moras: int = 0,
) -> float:
    '''
    A Levenshtein-based cost function:
        Minimum total cost of edits required to change s1 into s2
    NOTE: This may NOT satisfy the triangle inequality
    '''

    s1 = replace_Hs(hiragana_to_mora(s1))
    s2 = replace_Hs(hiragana_to_mora(s2))
    v1 = extract_vowels(s1)
    v2 = extract_vowels(s2)

    n1 = len(s1)
    n2 = len(s2)
    dp = np.zeros((n1 + 1, n2 + 1), dtype=float)
    for i in range(n1):
        dp[i + 1, 0] = dp[i, 0] + COST_DELETE[s1[i]]
    for j in range(n2):
        dp[0, j + 1] = dp[0, j] + COST_INSERT
    for i in range(n1):
        cost_delete = COST_DELETE[s1[i]]
        for j in range(n2):
            if (j < same_first_n_moras or n2 - j <= same_last_n_moras) and s1[i] != s2[j]:
                cost_insert = math.inf
                cost_replace = math.inf
            elif (j < same_first_n_vowels or n2 - j <= same_last_n_vowels) and v1[i] != v2[j]:
                cost_insert = math.inf
                cost_replace = math.inf
            else:
                cost_insert = COST_INSERT
                cost_replace = COST_MATRIX[s1[i]][s2[j]]
            dp[i + 1, j + 1] = min(
                dp[i, j + 1] + cost_delete,
                dp[i + 1, j] + cost_insert,
                dp[i, j] + cost_replace,
            )
    return dp[n1, n2]
