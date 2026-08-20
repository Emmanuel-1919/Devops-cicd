# Runbook — DevOps CI/CD


Bitácora de comandos manuales, para convertir después en pipeline.


#         Instalacion (herramientas de troubleshooting)

## herramientas de troubleshooting

  find <ruta> -name "<patrón>"       # localizar archivos mal ubicados o duplicados
  ls -la <ruta>                       # confirmar existencia/tamaño de archivos
  wc -l <archivo>                     # confirmar que un archivo no está vacío
  grep -A 1 "<patrón>" <archivo>       # buscar una línea específica dentro de un archivo
  cat ~/devops-cicd/runbook.md
  rm
  mkdir
  mv
  clean

 HABILITAR EXTENCIONES EN VISUAL STUDIO CODE VIA TERMINAL

  code --install-extension ms-azuretools.vscode-docker
  code --install-extension ms-kubernetes-tools.vscode-kubernetes-tools
  code --install-extension ms-python.python
  code --install-extension vscjava.vscode-java-pack

 CREAR ARCHIVOS VIA TERMINAL (VISUAL STUDIO CODE)

  mkdir -p ~/devops-cicd/app-python/tests
  mkdir -p ~/devops-cicd/app-java-maven/src/main/java/com/example/demo
  mkdir -p ~/devops-cicd/app-java-maven/src/main/resources
  mkdir -p ~/devops-cicd/app-java-maven/src/test/java/com/example/demo
  mkdir -p ~/devops-cicd/app-java-gradle/src/main/java/com/example/demo
  mkdir -p ~/devops-cicd/app-java-gradle/src/main/resources
  mkdir -p ~/devops-cicd/app-java-gradle/src/test/java/com/example/demo
  touch ~/devops-cicd/runbook.md

 PATH BINARIO

  hash -r
  which code


## Comandos de Instalacion (Diagnostico, Fase 0)

 sw_vers ; uname -m                                      
 xcode-select -p
 brew --version
 git --version
 python3 --version ; pip3 --version
 java -version ; echo $JAVA_HOME
 mvn -version
 gradle -version
 docker --version ; docker compose version
 kubectl version --client
 kind --version
   
 # HOMEBREW

  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  echo >> /Users/qualtop/.zprofile
  echo 'eval "$(/opt/homebrew/bin/brew shellenv zsh)"' >> /Users/qualtop/.zprofile
  eval "$(/opt/homebrew/bin/brew shellenv zsh)"

  brew --version
  which brew

  brew install git

  git --version
  which git

 # GIT

  hash -r
  which git
  git --version
  
  git config --global user.name "Tu Nombre"
  git config --global user.email "tu-correo@ejemplo.com"
  git config --global init.defaultBranch main

  git config --global --list

  cd ~
  git clone git@github.com:octocat/Hello-World.git
  cd Hello-World
  ls -la
  cd ~
  rm -rf Hello-World



 # PYTHON VIA HOMEBREW
 
  brew install python3

  AMBIENTE VIRTUAL (BLOQUE)

  cd ~
  python3 -m venv prueba
  source prueba/bin/activate
  which python3
  which pip3
  pip3 install requests

  deactivate
  rm -rf ~/prueba
  which python3
  
  AMBIENTE VIRTUAL (BLOQUE)

 # JAVA JDK 21 (JAVA DEVELOPER KIT) VIA HOMEBREW 
  
  brew install openjdk@21

  sudo ln -sfn /opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-21.jdk
  echo 'export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"' >> ~/.zshrc
  source ~/.zshrc

  echo 'export JAVA_HOME="/opt/homebrew/opt/openjdk@21"' >> ~/.zshrc
  source ~/.zshrc

  hash -r
  java -version
  echo $JAVA_HOME
  which java

 # MAVEN VIA HOMEBREW

  brew install maven
  
  sudo ln -sfn /opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-21.jdk
  echo 'export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"' >> ~/.zshrc
  source ~/.zshrc

  echo 'export JAVA_HOME="/opt/homebrew/opt/openjdk@21"' >> ~/.zshrc
  source ~/.zshrc

  hash -r
  java -version
  echo $JAVA_HOME
  which java

 # GRADLE VIA HOMEBREW
 
  brew install gradle
  hash -r
  gradle -version
  
 # Python

 cd ~/devops-cicd/app-python
 python3 -m venv venv
 source venv/bin/activate
 pip3 install -r requirements-dev.txt
 pytest
 python3 app.py

 # KIND Y KUBECTL (KUBERNETES IN DOCKER) VIA HOMBREW  
 
  brew install kind kubectl
  hash -r
  kind --version
  which kubectl
  kubectl version --client

