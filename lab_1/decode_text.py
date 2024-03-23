import copy

text = ""
with open("cod9.txt", 'r') as f:
    text = f.read()
src_text = copy.copy(text)
print(text)
symbols_count = {}
for symb in text:
    if symb in symbols_count.keys():
        symbols_count[symb] += 1
    else:
        symbols_count[symb] = 1

print(symbols_count)
freqs = {}
with open("freqs.txt", 'r', encoding='utf-8') as f:
    for row in f.readlines():
        row = row.split(' ')
        freqs[row[0]] = row[2]
freqs[' '] = freqs['пробел']
del freqs['пробел']
symbols_sorted_cod = symbols_count.keys()
symbols_sorted_cod = sorted(symbols_sorted_cod, key=lambda k: symbols_count[k])
freqs_sorted = freqs.keys()
freqs_sorted = sorted(freqs_sorted, key=lambda k: freqs[k])
decode_dict = dict(zip(symbols_sorted_cod, freqs_sorted))
print(decode_dict)
for i in range(0, len(symbols_sorted_cod)):
    text = text.replace(symbols_sorted_cod[i], freqs_sorted[i])
print(text)


def correct_decode_dict(phrase, correct_phrase, text):
    global decode_dict
    ind = text.find(phrase)
    print(ind)
    analog = src_text[ind:ind + len(phrase)]
    for i in range(0, len(analog)):
        decode_dict[analog[i]] = correct_phrase[i]


# Очевидно, что """АДМИСИТНРАНИВСЗМИ МЕРАМИ""" это """административными мерами""", найдем индекс вхождения этой подстроки в текст:
key_word = "АДМИНИСТРАТИВНЫМИ МЕРАМИ"
ind = text.find("АДМИСИТНРАНИВСЗМИ МЕРАМИ")
print(ind)
analog = src_text[ind:ind + len("АДМИСИТНРАНИВСЗМИ МЕРАМИ")]
for i in range(0, len(analog)):
    decode_dict[analog[i]] = key_word[i]
new_text = copy.copy(src_text)
for i in range(0, len(new_text)):
    new_text = new_text.replace(src_text[i], decode_dict[src_text[i]])
print(new_text)
key_word = """ПОТОРЫЕ ВОКНИПАХТ ЛРИ ЛЕРЕДАГЕ ИНЙОРМАШИИ ЛО СЕТЫМ"""
correct_decode_dict("""ПОТОРЫЕ ВОКНИПАХТ ЛРИ ЛЕРЕДАГЕ ИНЙОРМАШИИ ЛО СЕТЫМ""",
                    """КОТОРЫЕ ВОЗНИКАЮТ ПРИ ПЕРЕДАЧЕ ИНФОРМАЦИИ ПО СЕТЯМ""", new_text)
new_text = copy.copy(src_text)
for i in range(0, len(new_text)):
    new_text = new_text.replace(src_text[i], decode_dict[src_text[i]])
print()
print(new_text)

correct_decode_dict(
    """ЗА НЕСКОЯУКО ПОСЯЕДНИЧ ДЕСЯТИЯЕТИЖ ТРЕЬОВАНИЯ К ИНФОРМАЦИОННОЖ ЬЕЗОПАСНОСТИ СФЮЕСТВЕННО ИЗМЕНИЯИСУ""",
    """ЗА НЕСКОЛЬКО ПОСЛЕДНИХ ДЕСЯТИЛЕТИЙ ТРЕБОВАНИЯ К ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ СУЩЕСТВЕННО ИЗМЕНИЛИСЬ""", new_text)
correct_decode_dict(
    """ЦИРОКОБО""",
    """ШИРОКОГО""", new_text)
correct_decode_dict(
    """ЪТАП""",
    """ЭТАП""", new_text)
correct_decode_dict(
    """ТАКЭЕ""",
    """ТАКЖЕ""", new_text)
new_text = copy.copy(src_text)
for i in range(0, len(new_text)):
    new_text = new_text.replace(src_text[i], decode_dict[src_text[i]])
print()
print(new_text)
print(decode_dict)
for key in decode_dict.keys():
    if decode_dict[key] in freqs.keys():
        del freqs[decode_dict[key]]
print(freqs)