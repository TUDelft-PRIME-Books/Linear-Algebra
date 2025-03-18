
Write-Host "Installing dependencies..."
try{
	pip install -r requirements.txt
}
catch{
	Write-Host "An error ocurred. Make sure pip is in the PATH"
	exit -1
}

Write-Host "Installing sphinx-grasple..."
Write-Host "Downloading the package..."

git clone https://github.com/dbalague/sphinx-grasple

cd sphinx-grasple
try {
	python setup.py install
}
catch {
	Write-Host "python is not recognized... Trying python3:"
	Write-Host $_.ScriptStackTrace
}
try{
	python3 setup.py install
}
catch {
	"An error ocurred. Make sure python is installed and in the PATH"
}
finally{
	cd ..
	#rm -rf sphinx-grasple
	Write-Host 
	Write-Host "sphinx-grasple package installed"
	Write-Host "Ready!"
}
