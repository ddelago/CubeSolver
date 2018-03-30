#include <Wire.h>
#include <Adafruit_MotorShield.h>

char inchar;
//motorshield 1
Adafruit_MotorShield AFMS = Adafruit_MotorShield(0x60); 
Adafruit_StepperMotor *myMotor = AFMS.getStepper(200, 1);
Adafruit_StepperMotor *myMotor2 = AFMS.getStepper(200, 2);
//motorshield 2
Adafruit_MotorShield AFMS1 = Adafruit_MotorShield(0x61); 
Adafruit_StepperMotor *myMotor3 = AFMS1.getStepper(200, 2);
Adafruit_StepperMotor *myMotor4 = AFMS1.getStepper(200, 1);
//motorshield 3
Adafruit_MotorShield AFMS2 = Adafruit_MotorShield(0x62); 
Adafruit_StepperMotor *myMotor5 = AFMS2.getStepper(200, 2);
Adafruit_StepperMotor *myMotor6 = AFMS2.getStepper(200, 1);

void setup() {                                                                                     
  Serial.begin(9800);  
  AFMS.begin();  
  AFMS1.begin();  
  AFMS2.begin(); 
  myMotor->setSpeed(4048);
  myMotor2->setSpeed(4048); 
  myMotor3->setSpeed(4048);
  myMotor4->setSpeed(4048);  
  myMotor6->setSpeed(4048);  

}

void loop() {
  //motor mapping for soution (side note Clockwise = Backward, Counter = Forward)
  inchar = Serial.read();
  if(inchar >= 32 && inchar <= 122){
    switch(inchar){
     //R
      case 'R':
        myMotor2->step(50, BACKWARD, DOUBLE); 
        break;
      case 'r':
        myMotor2->step(50, FORWARD, DOUBLE); 
        break;
     //L
      case 'L':
        myMotor->step(50, BACKWARD, DOUBLE); 
        break;
      case 'l':
        myMotor->step(50, FORWARD, DOUBLE); 
        break;
     //F
      case 'F':
        myMotor3->step(50, BACKWARD, DOUBLE); 
        break;
      case 'f':
        myMotor3->step(50, FORWARD, DOUBLE); 
        break;
     //B
      case 'B':
        myMotor4->step(50, BACKWARD, DOUBLE); 
        break;
      case 'b':
        myMotor4->step(50, FORWARD, DOUBLE); 
        break;
     //U
      case 'U':
        myMotor5->step(50, BACKWARD, DOUBLE); 
        break;
      case 'u':
        myMotor5->step(50, FORWARD, DOUBLE); 
        break;
     //D
      case 'D':
        myMotor6->step(50, BACKWARD, DOUBLE); 
        break;
      case 'd':
        myMotor6->step(50, FORWARD, DOUBLE); 
        break;
      case 'p':
        myMotor->release(); 
        myMotor2->release();
        myMotor3->release();
        myMotor4->release();
        myMotor5->release();
        myMotor6->release();
        break;
    }
    delay(250);
    
  }

}
