#!/bin/bash

# Change to the directory manage.py is defined
cd `dirname "$0"`
echo `pwd`
cd ../azine

if [[ ! -e "manage.py" ]]
then
	echo "Could not find manage.py. Script will be stopped"
	exit 1
fi


if [[ -z $1 ]]
then
	echo "Command List"
	echo "------------"
	echo "Choose one of the following commands:" 
	echo
	echo "migration -> creates migration definitions"
	echo "fixture -> Creates a fixture of the current database"
	echo "migrate -> executes migration"
	echo "load -> loads the dumps into the database"
	echo
	read command
else
	command=$1
fi

migration ()
{
	echo "Start migration"
        ./manage.py schemamigration azine_main --auto
}

fixture ()
{
	echo "Create fixture"
	./manage.py dumpdata cms --indent=2 > ./fixtures/cms.json
	./manage.py dumpdata cms text --indent=2 > ./fixtures/cms-text.json
	./manage.py dumpdata auth --indent=2 > ./fixtures/auth.json
	./manage.py dumpdata azine_main --indent=2 > ./fixtures/azine_main.json
}

migrate ()
{
	echo "Start to migrate"
	./manage.py migrate azine_main
}

load ()
{
	echo "Start to load"
	./manage.py flush
	dumps=`ls ./fixtures`
	for dump in $dumps
	do
		./manage.py loaddata ./fixtures/$dump
	done
}




case "$command" in
	"migration")
		migration;;
	"fixture")
		fixture;;
	"migrate")
		migrate;;
	"load")
		load;;
esac

exit