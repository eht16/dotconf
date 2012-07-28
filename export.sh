#!/usr/bin/zsh

cd $(dirname $0)


git pull

for file in $(ls -A user/)
do
	cp -r "user/${file}" ~/
done
