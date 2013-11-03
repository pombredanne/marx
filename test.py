from marx.docker.wrapper import Docker

d = Docker()

#for x in d.rm(*[x['id'] for x in d.ps(a=True)]):
#    print "Removed: %s" % (x)

hsh = d.run("ubuntu", "echo", "hello", d=True)
