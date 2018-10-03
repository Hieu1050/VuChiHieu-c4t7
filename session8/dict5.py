#15
words = {
    "banana": '''Chuối- là tên gọi các loài cây thuộc chi Musa;
     trái của nó là trái cây được ăn rộng rãi nhất. 
     Những cây này có gốc từ vùng nhiệt đới ở Đông Nam Á và Úc. 
     Ngày nay, nó được trồng khắp vùng nhiệt đới. Chuối được trồng ở ít nhất 107 quốc gia.''',
    "apple": "táo",
    "pineapple":"dứa",
}
search = input("what?   ")
search = search.lower()
while search not in words:
    choice = input ("want to add your new word?Yes (1) or No (0)")
    if choice == '0':
        search = input("WHAT?   ")
        search = search.lower()
    else : 
        term = input ("enter term   ")
        meaning = input ("enter definition  ")
        words[term] = meaning
        print ("new word added")
    print (words[search])