✅ Xcode CLT
✅ Homebrew
✅ Git (2.55.0)
✅ Python 3 (3.14.6) + venv
✅ Java JDK 21 + JAVA_HOME
✅ Maven (3.9.16)
✅ Gradle (9.7.0)
✅ Docker Desktop (4 CPU / 12 GB / 80 GB)
✅ kind (0.32.0) + kubectl (1.36.3, vía Homebrew)

WRAPPER DE MAVEN Y GRADLE 

 cd ~/devops-cicd/app-java-maven
 mvn -N wrapper:wrapper -Dmaven=3.9.9

 cd ~/devops-cicd/app-java-gradle 
 gradle wrapper --gradle-version 8.10
  
COMANDOS PARA CORRER Y PROBAR CADA APP LOCAL SIN CONTENEDOR

  PYTHON

  cd ~/devops-cicd/app-python : No pone en la ruta donde vamos a ejcutar los demas comandos

  python3 -m venv venv : Crea un ambiente virtual aislado para no tocar otras dependencias

  source venv/bin/activate : Modifica las variables de entorno en tu sesion actual de SHELL

  pip3 install -r requirements-dev.txt : 

  pytest : corre pruebas automatizadas ya declaradas 

  python3 app.py : comando que arranca en en el servidor FLASK en modo desarrollo

  ABRE http://localhost:8080 
  TERMINAL CTRL*C

  MAVEN

  cd ~/devops-cicd/app-java-maven
  ./mvnw test
  ./mvnw spring-boot:run

  ABRE http://localhost:8080 
  TERMINAL CTRL*C

  GRADLE

  cd ~/devops-cicd/app-java-gradle
  ./gradlew test
  ./gradlew bootRun

  ABRE http://localhost:8080 
  TERMINAL CTRL*C
 





## Maven

 cd ~/devops-cicd/app-java-maven
 ./mvnw clean package
 java -jar target/app-java-maven.jar

  java -jar target/app-java-maven.jar : es un archivo crudo que aun no puede ser autosucificente, es la base para que se proceda el siguente comando 

 ./mvnw clean package : limpia el camino y empaqueta para que pueda estar en un servidor temporal 

## Gradle

 cd ~/devops-cicd/app-java-gradle
 ./gradlew clean build
 java -jar build/libs/app-java-gradle.jar

 cd ~/devops-cicd/app-java-gradle : 

 ./gradlew clean build : hace una limpieza para despejar cualquier comando annterior

 ls -la build/libs/ : hace una lectura de carpetas en donde indicamos si existe esa carpeta 
 

 
#        Dockerfiles y Construccion (Bloque 2)

  docker ps
  docker run hello-world

  docker run -p 8080:8080 (host:contenedor)

 ## Python

 cd ~/devops-cicd/app-python
 docker build -t app-python:dev .
 docker run -d -p 8080:8080 --name app-python-dev app-python:dev
 docker logs app-python-dev
 docker stop app-python-dev
 docker rm app-python-dev

 ## Maven

 cd ~/devops-cicd/app-java-maven
 docker build -t app-java-maven:dev .
 docker run -d -p 8081:8080 --name app-java-maven-dev app-java-maven:dev
 docker logs app-java-maven-dev
 docker ps
 docker stop app-java-maven-dev
 docker rm app-java-maven-dev

 ## Gradle

 cd ~/devops-cicd/app-java-gradle
 docker build -t app-java-gradle:dev .
 docker run -d -p 8082:8080 --name app-java-gradle-dev app-java-gradle:dev
 docker logs app-java-gradle-dev
 docker stop app-java-gradle-dev
 docker rm app-java-gradle-dev
  
