import os, platform

#root permission needed

#list of packages that i like and don't come with most debian-based distributions
#will not remove packages that the os use, so this brakes nothing

def appsPurge():
    apps= [ 'thunderbird',
            'thunderbird-gnome-support',
            'thunderbird-locale-en',
            'thunderbird-locale-en-us',
            'rhythmbox',
            'rhythmbox-data',
            'rhythmbox-plugin-tray-icon',
            'rhythmbox-plugins',
            'hexchat','hexchat-common' ];

    for i in range(0, len(apps)):
		print ("##### " + apps[i] + " PURGE #############" )
		os.system('sudo apt-get purge '+apps[i])
		
    pass;

def appsInstall():
    apps =['vlc',
           'vlc-data',
           'vlc-nox',
           'vlc-plugin-notify',
           'glade',
           'git',
           'git-core',
           'git-man',
           'gitg',
           'geany',
           'geany-core',
           'virtualbox',
           'virtualbox-dkms',
           'virtualbox-qt',
           'flatpak',
           'plank',
           'dropbox',
           'geary' ];

    for i in range(0, len(apps)):
		print ("##### " + apps[i] + " INSTALATION #######" );
		os.system('sudo apt-get install '+apps[i])
        
    print("##### NODE INSTALATION ############");    
    os.system("curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -");
    os.system("sudo apt-get install -y nodejs");
    
    print("##### MONGODB INSTALATION #########");
    os.system("sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5");
    os.system("echo 'deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse' | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list");
    os.system("sudo apt-get update");
    os.system("sudo apt-get install -y mongodb-org");
    
    pass
    
appsInstall();
appsPurge();

#extract desktop enviroment and modify it

def modify_xfce():
    pass

def modify_mate():
	
	
	
	pass

desktopEnvironment = os.environ.get('DESKTOP_SESSION').upper();
desktopEnvironment.upper;

deMod = {
        'XFCE': modify_xfce,
        'MATE': modify_mate,
	};

try:
    deMod[desktopEnvironment]();
except:
	pass;

input('qlqr coisa para sair');
