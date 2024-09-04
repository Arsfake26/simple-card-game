#dilakukan agar fungsi pengacakan dapat dijalankan
import random

#membuat class untuk objek kartu
class Card(object):
    #konstruktor objek dari class Card
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    
    #implementasi built-in methods sehingga card object dapat dibaca dan dikonstruksi lagi
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()
    
    #mengganti value beberapa kartu menjadi nama
    def show(self):
        if self.value == 1:
            val = 'Ace'
        elif self.value == 11:
            val = 'Jack'
        elif self.value == 12:
            val = 'Queen'
        elif self.value == 13:
            val = 'King'
        else:
            val = self.value

        return ("{} {}".format(val, self.suit))

#membuat class untuk penempatan objek kartu
class Deck(object):
    #konstruktor objek dari class Deck
    def __init__(self):
        self.cards = []
        self.build()


    # Generate 52 kartu dengan cara stacking
    def build(self):
        self.cards = []
        for suit in ['Heart', 'Club', 'Diamond', 'Spade']:
            for val in range(1,14):
                self.cards.append(Card(suit, val))

    # Shuffle deck
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            #shuffle menggunakan algoritma Fisher-Yates
            for i in range(length-1, 0, -1):
                r = random.randint(0, i)
                if i == r:
                    continue
                self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    # Pop kartu teratas dari deck 
    def deal(self):
        return self.cards.pop()




  
    

#membuat class untuk pemain
class Player(object):
    #konstruktor objek dari class Player
    def __init__(self, name, urutan):
        self.name = name
        self.hand = []
        self.urutan = urutan

    

    # Draw n kartu dari deck
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            #stack kartu dari deck ke tangan pemain
            if card:
                self.hand.append(card)
            else: 
                return False
        return True

    # Display kartu di tangan pemain
    def showHand(self):
        print ("{}'s hand: {}".format(self.name, self.hand))
        return self


#memasukkan nama pemain
print("What's your name player 1?")
nama1 = input()
player1 = Player(str(nama1), 1)
print("")
print("What's your name player 2?")
nama2 = input()
player2 = Player(str(nama2), 2)

#memasukkan pemain ke dalam array list
List = [player1,player2]
print("")

#membuat deck
myDeck = Deck()

#mengacak deck
myDeck.shuffle()

#menentukan jumlah kartu awal di tangan
while 1:
    print("Tentukan jumlah kartu awal di tangan")
    starting = input()
    if starting =="0":
        print("")
        print("(--')")
        print("You can't play card games without any cards, but if you insist...")
        continue
    else:
        break
print("")
print("Jumlah kartu awal di tangan :",int(starting))
print("")


print("'GLHF' -{}".format(player1.name))
print("")
print("'GLHF' -{}".format(player2.name))
print("")
#men-stack tangan pemain dengan kartu dari deck
player1.draw(myDeck, int(starting))
player1.showHand()
player2.draw(myDeck, int(starting))
player2.showHand()

#menentukan sisa pemain
sisa = 2

#mengambil kartu teratas dari deck sebagai patokan awal permainan
awal = myDeck.deal()
print("")
print("")
print('First Card : {} {} '.format(awal.value, awal.suit))

#membuat array kosong tempat kartu dikeluarkan
playzone = []


#membuat array kosong tempat kartu dibandingkan
compareCard = []

#permainan diakhiri
game = True

