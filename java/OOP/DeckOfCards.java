interface identifyCard {
    public void getCardName();
}

public class DeckOfCards {
    public static DeckOfCards getCards(String type) {
        if (type == "Diamonds") {
            return new Diamonds();
        }
        return null;
    }

    public static void main(String[] args) {
        Diamonds cards = (Diamonds) DeckOfCards.getCards("Diamonds");
        cards.getCardName();
    }
}

class Diamonds extends DeckOfCards implements identifyCard {
    private String name = "A diamond card";

    @Override
    public void getCardName() {
        System.out.println(name);
    }

}
// public class Diamonds extends DeckOfCards {
    
// }
// public class Diamonds extends DeckOfCards {
    
// }
// public class Diamonds extends DeckOfCards {
    
// }