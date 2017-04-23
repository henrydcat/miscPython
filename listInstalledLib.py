import pip
packages = pip.get_installed_distributions()
packages_list = sorted(["%s==%s" % (i.key, i.version)
  for i in packages])

for i in packages_list: 
  print i


