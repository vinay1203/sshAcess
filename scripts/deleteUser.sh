host=$1
user=$2

ssh $1 "userdel -r $2"
