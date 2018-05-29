How to build OpenCV

https://www.learnopencv.com/install-opencv3-on-ubuntu/
sudo apt-get install libgtkglext1 libgtkglext1-dev # To get OPENGL support for GTK+

----------------

Also: https://github.com/opencv/opencv_contrib/issues/1131
Workaround: -DBUILD_opencv_xfeatures2d=OFF

Final:
cmake -DCMAKE_BUILD_TYPE=Release -DWITH_TBB=ON -DWITH_V4L=ON -DWITH_OPENGL=ON -DBUILD_EXAMPLES=ON -DBUILD_opencv_xfeatures2d=OFF ../opencv-3.4/

----------------------------------------------------------------------

For CUDA support:-
Also should do: 
    -D ENABLE_FAST_MATH=1 \
    -D CUDA_FAST_MATH=1 \
    -D WITH_CUBLAS=1 \

------------

FINAL:

cmake -DCMAKE_BUILD_TYPE=Release -DWITH_TBB=ON -DWITH_V4L=ON -DWITH_OPENGL=ON
 -DWITH_CUDA=ON -DBUILD_EXAMPLES=ON -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-3.4/modules ../opencv-3.4/


-----------

Had to also add HTTPS support to cmake for things to work properly (cmake requires HTTPS downloads)

Rebuild cmake with the following: 
sudo apt-get install libcurl4-gnutls-dev
sudo apt-get install zlib1g-dev
./bootstrap --parallel=$(nproc) --system-curl
make && sudo make install
