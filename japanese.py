HIRAGANAS = list(
    'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわゐゑをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽぁぃぅぇぉっゃゅょゎゔー'
)
KATAKANAS = list(
    'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヰヱヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポァィゥェォッャュョヮヴー'
)

HIRAGANA_A_ROW = list('あかさたなはまやらわがざだばぱぁゃゎ')
HIRAGANA_I_ROW = list('いきしちにひみりゐぎじぢびぴぃ')
HIRAGANA_U_ROW = list('うくすつぬふむゆるぐずづぶぷぅゅゔ')
HIRAGANA_E_ROW = list('えけせてねへめれゑげぜでべぺぇ')
HIRAGANA_O_ROW = list('おこそとのほもよろをごぞどぼぽぉょ')

# mora = consonant? semivowel? vowel | special_mora
VOWELS = ['a', 'i', 'u', 'e', 'o']  # 母音
SEMIVOWELS = ['y', 'w']  # 半母音
CONSONANTS = ['k', 's', 't', 'n', 'h', 'm', 'r', 'g', 'z',
              'd', 'b', 'p', 'c', 'f', 'v']  # 子音  NOTE: 'c' means 'ts'
SPECIAL_MORAS = ['N', 'Q', 'H']  # 特殊拍

HIRAGANA_TO_MORA = {
    # (empty), k, s, t, n, h, m, r
    'あ':     'a', 'い':    'i', 'う':     'u', 'え':     'e', 'お':     'o',
    'や':    'ya',               'ゆ':    'yu', 'いぇ':  'ye', 'よ':    'yo',
    'わ':    'wa', 'うぃ': 'wi',                'うぇ':  'we', 'うぉ':  'wo',
    'か':    'ka', 'き':   'ki', 'く':    'ku', 'け':    'ke', 'こ':    'ko',
    'きゃ': 'kya',               'きゅ': 'kyu',                'きょ': 'kyo',
    'さ':    'sa', 'すぃ': 'si', 'す':    'su', 'せ':    'se', 'そ':    'so',
    'しゃ': 'sya', 'し':  'syi', 'しゅ': 'syu', 'しぇ': 'sye', 'しょ': 'syo',
    'た':    'ta', 'てぃ': 'ti', 'とぅ':  'tu', 'て':    'te', 'と':    'to',
    'てゃ': 'tya',               'てゅ': 'tyu',                'てょ': 'tyo',
    'な':    'na', 'に':   'ni', 'ぬ':    'nu', 'ね':    'ne', 'の':    'no',
    'にゃ': 'nya',               'にゅ': 'nyu',                'にょ': 'nyo',
    'は':    'ha', 'ひ':   'hi', 'ふ':    'hu', 'へ':    'he', 'ほ':    'ho',
    'ひゃ': 'hya',               'ひゅ': 'hyu',                'ひょ': 'hyo',
    'ま':    'ma', 'み':   'mi', 'む':    'mu', 'め':    'me', 'も':    'mo',
    'みゃ': 'mya',               'みゅ': 'myu',                'みょ': 'myo',
    'ら':    'ra', 'り':   'ri', 'る':    'ru', 'れ':    're', 'ろ':    'ro',
    'りゃ': 'rya',               'りゅ': 'ryu',                'りょ': 'ryo',
    # g, z, d, b, p
    'が':    'ga', 'ぎ':   'gi', 'ぐ':    'gu', 'げ':    'ge', 'ご':    'go',
    'ぎゃ': 'gya',               'ぎゅ': 'gyu',                'ぎょ': 'gyo',
    'ざ':    'za', 'ずぃ': 'zi', 'ず':    'zu', 'ぜ':    'ze', 'ぞ':    'zo',
    'じゃ': 'zya', 'じ':  'zyi', 'じゅ': 'zyu', 'じぇ': 'zye', 'じょ': 'zyo',
    'だ':    'da', 'でぃ': 'di', 'どぅ':  'du', 'で':    'de', 'ど':    'do',
    'でゃ': 'dya',               'でゅ': 'dyu',                'でょ': 'dyo',
    'ば':    'ba', 'び':   'bi', 'ぶ':    'bu', 'べ':    'be', 'ぼ':    'bo',
    'びゃ': 'bya',               'びゅ': 'byu',                'びょ': 'byo',
    'ぱ':    'pa', 'ぴ':   'pi', 'ぷ':    'pu', 'ぺ':    'pe', 'ぽ':    'po',
    'ぴゃ': 'pya',               'ぴゅ': 'pyu',                'ぴょ': 'pyo',
    # c, f, v (not appeared in usually romans)
    'つぁ':  'ca', 'つぃ': 'ci', 'つ':    'cu', 'つぇ':  'ce', 'つぉ':  'co',
    'ちゃ': 'cya', 'ち':  'cyi', 'ちゅ': 'cyu', 'ちぇ': 'cye', 'ちょ': 'cyo',
    'ふぁ':  'fa', 'ふぃ': 'fi',                'ふぇ':  'fe', 'ふぉ':  'fo',
    'ふゃ': 'fya',               'ふゅ': 'fyu',                'ふょ': 'fyo',
    'ゔぁ':  'va', 'ゔぃ': 'vi', 'ゔ':    'vu', 'ゔぇ':  've', 'ゔぉ':  'vo',
    'ゔゃ': 'vya',               'ゔゅ': 'vyu',                'ゔょ': 'vyo',
    # special mora
    'ん':  'N',
    'っ':  'Q',
    'ー':  'H',
    # N to 1 assignment
    'ゐ':    'i', 'ゑ':     'e', 'を':     'o',
    'づぃ': 'zi', 'づ':    'zu',
    'ぢゃ': 'zya', 'ぢ':  'zyi', 'ぢゅ': 'zyu', 'ぢぇ': 'zye', 'ぢょ': 'zyo',
}

