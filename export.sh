#!/usr/bin/zsh

git pull

for file in $(ls -A user/)
do
	cp -r "user/${file}" ~/
done
