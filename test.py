from marx.docker.wrapper import Docker

d = Docker()
for line in d.history('ubuntu'):
    print line
