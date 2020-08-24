#include <iostream>
#include <time.h>
#include <algorithm>

class Warrior
{
private:
    std::string name;
    int health;
    int attackPower;
    int defensePower;

public:
    Warrior(): name(""), health(0), attackPower(0), defensePower(0) {}
    Warrior(std::string name, int health, int attackPower, int defensePower): name(name), health(health), attackPower(attackPower), defensePower(defensePower) {}

    std::string GetName();
    bool Attack(Warrior& other);
    
    ~Warrior() {}
};

std::string Warrior::GetName() {
    return this->name;
}

bool Warrior::Attack(Warrior& other) {
    other.health -= this->attackPower + other.defensePower;
    other.health = std::max(other.health, 0);
    
    std::cout << this->name << " attacks " << other.name << " and deals " << this->attackPower << " damage\n";
    std::cout << other.name << " is down to " << other.health << " health\n";
    
    if (other.health == 0)
        return true;
    return false;
}


class Battle
{
public:
    Battle() {}
    
    static void StartFight(Warrior& player1, Warrior& player2);
    
    ~Battle() {}
};


void Battle::StartFight(Warrior& player1, Warrior& player2) {
    Warrior winner;
    Warrior loser;
    
    while (1) {
        if (player1.Attack(player2)) {
            winner = player1;
            loser = player2;
            break;
        }
        if (player2.Attack(player1)) {
            winner = player2;
            loser = player1;
            break;
        }
    }
    
    std::cout << loser.GetName() << " has died and " << winner.GetName() << " is victorious\n";
    std::cout << "Game Over\n";
}






int main()
{
    srand(time(0));
    Warrior thor("Thor", 100, 30, 15);
    Warrior hulk("Hulk", 135, 25, 10);

    Battle::StartFight(thor, hulk);

}
