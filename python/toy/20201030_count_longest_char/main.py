import random


#
# string型を引数として文字と文字数を返却
# 同じ長さの文字が出てきた場合は、最初の文字のみを返却
#
def search_longest_char(target):
    longest_char_count = 0
    longest_char = ""
    current_char_count = 0
    current_char = ""

    # 型例外
    if type(target) is not str:
        raise Exception("type of args is only str.")

    for c in target:
        # 次の文字が何かによって処理を変える

        if current_char != c:
            # 1文字目の場合 (新しい文字となった場合)

            # current_char ... c に変更
            # count ... 1文字目にリセット
            current_char = c
            current_char_count = 1
        else:
            # 2文字目以降の場合 (同じ文字列が継続した場合)

            # current_char .. 変更しない
            # current_char_count ... カウントアップ
            current_char_count += 1

        # longest_charと比較して、より大きい値を上書き
        # 同じ場合は無視
        if longest_char_count < current_char_count:
            longest_char = current_char
            longest_char_count = current_char_count

    return (longest_char, longest_char_count)


def print_longest_char(input_string):
    longest_char, longest_char_count = search_longest_char(input_string)

    print(input_string, ":", longest_char, "x", longest_char_count)


#
# 数値を引数として、abcのいずれかのの文字を使って引数分の文字数を持つ文字列を作成
# 数値以外が文字列の場合は、Exceptionを返却
#
def make_random_string(num):

    if type(num) is not int:
        raise Exception("call with non int args. args must be int.")

    source = "abc"
    return "".join(random.choices(source, k=num))


for i in range(10):
    print_longest_char(make_random_string(10))

# str型以外を引数に指定
print_longest_char(100)
print_longest_char(Exception())
print_longest_char(1.0)
print_longest_char(u"aaaabbcc")
