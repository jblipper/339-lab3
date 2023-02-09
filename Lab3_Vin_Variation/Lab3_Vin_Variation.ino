int Vout1 = A1;
int Vout2 = A0;
int Vinput = 3;
const int arraySize = 300;
int readings1[arraySize]; //The array that will hold our readings
int readings2[arraySize];

int timeBase=50; //Time between analog readings (for stability)
int readingPtr; //The array pointer that points to the current reading
void setup()
{
pinMode(Vout1, INPUT);
pinMode(Vout2, INPUT);
pinMode(Vinput, OUTPUT);
Serial.begin(9600);
}
void loop()
{
  if(Serial.available() > 0)
  {
    int out=Serial.read();
    analogWrite(Vout1, out);
    analogWrite(Vout2, out);
    //Make analog readings with delay timeBase
    for(readingPtr = 0; readingPtr < arraySize; readingPtr++)
    {
      readings1[readingPtr] = analogRead(Vout1);
      readings2[readingPtr] = analogRead(Vout2);
      
      delayMicroseconds(timeBase);
    }
      //Write array values to serial port. Note that we round our 10-bit measurements to 8-bit.
    
      //byte reading1=highByte(readings1[readingPtr]<<6);
      //byte reading2=highByte(readings2[readingPtr]<<6);
      //byte readings [2] = {reading1, reading2};
      //Serial.write(readings); //shift bits left six times and use only top eight
    for(readingPtr = 0; readingPtr < arraySize; readingPtr++) 
    {
      Serial.write(highByte(readings1[readingPtr]<<6));
      Serial.write(highByte(readings2[readingPtr]<<6));
        
    }
  }
}
