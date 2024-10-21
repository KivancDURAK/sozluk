meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "COOL": " Havalı olan bişey veya kimse",
            "ROFL": "Bir şakaya karşılık cevap",
            "SHEESH": "Onaylamak",
            "CPEEPY": "Korkunç",
            "AGGRO": "Sinirlenmek"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print(word,"kelimesi arşivlerimizde bulunmuyor")
