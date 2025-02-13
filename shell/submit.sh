#!/bin/zsh

cd $1  # sets the working dir 
source /Users/tizianocausin/anaconda3/etc/profile.d/conda.sh 
conda activate devtools_scicomp
python -m pip install pytest
mkdir -p src/pyclassify/ scripts test shell experiments
touch src/pyclassify/__init__.py src/pyclassify/utils.py scripts/run.py shell/sumbit.sbatch experiments/config.yaml test/test_.py
touch pyproject.toml
python -m pip freeze > requirements.txt 

pyproj="
[project]
\nname = \"pyclassify\"
\nversion = \"0.0.1\"
\ndescription = \"Tiziano's project\"
\nreadme = \"README.md\"
\nrequires-python = \">=3.9\"
\nlicense = { file = \"LICENSE\" }
\nauthors = [{ name = \"Tiziano Causin\", email = \"causintiziano@gmail.com\" }]
\ndynamic = [\"dependencies\"]

\n[tool.setuptools.packages.find]
\nwhere = [\"src\"]
\nexclude = [\"scripts\", \"tests\", \"shell\", \"experiments\"]

\n[tool.setuptools.dynamic]
\ndependencies = { file = [\"requirements.txt\"] }

\n[project.optional-dependencies]
\ntest = [\"pytest\"]
"
echo -e $pyproj > pyproject.toml

# copying the .gitignore file in every dir
for dir in $(ls -d */);
do 
    cp .gitignore $dir
done
git add . 
git commit -m "project skeleton"
git push origin HEAD:main
