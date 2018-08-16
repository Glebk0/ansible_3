Vagrant.configure("2") do |config|

  config.vm.define "webserver" do |web|
	web.vm.box = "sbeliakou/centos"
	web.vm.box_version = "7.5"
	web.vm.hostname = 'webserver'
	web.vm.network :private_network, ip: "192.168.1.70"		
	web.vm.provider :virtualbox do |v|
		v.customize ["modifyvm", :id, "--memory", 1024]
		v.customize ["modifyvm", :id, "--name","webserver"]
	end
  end

  config.vm.define "appserver" do |app|
	app.vm.box = "sbeliakou/centos"
	app.vm.box_version = "7.5"
	app.vm.hostname = 'appserver'
	app.vm.network :private_network, ip: "192.168.1.71"		
	app.vm.provider :virtualbox do |v|
		v.customize ["modifyvm", :id, "--memory", 1024]
		v.customize ["modifyvm", :id, "--name","appserver"]
	end
  end
  config.vm.define "ansible" do |app|
	app.vm.box = "sbeliakou/centos"
	app.vm.box_version = "7.5"
	app.vm.hostname = 'ansible'
	app.vm.network :private_network, ip: "192.168.1.72"		
	app.vm.provider :virtualbox do |v|
		v.customize ["modifyvm", :id, "--memory", 1024]
		v.customize ["modifyvm", :id, "--name","ansible"]
	end
  end
end
