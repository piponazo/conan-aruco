#include <aruco/marker.h>

#include <iostream>
#include <cstdlib>

int main(int argc, char **argv)
{
    aruco::Marker marker1(1);

    std::vector<cv::Point2f> corners {{0.f, 0.}, {0.f, 1.}, {1.f, 0.}, {1.f, 1.}};
    aruco::Marker marker2(corners, 2);

    std::cout << "Marker without corners : isValid()?: " << marker1.isValid() << "\n";
    std::cout << "Marker with corners : isValid()?: " << marker2.isValid() << "\n";

    std::cout << "Application ran correctly\n";

    return EXIT_SUCCESS;
}
