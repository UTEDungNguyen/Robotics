#include <AccelStepper.h>
#include <MultiStepper.h>
#include <math.h>
#include <stdlib.h>
#define pi 3.14159265
#define Enable 8
unsigned int mang2[3]={-100,0,100};
unsigned int mang1[3]={210,310,410};
AccelStepper stepperX(1, 2, 5);//Set up chân cho động cơ X(dưới đáy, u=11)
AccelStepper stepperY(1, 3, 6);//Set up chân cho động cơ Y(cánh tay, u=2)
AccelStepper stepperZ(1, 4, 7);//Set up chân cho động cơ Y(cánh tay, u=2)
int Steps;
int Steps_X;
int Steps_Y;
int do_dai;
int theta_1;
int theta_2;
int S = 44;
float X,Y,R,X1,Y1;
int x_home, y_home;
int dong_co;
String python;
int Re=20 ;
unsigned char S1_state=1;
int vi_tri=0;

int number=0; // valuid...

void setup() {
  Serial.begin(9600);
  pinMode(2,OUTPUT); //int dirX = 5 ;  int stepX = 2 ;
  pinMode(5,OUTPUT);

  pinMode(3,OUTPUT);
  pinMode(6,OUTPUT);

   pinMode(4,OUTPUT);  
   pinMode(7,OUTPUT);
  pinMode(Enable,OUTPUT); //#define Enable 8

  stepperY.setMaxSpeed(4500);//Không biết lun
  stepperY.setSpeed(1000*S);//Tốc độ quay nhanh chậm
  stepperY.setAcceleration(3000);//Gia tốc mong muốn step/s (tính theo bước trên giây trên giây)

  stepperX.setMaxSpeed(1000);
  stepperX.setSpeed(500);  stepperX.setAcceleration(200);

   stepperZ.setMaxSpeed(4000);
   stepperZ.setSpeed(900);
   stepperZ.setAcceleration(3000);

  //stepperY.setPinsInverted(3);  //Sets the inversion for stepper driver pins
  digitalWrite(Enable, LOW);//Low là cho phép động cơ hoạt động
    

    stepperZ.setCurrentPosition(0);
    

}
void TrucZ (float z)
{    stepperZ.setCurrentPosition(0);    
     do_dai= z;
     Serial.println(do_dai);
     Steps = do_dai*200*2*2/2;
     stepperZ.moveTo(Steps);
     while(stepperZ.distanceToGo()!=0)
    {
       stepperZ.run();
     }
    
   
  }
void dau_X(float X1, float Y1){
  TrucZ(30);
  delay(1);  
      for (float t = 0; t < (2*pi+0.03*5); t = t+0.03)
    { 
     // X = X1 + Re*cos(t);                       //X = p*50 + 40*cos(t);
     // Y = Y1 +  Re*sin(t); 
      X = X1 + 3*(t)-10;                      //7x7
      Y = Y1 +  3*(t)-10; 
//      X = X1 + 6*(t)-20;                        //3x3
//      Y = Y1 +  6*(t)-20; 
      //  Y = p*50 + 40*sin(t);
      Move(X,Y);
    }
    TrucZ(-30);
    delay(1);
    Move(X1-10,Y1-10+19.3);  //9.65   //7x7
//    Move(X1-20,Y1-20+38.6);    //3x3
    TrucZ(30);
    delay(1);
      for (float t = 0; t < (2*pi+0.03*5); t = t+0.03)
    { 
     // X = X1 + Re*cos(t);                       //X = p*50 + 40*cos(t);
     // Y = Y1 +  Re*sin(t); 
      X = X1 + 3*(t)-10;                     //7x7
      Y = Y1 -  3*(t)+9.3;  //-0.35
//      X = X1 + 6*(t)-20;                       //3x3
//      Y = Y1 -  6*(t)+18.6;  //-0.35
      //  Y = p*50 + 40*sin(t);
      Move(X,Y);
    }
    TrucZ(-30);
    delay(1);    
    Move(850,-300);
    python="0";
    vi_tri=0;
       delay(500);
  }
void circle(float X1, float Y1){
     TrucZ(30);
     delay(1);
       for (int p = 1; p < 2; p++)// vị trí
    {
      for (float t = 0; t < (2*pi+0.03*5); t = t+0.03)
    { 
      X = X1 + Re*cos(t);                       //X = p*50 + 40*cos(t);
      Y = Y1 + Re*sin(t); 
      //X = 0 + 5*(t);                       //X = p*50 + 40*cos(t);
      //Y = 350 +  5*(t); 
      //  Y = p*50 + 40*sin(t);
      Move(X,Y);

    }
    delay(1);
    TrucZ(-30);
    Move(850,-300);
    python="0";
    vi_tri=0;
       delay(500);
    }  
  }
