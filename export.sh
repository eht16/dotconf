#!/usr/bin/zsh


for file in $(ls -A user/)
do
	cp -r "user/${file}" ~/
done
