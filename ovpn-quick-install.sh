#!/bin/bash
#A startup script to install ovpn and easy-rsa and then generate baseline keys (server and client)
#by Ross James
#More in depth instructions can be found on the OpenVPN website at 
#https://openvpn.net/index.php/open-source/documentation/howto.html


#Define vars
install_list=("openvpn easy-rsa")

#### Functions
#Move the default directory and generate all neccesary keys  
key_install()
{
  echo "---->Copying the default Easy-RSA location to /etc/openvpn/" # Moving so future updates don't step on any customizations
  if [ -d "/etc/openvpn/easy-rsa/2.*" ]; then
    mkdir /etc/openvpn/easy-rsa
    cp -rf /usr/share/easy-rsa/2.0/* /etc/openvpn/easy-rsa
    cd /etc/openvpn/easy-rsa/2.0/
  else
    mkdir /etc/openvpn/easy-rsa
    cp -rf /usr/share/easy-rsa/* /etc/openvpn/easy-rsa
    cd /etc/openvpn/easy-rsa/
  fi
  echo "---->Generating CA, Server Key, Client Key, Diffe-Helman Parameters, Tls-auth key"
  source ./vars
  ./clean-all
  ./build-ca
  ./build-key-server server
  ./build-key client
  ./build-dh
  openvpn --genkey --secret ta.key
}

#Check for sudo 
if [ "$EUID" -ne "0" ] ; then
	echo "Please run with sudo"
	exit
else
  echo "Determining Package Manager (apt-get or yum)"
fi

#Check for apt-get, if not assume yum
if apt-get -qq update && apt-get -qq upgrade ; then
  echo "---->Using apt-get!"
  for i in $install_list; do 
    if dpkg -l | grep $i; then
      echo "---->$i is already installed!"
    else
      echo "---->Installing $i"
      apt-get -qq install $i > /dev/null
    fi
  done


elif yum -q -y update; then 
  echo "---->Using yum!"
  for i in $install_list; do 
    if rpm -qa | grep -qw $i ; then
      echo "---->$i is already installed!"
    else
      echo "---->Installing $i"    
      yum -q -y install $i > /dev/null
    fi
  done

else echo "Your system must have apt-get or yum for this script to work."
fi
key_install