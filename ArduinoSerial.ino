int fortRead = A0; // A0 is a physical pin on the board
int readValue; // Declare a variable to store the in-coming data
// float voltage; //

void setup() 
{
  pinMode(fortRead, INPUT); // set up pin A0 to be an 'INPUT' pin
  Serial.begin(9600); // open the serial port,
  // and set the serial communication port to be 9600 bits/s
}

void loop() 
{
readValue = analogRead(fortRead);
Serial.println(readValue);
}
