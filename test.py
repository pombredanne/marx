from marx.docker.wrapper import Docker

d = Docker()

#for x in d.rm(*[x['id'] for x in d.ps(a=True)]):
#    print "Removed: %s" % (x)

for line in d.run("ubuntu", "echo", "hello"):
    print line