void Mode_Control(float X1, float Y1){
  circle(X1,Y1);
  }
void Move(float x, float y)
{
  float l2 = 340; // The first arm
  float l3 = 160; // The second arm
  float l01 = 160;
  float l02 = 170;


  float A;
  float B;
  double c2,s2,t2,c1,s1,t1;

  A = x;
  B = y;
  c2 = (pow(A,2) + pow(B,2) - pow(l2,2) - pow(l3,2))/(2*l2*l3);
  s2 = sqrt(abs(1 - pow(c2,2)));
  t2 = atan2(s2,c2)*180/pi;
  s1 = B*(l3*c2  + l2) - A*(l3*s2);
  c1 = A*(l3*c2 + l2) + B*(l3*s2);
  t1 = atan2(s1,c1)*180/pi;
  Serial.println(t1);
  Serial.println(t2);
  Steps_X = (t1)*4*20/9;         // số xung (t1)*20*2*2/3; theta_2*2*2*2*20/9;       theta_1*4*20*2*2/3;
  stepperX.moveTo(1*Steps_X);
  Steps_Y = (t2)*2*2*20/9;          //(t2)*2*2*20/9;
  stepperY.moveTo(1*Steps_Y);
  while((stepperX.distanceToGo()!=0) || (stepperY.distanceToGo()!=0))
  {
    stepperY.run();
   // delayMicroseconds(1);
    stepperX.run();
  //  delayMicroseconds(1);
  }
}
void loop() {
  
      while (Serial.available())    //whatever the data that is coming in serially and assigning the value to the variable “data”
{ 
    python = Serial.readStringUntil('\n');
    vi_tri=python.toInt();
}

 if (python=="1001"){
    X1= -100; //-100
    Y1= 210; //190;
    Move(X1+20,Y1);
    circle(X1,Y1);
  }
  if (python=="1003"){
    X1= mang2[2]; //100
    Y1= mang1[0]; //210
    Move(X1+20,Y1);
    circle(X1,Y1);
  }
  if (python=="1007"){
    X1= -100; //-100
    Y1= mang1[2]; //410
    Move(X1+20,Y1);
    circle(X1,Y1);
  }
  if (python=="1009"){
    X1= mang2[2]; // 100
    Y1= mang1[2]; //410
    Move(X1+20,Y1);
    circle(X1,Y1);
  }
  if (python=="2001"){
    X1= -100; //-100
    Y1= 210; //190;
    Move(X1-10,Y1-10);
    dau_X(X1,Y1);
  }
  if (python=="2003"){
    X1= mang2[2]; //100
    Y1= mang1[0]; //210
    Move(X1-10,Y1-10);
    dau_X(X1,Y1);
  }
  if (python=="2007"){
    X1= -100; //-100
    Y1= mang1[2]; //410
    Move(X1-10,Y1-10);
    dau_X(X1,Y1);
  }
  if (python=="2009"){
   X1= mang2[2]; // 100
    Y1= mang1[2]; //410
    Move(X1-10,Y1-10);
    dau_X(X1,Y1);
  }

//  Serial.print("Nhập j đó đi ông cháu ơi!!! ");
////  number = getval();
//  while(Serial.available()==0){};
//  dong_co = Serial.parseInt();
//  Serial.println(dong_co); 
//  // dong_co=number;  


  if (dong_co == 90)
  { 
    Serial.println("Nhập số vị trí góc : ");
    while(Serial.available()==0){};
    delay(2000);
    theta_1 = Serial.parseInt();
    Serial.println(theta_1);
    Steps = theta_1*4*20/9; 
    stepperX.moveTo(1*Steps);
    while(stepperX.distanceToGo()!=0)
    {
      stepperX.run();
    }
  }
  

  if (dong_co == 91)
    { 
      Serial.println("Nhập số góc cần quay: ");
      while(Serial.available()==0){};
      delay(2000);  
      theta_2 = Serial.parseInt();
      Serial.println(theta_2);
      Steps = theta_2*2*2*20/9;
      
      stepperY.moveTo(1*Steps);
      Serial.println(theta_2*2*2*20/9);
      while(stepperY.distanceToGo()!=0)
      {
        stepperY.run();
      }  
    }
   if (dong_co == 92)
   { 
     stepperZ.setCurrentPosition(0);
     Serial.println("Nhập số mm cần di chuyển: ");
     while(Serial.available()==0){};
     do_dai= Serial.parseInt();
     Serial.println(do_dai);
     Steps = do_dai*200*2*2/2;
     stepperZ.moveTo(Steps);
     while(stepperZ.distanceToGo()!=0)
    {
       stepperZ.run();
     }
    
   }
   if (dong_co == 93)
  { 

    Serial.println("Nhập góc quay cho X: ");
    while(Serial.available()==0){};
    delay(2000);
    theta_1= Serial.parseInt();
    Serial.println(theta_1);
    Serial.println("Nhập góc quay cho Y: ");
    while(Serial.available()==0){};
    delay(2000);
    theta_2= Serial.parseInt();
    Serial.println(theta_2);
    
    Steps_X = theta_1*20*2*2/3; 
    stepperX.moveTo(-1*Steps_X);
    Steps_Y = theta_2*2*2*2*20/9;
    stepperY.moveTo(-1*Steps_Y);
    

    while((stepperX.distanceToGo()!=0)||(stepperY.distanceToGo()!=0))
    {
      stepperX.run();
      delayMicroseconds(10);
      stepperY.run();
      delayMicroseconds(10);
    }
    
  }


  // test move stepmotor
  if (vi_tri == 1)     // python == "9"
    { 
    X1= -100; //-100
    Y1= 210; //190;
    Move(X1+20,Y1);
    Mode_Control(X1,Y1) ;
  }
    if (vi_tri == 2) //01 python == "1"
    { 
    X1= mang2[1]; //0
    Y1= 210; //190 //210
    Move(X1+20,Y1);
   Mode_Control(X1,Y1) ;     
  }
      if (vi_tri == 4)//10 python == "2"
    { 
    X1= -100; // -100
    Y1= mang1[1]; //  310
    Move(X1+20,Y1);
   Mode_Control(X1,Y1) ;     
  }
       if (vi_tri == 5)  //11 python == "3"
    { 
    X1= mang2[1]; //0 
    Y1= mang1[1]; //310
    Move(X1+20,Y1);
    Mode_Control(X1,Y1) ;
  }
       if (vi_tri == 7) //02 python == "4"
    { 
    X1= -100; //-100
    Y1= mang1[2]; //410
    Move(X1+20,Y1);
    Mode_Control(X1,Y1) ;     
  }
       if (vi_tri == 8) //12 python == "5"
    { 
    X1= mang2[1]; //0
    Y1= 410; //390 //410
    Move(X1+20,Y1);
    Mode_Control(X1,Y1) ;      
  }
       if (vi_tri == 9) //22 python == "6"
    { 
    X1= mang2[2]; // 100
    Y1= mang1[2]; //410
    Move(X1+20,Y1);
    Mode_Control(X1,Y1) ;    
  }
       if (vi_tri == 3) //20 python == "7"
    { 
    X1= mang2[2]; //100
    Y1= mang1[0]; //210
    Move(X1+20,Y1);
    Mode_Control(X1,Y1) ;  
  }
       if (vi_tri == 6) //21 python == "8"
    { 
    X1= mang2[2]; //100
    Y1= mang1[1];  //410
    Move(X1+20,Y1);
    Mode_Control(X1,Y1) ; 
  }
    if (python == "S")
    { 
//     Serial.println("Nhập tọa độ X: ");
//     while(Serial.available()==0){};
//     delay(500);
     X = 0;
//     Serial.println(X);
//     Serial.println("Nhập tọa độ Y: ");
//     while(Serial.available()==0){};
//     delay(500);
     Y = 310;
//     Serial.println(Y);
     Move(X,Y);}
     
     
   if (dong_co == 100)
    { 
     Serial.println("Nhập tọa độ X1: ");
     while(Serial.available()==0){};
     delay(1000);
       X1 = Serial.parseInt();
     Serial.println(X1);
     Serial.println("Nhập tọa độ Y1: ");
     while(Serial.available()==0){};
     delay(1000);
     Y1 = Serial.parseInt();
     Serial.println(Y1);
     Serial.println("Nhập ban kinh : ");
     while(Serial.available()==0){};
     delay(1000);
     R = Serial.parseInt();
     Serial.println(R);
    TrucZ(-20);
    Move(X1,Y1);
    TrucZ(30);
   
    for (int p = 1; p < 2; p++)// vị trí
    {
      for (float t = 0; t < (2*pi+0.03*5); t = t+0.03)
    { 
      //X = X1 + R*cos(t);                       //X = p*50 + 40*cos(t);
      //Y = Y1 +  R*sin(t); 
      X = X1 + R*(t);                       //X = p*50 + 40*cos(t);
      Y = Y1 +  R*(t); 
      //  Y = p*50 + 40*sin(t);
      Move(X,Y);

    }
    TrucZ(-10);
    Move(0,0);
       delay(500);
    } 
    
    
    }
        if (dong_co == 11) //21 python == "8"
    { 
    X1= mang2[2]; //100
    Y1= mang1[1];  //290
    TrucZ(-20);
    Move(X1-30,Y1-30);
    TrucZ(30);
    
  }

  /* Set vi tri home
  if*/
  
  


}
