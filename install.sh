# make dir
mkdir ~/.mpu
# copy all files
cp * ~/.mpu -r
# aliases
#cat .bashrc >> ~/.bashrc
#cat .bash_profile >> ~/.bash_profile
echo "alias mpu=\"python3 ~/.mpu/src/main.py\"" >> ~/.bashrc
echo "export PATH=$PATH:~/.mpu/packages/usr/bin" >> ~/.bashrc
# important directories and files
mkdir ~/.mpu/packages
mkdir ~/.mpu/log
touch ~/.mpu/world
# reload bash
exec bash
