#!/bin/bash
CURRENT_DATETIME=$(date +%F_%H-%M-%S)

echo '======================================================='
BUILDED_FILES_DIR='shopping_manager__'$CURRENT_DATETIME
echo 'Start build in '$CURRENT_DATETIME' ...'
echo 'Out package name: '$BUILDED_FILES_DIR

echo 'Start build frontend...'
cd frontend

source ~/.nvm/nvm.sh

rm -rf app/static

nvm use 
# yarn run build

echo 'Frontend build success!'

cd ../

echo 'Start make package...'

echo 'Start create directories...'

OUT_DIR_BASE=.builds
if [ -d "$OUT_DIR_BASE" ];
then
    echo "$OUT_DIR_BASE directory exists."
else
	echo "$OUT_DIR_BASE directory does not exist. create dir"
    mkdir $OUT_DIR_BASE
fi



OUT_DIR=$OUT_DIR_BASE/$BUILDED_FILES_DIR

mkdir $OUT_DIR

echo 'Directories created success!'

echo 'Start copy files...'

cp -R .etc $OUT_DIR/.etc
cp -R app $OUT_DIR/app
cp alembic.ini $OUT_DIR/alembic.ini
cp docker-compose.yml $OUT_DIR/docker-compose.yml
cp Makefile $OUT_DIR/Makefile
cp manage.py $OUT_DIR/manage.py
cp pyproject.toml $OUT_DIR/pyproject.toml
cp pytest.ini $OUT_DIR/pytest.ini
cp README.md $OUT_DIR/README.md
cp requirements.txt $OUT_DIR/requirements.txt
cp settings.py $OUT_DIR/settings.py
cp setup.cfg $OUT_DIR/setup.cfg

echo 'Files copied!'

echo 'Clear build directory...'

find $OUT_DIR -name '*.pyc' -delete
find $OUT_DIR -type d -name "__pycache__" -delete

echo 'Build directory cleaned!'

echo 'compress build directory...'

cd $OUT_DIR_BASE

zip -r $BUILDED_FILES_DIR.zip $BUILDED_FILES_DIR

rm -rf $BUILDED_FILES_DIR

cd ../

echo 'Compress success!'

echo 'Build success!'