#include <AccelStepper.h>
#include <MultiStepper.h>
#include <math.h>
#include <stdlib.h>
#define pi 3.14159265
#define Enable 8
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
float X,Y,R,X0,Y0;
int x_home, y_home;
int dong_co;
String python;
int Re=10 ; //7x7 Re=10 5x5 Re=15
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
stepperX.setCurrentPosition(0);    
stepperY.setCurrentPosition(0);
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
//void Mode_Control(){
//  if (S1_state==1){dau_X();}
//  else {circle();}
//  }
void Move(float x, float y)
{
  float l2 = 340; // The first arm
  float l3 = 160; // The second arm
  float l01 = 150;
  float l02 = 180;


  float A;
  float B;
  double c2,s2,t2,c1,s1,t1;

  A = x-l01;
  B = y+l02;
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
  
//      while (Serial.available())    //whatever the data that is coming in serially and assigning the value to the variable “data”
//{ 
//    python = Serial.readStringUntil('\n');
//    dong_co=python.toInt();
//}
//
//if (python=="100"){
//    S1_state=0;
//    python="0";
//    vi_tri=0;
//  }
//if (python=="200"){
//    S1_state=1;
//    python="0";
//    vi_tri=0;
//  }

  Serial.print("Nhập j đó đi ông cháu ơi!!! ");
  //number = getval();
  while(Serial.available()==0){};
  dong_co = Serial.parseInt();
  Serial.println(dong_co); 
 // dong_co=number;  
  if(dong_co==20) //caro
  {
    
    int total;
    int x_o;
    int turn = 0;
    int target; // vị trí 
    int tar_x;  // vị trí ngang
    int tar_y;  // vị trí dọc
    
    Serial.println("Chọn X hoặc O: ");
    while(Serial.available()==0){};
    x_o = Serial.parseInt();
    
    Serial.println("Nhập số ô : ");
    while(Serial.available()==0){}; 
    total = Serial.parseInt();
    Serial.println(total);
    
    while (turn < total)
    {
        Serial.println("nhập ô tiếp theo:");
        while(Serial.available()==0){};
        target= Serial.parseInt();
        tar_x=target%10;
        tar_y=(target-tar_x)/10;//target%10; //chia lấy dư
        tar_x=-300/sqrt(total)/2+tar_x*300/sqrt(total); //total là tổng số ô
        tar_y=-300/sqrt(total)/2+tar_y*300/sqrt(total);
  //tar_x y là tọa độ
        Serial.println(" ");
        // đánh X hoặc O
        if (x_o%2==0)
        { //Move(0,0);
//          delay(1000);
//          Serial.println("O");
          Move(tar_x+Re,tar_y);
           circle(tar_x,tar_y);
//          delay(1000); //đánh O
        } else if (x_o%2==1)
        { //Move(0,500);
//          delay(1000);
//          Serial.println("X");
          Move(tar_x-10,tar_y-10);   //7x7
//          Move(tar_x-20,tar_y-20);     //3x3
          dau_X(tar_x,tar_y);
//          delay(1000); //đánh x
        }
     //   Move(-100,-100);
        //turn=turn+1;
    }
  }

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
    if (dong_co == 50)
    { 
     Serial.println("Nhập tọa độ X: ");
     while(Serial.available()==0){};
     delay(500);
     X = Serial.parseInt();
     Serial.println(X);
     Serial.println("Nhập tọa độ Y: ");
    while(Serial.available()==0){};
     delay(500);
     Y = Serial.parseInt();
     Serial.println(Y);
     Move(X,Y);}
     
     
//   if (dong_co == 100)
//    { 
//     Serial.println("Nhập tọa độ X1: ");
//     while(Serial.available()==0){};
//     delay(1000);
//       X0 = Serial.parseInt();
//     Serial.println(X0);
//     Serial.println("Nhập tọa độ Y1: ");
//     while(Serial.available()==0){};
//     delay(1000);
//     Y0 = Serial.parseInt();
//     Serial.println(Y);
//    Move(X0,Y0); 
//    }
        if (dong_co == 96) // set home
    { 
    Move(150,150);
    dong_co=0;
    
  }
        if (dong_co == 95) //set vi tri ban dau
    { 
    Move(850,-300);
    
  }

  /* 
  if*/
  
  


}
