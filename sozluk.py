meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "TAMTAM":"haberleşmek için kullanılan tabir",
            "GG":"İyi oyundu",
            "AFK":"Klavye başından uzak",
            "BRUH":"ŞAŞIRMA EFEKTİ",
            "SUS":"Şüpheli",
            "POV":"Bakış açısı"
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

while(word):
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Bir hata oldu lütfen başka bir tane deneyin")
