.include "/home/sireesha/Desktop/assembly_code/m328Pdef.inc"

ldi r16,high(RAMEND)
OUT SPH,r16
ldi r16,low(RAMEND)
OUT SPL,r16

ldi r16,0b11111000  ;identifying input pins 8,9,10
OUT DDRB,r16

ldi r17,0b11100000  ;identifying output pins 5,6,7
OUT DDRD,r17

ldi r27, 0b00000101 ;clk
out TCCR0B, r27

loopw:
IN r16,PINB
ldi r18,0b00000001
ldi r19,0b00000001
ldi r20,0b00000001

and r18,r16         ;r18=X
lsr r16
and r19,r16         ;r19=B
lsr r16
and r20,r16         ;r20=A

ldi r21,0b00000001
eor r21,r18         ;r21=X'
ldi r22,0b00000001
eor r22,r19         ;r22=B'
ldi r23,0b00000001
eor r23,r20         ;r23=A'

mov r0,r23         ;r0=A'
and r0,r19          ;r0=A'B
and r0,r21          ;r0=A'BX'
 
mov r1,r20         ;r1=A
and r1,r22          ;r1=AB'
and r1,r21          ;r1=AB'X'
or r0,r1              ;r0=A'BX'+AB'X' (P)

mov r2,r20         ;r2=A
and r2,r22          ;r2=AB'
mov r3,r18         ;r3=X
or r2,r3              ;r2=AB'+ X (Q)

mov r4,r20         ;r4=A
and r4,r19          ;r4=AB
and r4,r18          ;r4=ABX (Y)

;for clk
sbi DDRB,5
ldi r24,0b01000000
call DELAY
cbi DDRB,5
ldi r24,0b01000000
call DELAY

mov r17,r0
lsl r17
or r17,r2
lsl r17
or r17,r4
lsl r17
lsl r17
lsl r17
lsl r17
lsl r17

OUT PORTD,r17

DELAY:
loop:
in r16, TIFR0
ldi r17,0b00000010
and r16,r17        ;Check if timer overflow (given 0x02 which mask for compare)
breq DELAY      ;If not, keep checking
out TIFR0, r17
dec r24
brne loop
ret

start:
rjmp start