MORAS = list(HIRAGANA_TO_MORA.values())


def is_hiragana(c: str) -> bool:
    '''Whether the given character is a hiragana'''
    return c in HIRAGANAS


def is_katakana(c: str) -> bool:
    '''Whether the given character is a katakana'''
    return c in KATAKANAS


def is_vowel(c: str) -> bool:
    '''Whether the given character is a vowel (母音)'''
    return c in VOWELS


def is_semivowel(c: str) -> bool:
    '''Whether the given character is a semivowel (半母音)'''
    return c in SEMIVOWELS


def is_consonant(c: str) -> bool:
    '''Whether the given character is a consonant (子音)'''
    return c in CONSONANTS


def is_special_mora(c: str) -> bool:
    '''Whether the given character is a special mora (特殊拍)'''
    return c in SPECIAL_MORAS


def is_voiced(cons: str) -> bool:
    '''Whether the given consonant is a voiced (有声音)'''
    return cons in ['n', 'm', 'r', 'g', 'z', 'd', 'b', 'v']


def is_nasal(cons: str) -> bool:
    '''Whether the given consonant is a nasal (鼻音)'''
    return cons in ['n', 'm']


def is_lateral(cons: str) -> bool:
    '''Whether the given consonant is a lateral (側面音)'''
    return cons in ['r']


def is_obstruent(cons: str) -> bool:
    '''Whether the given consonant is an obstruent (阻害音)'''
    return is_plosive(cons) or is_affiricate(cons) or is_fricative(cons)


def is_plosive(cons: str) -> bool:
    '''Whether the given consonant is a plosive (破裂音)'''
    return cons in ['k', 't', 'g', 'd', 'b', 'p']


def is_affiricate(cons: str) -> bool:
    '''Whether the given consonant is an affiricate (破擦音)'''
    return cons in ['c']


def is_fricative(cons: str) -> bool:
    '''Whether the given consonant is a fricative (摩擦音)'''
    return cons in ['s', 'h', 'z', 'f', 'v']


def hiragana_to_mora(hiragana: str) -> list[str]:
    '''
    Convert hiragana string to moras

    Examples
    'じぇいす' -> ['zye', 'i', 'su']
    'にっさ' -> ['ni', 'Q', 'sa']
    'かーん' -> ['ka', 'H', 'N']
    '''
    moras = []
    s = hiragana
    while s != '':
        if s[:2] in HIRAGANA_TO_MORA:
            moras.append(HIRAGANA_TO_MORA[s[:2]])
            s = s[2:]
        elif s[:1] in HIRAGANA_TO_MORA:
            moras.append(HIRAGANA_TO_MORA[s[:1]])
            s = s[1:]
        elif s[0] in 'ぁぃぅぇぉゎ':  # e.g. すぅるたい
            d = dict(zip('ぁぃぅぇぉゎ', ['a', 'i', 'u', 'e', 'o', 'wa']))
            moras.append(d[s[0]])
            s = s[1:]
        else:
            raise RuntimeError(f'Unexpected input: {s} of {hiragana}')
    return moras
