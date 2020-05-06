#!/usr/bin/zsh

CWD=$(dirname $0)
cd $CWD


function confirm() {
	# test if 1 (stdout) is an open fd (which is not when piping or output redirection)
	if [ ! -t 1 ]; then
		echo "Running non-interactively as no output was detected"
		return
	fi

	read -r -q "response?${1:-Are you sure? [y/N]}?"
	echo
	if [ "${response}" = "y" ];
	then
		true
	else
		false
	fi
}


# we need you, ZSH
if [ -z "$ZSH_VERSION" ]; then
	echo "This script needs to be executed in ZSH!"
	exit 1
fi


# start the party
git pull
for file in $(find user -type f -printf '%P ')
do
	old_file="${HOME}/${file}"
	new_file="${CWD}/user/${file}"

	# get the diff
	file_diff="$(diff -Naur "${old_file}" "${new_file}")"
	if [ "${file_diff}" ]; then
		echo "File ${new_file} has changed:\n${file_diff}"
		# copy file only if confirmed by user
		if confirm "Do you want to replace it? [y/N]"; then
			old_file_dirname="$(dirname "${old_file}")"
			# create target directory if it doesn't exist yet
			if [ ! -d "${old_file_dirname}" ]; then
				mkdir -p "${old_file_dirname}"
			fi
			cp "${new_file}" "${old_file}"
			echo "${new_file} replaced with new version"
		fi
	fi
done
