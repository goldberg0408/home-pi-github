#include <mega128.h> 
#include <delay.h>
#include <stdlib.h> //�Ǽ����� ���������� �ٲٱ� ���� �������  



float adc_read(unsigned char ch){
  int ADC_I;
  float ADC_F;
  
  ADMUX=ch;   // ä�� ���� ,�ܺδ��� AREF ���  
  ADCSRA=0b11000111; //��������  0b11100111 , ���Ϻ�ȯ 0b11000111; ���ֺ� 128
  while(!(ADCSRA&(1<<ADIF))); //�������׸�忡�� ADC�� �Ϸ�Ǹ� �ڵ����� ��Ʈ�� 1�� �Ǳ⶧���� 
  //�Ϸ� �ɴ� ���� WHILE�� ����
  delay_us(100);
  ADC_I=ADCW;//ADCH +ADCL�� �� �������� 
  ADC_F=(float)ADC_I * 5.0/1023.0;
  return ADC_F;
}
void putch_usart1(char data) //�ѹ��ڸ� ���
{
  while(!(UCSR1A & (1<<UDRE1))); //UDRE0 �� 1�� �Ǹ�  WHILE���� �������� (�����͸� ���� �غ� �Ǹ�)

  UDR1 = data;
}
void puts_usart1(char *str)  //���ڿ� ����Լ�  
{
   while(*str!=0)
   {
     putch_usart1(*str);
     str++;
   }
}
void main(void){
  char   ch=0;    //ADC ä��
  float f[8]; //ADC ���� ����� ���  
  char str_0[];
  char str_1[];
  

  DDRF=0x00;

  
  UCSR1A = 0x00;
  UCSR1B = 0b10011000; //bit 6 :���� �Ϸ� ���ͷ�Ʈ �㰡
  UCSR1C = 0b10000110; // 8 ������ ��Ʈ ����   ,�и�Ƽ ��Ʈ ������� ����   P
  UBRR1H=0;
  UBRR1L=8; //115200 bps    jmod bt-1 ������� ������ 
  SREG=0x80;
  
  

  
  delay_ms(300);
  
  //�׷��� PORTD.0=1 (5V)�� �༭ ������������ ���� 
  

  
  while(1)
  {  
        for(ch=0; ch<8; ch++)
        {
          f[ch]=adc_read(ch);
        
        }
       //f[0]=adc_read(0);
        
     //ftoa(f[0],5,str_0); //adc0 ,pf 2

     //ftoa(f[2],5,str_1); //adc1 ,pf 1
     
 
     puts_usart1("ch=1:"); 
     putch_usart1(f[1]+'0');
     puts_usart1("ch=0:");
     putch_usart1(f[0]+'0');
     putch_usart1('V');
     puts_usart1("\r\n");
     

     
     
     delay_ms(250);

  }
}
