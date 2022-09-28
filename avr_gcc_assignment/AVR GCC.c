#include <avr/io.h>
#include <util/delay.h>

int A, B, X, P, Q, Y;

void gpio_init(void)
{	
DDRD = 0b00111100;      //pin 5,6,7 enabled as output pins (1's) 
DDRB = 0b00100000;      //pin 13 enabled as output (1)
DDRB = 0b11111000;      //pin 8,9,10, enabled as inputs (0's)
}

void input(void){
  uint8_t in = PINB;      //digital read 
  
  in=PINB;
  if((in & 0x01)==0)
  A=0;
  else A=1;
  if((in & 0x02)==0)
  B=0;
  else B=1;
  if((in & 0x04)==0)
  X=0;
  else X=1;
}

void clock(void){
	PORTB |= ((1<<PB5));
  _delay_ms(1000);
  PORTB =((0<<PB5));
  _delay_ms(1000);
}

void  output(void){
 uint8_t  out;
 P= (!A&&B&&!X) || (A&&!B&&!X);
 Q= (A&&!B) || (X);
 Y= (A&&B&&X);
 out=(P<<7)|(Q<<6)|(Y<<5);
 PORTD=out;
}

int main (void)
{
 gpio_init();
  while(1){
    input();
    output();
    clock();
  }
  return 0;
}