#bila belum ada pemenang
while sisa > 1:
    for Player in List:
        
        #mengecek apabila pemain masih memiliki kartu di tangan
        if len(Player.hand) == 0:
            continue
        
        #Fungsi khusus pemain yang mendapat giliran pertama dan bukan awal permainan
        if Player == List[0] and not game:
            while 1:
                print("{}'s turn".format(Player.name))
                print("")
                print("Card(s) on the playzone: ")
                
                #menampilkan kartu di playzone
                for cards in playzone:
                    print(cards[0].value, cards[0].suit)
                print("")
                print("make your choice")
                
                #membuat pilihan untuk pemain
                for index, cards in enumerate(Player.hand):
                    print("{}. {} {}".format(index + 1, cards.value, cards.suit))
                print ("")
                
                #memasukkan pilihan
                choice = input()
                
                #apabila memilih 0, pesan akan keluar mengatakan kalau pemain tidak bisa draw kartu
                if choice == "0":
                    print("You can't draw cards from the deck! You must choose a card to be put into the playzone!")
                    continue
                
                #pilihan akan ditempatkan ke playzone
                else:
                    break
        #fungsi untuk pemain
        else:
            while 1:
                print("{}'s turn".format(Player.name))
                print("Card(s) on the playzone: ")
                
                #menampilkan kartu di playzone
                for cards in playzone:
                    print(cards[0].value, cards[0].suit)
                print("")
                print("make your choice")
                
                #membuat pilihan untuk pemain
                for index, cards in enumerate(Player.hand):
                    print("{}. {} {}".format(index + 1, cards.value, cards.suit))
                print ("0. Draw from the deck")
                print ("")
                choice = input()
                
                #apabila memilih 0, maka pemain akan draw kartu dari deck lalu melanjutkan gilirannya
                if choice == '0':
                    cards = myDeck.cards.pop()
                    Player.hand.append(cards)
                    continue
                
                #apabila jenis kartu tidak sesuai, pemain akan diminta untuk mengulangi pilihannya
                if Player.hand[int(choice) - 1].suit != awal.suit:
                    print("Invalid card, you must put a card with the same suit as the card on the playzone")
                    continue
                
                #pilihan akan ditempatkan ke playzone
                else:
                    break
        print ("")
        print ("")
        
        #pilihan pemain disederhanakan fungsinya
        pilihan = Player.hand[int(choice) - 1]
        print ("{} has been chosen".format(pilihan))
        
        #jika mendapat giliran pertama dan bukan awal permainan, pilihan pemain akan menjadi kartu awal
        if Player == List[0] and not game:
            awal = pilihan 
        
        #playzone akan mengambil kartu pilihan pemain dari tangannya
        playzone.append([pilihan, Player])

        #menghapus kartu pilihan pemain dari tangannya
        Player.hand.remove(pilihan)

        #jika tangan pemain telah kosong, maka pemain tersebut dideklarasikan sebagai pemenang
        if len(Player.hand) == 0:
            print("")
            print(" {} has 0 cards in their hand, {} win!".format(Player.name, Player.name))

            print("")
            print("")
            sisa = sisa - 1
        
        #jika tidak kosong, maka lanjut ke pembandingan
        else:
            compareCard.append([pilihan, Player])
        
        #jika sisa pemain dalam list tinggal 1, array list akan dihancurkan/dihentikan
        if sisa == 1:
            break
    
    #jika sisa pemain tinggal 1, loop dihentikan
    if sisa == 1:
        break
    
    #array pembanding kartu disederhanakan
    compare = compareCard[0]
    print ("Card(s) on the playzone: ")
    
    #menampilkan kartu di playzone
    for cards in playzone:
        print(cards[0].value, cards[0].suit)
    
    #membandingkan nilai kartu, kartu terbesar di array playzone akan dimasukkan ke array compareCard
    for cards in compareCard:
        if cards[0].value > compare[0].value:
            compare = cards
    
    #menampilkan kartu dengan nilai terbesar
    print("Biggest card value: {} {}".format(compare[0].value, compare[0].suit))
    
    #menampilkan pemain yang berikutnya akan mendapat giliran pertama pada ronde berikutnya
    print("Next turn: {}".format(compare[1].name))
    
    #array compare disederhanakan
    firstPlayer = compare[1]
    print("")
    
    #menentukan pemain yang akan mendapat giliran pertama pada ronde berikutnya
    if len(List) == 2:
        if firstPlayer.urutan == 1:
            List.clear()
            List = [player1, player2]
        if firstPlayer.urutan == 2:
            List.clear()
            List = [player2, player1]
    
    #permainan tetap berjalan
    game = False
    
    #membersihkan tempat array untuk menaruh kartu di playzone
    playzone.clear()

    #membersihkan tempat array untuk membandingkan nilai kartu
    compareCard.clear()


