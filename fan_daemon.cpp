#include <iostream>
#include <fstream>
#include <thread>
#include <chrono>

using namespace std;

int readTemperature() {
    ifstream infile("temperature.txt");
    int temp = 25; // default
    if (infile.is_open()) {
        infile >> temp;
        infile.close();
    }
    return temp;
}

void writeFanStatus(bool on) {
    ofstream outfile("fan_status.txt");
    if (outfile.is_open()) {
        outfile << (on ? "ON" : "OFF");
        outfile.close();
    }
}

void controlFan(int temp) {
    static bool fanOn = false;
    if (temp >= 60 && !fanOn) {
        cout << "[FAN ON] Temperature: " << temp << "°C" << endl;
        fanOn = true;
        writeFanStatus(true);
    } else if (temp <= 45 && fanOn) {
        cout << "[FAN OFF] Temperature: " << temp << "°C" << endl;
        fanOn = false;
        writeFanStatus(false);
    }
}

int main() {
    cout << "Fan Daemon started..." << endl;
    while (true) {
        int temp = readTemperature();
        controlFan(temp);
        this_thread::sleep_for(chrono::seconds(5));
    }
    return 0;
}

