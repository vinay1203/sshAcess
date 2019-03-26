key=$1
user=$2
host=$3

keyContent=`cat "$key"`
echo $key
echo $keyContent
ssh $3 "mkdir /home/$user/.ssh"
ssh $3 "echo $keyContent >> /home/$user/.ssh/authorized_keys"
