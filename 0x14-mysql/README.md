0x14-mysql

# SSH into web-01 server
ssh ubuntu@web-01

# Update package lists
sudo apt update

# Install MySQL Server 5.7.x
sudo apt install mysql-server-5.7

# Once installed, check MySQL version
mysql --version

# Repeat the same process for web-02 server
ssh ubuntu@web-02
sudo apt update
sudo apt install mysql-server-5.7
mysql --version
