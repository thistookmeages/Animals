from kitkat import KitKat
from doggo  import Doggo

if __name__ == "__main__":
    goldcrnchkitkat: KitKat = KitKat('persian', 'golden', 'Mittens', 5)
    wasabikitkat: KitKat = KitKat('balinese', 'green', 'sarah', 3)
    buddy: Doggo = Doggo('Labrador Retriever','chocolate', 'Buddy', 3, 87.5)

    goldcrnchkitkat.live()
    buddy.woof()
    goldcrnchkitkat.meow()
    buddy.live()