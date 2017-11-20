#include <mega128.h> 
#include <delay.h>
#include <stdlib.h> //실수형을 문자형으로 바꾸기 위한 헤더파일  



float adc_read(unsigned char ch){
  int ADC_I;
  float ADC_F;
  
  ADMUX=ch;   // 채널 지정 ,외부단자 AREF 사용  
  ADCSRA=0b11000111; //프리런닝  0b11100111 , 단일변환 0b11000111; 분주비 128
  while(!(ADCSRA&(1<<ADIF))); //프리러닝모드에서 ADC가 완료되면 자동으로 비트가 1셋 되기때문에 
  //완료 될대 까지 WHILE문 실행
  delay_us(100);
  ADC_I=ADCW;//ADCH +ADCL을 한 레지스터 
  ADC_F=(float)ADC_I * 5.0/1023.0;
  return ADC_F;
}
void putch_usart1(char data) //한문자만 출력
{
  while(!(UCSR1A & (1<<UDRE1))); //UDRE0 이 1이 되면  WHILE문을 빠져나옴 (데이터를 보낼 준비가 되면)

  UDR1 = data;
}
void puts_usart1(char *str)  //문자열 출력함수  
{
   while(*str!=0)
   {
     putch_usart1(*str);
     str++;
   }
}
void main(void){
  char   ch=0;    //ADC 채널
  float f[8]; //ADC 값이 저장될 장소  
  char str_0[];
  char str_1[];
  

  DDRF=0x00;

  
  UCSR1A = 0x00;
  UCSR1B = 0b10011000; //bit 6 :수신 완료 인터럽트 허가
  UCSR1C = 0b10000110; // 8 데이터 비트 설정   ,패리티 비트 사용하지 않음   P
  UBRR1H=0;
  UBRR1L=8; //115200 bps    jmod bt-1 블루투스 스펙임 
  SREG=0x80;
  
  

  
  delay_ms(300);
  
  //그래서 PORTD.0=1 (5V)를 줘서 가변저항으로 돌림 
  

  
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
