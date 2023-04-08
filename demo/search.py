import csv
import heapq
from argparse import ArgumentParser
from pathlib import Path

from tqdm import tqdm

from mondegreen_distance import distance, is_hiragana


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('db_path', type=Path, help='辞書(csvファイル)のパス')
    parser.add_argument('n_words', type=int, nargs='?', default=30,
                        help='出力件数 (デフォルト値: 30)')
    parser.add_argument('same_first_n_vowels', type=int, nargs='?', default=0,
                        help='先頭何拍で韻を踏むことを強制するか (デフォルト値: 0)')
    parser.add_argument('same_last_n_vowels', type=int, nargs='?', default=0,
                        help='末尾何拍で韻を踏むことを強制するか (デフォルト値: 0)')
    parser.add_argument('same_first_n_moras', type=int, nargs='?', default=0,
                        help='先頭何拍が一致することを強制するか (デフォルト値: 0)')
    parser.add_argument('same_last_n_moras', type=int, nargs='?', default=0,
                        help='末尾何拍が一致することを強制するか (デフォルト値: 0)')
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    db_path = args.db_path  # type: Path
    assert db_path.exists(), f'{db_path} does not exist'

    n_words = args.n_words
    same_first_n_vowels = args.same_first_n_vowels
    same_last_n_vowels = args.same_last_n_vowels
    same_first_n_moras = args.same_first_n_moras
    same_last_n_moras = args.same_last_n_moras

    print(f'上位{n_words}件を表示')
    print('条件')
    print(f'  先頭{same_first_n_vowels}拍は必ず韻を踏む')
    print(f'  末尾{same_last_n_vowels}拍は必ず韻を踏む')
    print(f'  先頭{same_first_n_moras}拍は必ず一致する')
    print(f'  末尾{same_last_n_moras}拍は必ず一致する')

    with db_path.open('r', encoding='utf-8') as file:
        db = list(csv.reader(file))

    while True:
        print('Input: ', end='')
        target = input()
        if not all(is_hiragana(c) for c in target):
            print('Input string must be in hiragana')
            continue

        pq = []  # type: list[tuple[float, str]]
        for word in tqdm(db):
            _, jp_name, _, pronunciation = word
            cost = distance(
                pronunciation,
                target,
                same_first_n_vowels=same_first_n_vowels,
                same_last_n_vowels=same_last_n_vowels,
                same_first_n_moras=same_first_n_moras,
                same_last_n_moras=same_last_n_moras,
            )
            if len(pq) < n_words:
                heapq.heappush(pq, (-cost, jp_name))
            else:
                heapq.heappushpop(pq, (-cost, jp_name))
        pq.sort(key=lambda x: -x[0])

        for neg_cost, jp_name in pq:
            cost = -neg_cost
            print(f'{jp_name}: cost {cost:.3f}')
        print()


if __name__ == '__main__':
    main()
