#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    // Get and validate input
    float change = 0.0;
    do
    {
        printf("How much change is owed?\n");
        change = GetFloat();
    } while (change < 0);
    
    // round input to cents
    int cents = (round(change * 100));

    // calculate coins    
    int cnt_coins = 0;

    cnt_coins += (cents / 25);
    cents = cents - (cents / 25) * 25;
    
    cnt_coins += (cents / 10);
    cents = cents - (cents / 10) * 10;

    cnt_coins += (cents / 5);
    cents = cents - (cents / 5) * 5;
    
    cnt_coins += (cents / 1);
    
    // output num of coins
    printf("%i\n", cnt_coins);
    return 0;
}
