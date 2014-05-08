#confirm keygen.sh is in same directory as keypullpush.sh
echo "This Script will pull key from Server and apply authorized Keys to local machine."

#copies authorized keys to local machine
scp -i $HOME/.ssh/sshkey.pem user@192.168.1.2:.ssh/authorized_keys ~/.ssh

#run keygen.sh script
./keygen.sh

#copy id_rsa.pub into authorized_keys file
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

#copies local authorized_keys file to remote server
scp -i $HOME/.ssh/sshkey.pem $HOME/.ssh/authorized_keys user@192.168.1.2:.ssh/

#removes local authorized_keys
rm ~/.ssh/authorized_keys

#create authorized_keys file
vi ~/.ssh/authorized_keys
