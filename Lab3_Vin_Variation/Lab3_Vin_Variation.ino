int Vout1 = A1;
int Vout2 = A0;
int Vinput = 3;
int readings1[250]; //The array that will hold our readings
int readings2[250];
int timeBase=5000; //Time between analog readings (for stability)
int readingPtr; //The array pointer that points to the current reading
void setup()
{
pinMode(Vout1, OUTPUT);
pinMode(Vout2, OUTPUT);
pinMode(Vinput, INPUT);
Serial.begin(9600);
}
void loop()
{
  if(Serial.available() > 0)
  {
    int out=Serial.read();
    analogWrite(Vout1, out);
    //analogWrite(Vout2, out);
    //Make analog readings with delay timeBase
    for(readingPtr = 0; readingPtr < 500; readingPtr++)
    {
      readings1[readingPtr] = analogRead(Vinput);
      //readings2[readingPtr] = analogRead(Vout2);
      delayMicroseconds(timeBase);
    }
      //Write array values to serial port. Note that we round our 10-bit measurements to 8-bit.
    for(readingPtr = 0; readingPtr < 500; readingPtr++) 
    {
      int reading1=highByte(readings1[readingPtr]<<6);
      int reading2=highByte(readings2[readingPtr]<<6);
      int readings [2] = {reading1, reading2};
        Serial.write(readings); //shift bits left six times and use only top eight 
        //Serial.write(highByte(readings2[readingPtr]<<6));
        
    }
  }
}
