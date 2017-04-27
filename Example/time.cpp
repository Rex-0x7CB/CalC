#include<iostream>
#include<unistd.h>

int main()
{
    int time = 5;
    std::cout<<"Enter the number of seconds : "<<std::endl;
    std::cin>>time;
    std::cout<<"Waiting for "<<time<<" seconds"<<std::endl;
    sleep(time);
}
